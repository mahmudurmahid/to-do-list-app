FILEPATH = "files/todos.txt"

def get_todos(filepath=FILEPATH):
    """Read a text file and return a list of todo items."""
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local

# write_todos function behaves as a procedure because it does not return a value
def write_todos(todos_arg, filepath=FILEPATH):
    """Write a list of todo items into a text file."""
    with open(filepath, "w") as file:
        file.writelines(todos_arg)
