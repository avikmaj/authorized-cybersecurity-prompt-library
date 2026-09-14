from pathlib import Path
import json, re
root = Path(__file__).resolve().parents[1]
items = []
for p in root.rglob("*.md"):
    if any(x in p.parts for x in ("bundles", "templates", ".git")): continue
    t = p.read_text(encoding="utf-8")
    m = re.match(r"^---\s*\n(.*?)\n---", t, re.S)
    if not m: continue
    d = {}
    for line in m.group(1).splitlines():
        if ":" in line:
            k,v=line.split(":",1); d[k.strip()]=v.strip()
    if d.get("id"):
        d["path"] = str(p.relative_to(root)).replace("\\", "/")
        items.append(d)
(root / "PROMPT-INDEX.json").write_text(json.dumps({"count":len(items),"prompts":items}, indent=2)+"\n", encoding="utf-8")
print(f"Indexed {len(items)} prompts")
