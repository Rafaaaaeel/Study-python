wrd=input("Please enter a word")
rvs=wrd[::-1].capitalize()
print(rvs)
if wrd.capitalize() == rvs:
    print("This word is a palindrome")
else:
    print("This word is not a palindrome")
