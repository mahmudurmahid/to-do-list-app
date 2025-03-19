while True:
    user_action = input("Type add, show, edit, complete, or exit: ")
    user_action = user_action.strip().lower()


    if "add" in user_action or "new" in user_action: # or operator added to show comparison operator
        todo = user_action[4:]

        with open("files/todos.txt", "r") as file:
            todos = file.readlines()

        todos.append(todo)

        with open("files/todos.txt", "w") as file:
            file.writelines(todos)

    elif "show" in user_action and "display" in user_action: # and operator added to show comparison operator
        with open("files/todos.txt", "r") as file:
            todos = file.readlines()
        # new_todos = [item.strip("\n") for item in todos] # List comprehension example
        for index, item in enumerate(todos):
            item = item.strip("\n")
            row = f"{index + 1}-{item}"
            print(row)

    elif "edit" in user_action:
        number = int(user_action[5:])
        number = number - 1

        with open("files/todos.txt", "r") as file:
            todos = file.readlines()
        
        new_todo = input("Enter the new todo: ")
        todos[number] = new_todo + "\n"

        with open("files/todos.txt", "w") as file:
            file.writelines(todos)

    elif "complete" in user_action:
        number = int(user_action[9:])

        with open("files/todos.txt", "r") as file:
            todos = file.readlines()

        index = number - 1
        todo_to_remove = todos[index].strip("\n")
        todos.pop(index)

        with open("files/todos.txt", "w") as file:
            file.writelines(todos)
        message = f"Todo number {todo_to_remove} has been completed and removed from the list."
        print(message)

    elif "exit" in user_action:
        break

    else:
        print("Invalid action. Please try again.")