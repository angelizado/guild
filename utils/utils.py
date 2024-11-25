import os
import sys
from rich.console import Console

console = Console()

def clear():
    if sys.platform.startswith('win'):
        os.system('cls')
    else:
        os.system('clear')

def welcome():
    console.print("[link=https://github.com/angelizado/guild]Guild Rotator[/link].", style="bold")
    console.print("[link=https://github.com/angelizado]@angelizado[/link] | 24/11/24", style="bold")
