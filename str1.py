def string_reverse(str):
    rstr = ''
    i= len(str)
    while i>0:
        rstr = rstr+ str[i-1]
        i=i-1
    return rstr

ip_str= input("Enter a string to reverse")
reversed_string=string_reverse(ip_str)
print("Reversed string: ", reversed_string)