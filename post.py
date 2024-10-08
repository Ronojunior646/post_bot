import pyautogui
import time
import pyperclip

def send_message():
    pyautogui.hotkey('ctrl', 'v')  # Paste the message
    pyautogui.press('enter')  # Send the message
    time.sleep(0.3)  # Wait for the message to be sent

    pyautogui.press('enter')  # Optional second enter press

def main():
    time.sleep(10)  # Wait for 10 seconds to focus on the target application
    message = "🛑🛑READY TO DOMINATE? GET INSIDER STRATEGIES AND TIPS FROM OUR EXPERTS. CONTACT:/share_bet:5306339213"
    pyperclip.copy(message)  # Copy the message to the clipboard
    max_iterations = 100  # Set a reasonable number of iterations for testing
    for _ in range(1000000000):
        send_message()
        time.sleep(1)  # Wait for 1 second between messages to avoid overwhelming the application

if __name__ == "__main__":
    main()
    




