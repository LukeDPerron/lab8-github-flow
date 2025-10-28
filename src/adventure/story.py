from adventure.utils import read_events_from_file
import random
from rich import print
from rich.style import Style
from rich.console import Console

default_message = "You stand still, unsure what to do. The forest swallows you."

def step(choice: str, events):
    random_event = random.choice(events)

    if choice == "left":
        return left_path(random_event)
    elif choice == "right":
        return right_path(random_event)
    else:
        return default_message

def left_path(event):
    return "You walk left. " + "[red]" + event

def right_path(event):
    return "You walk right. " + "[green]" + event

if __name__ == "__main__":
    events = read_events_from_file('events.txt')

    print("You wake up in a dark forest. You can go left or right.")
    while True:
        console = Console()
        choice = console.input("[italic bold blue]Which direction do you choose? (left/right/exit): [/italic bold blue]")
        choice = choice.strip().lower()
        if choice == 'exit':
            print("goodbye again")
            break
        
        print(step(choice, events))
