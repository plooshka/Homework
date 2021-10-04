class Opener:

    def __init__(self, file_name, method):
        try:
            self.file_obj = open(file_name, method)
        except (FileNotFoundError, FileExistsError) as err:
            print(err)

    def __enter__(self):
        try:
            return self.file_obj
        except AttributeError as err:
            print(err)

    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            self.file_obj.close()
        except AttributeError as err:
            print(err)
        return True


with Opener("text.txt", "r") as file:
    print(file.name)
    print()
