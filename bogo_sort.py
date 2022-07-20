import random
import time



def generate_random_array(length, smallest, largest):
    new_array = []
    for i in range(length):
        random_number = random.randint(smallest, largest)
        while random_number in new_array:
            random_number = random.randint(smallest, largest)
        new_array.append(random_number)
    return new_array

def bogo_sort(array):
    def check_is_sorted(array):
        for i in range(1, len(array)):
            if not array[i - 1] <= array[i]:
                return False
        return True

    # Fisher–Yates shuffle
    def randomize_array(array):
        for i in range(len(array) - 1):
            swap = random.randrange(i, len(array))
            temp = array[i]
            array[i] = array[swap]
            array[swap] = temp
        return array

    sort_count = 0
    while not check_is_sorted(array):
        print(f"Array is not sorted! Current array: {array}. Currently sorted {sort_count} times")
        array = randomize_array(array)
        sort_count += 1
        time.sleep(1)
    
    print(f'Array is now sorted after {sort_count} tries: {array}')


def user_interface():
    array_size = -1
    while array_size < 1:
        try:
            array_size = int(input("how many numbers do you want in your array?\n"))
        except ValueError:
            print("Please enter a valid number\n")
        if array_size < 1:
            print("Please enter a number bigger than 0\n")


    def get_number(small_or_large):
        default = 0 if small_or_large == "smallest" else 50
    
        number = input(f"enter the {small_or_large} number in the array. default={default}\n")

        if not number:
            number = default
        else:
            success = False
            while not success:
                try:
                    int(number)
                    success = True
                except ValueError:
                    smallest = input('please enter a valid integer\n')
        return number
    
    smallest = get_number("smallest")
    largest = get_number("largest")


    new_array = generate_random_array(array_size, smallest, largest)

    print(f'Your randomly generated array is: {new_array}\n')

    bogo_sort(new_array)

user_interface()