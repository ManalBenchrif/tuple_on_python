#A tuple is a collection which is ordered and unchangeable=immutable . 
tuple_1=("manal","sanae","dina","salwa","jaydae","najlae","asmae") #we start by index 0
print(tuple_1)

#Access Tuple Items
print("print out item where index=2: ",tuple_1[2])

#Negative Indexing :Negative indexing means beginning from the end, -1 refers to the last item.
print("print out item where index=-3: ",tuple_1[-3]) #index :-3 refer to jaydae

#Range of Indexes: 
#You can specify a range of indexes by specifying where to start and where to end the range.
#when specifying a range, the return value will be a new tuple with the specified items.
new_tuple1=tuple_1[1:5] # The search will start at index 1 (included) and end at index 5 (not included).
print("new tuple from 1 to : ",new_tuple1) 

#Range of Negative Indexes: Specify negative indexes if you want to start the search from the end of the tuple:
print("negative index: ",tuple_1[-7:-3])

#Change Tuple Values: Once a tuple is created, you cannot change its values.But there is a workaround. 
  #1.Convert the tuple into a list
  #2. change the list
  #3.and convert the list back into a tuple.
tuple_to_liste = list(tuple_1)
tuple_to_liste[1] = "betty"  #change sanae to betty
liste_to_tuple= tuple(tuple_to_liste)
print("tuple after change: ",liste_to_tuple)

#Loop Through a Tuple: using for loop
tuple2=[1,5,70,-9]
for i in tuple2:
    print(i)

#Check if Item Exists: use the in keyword:
if input("enter a nbr: ") in tuple2:
    print("yes! the item exist")
else:
    print("the item doesn't exist")

#Tuple Length:how many items a tuple has? use len() function
print("tuple2 has %d item." %len(tuple2))

#Create Tuple With One Item: you have to add a comma after the item, otherwise Python will not recognize it as a tuple.
#this is a time: thanks to comma,
tuple3 = ("apple",)
print(type(tuple3)) #type() function allow you to know the class of any object in python

#NOT a tuple: no comma,
tuple3 = ("apple")
print(type(tuple3))

#Remove Items : Tuples are unchangeable, so you cannot remove items from it, but you can delete the tuple completely:
#The del keyword can delete the tuple completely:
tuple4=("python","java","php")
del tuple4
#print(tuple4) #out put: NameError: name 'tuple4' is not defined because tuple4 was deleted completely

#Join  Tuples: use the + operator:
t1=("doae","afaf")
t2=(7,-8,80,0,17,-8,4,8)
t3=("islam","daniel")
join_tuple=t1+t2+t3
print("Result of join tuples: ",join_tuple)

#The tuple() Constructor : the 2 way to make tuple
my_tuple=tuple(("big data","AI","ML"))  # note the double round-brackets
print(my_tuple)

#Tuple Methods: Python has two built-in methods that you can use on tuples.
    #count()	Returns the number of times a specified value occurs in a tuple
    #index()	Searches the tuple for a specified value and returns the position of where it was found
print(" 8 occurs %d time" %t2.count(8))
print("position of 17 is %d " %t2.index(17))