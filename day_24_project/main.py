# with open('data_file.txt') as file:
#     contents = file.read()
#     print(contents)


with open('data_file.txt',mode='a') as file:
    file.write("\nnew text.")


