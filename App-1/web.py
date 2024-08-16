import streamlit as slt
import modules

todos = modules.getTodos()

def addTodo():
    todoToAdd = slt.session_state["newTodo"] + '\n'
    todos.append(todoToAdd)
    modules.writeTodos(todos)

slt.title("My To-Do App!")

for index, todo in enumerate(todos):
    checkbox = slt.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        modules.writeTodos(todos)
        del slt.session_state[todo]
        slt.rerun()

slt.text_input(label="Enter a to-do", placeholder="To-do goes here...",
               on_change=addTodo, key='newTodo')
