import string
sentence= input("Enter a sentence")
Wordlist= sentence.strip().split(" ")
print(f"THE leng of word in sentence{len(Wordlist)}")
digit_count=uppercase_count=lowercase_count=0
for character in Wordlist:
    if character in string.digits:
        digit_count+=1
    elif character in string.ascii_uppercase:
        uppercase_count+=1
    elif character in string.ascii_lowercase:
        lowercase_count+=1

print(f"This sentence has {digit_count} digits",
      f"{uppercase_count} uppercase letters",
      f"{lowercase_count} lowercase letters",sep='\n')

#given array of int and num cake find countof distsnt ele in every window of size key of array.