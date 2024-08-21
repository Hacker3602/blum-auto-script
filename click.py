from pynput.mouse import Controller, Button
from pynput import keyboard
from PIL import ImageGrab

mouse = Controller()
running = True
tc1 = (129, 255, 41)
tc2 = (130, 221, 233)

def on_press(key):
    global running
    try:
        if key.char == 'c':
            running = False
            return False
    except AttributeError:
        pass

def find_color_and_click(target_colors, step=5, region=None):
    if region:
        screenshot = ImageGrab.grab(bbox=region)
    else:
        screenshot = ImageGrab.grab()
    
    width, height = screenshot.size
    for x in range(0, width, step):
        for y in range(0, height, step):
            pixel_color = screenshot.getpixel((x, y))[:3]
            if pixel_color in target_colors:
                mouse.position = (x + (region[0] if region else 0), y + (region[1] if region else 0))
                mouse.click(Button.left, 1)
                return True
    return False

if __name__ == "__main__":
    listener = keyboard.Listener(on_press=on_press)
    listener.start()
    print("[*] Blum Script started. Press 'c' to stop.")
    target_colors = [tc1, tc2]
    search_region = None
    while running:
        clicked = find_color_and_click(target_colors, step=5, region=search_region)
