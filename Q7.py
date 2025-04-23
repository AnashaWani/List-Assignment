# Adding elements in an Empty list in Python using Insert function based on user choice :

List=[]
# While True is used as a continous loop, till the condition for break is reached.
while True :
    i=int(input("Enter index/position of the element (-1 to stop):"))
    if i==-1:
        break
    v=input("Enter the value of the element:")
    List.insert(i,v)
    print("Updated List:",List)