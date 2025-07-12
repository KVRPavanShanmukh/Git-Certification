"""
list is something that is used to store multiple items in a single variable.
list is one of the 4 built in datatypes of Py for storing a collection of data.
the other three are tuple,set and dictionary.
list is a kind of array(indexing starts from zero) that can store elements of multiple types.
"""
this_list_is_private = ["a",5,True,0.007]
print(this_list_is_private)

#duplication is allowed
#items are ordered, and are always changeable. some methods of the list can change the order, but no used in geenral.

print(len(this_list_is_private))
print(type(this_list_is_private))

#list constructor
thislist = list(("a","b","c","d","e","f","g","h","i","j"))
print(thislist)
print(type(thislist))

#accessing the list items
print(this_list_is_private[0],this_list_is_private[3])
#negative indexing access:
print(this_list_is_private[-1]) #prints the last element in the list

#using the range function
print(thislist[1:3]) # 2 included and 5 excluded

#with no starting and ending points of range function:
print(thislist[1:])
print(thislist[:3])

#list access with negative indexes:
print(thislist[-7:-3])

#check the existence of an item in the list:
if "a" in thislist:
    print("Yes")

#new list for new example
#change the values of the list
nl = ["a","b","c","d","e","f","g","h","i","j","k","l"]
nl[-2] = 0 # We can replace a value of any datatype with a value in the list
nl[-1] = "z"
print(nl)

# If you add more items, only the items of that index are affected, other items move accordingly:
nl[5:6]= ["sai","sai rama"]
print(nl)

#If you insert less items than you replace, the new items will be
#inserted where you specified, and the remaining items will move accordingly:
nl[1:3]= ["shannu"]
print(nl)

#insert method
nl.insert(9, "watermelon")
print(nl)

#to add item at the end of the list, we use append method
nl.append("orange")
print(nl)

#list is being added to other list by extend function: appending a list
extendedlist=["avakaya","maagaya","gongoora","pudina","kobbari maammidi"]
nl.extend(extendedlist)
print(nl)

#removing the list items:
#remove():
newlist = ["avakaya","maagaya","gongoora","pudina","kobbari maammidi","beerakaya tomato","allam","palli","tomato ulli"]
newlist.remove("avakaya")
print(newlist)
#or
# to remove items base on indexes:
newlist.pop(3) #to remove elements on index basis.
del newlist[5] #to remove elements on index basis.
print(newlist)
newlist.pop()
print(newlist)

#clear the list:
newlist.clear()
print(newlist) #empty list is printed

#looping is completed in short. refer w3schools for this.
