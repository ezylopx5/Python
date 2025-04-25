# Write a program that asks the user to enter a word and then capitalizes every other letter of that word.
# So, if the user enters rhinoceros, the program should print rHiNoCeRoS.

# lets take a input from the user
word = str(input("Enter the word: "))
l = len(word)
list_ = list(word)
for i in range(1,l):
    if i % 2 != 0:
        list_[i] = list_[i].capitalize()


word_ = "".join(list_) #SO we can convert list to string
print(word_)


    

