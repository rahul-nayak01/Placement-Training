def get_positive_integer():
    while True:
        try:
            number=int(input("ENter  a number"))
            if number <=0:
                raise ValueError("NOt a positive integer!")
            return number
        except ValueError as e:
            print("Error:".e)

positive_integer=get_positive_integer()
print("You entered positive integer:",positive_integer)
                             
                    