#Input a word or sentence
string = input("Please enter a word : ")
string2 = ('')
#loop for printing in reverse
for i in string:
    string2 = i + string2
print("The Original string =", string)
print("The Reversed string =", string2)