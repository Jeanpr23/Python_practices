import keyboard


keyboard.hook_key(78, lambda e: keyboard.press_and_release("backspace"))

keyboard.wait()