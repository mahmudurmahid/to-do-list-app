todos = []

while True:
    user_action = input("Type add, show, or exit: ")

    match user_action:
        case "add":
            todo = input("Enter your todo: ")
            todos.append(todo)
        case "show":
            print(todos)
        case "exit":
            break

print("Goodbye!")