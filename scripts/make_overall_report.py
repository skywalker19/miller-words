#!/usr/bin/env python3
"""Rebuild the word notebook, report data and personal-site staging files."""
import argparse
import hashlib
import html
import json
import re
import shutil
import subprocess
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT.parent / 'personal-site'
STAGE = ROOT / 'output/site-staging'


def read_words():
    section = (ROOT / 'words.md').read_text().split('## 2.')[0]
    words = []
    for line in section.splitlines():
        cells = [cell.strip() for cell in line.strip().strip('|').split('|')]
        if len(cells) != 6 or not cells[1].isdigit() or not cells[2].isdigit():
            continue
        words.append(dict(week=int(re.search(r'\d+', cells[0]).group()),
                          day=int(cells[1]), ordinal=int(cells[2]),
                          word=cells[3], meaning=cells[4],
                          pending='待确认' in cells[5]))
    return sorted(words, key=lambda row: (row['week'], row['day'], row['ordinal']))


def rich(text):
    return re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', html.escape(text))


def parse_story(number):
    source = (ROOT / f'practice/story-{number:03}.md').read_text()
    title = source.splitlines()[0].split(' — ', 1)[1]
    zh = re.search(r'中文标题：(.*)', source)
    title_zh = zh.group(1).strip() if zh else 'Miller 奇妙的一天'
    scenes = []
    for match in re.finditer(r'## Scene (\d+) — ([^\n]+)\n(.*?)(?=\n## |\Z)', source, re.S):
        scene, heading, body = match.groups()
        image = re.search(r'!\[[^\]]*\]\(([^)]+)\)', body).group(1)
        clean = re.sub(r'!\[[^\]]*\]\([^)]+\)\s*', '', body)
        english = clean.split('中文解释：')[0].strip()
        english = '\n\n'.join(p for p in english.split('\n\n') if not p.startswith('场景：'))
        translation = re.search(r'中文解释：(.*)', body)
        labels = re.search(r'Words used: (.*)', body)
        origin = re.search(r'单词来源：(.*)', body)
        scenes.append(dict(number=int(scene), title=heading, image=Path(image).name,
                           english=english, translation=translation.group(1) if translation else '',
                           labels=labels.group(1) if labels else '',
                           days=origin.group(1) if origin else ''))
    return dict(id=f'story-{number:03}', title=title, titleZh=title_zh,
                intro=scenes[0]['english'].split('\n\n')[0], scenes=scenes)


