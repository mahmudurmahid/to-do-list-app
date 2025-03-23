import zipfile
import pathlib


def make_archive(filepaths, dest_dir):
    dest_path = pathlib.Path(dest_dir, "compressed.zip")
    with zipfile.ZipFile(dest_path, "w") as archive:
        filepath = pathlib.Path(filepath)
        for filepath in filepaths:
            archive.write(filepath, arcname=filepath.name)


if __name__ == "__main__":
    make_archive(filepaths=["2.22a.py", "2.22b.py"], dest_dir="coding_exercises")
