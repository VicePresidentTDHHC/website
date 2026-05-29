import re
from pathlib import Path

html = Path("../../archive/raw/home.html").read_text(encoding="utf-8", errors="replace")
m = re.search(r'<style id="et-critical-inline-css">(.*?)</style>', html, re.S)
if not m:
    raise SystemExit("no critical css")
css = m.group(1)
for pat in ["section_7", "section_5", "divider", "d7282f", "background-image"]:
    for match in re.finditer(re.escape(pat), css):
        i = match.start()
        print(pat, ":", css[max(0, i - 100) : i + 300])
        print("---")
