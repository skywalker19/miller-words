import fs from 'node:fs';
import {createHash} from 'node:crypto';
import {renderReport} from './render-report.mjs';

const [dataFile, htmlFile] = process.argv.slice(2);
if (!dataFile || !htmlFile) throw new Error('Usage: node build-report.mjs DATA_JSON OUTPUT_HTML');
const data = JSON.parse(fs.readFileSync(dataFile, 'utf8'));
const cssVersion = createHash('sha256').update(fs.readFileSync(new URL('./report.css', import.meta.url))).digest('hex').slice(0, 10);
fs.writeFileSync(htmlFile, `<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Miller 的单词本 · 总报告</title><link rel="stylesheet" href="miller-words-report.css?v=${cssVersion}"><style>body{margin:0;background:#eef2f0}html{scroll-behavior:smooth}</style></head><body>${renderReport(data)}<script src="miller-words-report.js" defer></script></body></html>`);
