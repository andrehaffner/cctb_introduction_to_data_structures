
main_list = [1, 2, 2, 5, 8, 4, 4, 8, 2, 1, 6]
reversed_list = main_list.reverse()
switch10_list = [10 if x == 10 else x for x in main_list]
doubled = len(main_list) - len(set(main_list))
print("List :", main_list)
print("Reversed list:", reversed_list)
print("The original list after replacing the value 5 by 10:", switch10_list)
print("Number of duplicated values:", doubled)
