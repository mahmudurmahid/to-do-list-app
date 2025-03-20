def get_todos(filepath):
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local

# write_todos function behaves as a procedure because it does not return a value
def write_todos(filepath, todos_arg):
    with open(filepath, "w") as file:
        file.writelines(todos_arg)


while True:
    user_action = input("Type add, show, edit, complete, or exit: ")
    user_action = user_action.strip().lower()


    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = get_todos("files/todos.txt")

        todos.append(todo + "\n")

        write_todos("files/todos.txt", todos)

    elif user_action.startswith("show"):
        todos = get_todos("files/todos.txt")
        # new_todos = [item.strip("\n") for item in todos] # List comprehension example
        for index, item in enumerate(todos):
            item = item.strip("\n")
            row = f"{index + 1}-{item}"
            print(row)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = get_todos("files/todos.txt")
            
            new_todo = input("Enter the new todo: ")
            todos[number] = new_todo + "\n"

            write_todos("files/todos.txt", todos)
        except ValueError:
            print("Invalid number. Please try again.")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            todos = get_todos("files/todos.txt")

            index = number - 1
            todo_to_remove = todos[index].strip("\n")
            todos.pop(index)

            write_todos("files/todos.txt", todos)

            message = f"Todo number {todo_to_remove} has been completed and removed from the list."
            print(message)
        except IndexError:
            print("Invalid item number. Please try again.")
            continue

    elif user_action.startswith("exit"):
        break

    else:
        print("Invalid action. Please try again.")

print("Goodbye!")