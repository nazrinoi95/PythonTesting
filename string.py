str = "RahulShettyAcademy.com"
str1 = "Consulting firm"
str3 = "Rahulshetty"

print (str[1]) # if print like this it will print index 1 of the string
print (str[0:5])# get 1 to 4
print (str + str1)

# Validation of string
print (str3 in str)

# Splitting the string dekat mana
var = str.split(".")
print (var)
print (var[0])

# Trim = untuk buang white spaces

str4 = " great "
print (str4.strip())
print (str4.lstrip())
print (str4.rstrip())