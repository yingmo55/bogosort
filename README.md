# Bogosort in Python

The infamous sorting algorithm that first check if the array is sorted from beginning to end. If two nearby elements are not sorted, it shuffles the array and then check again if it is sorted.

## Running this ~~abomination~~ Masterpiece on Your Machine 

1. First, ensure you have Python 3.6 and above installed because I used f string in the script.

2. Second, you can either execute the script by typing `./bogo_sort.py` in the terminal after navigating to the folder, or double click on the file to execute it.

3. Follow the prompts to enter the array size, and the number ranges.

### Warning & Disclaimer
I set a 1 second interval between each shuffle to prevent high CPU usage. 
Disabling it in the script may cause high CPU usage and overheat your machine. Only disable it when you are certain your machine can handle the calculation. *Do it at your own risk.*


## How does it work under the hood?

The shuffle function uses an algorithm called "[Fisher-Yates shuffle](https://en.wikipedia.org/wiki/Fisher%E2%80%93Yates_shuffle)". It randomly picks an element in the array to swap with the first element, and the picked element will not be selected for swapping again. It repeats the process until it reaches the end of the array.

### But doesn't Python's `random` module comes with a shuffle method?

I wanted to practice writing Fisher–Yates shuffle.

### Limitations
Currently it relies on Python's `random` module to generate a random number for swapping the array entries. While it gets the job done, I don't fully understand the algorithm under the hood, which means this may not be true random.

## But why?

Why not?

This is my 2nd favorite "joke" sorting algorithm that I can implement in code.  
My top favorite "joke" algorithm is [miracle sort](https://www.thecshandbook.com/Miracle_Sort), and I unfortunately cannot (and probably will not be able to) implement one that *can successfully sort an array*, due to the nature of said algorithm.

## Feedback on Improving the Code? Questions? Comments?

Please submit an issue if you have and feedback or comments.

## Reference & Further reading
[Slow sorting: Stooge sort and Bogo sort](https://youtu.be/bfzYj-qGw7U?t=2316) by [udiprod](https://www.youtube.com/c/udiprod)  

[Bogosort](https://en.wikipedia.org/wiki/Bogosort)

[Fisher-Yates shuffle](https://en.wikipedia.org/wiki/Fisher%E2%80%93Yates_shuffle) on Wikipedia
