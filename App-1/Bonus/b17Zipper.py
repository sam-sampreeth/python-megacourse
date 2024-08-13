import zipfile
import pathlib
def makeArchive(filepaths, destination):
    destpath = pathlib.Path(destination, "compressed.zip")
    with zipfile.ZipFile(destpath, 'w') as arc:
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            arc.write(filepath, arcname=filepath.name)

if __name__ == '__main__':
    makeArchive(filepaths=["b3.py", "b4.py"], destination="subfiles")