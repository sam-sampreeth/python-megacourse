import modules
import FreeSimpleGUI as fsg
import time
import os

if not os.path.exists("todos.txt"):
    with open ("todos.txt", "w") as file:
        pass

fsg.theme("DarkBlue2")

timeLabel = fsg.Text('', key='clock')
label = fsg.Text("Enter your to-do: ")
inputBox = fsg.InputText(tooltip="Enter to-do", key="todo")
addButton = fsg.Button("Add")
listBox = fsg.Listbox(values=modules.getTodos(),
                      key="todos", enable_events=True, size=[45, 10])
editButton = fsg.Button("Edit")
completeButton = fsg.Button("Complete")
exitButton = fsg.Button("Exit")

window = fsg.Window('To-Do App',
                    layout=[[timeLabel],
                            [label],
                            [inputBox, addButton],
                            [listBox, editButton, completeButton],
                            [exitButton]],
                    font=('Helvetica', 14))
while True:
    event, values = window.read(timeout=1000)
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M"))
    match event:
        case "Add":
            todos = modules.getTodos()
            newTodo = values['todo'] + '\n'
            todos.append(newTodo)
            modules.writeTodos(todos)
            window['todos'].update(values=todos)

        case "Edit":
            try:
                todoToEdit = values['todos'][0]
                newTodo = values['todo']
                todos = modules.getTodos()
                editIndex = todos.index(todoToEdit)
                todos[editIndex] = newTodo
                modules.writeTodos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                fsg.popup("Please select an item to edit", font=('Helvetica', 10))

        case 'Complete':
            try:
                todoToComplete = values['todos'][0]
                todos = modules.getTodos()
                todos.remove(todoToComplete)
                modules.writeTodos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                fsg.popup("Please select an item to complete", font=('Helvetica', 10))
        case 'Exit':
            break

        case 'todos':
            window['todo'].update(value=values['todos'][0])

        case fsg.WIN_CLOSED:
            break

window.close()
