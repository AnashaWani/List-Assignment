# Creating a List in Python to perform different menu based operations based on user chioce :

# To create a list :
List = input("Enter Elements (Seperated by blank space):").split()
print("List:",List)

while True:
 # To perform insert :
 ind=int(input("Enter the index of the element to be inserted (Enter -1 to stop):"))
 if ind==-1:
  break
 v=input("Enter the element to be inserted:")
 List.insert(ind,v)
 print("Updated List:",List)

 # To perform append :
 i=input("Value you want to append to the list:")
 List.append(i)
 print("Updated List:",List)

 # To perform remove :
 r=input("Enter the element to be removed:")
 List.remove(r)
 print("Updated List:",List)

 # To perform pop :
 p=int(input("Enter index of the element to be popped:"))
 List.pop(p)
 print("Updated List:",List)

 # To perform copy :
 List.copy()
 print("Copied List:", List)