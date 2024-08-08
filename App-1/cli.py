import modules
import time

now = time.strftime("%b %d, %Y %H:%M")
print("It's", now)
while True:
    action = input("Type add, show, edit, complete or exit: ")
    action = action.strip()

    if action.startswith("add"):
        todo = action[4:]
        todos = modules.getTodos()

        todos.append(todo + '\n')

        modules.writeTodos(todos)
        print("Added!")

    elif action.startswith("show"):
        todos = modules.getTodos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            var = f"{index + 1}. {item}"
            print(var)

    elif action.startswith("edit"):
        try:
            numb = int(action[5:]) - 1
            todos = modules.getTodos()

            edited_todo = input("Enter new to-do: ")
            todos[numb] = edited_todo + '\n'

            modules.writeTodos(todos)

            print("Edited successfully!")
        except ValueError:
            print("Please enter a number after edit keyword")
            continue

    elif action.startswith("complete"):
        try:
            completed_todo = int(action[9:])
            todos = modules.getTodos()

            index = completed_todo - 1
            completed = todos[index].strip('\n')

            todos.pop(index)

            modules.writeTodos(todos)

            print(f"Todo {completed} completed!")
        except ValueError:
            print("Please enter a number after complete keyword")
            continue
        except IndexError:
            print("There is no item with that number")
            continue

    elif action.startswith("exit"):
        break

    else:
        print("Invalid command.")

print("Exit successfully")
