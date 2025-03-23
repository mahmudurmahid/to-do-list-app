from random import randint

lower_bound = int(input("Enter your lower bound number: "))
upper_bound = int(input("Enter your upper bound number: "))

def random_number_generator(lower_bound, upper_bound):
    random_number = randint(lower_bound, upper_bound)
    return random_number

print(random_number_generator(lower_bound, upper_bound))