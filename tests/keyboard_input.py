import sys

sys.path.insert(0, '')

from keyboard_input import KeyboardInput

keyboard_input = KeyboardInput()

while True:
    events = keyboard_input.events()

    if events:
        print(events)