waiting_list = ["jerry", "tom", "ben"]
waiting_list.sort()

for index, item in enumerate(waiting_list):
    row = f"{index + 1}. {item.capitalize()}"
    print(row)