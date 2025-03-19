while True:
    user_action = input("Type add, show, edit, complete, or exit: ")
    user_action = user_action.strip().lower()


    if "add" in user_action:
        todo = input("Enter your todo: ") + "\n"

        with open("files/todos.txt", "r") as file:
            todos = file.readlines()

        todos.append(todo)

        with open("files/todos.txt", "w") as file:
            file.writelines(todos)

    if "show" in user_action:
        with open("files/todos.txt", "r") as file:
            todos = file.readlines()
        # new_todos = [item.strip("\n") for item in todos] # List comprehension example
        for index, item in enumerate(todos):
            item = item.strip("\n")
            row = f"{index + 1}-{item}"
            print(row)
    if "edit" in user_action:
        number = int(input("Enter the number of the todo you want to edit: "))
        number = number - 1

        with open("files/todos.txt", "r") as file:
            todos = file.readlines()
        
        new_todo = input("Enter the new todo: ")
        todos[number] = new_todo + "\n"

        with open("files/todos.txt", "w") as file:
            file.writelines(todos)

    if "complete" in user_action:
        number = int(input("Enter the number of the todo you have completed: "))

        with open("files/todos.txt", "r") as file:
            todos = file.readlines()

        index = number - 1
        todo_to_remove = todos[index].strip("\n")
        todos.pop(index)

        with open("files/todos.txt", "w") as file:
            file.writelines(todos)
        message = f"Todo number {todo_to_remove} has been completed and removed from the list."
        print(message)

    if "exit" in user_action:
        break

print("Goodbye!")