#given array of int and num cake find countof distsnt ele in every window of size key of array.

def main():
    arr = [1, 2, 1, 3, 4, 2, 3]
    key = 3
    window_count(arr, key)


def window_count(arr, key):
    for i in range(len(arr) - key + 1):
        window = arr[i:i + key]

        print(window)

if __name__ == '__main__':
    main()

#equlibrium index is index such that sum of ele at lower index is equal to sumof  index at higher indices ex- array[-7,1,2,-4,3,0] o/p is 3
#else if no such point exists return -1