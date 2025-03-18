content = ["All carrots must be sliced longitudinally", 
           "All onions must be diced", 
           "All tomatoes must be sliced"]

filenames = ["carrots.txt", "onions.txt", "tomatoes.txt"]

for content, filenames in zip(content, filenames):
    file = open(f"../files/experiments_bonuses/{filenames}", "w")
    file.write(content)
