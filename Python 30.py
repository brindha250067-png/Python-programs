list1 = [10, 20, 30, 40, 50]
key = int(input("Enter element to search: "))

for i in range(len(list1)):
    if list1[i] == key:
        print("Element found at position", i)
        break
else:
    print("Element not found")
