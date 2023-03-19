from linked_lists.linked_list import SinglyLinkedList
from arrays.random_array import Array

if __name__ == '__main__':
    numbers = Array(5)
    numbers.__random_fill__()
    print("The array numbers is: ")
    for i in range(numbers.__len__()):
        print(numbers[i])

    # Transfer data in a single linked list
    list_array = SinglyLinkedList()
    for number in numbers.__iter__():
        list_array.append(number)

    # Print the single linked list
    print("The single linked list is: \n")
    list_array.show()

    

