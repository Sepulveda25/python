#Using Lists as Stacks
color_list=["Red", "Blue", "Green", "Black"]
print(color_list)
#['Red', 'Blue', 'Green', 'Black']
color_list.append("White")
color_list.append("Yellow")
print(color_list)
#['Red', 'Blue', 'Green', 'Black', 'White', 'Yellow']
color_list.pop() 
#'Yellow'
color_list.pop()
#'White'
color_list.pop()
#'Black'
print(color_list)
#['Red', 'Blue', 'Green']