todos = []

while True:
    user_action = input("Type add, show, edit, or exit: ")
    user_action = user_action.strip().lower()

    match user_action:
        case "add":
            todo = (input("Enter your todo: "))
            todos.append(todo)
        case "show":
            for index, item in enumerate(todos):
                row = f"{index + 1}-{item}"
                print(row)
            print("Hello", index, item) # Shows the last item in the list and index number as this is how for loop works
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