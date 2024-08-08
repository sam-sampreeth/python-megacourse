FILEPATH = "todos.txt"


def getTodos(filepath=FILEPATH):
    """ Reads todos from the file todos.txt and returns them in a list """
    with open(filepath, 'r') as localFile:
        localTodos = localFile.readlines()
    return localTodos


def writeTodos(localTodo, filepath=FILEPATH):
    """ Writes todos to the file todos.txt """
    with open(filepath, 'w') as localFile:
        localFile.writelines(localTodo)


if __name__ == "__main__":
    print("Hello")
    print(getTodos())
