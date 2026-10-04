#!/usr/bin/env python3
"""從公開 JSON 重建網站資料腳本；僅使用 Python 標準函式庫。"""
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
source = root / 'data' / '世界宗教導覽資料.json'
data = json.loads(source.read_text(encoding='utf-8'))
serialized = json.dumps(data, ensure_ascii=False, indent=2).replace('</', '<\\/')
output = root / 'data' / 'content.js'
output.write_text('/* 世界宗教小百科：公開教育資料；來源與限制請見 JSON 及網站。 */\nwindow.GUIDE_DATA = ' + serialized + ';\n', encoding='utf-8')
print('已同步公開 JSON 與網站資料腳本。')
