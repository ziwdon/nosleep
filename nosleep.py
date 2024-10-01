import ctypes
import time
import msvcrt  # For detecting key presses

# Constants from the Windows API
ES_CONTINUOUS       = 0x80000000
ES_SYSTEM_REQUIRED  = 0x00000001
ES_DISPLAY_REQUIRED = 0x00000002

# Constants for mouse events
MOUSEEVENTF_LEFTDOWN  = 0x0002    # Left button down
MOUSEEVENTF_LEFTUP    = 0x0004    # Left button up
MOUSEEVENTF_RIGHTDOWN = 0x0008    # Right button down
MOUSEEVENTF_RIGHTUP   = 0x0010    # Right button up

def click_mouse(click_type):
    if click_type == 'left':
        # Simulate left mouse button click
        ctypes.windll.user32.mouse_event(MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
        ctypes.windll.user32.mouse_event(MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
        print("[Info] Left mouse button clicked.")
    elif click_type == 'right':
        # Simulate right mouse button click
        ctypes.windll.user32.mouse_event(MOUSEEVENTF_RIGHTDOWN, 0, 0, 0, 0)
        ctypes.windll.user32.mouse_event(MOUSEEVENTF_RIGHTUP, 0, 0, 0, 0)
        print("[Info] Right mouse button clicked.")
    else:
        # No click performed
        pass

def prevent_sleep():
    # Prevent sleep and display off
    ctypes.windll.kernel32.SetThreadExecutionState(
        ES_CONTINUOUS | ES_SYSTEM_REQUIRED | ES_DISPLAY_REQUIRED)

def restore_settings():
    # Restore default behavior
    ctypes.windll.kernel32.SetThreadExecutionState(ES_CONTINUOUS)

def nosleep(click_type):
    try:
        print("\nPress 'Ctrl+C' or 'ESC' to stop the script.\n")
        while True:
            prevent_sleep()
            if click_type != 'none':
                click_mouse(click_type)
            # Sleep in small intervals and check for ESC key press
            for _ in range(60):  # Total sleep time of 60 seconds
                time.sleep(1)
                if msvcrt.kbhit():
                    key = msvcrt.getch()
                    if key == b'\x1b':  # ESC key
                        raise KeyboardInterrupt
    except KeyboardInterrupt:
        restore_settings()
        print("\n[Info] Sleep prevention stopped.")
        time.sleep(3)

if __name__ == "__main__":
    print("=== Sleep Prevention Script ===")
    print("This script will prevent your computer from sleeping.")
    print("Which mouse click would you like the script to perform?")
    print("1. Left Click")
    print("2. Right Click")
    print("3. No Click")
    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        click_type = 'left'
        print("\n[Info] Automated left mouse button clicks will be performed.")
    elif choice == '2':
        click_type = 'right'
        print("\n[Info] Automated right mouse button clicks will be performed.")
    elif choice == '3':
        click_type = 'none'
        print("\n[Info] No mouse clicks will be performed.")
    else:
        click_type = 'none'
        print("\n[Warning] Invalid input. No mouse clicks will be performed.")

    nosleep(click_type)
