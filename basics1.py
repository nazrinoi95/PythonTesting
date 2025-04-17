#How to print output
#print ("Ramadhan Mubarak")

# Variables does not need to inform what type int / float / string

"""
a = 3
print (a)
"""
# mix / concatenate string / int value output
"""
a = 3.2
b = "Teh o ais"
print("{} {} {}".format(b,"=",a))
"""

# telling type of variables
"""
a = 2.5
b = 1
c = "kjlkajsdlkfjladsjf"
d = True
print (type(a))
print (type(b))
print (type(c))
print (type(d))

"""

# List in Python
"""
values = [ 1, 2, 3, "nazrin" , 123]
print(values[3]) # nazrin
print(values[4]) # 123
print(values[-1]) # to call the last item in the list 123
print(values[1:4]) # to call index 1 to 4 but excluding 4, 2 3 "nazrin"
values.insert(1,"newly insert")
print(values)
values.append("Akhir") #append at the end of the list
print(values)

values[3]= "NAZRIN" #this is updating the values in the list
del values [1]
print (values)

"""

# Tuple in python (basically a list that cannot be edited)
"""
kan = (1, 2, 3, 3.4 , "what")
print (kan[1])
kan[4] = "WHAT" #If want to assign new values it will throw an error

"""

#Dictionary : basically unordered, indexed by keys eg:
"""
kam = {1:"nama", "umur":2.4, "tempat lahir": "Subang Jaya"}
print (kam["umur"])
"""

# Adding dictionary from an empty dic
"""
kam1 = {}
kam1 ["nama"] = "Nazrin"
kam1 ["nama bapa"] = "Othman Ali"
kam1 ["umur"] = 29
kam1 ["tarikh lahir"] = "27/12/1995"
print(kam1)
print(kam1["tarikh lahir"])
"""

# f way in formatting output

nama= ["list1","list2","list3", "List4"]
print(f"Nama orang kedua:{nama[1]}")
print (f"Nama orang pertama: {nama[0]}")
print (f"Nama orang last: {nama[-1]}")