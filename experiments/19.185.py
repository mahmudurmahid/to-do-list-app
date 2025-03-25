# order of the widgets matter

import streamlit as st
from functions import get_todos, write_todos


todos = get_todos()

st.set_page_config(layout="wide")

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    write_todos(todos)

st.title("My To Do App")
st.subheader("Tasks for you to complete")
st.write("This app is to increase your <b>productivity</b>",
         unsafe_allow_html=True)

st.text_input(label="Enter a to do:", placeholder="Add a new to do item here",
              on_change=add_todo, key="new_todo")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="Enter a to do:", placeholder="Add a new to do item here",
              on_change=add_todo, key="new_todo")
