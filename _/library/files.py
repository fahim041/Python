from pathlib import Path

path = Path("_/library/text.txt")
print(path)
print(path.read_text())
path.write_text("next line")