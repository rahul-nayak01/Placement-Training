import random
def demonstrate_random_module():
    print("Random module demonstration:")

    print("\nrandom.random():")
    print(random.random())        #0.0 -1.0 float

    print("\nrandom.uniform(1,10):")
    print(random.uniform(1,10))      #float in range

    print("\nrandom.randint(1,10):")
    print(random.randint(1,10))                

    print("\nrandom.randrange(1,10,2):")
    print(random.randrange(1,10,2))

    my_list=[1,2,3,4,5]
    print("\nrandom.choice([1,2,3,4,5]):")
    print(random.choice(my_list))

    print("\nrandom.choices([1,2,3,4,5],k=3):")
    print(random.choices(my_list,k=3))

    print("\nrandom.choice([1,2,3,4,5], k=3):")
    print(random.sample(my_list, k=3))

    
    print("\nrandom.choice([1,2,3,4,5], k=3):")
    random.shuffle(my_list)
    print(my_list)

    print("\nrandom.seed(10) and random.random():")
    random.seed(10)
    print(random.random())

    print("\nrandom.getrandbits(5):")
    print(random.getrandbits(5))

    print("\nrandom.gauss(0,1):")
    print(random.gauss(0,1))

if __name__ == "__main__":
    demonstrate_random_module()
