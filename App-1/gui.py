import modules
import FreeSimpleGUI as fsg

label = fsg.Text("Enter your to-do: ")
inputBox = fsg.InputText(tooltip="Enter to-do")
addButton = fsg.Button("Add")
window = fsg.Window('To-Do App', layout=[[label], [inputBox,addButton]])
window.read()
window.close()
