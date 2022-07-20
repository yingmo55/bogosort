import random
import time

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

def generate_random_array(length, smallest=0, largest=50):
    new_array = []
    for i in range(length):
        random_number = random.randint(smallest, largest)
        while random_number in new_array:
            random_number = random.randint(smallest, largest)
        new_array.append(random_number)
    return new_array


num_array = generate_random_array(6)
print(num_array)

def bogo_sort(array):
    sort_count = 0
    while not check_is_sorted(array):
        array = randomize_array(array)
        sort_count += 1
        print(f"array is not sorted! current array: {array}. Currently sorted {sort_count} times")
        #time.sleep(1)
    
    print(f'array is now sorted after {sort_count} tries: {array}')

bogo_sort(num_array)