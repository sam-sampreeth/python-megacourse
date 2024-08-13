import modules
import FreeSimpleGUI as fsg

label = fsg.Text("Enter your to-do: ")
inputBox = fsg.InputText(tooltip="Enter to-do", key="todo")
addButton = fsg.Button("Add")
listBox = fsg.Listbox(values=modules.getTodos(),
                      key="todos", enable_events=True, size = [45, 10])
editButton = fsg.Button("Edit")

window = fsg.Window('To-Do App',
                    layout=[[label], [inputBox, addButton], [listBox, editButton]],
                    font=('Helvetica', 14))
while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = modules.getTodos()
            newTodo = values['todo'] + '\n'
            todos.append(newTodo)
            modules.writeTodos(todos)
            window['todos'].update(values=todos)
        case "Edit":
            todoToEdit = values['todos'][0]
            newTodo = values['todo']
            todos = modules.getTodos()
            editIndex = todos.index(todoToEdit)
            todos[editIndex] = newTodo
            modules.writeTodos(todos)
            window['todos'].update(values=todos)

        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case fsg.WIN_CLOSED:
            break
window.close()
