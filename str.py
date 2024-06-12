input_str=input("Enter a string:")

print(len(input_str))
print(input_str.upper())
print(input_str.isupper())
print(input_str.lower())
print(input_str.islower())
print(input_str.capitalize())
print(input_str.title())

substring = input("Enter a substring to count: ")
print(input_str.count(substring))

prefix=input("Enter a prefix")
print(input_str.startswith(prefix))

suffix=input("Enter a suffix")
print(input_str.endswith(suffix))
    
old_substring=input("Enter a substring")
new_substring=input("Enter a new substring")
print(input_str.replace(old_substring, new_substring))

delimiter=input("Enter a delimiter:")
print(input_str.split(delimiter))     #delimiter any space or character

substrings=input("Enter a substrings to join(separated by space) :").split()
join_delimiter=input("Enter a delimiter to join ")
print(join_delimiter.join(substrings)) # ''.join(substrings)

print(input_str.strip())
print(input_str.lstrip())
print(input_str.rsplit())
print(input_str.rjust())
print(input_str.rfind("l"))
print(input_str.rindex("l"))

age=36
name=input()
print(f"{name}")