import os
import math
import time
from rich import print
from rich.prompt import Prompt

if os.name == 'nt': # checks if the os is windows
 os.system('cls')
 os.system('title EasyCalculator 1.1')
else: # if the os is not windows then
 os.system('echo -ne "\033]0;EasyCalculator 1.1\007"')
 os.system('clear')
print("[bold red]Welcome to EasyCalculator 1.1!")
print("")
number1 = Prompt.ask("[yellow]Number 1")
number2 = Prompt.ask("[yellow]Number 2")
print("")
number1 = float(number1) # converts number1 to float
number2 = float(number2) # converts number2 to float
# calculations
result1 = float(number1) + float(number2)
result2 = float(number1) - float(number2)
result3 = float(number1) * float(number2)
result4 = float(number1) / float(number2)
result5 = math.sin(number1)
result6 = math.sin(number2)
result7 = math.cos(number1)
result8 = math.cos(number2)
result9 = math.tan(number1)
result10 = math.tan(number2)
result11 = math.sqrt(number1)
result12 = math.sqrt(number2)
# results
print("[bold blue]Addition: " + str(result1))
print("[bold blue]Subtraction: " + str(result2))
print("[bold blue]Multiplication: " + str(result3))
print("[bold blue]Division: " + str(result4))
print("[bold blue]The sin of number 1: " + str(result5))
print("[bold blue]The sin of number 2: " + str(result6))
print("[bold blue]The cos of number 1: " + str(result7))
print("[bold blue]The cos of number 2: " + str(result8))
print("[bold blue]The tan of number 1: " + str(result9))
print("[bold blue]The tan of number 2: " + str(result10))
print("[bold blue]The square root of number 1: " + str(result11))
print("[bold blue]The square root of number 2: " + str(result12))
# end
print("")
print("[bold red]The program will close in 10 seconds...")
time.sleep(10)
print("")
print("[bold red]Goodbye!")
exit()