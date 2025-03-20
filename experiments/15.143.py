#content - teaches about commonly used csv, glob, webbrowser, and shutil modules
import glob, webbrowser

# glob
myfiles = glob.glob("* .txt")
print(myfiles)

for filepath in myfiles:
    with(open filepath, "r") as file:
        print(file.read().isupper())

# webbrowser
user_term = input("Enter your search criteria here: ").replace(" ", "+")

webbrowser.open("https://www.google.com/search?q=" + user_term)
