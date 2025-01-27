import eel
import threading
# let me defend my self here i could easly write my own code here but i was running out of time so i had to use this code from the internet
# Define a function to stop the server
# if my mom saw me codeing instead of studying she would kill me
# i hope she dosent see this
# i hope i dont get caught
# pray for me  , Ameen
# Initialize the eel app

import math
import sys
from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel

console = Console()

def display_welcome():
    console.print(Panel("[bold cyan]Yes this CLI calc is AI generated![/bold cyan]\n[magenta]my account on X,Discord @0xMohammedKAM .[/magenta]\n[bold yellow]Supported operators: +, -, *, /, ^ (power)[/bold yellow]", expand=False))

def evaluate_expression(expression):
    try:
        # Replace '^' with '**' for Python's power operator
        expression = expression.replace('^', '**')
        result = eval(expression, {"__builtins__": None}, {
            "math": math,
            "sqrt": math.sqrt,
            "sin": lambda x: math.sin(math.radians(x)),
            "cos": lambda x: math.cos(math.radians(x)),
            "tan": lambda x: math.tan(math.radians(x)),
            "log": math.log,
        })
        return result
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed!"
    except Exception as e:
        return f"Error: Invalid expression! ({str(e)})"

def calculator():
    display_welcome()
    while True:
        expression = Prompt.ask("[bold green]Enter your calculation (or type 'exit' to quit)")
        if expression.lower() == 'exit':
            console.print("[bold cyan]Exiting the calculator. Goodbye!")
            sys.exit()
        result = evaluate_expression(expression)
        console.print(f"[bold yellow]Result:[/bold yellow] [bold green]{result}")

eel.init("web")
thread = threading.Thread(target=calculator)
thread.start()
eel.start("index.html" , port=9991)