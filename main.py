while True:
    user_action = input("Type add, show, edit, or exit: ")
    user_action = user_action.strip().lower()

    match user_action:
        case "add":
            todo = input("Enter your todo: ") + "\n"

            file = open("files/todos.txt", "r")
            todos = file.readlines()
            file.close()

            todos.append(todo)

            file = open("files/todos.txt", "w")
            file.writelines(todos)
            file.close()
        case "show":
            file = open("files/todos.txt", "r")
            todos = file.readlines()
            file.close()
            for index, item in enumerate(todos):
                row = f"{index + 1}-{item}"
                print(row)
        case "edit":
            number = int(input("Enter the number of the todo you want to edit: "))
            number = number - 1
            new_todo = input("Enter the new todo: ")
            todos[number] = new_todo
        case "complete":
            number = int(input("Enter the number of the todo you have completed: "))
            todos.pop(number - 1)
        case "exit":
            break

print("Goodbye!")