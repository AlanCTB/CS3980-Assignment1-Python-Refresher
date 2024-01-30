# CS3980 Assignment 1 Python Refresher
 
 0. Create a GitHub Repository
If you are new to GitHub, you can follow this tutorial to create a repository.

https://docs.github.com/en/repositories/creating-and-managing-repositories/quickstart-for-repositoriesLinks to an external site.

This repository will include a Readme.md file, a few screenshot images about your code and output, and your Python code.

The Readme.md file is critical in grading. Please document your assignment work with screenshots about your code and output, and pay attention to formatting the Readme.md file.

If you are new to writing Markdown file, you can read this tutorial.

https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntaxLinks to an external site.

 

1. Python Programming Basics
Create a Python script file named as echo.py. The echo.py file contains a method to imitate a real-world echo. The method signature should follow the code snippet below.
01-1.png
The method echo() has two input parameters: text is a string which represents what you yelled at a mountain; repetitions is an integer which represents the number of times that the mountain echoes your voice.
The method echo() returns a string which represents the echoed sound with fading effect. A couple of example outputs are as follows.
   $ python echo.py
   Yell something at a mountain: Helloooo
   ooo
   oo
   o
   .
   $ python echo.py
   Yell something at a mountain: echo 123
   123
   23
   3
   .
2. Python Decorator Implementation
Create a Python script file named as fib.py. The fib.py file contains a method to calculate Fibonacci sequence. The method signature should follow the code snippet below.
01-2.png
The method fib() will compute the nth Fibonacci number in a recursive manner. The calculation time will increase tremendously by increasing the value of n.

To optimize the execution time, you would like to use a lru_cache decorator from a Python package functools. For Python 3.12, the package functools is already included in Python. If you don't have this package (which I strongly recommend you to uninstall your old Python, and install a latest Python interpreter), then the functools package can be installed using the following command:
pip install functools
You also need to implement a timer decorator to check the execution time. In the end, the output should be something similar to the following:
    Finished in 0.00000070s: f(1) -> 1
    Finished in 0.00000130s: f(0) -> 0
    Finished in 0.00045070s: f(2) -> 1
    Finished in 0.00050900s: f(3) -> 2
    Finished in 0.00063150s: f(4) -> 3
    Finished in 0.00069030s: f(5) -> 5
    ... # omitted for simplicity
    Finished in 0.00819690s: f(98) -> 135301852344706746049
    Finished in 0.00825210s: f(99) -> 218922995834555169026
    Finished in 0.00831470s: f(100) -> 354224848179261915075
You can take the timing for each execution and plot them in a graph. You should get something similar to the following image.
fib.png
In the image above, x-axis represents the n in Fibonacci number calculation, and y-axis represents the time in seconds.
You should include your plot in your repository and display it in the Readme.md file. It would be even better if you can add a couple of sentences to explain the plot.
