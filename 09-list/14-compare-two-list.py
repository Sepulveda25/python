#Compare two lists in Python
listx1, listx2=[3, 5, 7, 9], [3, 5, 7, 9]
print (listx1 == listx2)
#True
listx1, listx2=[9, 7, 5, 3], [3, 5, 7, 9]	#create two lists equal, but unsorted.
print(listx1 == listx2)
#False

listx1.sort()
listx2.sort()
print(listx1 == listx2)	#order and compare
#True

listx1, listx2 =[2, 3, 5, 7], [3, 5, 7, 9]	#create two different list
print(listx1 == listx2)
#False
