import csv

user_input = input()
input_file = open(user_input)
file_lines = input_file.readlines()
show_list = []
show_dict = {}

# assigning variables to seasons and shows to list
for i in range(0, len(file_lines) -1, 2):
    show_title = file_lines[i + 1].strip()
    seasons_num = int(file_lines[i])
    print(show_title)
    show_list.append(show_title)

    if show_dict.get(seasons_num) == None:
        show_dict[seasons_num] = [show_title]
    else:
        show_dict[seasons_num].append(show_title)



#for item in (show_list):
    #show_dict[show_list[item]] = show_list[item + 1]

# test print
print(show_dict)
