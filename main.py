def swap_file_data():
    file1_name = input('Input name of first file you want to swap: ')
    file2_name = input('Input name of second file you want to swap: ')
    with open(file1_name, 'r') as a:
        data_a = a.read()
    with open(file2_name, 'r') as b:
        data_b = b.read()
    with open(file1_name, 'w') as a:
        a.write(data_b)
    with open(file2_name, 'w') as b:
        b.write(data_a)


swap_file_data()
