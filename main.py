todos = []

while True:
    user_action = input("Type add, show, or exit: ")
    user_action = user_action.strip().lower()

    match user_action:
        case "add":
            todo = input("Enter your todo: ")
            todos.append(todo)
        case "show":
            for item in todos:
                print(item)
        case "exit":
            break

print("Goodbye!")