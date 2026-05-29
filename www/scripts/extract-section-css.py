import re
from pathlib import Path

html = Path("../../archive/raw/home.html").read_text(encoding="utf-8", errors="replace")
m = re.search(r'<style id="et-critical-inline-css">(.*?)</style>', html, re.S)
css = m.group(1) if m else ""
# write full critical css for manual inspection
Path("../../reference/divi-css/home-critical.css").write_text(css, encoding="utf-8")
for cls in re.findall(r"\.et_pb_section_\d+[^}]+}", css):
    print(cls[:800])
    print("---")
