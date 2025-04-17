#it will only enter if cond = TRUE and only exit once it is FALSE
it = 10

while it > 1:
    if it == 9:
        it = it -2
        continue # using continue will skip other part of loop an re-execute the while from the beginning
    if it == 3:
        break # using break will exit the while loop
    print(it)
    it = it - 1

print ("while loop done")


