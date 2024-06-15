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

