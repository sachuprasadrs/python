color_list1 = input("Enter colors for list 1 separated by spaces: ").split()
color_list2 = input("Enter colors for list 2 separated by spaces: ").split()
unique_colors = [color for color in color_list1 if color not in color_list2]
print("Colors in list 1 not in list 2:", unique_colors)
