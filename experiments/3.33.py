todos = []

while True:
    user_action = input("Type add, show, or exit: ")
    user_action = user_action.strip().lower()

    match user_action:
        case "add":
            todo = input("Enter your todo: ")
            todos.append(todo)
        case "show" | "display": # or operator
            for item in todos:
                item = item.title()
                print(item)
        case "exit":
            break
        case _: # default case
            print("Invalid command")

print("Goodbye!")