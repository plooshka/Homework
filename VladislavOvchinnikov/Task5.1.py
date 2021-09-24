"""Sort the names and write them to a new file"""

with open("unsorted_names.txt", "r") as unsorted_file:
    data = unsorted_file.read()
    unsorted_names = data.split('\n')
with open("sorted_names.txt", "w") as sorted_file:
    for name in sorted(unsorted_names):
        sorted_file.write(name + "\n")
