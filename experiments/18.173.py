# adding images to buttons and changing other styling options
from functions import get_todos, write_todos
import FreeSimpleGUI as sg
import time


sg.theme("Black")

clock = sg.Text("", key="clock")
label = sg.Text("Type in a to do:")
input_box = sg.InputText(tooltip="Enter to do", key="todo")
add_button = sg.Button(size=2, image_source="add.png", mouseover_colors="LightBlue2",
                       tooltip="Add to do", key="Add")
list_box = sg.Listbox(values=get_todos(), key="todos", enable_events=True, size=[45, 10])

edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

window = sg.Window("My To Do App",
                   layout=[[clock],
                           [label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=("Helvetica", 20))

while True:
    event, values = window.read(timeout=200)
    window["clock"].update(value=time.strftime("%d %b %Y, %H:%M:%S"))
    match event:
        case "Add":
            todos = get_todos()
            new_todo = values["todo"] + "\n"
            todos.append(new_todo)
            write_todos(todos)
            window["todos"].update(values=todos)

        case "Edit":
            try:
                todo_to_edit = values["todos"][0]
                new_todo = values["todo"]

                todos = get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                write_todos(todos)
                window["todos"].update(values=todos)
            except IndexError:
                sg.popup("Please select an item first", font=("Helvetica", 20))
        
        case "Complete":
            try:
                todo_to_complete = values["todos"][0]
                todos = get_todos()
                todos.remove(todo_to_complete)
                write_todos(todos)
                window["todos"].update(values=todos)
                window["todo"].update(value="")
            except IndexError:
                sg.popup("Please select an item first", font=("Helvetica", 20))
        
        case "Exit":
            break

        case "Todos":
            window["todo"].update(value=values["todos"][0])

        case sg.WIN_CLOSED:
            break


window.close() 
