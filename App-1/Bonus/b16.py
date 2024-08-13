import FreeSimpleGUI as fsg
from b17Zipper import makeArchive

label1 = fsg.Text("Select files to compress")
input1 = fsg.Input()
button1 = fsg.FilesBrowse("Choose", key="file")

label2 = fsg.Text("Select destination directory")
input2 = fsg.Input()
button2 = fsg.FolderBrowse("Choose", key="dir")

compressButton = fsg.Button("Compress")
output = fsg.Text("", key="output", text_color="blue")

window = fsg.Window("Compressor", layout=[[label1, input1, button1], [label2, input2, button2], [compressButton, output]])

while True:
    event, values = window.read()
    print(event, values)
    filePath = values["file"].split(';')
    folder = values["dir"]
    makeArchive(filePath, folder)
    window["output"].update(value="Compression Completed!")

window.close()
