import zipfile

def extract_archive(archivepath, dest_dir):
    with zipfile.ZipFile(archivepath, "r") as archive:
        archive.extractall(dest_dir)

if __name__ == "__main__":
    extract_archive("/Users/mahmudurmahid/Library/Mobile Documents/com~apple~CloudDocs/Software Engineering/Python/Python Mega Course - Learn Python in 60 Days, Build 20 Apps/App 1 - Build a ToDo List App/to-do-list-app/experiments/compressed.zip", "/Users/mahmudurmahid/Library/Mobile Documents/com~apple~CloudDocs/Software Engineering/Python/Python Mega Course - Learn Python in 60 Days, Build 20 Apps/App 1 - Build a ToDo List App/to-do-list-app/files")