def story_html(story, site=False):
    esc = html.escape
    back = '/things/miller-words/report/' if site else 'miller-words-report.html'
    exam = f'{back}?exam-story={story["week"]}#memory-exam'
    image_prefix = '../cartoon/' if site else '../../cartoon/'
    cards = []
    for scene in story['scenes']:
        english = ''.join('<p>' + rich(p) + '</p>' for p in scene['english'].split('\n\n'))
        cards.append(f'''<article><h2>Scene {scene['number']} — {esc(scene['title'])}</h2>
<p class="meta">{esc(scene['days'])}</p><a href="{image_prefix}{scene['image']}"><img src="{image_prefix}{scene['image']}" alt="{esc(scene['title'])}" width="1536" height="1024" loading="lazy"></a>
<div lang="en">{english}</div><p class="words">{esc(scene['labels'])}</p><details><summary>查看中文解释</summary><p>{esc(scene['translation'])}</p></details></article>''')
    questions = (ROOT / f'practice/{story["id"]}.md').read_text().split('## Recall activities\n')[-1]
    activities = ''.join('<li>'+rich(re.sub(r'^\d+\.\s*','',p))+'</li>' for p in questions.splitlines() if re.match(r'^[123]\. ',p))
    notes = (ROOT / f'practice/{story["id"]}.md').read_text().split('## Meaning and language notes\n')[-1].split('## Recall activities')[0]
    notes = ''.join('<li>'+rich(p[2:])+'</li>' for p in notes.splitlines() if p.startswith('- '))
    return f'''<!doctype html><html lang="zh-CN"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{esc(story['titleZh'])} · {story['id']}</title><style>
*{{box-sizing:border-box}}body{{margin:0;color:#14222d;background:#eef2f0;font:18px/1.7 "Avenir Next","PingFang SC",sans-serif}}main{{max-width:980px;margin:auto;padding:30px 22px 70px}}a{{color:inherit;text-underline-offset:4px}}h1{{font:500 clamp(32px,5vw,52px)/1.2 "Songti SC",serif}}h2{{font-size:24px;line-height:1.4}}article{{margin:26px 0;padding:24px;background:#f8faf8;border:1px solid #cbd4d1}}img{{width:100%;height:auto;display:block;margin-bottom:20px}}strong{{color:#9a582a}}.meta,.words{{color:#52616a;font-size:14px}}summary{{cursor:pointer}}.note{{font-size:15px}}:focus-visible{{outline:3px solid #4f72d3;outline-offset:4px}}@media(max-width:600px){{main{{padding:24px 14px}}article{{padding:18px}}}}@media print{{article{{break-inside:avoid}}main{{padding:0}}}}
</style><main><nav><a href="{back}">← 返回单词本总览</a> · <a href="{exam}">Memory Exam · 本篇单词配对</a></nav><p class="meta">{story['id'].upper()} · 第 {story['week']} 周{'（推定）' if story['week'] != 2 else ''} · Day {story['startDay']}–{story['endDay']} · {story['entryCount']} 个目标词</p><h1>{esc(story['titleZh'])}</h1><p lang="en">{esc(story['title'])}</p><p>每次练习约 5–8 个词，先读英文，再查看中文解释，最后遮住图片复述。点击图片可查看原图。</p>{''.join(cards)}<section><h2>复述练习</h2><ol>{activities}</ol><p>选两个目标词造新句。首次练习后第 1、3、7、14 天复习。</p><p><a href="{exam}">开始 Memory Exam →</a> · 可切换到全部五篇故事，或按 Day 练习。</p></section><details class="note"><summary>家长词义备注</summary><ul>{notes}</ul></details><p><a href="{back}">← 返回单词本总览</a></p></main></html>'''


def update_story_one():
    """Keep the original story layout, linking its exam to the shared section."""
    path = ROOT / 'output/html/story-001.html'
    source = path.read_text()
    source = re.sub(r'  <script>\s*const wordBank = .*?</script>\s*', '', source, flags=re.S)
    source = re.sub(r'      <div class="memory-strip".*?(?=    </header>)', '', source, flags=re.S)
    entry = '''    <section class="dashboard" aria-label="Memory exam">
      <article class="panel exam-panel" id="memory-exam">
        <p class="kicker">Memory Exam · Story 001–005</p>
        <h2>Match the word to its meaning</h2>
        <p class="section-note">单词配对已移到总览中的独立板块，覆盖全部五篇故事、Day 1–30。每轮最多 8 对，可按故事或 Day 选择范围，原来的配对记录会在同一浏览器中沿用。</p>
        <p><a class="button button-primary" style="display:inline-block;text-decoration:none" href="miller-words-report.html?exam-story=1#memory-exam">练习 Story 001 →</a> <a style="color:inherit;margin-left:14px" href="miller-words-report.html#memory-exam">练习全部故事 →</a></p>
      </article>
    </section>'''
    source = re.sub(r'    <section class="dashboard".*?</section>', entry, source, count=1, flags=re.S)
    source = source.replace('Story 001 - Miller Words · Matching progress is saved only in this browser.', 'Story 001 - Miller Words · Memory Exam is available in the word notebook overview.')
    path.write_text(source)
    site_source = source.replace('../../cartoon/', '../cartoon/').replace('miller-words-report.html', '/things/miller-words/report/')
    stage_text('public/things/miller-words/episodes/story-001/html/story-001.html', site_source)


