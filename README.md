# Bogosort

The infamous sorting algorithm that first check if the array is sorted from beginning to end. If two nearby elements are not sorted, it shuffles the array and then check again if it is sorted.

## Running this on your Local Machine 

First, ensure you have Python 3.6 and above installed because I used f string in the script.

Second, you can either execute the script by typing `./bogo_sort.py` in the terminal after navigating to the folder, or double click on the file to execute it.

Follow the prompts to enter the array size, and the number ranges.

### Warning & Disclaimer
I set a 1 second interval between each shuffle to mitigate high CPU usage. 
Disabling it in the script may cause high CPU usage and overheat your machine. Only disable it when you are certain your machine can handle the calculation & *do it at your own risk.*


## How does it work under the hood?


## Limitations
Currently it relies on Python's `random` module for generating a random number to swap the 

## But why?

Why not?

This is my 2nd favorite "joke" sorting algorithm that I can implement in code.  
My top favorite "joke" algorithm is miracle sort, and I unfortunately cannot (and probably will not be able to) implement one that can successfully sort an array, due to the nature of said algorithm.