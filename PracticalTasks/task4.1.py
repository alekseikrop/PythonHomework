def sort_file(filename: str):
    with open(filename, 'r') as unsorted:
        uns_list = unsorted.readlines()

    uns_list.sort()

    with open(r'data/sorted_names.txt', 'w') as sorted:
        sorted.writelines(uns_list)

sort_file(r'data/unsorted_names.txt')
