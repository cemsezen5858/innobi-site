from pathlib import Path
import re
path = Path(''assets/css/style.css'')
text = path.read_text()
pattern = re.compile(r'''<<<<<<< ours\s*<<<<<<< ours\s*<<<<<<< ours\s*<<<<<<< ours\s*.badge-offset \\.badge-original,\s*.badge-offset \\.badge-upcoming \{[\s\S]*?>>>>>>> theirs\s*>>>>>>> theirs\s*>>>>>>> theirs\s*>>>>>>> theirs\s*>>>>>>> theirs''')
replacement = "  .badge-offset .badge-original {\n    position: absolute;\n    top: 1.2rem;\n    right: 1.2rem;\n    z-index: 2;\n  }"
new, count = pattern.subn(replacement, text)
if not count:
    raise SystemExit('pattern not found')
path.write_text(new)
