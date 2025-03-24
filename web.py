import streamlit as st
from functions import get_todos, write_todos


todos = get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    write_todos(todos)

st.title("My To Do App")
st.subheader("Tasks for you to complete")
st.write("This app is to increase your productivity")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="Enter a to do:", placeholder="Add a new to do item here",
              on_change=add_todo, key="new_todo")
