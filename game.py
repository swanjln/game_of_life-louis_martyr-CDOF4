import numpy as np
import random
from board import Board
import keyboard
import time

def Run():
    max_gen = int(input("Enter the maximum number of generations (0 for unlimited): "))
    start = time.time()
    myboard = Board()
    stop = False
    while not keyboard.is_pressed('Escape') and (max_gen == 0 or myboard.generation < max_gen):
        if (time.time() - start) >= 0.5:
            print(myboard)
            myboard.Actualize()
            start = time.time()
    print("End of the iterations")
    # Prompt the user to press Enter to continue
    input("Press Enter to close the console...")

Run()
