file_list = ['1.txt', '2.txt', '3.txt']


def merging_file():
    row_in_file = {}
    for file in file_list:
        lines = 0
        with open(file, encoding='utf-8') as f:
            for line in f:
                lines += 1
            row_in_file[file] = lines
    sorted_dict = {}
    sorted_keys = sorted(row_in_file, key=row_in_file.get)
    for i in sorted_keys:
        sorted_dict[i] = row_in_file[i]
    with open('result.txt', 'w', encoding='utf-8') as f:
        for i, j in sorted_dict.items():
            with open(i, encoding='utf-8') as source:
                f.write(i + '\n' + str(j) + '\n')
                for k in source:
                    f.write(k)
                f.write('\n')


merging_file()