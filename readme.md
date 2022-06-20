# Installation and configuration of Python with Visual Studio Code
## First steps
Before all, you should execute the Visual Studio as administrator to install the things you will need. 

https://code.visualstudio.com/docs/python/python-tutorial

You need to have installed python interpreter and have configurate the environment variables (you have an option)

https://www.python.org/downloads/


Another extension for visual studio, which you will need is Python.

## The environment

To create the fizzbuzz project, we need to create an enviroment. You can open a new terminal => Terminal->New Terminal and write:

```
python -m venv venv
```

This action will create a folder with your enviroment where you will have you libraries. 

After this, we need to activate the environment. 

a) For a terminal of "Command prompt"
```
venv\Scripts\Activate.bat
```
b) For power shell
```
Set-ExecutionPolicy Unrestricted
```

You will know you are in the environment because you will see something like this:
```
(venv) c:\workspace\python\python_fizzbuzz>

```
For more information:
https://code.visualstudio.com/docs/python/environments#:~:text=Select%20and%20activate%20an%20environment,Ctrl%2BShift%2BP).

with Visual Studio Code you can open the Command Palette (Ctrl+Shift+P) and "Python:Create a terminal". This terminal will open with the environment by default.

Also, you will need to select the python interpreter using the command palette. You should select the python in you enviroment.

To test the enviroment you could create a python file with a hello world. For example, creating a file "main.py" with the following line:
``` python
print ("hello world")
```

From the terminal you could write:
```
python main.py
```

To execute main.py from Visual Studio Code you can select the "main.py" file and with context menu: "Run the python file in Terminal"

## Configuration of the debugger
You only have to set a break point and select: Run-> Start Debugging
With Run->Add configuration you could add an special configuration to run the file.

# unit tests configuration
You should install for example pytest.
```
pip install pytest
```

With pip you can install every library you need. In the case you want to unistall some library:
```
pip uninstall <library>
```

Pytest needs your tests are in a folder which must be start with "test_" or their files must finished 
with "_test.py"
https://realpython.com/pytest-python-testing/

For example, we are going to create a file fizzbuzz_test.py to create the test.

# The Kata FizzBuzz
Start with TDD and create a parametrized Test. The Kata is the following:
https://katalyst.codurance.com/fizzbuzz
## Introduction
This kata, taken from a popular children's maths game (or student drinking game), is the starting point on the TDD track. It's designed to be a semi-guided first stop for learning TDD from scratch.

We'll emphasise the following:

Start by writing a failing test for the simplest behaviour.
Implement the simplest amount of code needed to make the test pass.
As you add more tests, refactor to make the code more generic and more suitable.
## Instructions
Write a function that takes positive integers and outputs their string representation.

Your function should comply with the following additional rules:

If the number is a multiple of three, return the string "Fizz".
If the number is a multiple of five, return the string "Buzz".
If the number is a multiple of both three and five, return the string "FizzBuzz".
For example, given the numbers from 1 to 15 in order, the function would return:
```
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
```

# During the Kata...

* You should upgrade pip if you need "python -m pip install --upgrade pip"
* You must create a .gitignoreç
* You must create a git repository "git init"
* You can execute test with the command "pytest"
* You can install the extension Python test 
* You will need to install the extension autopep8 in order to format the code. Shortcut: Shift+Alt+F
* You will need to know, refactoring shortcuts: Shift+Alt+R
* You will need to know how to rename a symbol: F2
* For refactoring, you could install the Sourcery extension: https://docs.sourcery.ai/IDEs/VSCode/
* You will need to know some shortcuts:
  * Ctrl+Shift+K = delete line
  * Alt + UP = move line up
  * Alt + Down = move line down