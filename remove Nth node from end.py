"""
Author:Amal K Philip
Description:Given the head of a linked list, remove the nth node from the end of the list and return its head.
"""

list=input("Enter the numbers with space:")
list=list.split()
main_list=[]
for i in list:
    i=int(i)
    main_list.append(i)
print(main_list)
node=int(input("enter the position from last for remove element:"))
main_list.pop(-node)
final_list=[]
for i in main_list:
    i=int(i)
    final_list.append(i)
print(final_list)