def stage_text(relative, content):
    target = STAGE / relative
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(content)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--updated', default=date.today().isoformat())
    args = parser.parse_args()
    words = read_words()
    sessions, seen, cumulative = [], set(), 0
    for day in sorted({row['day'] for row in words}):
        entries = [row for row in words if row['day'] == day]
        new = {row['word'].casefold() for row in entries} - seen
        seen.update(row['word'].casefold() for row in entries)
        cumulative += len(entries)
        sessions.append(dict(id=f'day-{day}', label=f'Day {day}', day=day,
                             week=entries[0]['week'], entryCount=len(entries),
                             newWords=len(new), cumulativeEntries=cumulative))
    weeks, stories = [], []
    for week in sorted({row['week'] for row in words}):
        entries = [row for row in words if row['week'] == week]
        days = sorted({row['day'] for row in entries})
        weeks.append(dict(number=week, inferred=week != 2, startDay=min(days),
                          endDay=max(days), dayCount=len(days), entryCount=len(entries),
                          uniqueWords=len({row['word'].casefold() for row in entries})))
        story = parse_story(week)
        story.update(week=week, startDay=min(days), endDay=max(days),
                     entryCount=len(entries), sceneCount=len(story['scenes']),
                     cover=story['scenes'][0]['image'], coverAlt=story['scenes'][0]['title'],
                     hasPdf=(ROOT / f'output/pdf/{story["id"]}.pdf').exists())
        stories.append(story)
    data = dict(title='Miller Words · Word notebook', titleZh='Miller 的单词本',
                description='按 Day 和周次查看词汇积累，打开五篇故事与配图练习。',
                updated=args.updated, totalEntries=len(words), uniqueWords=len(seen),
                sessions=sessions, weeks=weeks, stories=stories, words=words,
                sceneCount=sum(story['sceneCount'] for story in stories),
                imageCount=sum(story['sceneCount'] for story in stories),
                sourceNote='来自已整理的 Day 1–30 单词记录。第 2 周由照片明确标注，其余周次按照片分隔推定；未记录具体学习日期。')
    data_path = ROOT / 'output/data/miller-words-report.json'
    data_path.parent.mkdir(parents=True, exist_ok=True)
    data_path.write_text(json.dumps(data, ensure_ascii=False, indent=2)+'\n')
    local = ROOT / 'output/html'
    shutil.copy2(ROOT / 'scripts/report/report.css', local / 'miller-words-report.css')
    shutil.copy2(ROOT / 'scripts/report/report.js', local / 'miller-words-report.js')
    shutil.copy2(ROOT / 'scripts/report/memory-exam.js', local / 'memory-exam.js')
    subprocess.run(['node', str(ROOT / 'scripts/report/build-report.mjs'), str(data_path),
                    str(local / 'miller-words-report.html')], check=True)
    update_story_one()
    for story in stories[1:]:
        (local / f'{story["id"]}.html').write_text(story_html(story))
        episode = Path('public/things/miller-words/episodes') / story['id']
        stage_text(episode / f'html/{story["id"]}.html', story_html(story, site=True))
        for scene in story['scenes']:
            destination = STAGE / episode / 'cartoon' / scene['image']
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(ROOT / 'cartoon' / scene['image'], destination)
    stage_text('src/data/miller-words-overall-report.json', json.dumps(data,ensure_ascii=False,indent=2)+'\n')
    stage_text('src/data/miller-words-overall-report.ts',
               'import data from "./miller-words-overall-report.json";\n\n// Generated from the canonical word notebook; rebuild with make_overall_report.py.\nexport const millerWordsOverallReport = data;\n')
    stage_text('src/utils/render-miller-words-report.mjs', (ROOT / 'scripts/report/render-report.mjs').read_text())
    stage_text('src/styles/miller-words-report.css', (ROOT / 'scripts/report/report.css').read_text())
    stage_text('public/things/miller-words/report/report.js', (ROOT / 'scripts/report/report.js').read_text())
    stage_text('public/things/miller-words/report/memory-exam.js', (ROOT / 'scripts/report/memory-exam.js').read_text())
    stage_text('src/pages/things/miller-words/report/index.astro', '''---
import BaseLayout from "../../../../layouts/BaseLayout.astro";
import {millerWordsOverallReport as report} from "../../../../data/miller-words-overall-report";
import {renderReport} from "../../../../utils/render-miller-words-report.mjs";
import "../../../../styles/miller-words-report.css";
---
<BaseLayout title={report.titleZh} description={report.description}>
  <Fragment set:html={renderReport(report, {site: true})} />
  <script is:inline src="/things/miller-words/report/report.js" defer></script>
</BaseLayout>
''')
    config = (SITE / 'src/content.config.ts').read_text()
    stage_text('src/content.config.ts', config.replace('pdfUrl: siteRelativeUrl,', 'pdfUrl: siteRelativeUrl.optional(),'))
    component = (SITE / 'src/components/EpisodeSet.astro').read_text()
    if '{episode.pdfUrl && (' not in component:
        component = component.replace('<a href={episode.pdfUrl}', '{episode.pdfUrl && (<a href={episode.pdfUrl}')
        component = component.replace('Download PDF <span aria-hidden="true">↓</span>\n            </a>',
                                      'Download PDF <span aria-hidden="true">↓</span>\n            </a>)}')
    stage_text('src/components/EpisodeSet.astro', component)
    thing = (SITE / 'src/content/things/miller-words.md').read_text()
    thing = re.sub(r'^updated:.*$', f'updated: {args.updated}', thing, flags=re.M)
    thing = thing.replace('label: Overall report', 'label: 打开单词本总览 · Day 与周次统计')
    episode_yaml = 'episodes:\n'
    for story in stories:
        episode_yaml += f'  - slug: {story["id"]}\n    title: "{story["title"].replace(chr(34), chr(39))} — {story["id"].replace("story-", "Story ")} · Day {story["startDay"]}–{story["endDay"]}"\n    htmlUrl: /things/miller-words/episodes/{story["id"]}/html/{story["id"]}.html\n'
        if story['hasPdf']:
            episode_yaml += f'    pdfUrl: /things/miller-words/episodes/{story["id"]}/pdf/{story["id"]}.pdf\n'
    thing = re.sub(r'episodes:\n.*?(?=related:)', episode_yaml, thing, flags=re.S)
    entry = f'## 单词本入口\n\n从[单词本总览](/things/miller-words/report/)进入全部故事，查看 Day 1–{sessions[-1]["day"]} 和第 1–{len(weeks)} 周的统计，以及按当天序号排列的完整词表。当前共 {len(words)} 条记录、{len(seen)} 个不同词形、{data["sceneCount"]} 个故事场景。Day 为累计学习序号，第 1、3、4、5 周为推定周次。\n\n'
    if '## 单词本入口\n' in thing:
        thing = re.sub(r'## 单词本入口\n.*?(?=## Story 001\n)',entry,thing,flags=re.S)
    else:
        thing = thing.replace('## Story 001\n',entry+'## Story 001\n')
    new_stories = '\n\n## Story 002–005\n\n四篇新故事覆盖 Day 9–30 的 95 个目标词，共 18 张记忆配图。scales 采用已确认的“鳞片”，保留硬币和自然海报中的鱼鳞画面。可在总览中按周选择故事阅读；新故事暂提供网页练习，PDF 入口仅在已有打印版时显示。\n'
    if '\n\n## Story 002–005\n' in thing:
        thing = thing.split('\n\n## Story 002–005\n')[0]+new_stories
    else:
        thing += new_stories
    stage_text('src/content/things/miller-words.md', thing)
    route = (SITE / 'src/pages/things/[...id].astro').read_text()
    route = route.replace('The word bank, together', '单词本总览').replace('See the aggregate record across Miller Words sessions, separate from the individual story practice.', '按 Day 和周次查看全部记录，选择故事练习，或查找具体单词。')
    stage_text('src/pages/things/[...id].astro', route)
    baseline = {}
    for target in sorted(path for path in STAGE.rglob('*') if path.is_file()):
        relative = target.relative_to(STAGE).as_posix()
        if relative == 'baseline.json':
            continue
        existing = SITE / relative
        baseline[relative] = hashlib.sha256(existing.read_bytes()).hexdigest() if existing.exists() else None
    (STAGE / 'baseline.json').write_text(json.dumps(baseline,ensure_ascii=False,indent=2)+'\n')
    print(f'Generated overall report: {len(words)} entries, {len(seen)} word forms, {len(sessions)} Days, {len(weeks)} weeks, {len(stories)} stories.')
    print('Personal-site changes are staged; no files in personal-site have been changed.')


if __name__ == '__main__':
    main()
