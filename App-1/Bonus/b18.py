import FreeSimpleGUI as fsg
from subfiles import b18extractor

fsg.theme("Black")

label1 = fsg.Text("Select archive")
input1 = fsg.Input()
button1 = fsg.FileBrowse("Choose", key="archive")

label2 = fsg.Text("Select directory")
input2 = fsg.Input()
button2 = fsg.FolderBrowse("Choose", key="folder")

extractButton = fsg.Button("Extract")
outputLabel = fsg.Text(key="output", text_color="blue")

window = fsg.Window("Archive Extractor",
                    layout=[[label1, input1, button1],
                            [label2, input2, button2],
                            [extractButton, outputLabel]])

while True:
    event, values = window.read()
    print(event, values)
    archivePath = values["archive"]
    destDir = values["folder"]
    b18extractor.extractArchive(archivePath, destDir)
    window["output"].update(value="Extraction complete!")
window.close()

