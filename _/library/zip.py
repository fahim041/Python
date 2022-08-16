from zipfile import ZipFile
from pathlib import Path

'''with ZipFile("files.zip", "w") as zip:
    for path in Path("_/library").rglob("*.*"):
        zip.write(path)'''

with ZipFile("files.zip") as zip:
    print(zip.namelist())