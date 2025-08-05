#A List of integers from user input and their sum
number = input ("Enter digital numbers separated by space: ")

NumList = [int (num) for num in number.split()]
nubsum = sum (NumList)

print ("The Sum of the Integers is: ", nubsum)


# Tuple of favourite books
TBooks = ("Bible", "Dictionary", "Corcondance", "Literatures", "Novel")

print ("My Favourite Books are:")
for Book in TBooks:
    print (Book)


# Collecting User Info and Store in a Dictionary
Dic = {}

Dic ['Name'] = input ("Enter your name: ")
Dic ['Age'] = input ("Enter your age: ")
Dic ['Color'] = input ("Enter your Favourite color: ")

print ("The Dictionary of Information Is: ", Dic)


# A Program the Accept User Input to Create Two Sets of Integers and New Set with elements in both sets
SetA_info = input ("Enter First Sets of Digital Numbers Separated by Space: ")
SetB_info = input ("Enter Second Sets of Digital Numbers Separated by Space: ")

SetA = set (map (int, SetA_info.split()))
SetB = set (map (int, SetB_info.split()))

SetC = SetA.intersection(SetB)
print ("The Common Elements in Both Sets are: ", SetC)


# A Program that Store Word List and New List with Words of Odd Number of Characters
Words = ["John", "Peterson", "Gabriel", "Jackson", "Paul"]

Odd_Words = [Word for Word in Words if len(Word) % 2 !=0]

print ("Words with Odd Number of Characters are: ", Odd_Words)