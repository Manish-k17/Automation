
# # # import pywhatkit as kit
# # # import time
# # # import pyautogui
# # # # from pynput.keyboard import Key, Controller

# # # # keyboard = Controller()

# # # # Global variable to track if WhatsApp Web is already open
# # # whatsapp_open = False

# # # def send_whatsapp_message_in_same_tab(phone_no, message):
# # #     """
# # #     Send WhatsApp message in already open WhatsApp Web tab using pyautogui.
# # #     Assumes WhatsApp Web is already open and logged in.
# # #     """
# # #     try:
# # #         # Focus WhatsApp Web tab (you may need to Alt+Tab or manually click it)
# # #         time.sleep(1)
# # #         pyautogui.hotkey('ctrl', 'f')  # Use 'ctrl+f' to activate browser find (optional)
# # #         time.sleep(0.5)

# # #         # Click on the WhatsApp search bar manually or set coordinates below using pyautogui.position()
# # #         # pyautogui.click(x=200, y=150)  # <-- adjust based on your screen
# # #         time.sleep(1)
        
# # #         # Type number or name to search
# # #         pyautogui.write(phone_no)
# # #         time.sleep(2)
# # #         pyautogui.press('enter')  # Open the chat
# # #         time.sleep(1)
        
# # #         # Write and send message
# # #         pyautogui.write(message)
# # #         time.sleep(0.5)
# # #         pyautogui.press('enter')

# # #         print("Message sent successfully!")
# # #         return True

# # #     except Exception as e:
# # #         print(f"Error sending message: {e}")
# # #         return False

# # # # The rest of your functions (get_message, get_phone_number, get_time_input, get_repeat_count)
# # # # remain the same as they handle user input and are independent of the sending mechanism.

# # # def get_message():
# # #     """Get message from user"""
# # #     while True:
# # #         message = input("Enter the Message: ").strip()
# # #         if message:
# # #             return message
# # #         print("Message cannot be empty!")

# # # def get_phone_number():
# # #     """Get valid phone number from user"""
# # #     while True:
# # #         try:
# # #             number = input("Enter the Phone number (with country code, e.g., +911234567890): ").strip()
# # #             if not number.startswith('+'):
# # #                 print("Please include country code (e.g., +91)")
# # #                 continue
# # #             # Simple validation - you might want to add more
# # #             if len(number) < 12:
# # #                 print("Phone number too short!")
# # #                 continue
# # #             return number
# # #         except Exception as e:
# # #             print(f"Invalid input: {e}")
# # #             get_phone_number()
            

# # # def get_time_input():
# # #     """Get time from user if they want to schedule"""
# # #     while True:
# # #         choice = input("Do you want to schedule the message? (yes/no): ").lower()
# # #         if choice in ['yes', 'no']:
# # #             if choice == 'yes':
# # #                 while True:
# # #                     try:
# # #                         hour = int(input("Enter hour (24-hour format): "))
# # #                         if 0 <= hour <= 23:
# # #                             break
# # #                         print("Hour must be between 0-23")
# # #                     except ValueError:
# # #                         print("Please enter a valid number")
                
# # #                 while True:
# # #                     try:
# # #                         minute = int(input("Enter minute: "))
# # #                         if 0 <= minute <= 59:
# # #                             break
# # #                         print("Minute must be between 0-59")
# # #                     except ValueError:
# # #                         print("Please enter a valid number")
                
# # #                 return hour, minute
# # #             else:
# # #                 return None, None

# # # def get_repeat_count():
# # #     """Get how many times to send the message"""
# # #     while True:
# # #         try:
# # #             count = int(input("How many times to send the message? (1-100): "))
# # #             if 1 <= count <= 100:
# # #                 return count
# # #             print("Please enter between 1-100")
# # #         except :
# # #             print("Please enter a valid number")

# # # def main():
# # #     print("WhatsApp Message Sender")
# # #     print("Note: Please ensure you're logged in to WhatsApp Web in your default browser")
# # #     print("Keep the browser open but don't touch your keyboard/mouse during sending\n")
    
# # #     phone_number = get_phone_number()
# # #     message = get_message()
# # #     hour, minute = get_time_input()
# # #     repeat_count = get_repeat_count()
    
# # #     success_count = 0
# # #     for i in range(repeat_count):
# # #         print(f"\nAttempt {i+1} of {repeat_count}")
        
# # #         try:
# # #             if hour is not None and minute is not None:
# # #                 # For scheduled messages, pywhatkit will still open a new tab
# # #                 kit.sendwhatmsg(phone_number, message, hour, minute)
# # #             else:
# # #                 # For instant messages, use the modified function
# # #                 if not send_whatsapp_message_in_same_tab(phone_number, message):
# # #                     continue
            
# # #             success_count += 1
            
# # #             # Small delay between messages
# # #             if i < repeat_count - 1:
# # #                 time.sleep(2) # Give WhatsApp Web a moment to process the previous message
                
# # #         except Exception as e:
# # #             print(f"Failed to send message: {e}")
    
# # #     print(f"\nSummary: Sent {success_count}/{repeat_count} messages successfully")
    
# # #     if input("\nSend more messages? (yes/no): ").lower() == 'yes':
# # #         main()

# # # if __name__ == "__main__":
# # #     main()

# # import pyautogui
# # import time
# # import os

# # def send_whatsapp_message(contact_name, message):
# #     os.system("start whatsapp:")  # opens WhatsApp Desktop
# #     time.sleep(5)

# #     pyautogui.hotkey('ctrl', 'f')  # search bar
# #     time.sleep(1)
# #     pyautogui.write("Manish")
# #     time.sleep(1)
# #     pyautogui.press('Down')  # select the contact
# #     time.sleep(1)
# #     pyautogui.press('enter')
# #     time.sleep(1)

# #     pyautogui.write("Hi")
# #     pyautogui.press('enter')

# # send_whatsapp_message("Your Contact Name", "Hello from Python!")

# # send_whatsapp_message("Manish", "Hello from Python!")  # Replace with your contact name

# import pyautogui
# import time
# import os
# import requests
# import webbrowser
# import screen_brightness_control as sbc
# from ctypes import cast, POINTER
# from comtypes import CLSCTX_ALL
# from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume


# # ✳️ Function to get Groq response
# def get_groq_response(prompt, groq_api_key):
#     headers = {
#         "Authorization": f"Bearer {groq_api_key}",
#         "Content-Type": "application/json"
#     }
#     body = {
#         "messages": [{"role": "user", "content": prompt}],
#         "model": "llama3-8b-8192"  # ✅ Use updated model
#     }

#     response = requests.post("https://api.groq.com/openai/v1/chat/completions", json=body, headers=headers)

#     try:
#         json_data = response.json()
#         print("[DEBUG] Groq Response:", json_data)
#         return json_data["choices"][0]["message"]["content"]
#     except Exception as e:
#         print("[ERROR] Invalid Groq response:", response.text)
#         raise e


# # ✳️ Function to execute actions
# def execute_task(response):
#     response = response.lower()
#     print(f"[INFO] Task from AI: {response}")

#     # WhatsApp message
#     if "whatsapp" in response and "send" in response:
#         try:
#             contact = "Manish"  # You can improve this with LLM parsing
#             message = "He is mental"

#             print("[INFO] Opening WhatsApp...")
#             os.system("start whatsapp:")  # Open WhatsApp desktop
#             time.sleep(5)

#             pyautogui.hotkey('ctrl', 'f')  # Focus on search
#             time.sleep(1)
#             pyautogui.write(contact)
#             pyautogui.press('enter')
#             time.sleep(1)

#             pyautogui.write(message)
#             pyautogui.press('enter')

#         except Exception as e:
#             print(f"[WARN] WhatsApp Desktop failed. Opening in browser: {e}")
#             webbrowser.open("https://web.whatsapp.com")

#     # Instagram messages
#     elif "instagram" in response and ("open" in response or "read" in response):
#         print("[INFO] Opening Instagram DMs...")
#         webbrowser.open("https://www.instagram.com/direct/inbox/")
#         time.sleep(5)

#     # Search something on Chrome
#     elif "search" in response:
#         search_term = response.split("search")[-1].strip()
#         print(f"[INFO] Searching on Google: {search_term}")
#         webbrowser.open(f"https://www.google.com/search?q={search_term}")
#         time.sleep(3)

#     # Increase/Decrease Volume
#     elif "volume" in response:
#         try:
#             devices = AudioUtilities.GetSpeakers()
#             interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
#             volume = cast(interface, POINTER(IAudioEndpointVolume))

#             if "increase" in response or "up" in response:
#                 volume.SetMasterVolumeLevelScalar(1.0, None)  # max
#             elif "decrease" in response or "down" in response:
#                 volume.SetMasterVolumeLevelScalar(0.2, None)
#             elif "mute" in response:
#                 volume.SetMute(1, None)
#             elif "unmute" in response:
#                 volume.SetMute(0, None)

#             print("[INFO] Volume updated.")
#         except Exception as e:
#             print(f"[ERROR] Volume control failed: {e}")

#     # Adjust Brightness
#     elif "brightness" in response:
#         try:
#             if "increase" in response or "up" in response:
#                 sbc.set_brightness(100)
#             elif "decrease" in response or "down" in response:
#                 sbc.set_brightness(20)
#             print("[INFO] Brightness updated.")
#         except Exception as e:
#             print(f"[ERROR] Brightness control failed: {e}")

#     # Other unsupported tasks
#     else:
#         print("[INFO] Sorry, this task is not yet supported.")


# # ✳️ Main program loop
# if __name__ == "__main__":
#     groq_api_key = "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"  # 🔐 Replace with your actual key

#     print("🔵 AI Assistant Ready. Type 'exit' to stop.\n")

#     while True:
#         user_input = input("🗣️ What should I do? ").strip()
#         if user_input.lower() in ["exit", "quit"]:
#             print("👋 Goodbye!")
#             break

#         try:
#             groq_reply = get_groq_response(user_input, groq_api_key)
#             print("🤖 Groq AI says:", groq_reply)
#             execute_task(groq_reply)
#         except Exception as e:
#             print(f"[ERROR] Something went wrong: {e}")

import os
import time
import webbrowser
import pyautogui
import requests
import json
import subprocess
from typing import Optional

# Configuration
GROQ_API_KEY = "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"  # Replace with your actual Groq API key
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"  # Updated endpoint

class GroqAutomation:
    def __init__(self):
        self.groq_headers = {
            "Authorization": f"Bearer {GROQ_API_KEY}",
            "Content-Type": "application/json"
        }
        pyautogui.FAILSAFE = True
        self.screen_width, self.screen_height = pyautogui.size()
        
    def query_groq(self, prompt: str) -> Optional[str]:
        """Send a prompt to Groq API and return the response."""
        data = {
            "messages": [{"role": "user", "content": prompt}],
            "model": "mixtral-8x7b-32768",
            "temperature": 0.7,
            "max_tokens": 1024
        }
        
        try:
            response = requests.post(GROQ_API_URL, headers=self.groq_headers, json=data)
            response.raise_for_status()
            result = response.json()
            return result['choices'][0]['message']['content']
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
            print(f"Response content: {response.text}")  # Debug info
        except Exception as e:
            print(f"Error querying Groq API: {e}")
        return None
    
# #     def open_app(self, app_name: str) -> bool:
# #         """Open an application by name."""
# #         apps = {
# #             'whatsapp': ['WhatsApp.exe', 'https://web.whatsapp.com'],
# #             'instagram': ['Instagram.exe', 'https://www.instagram.com/direct/inbox'],
# #             'chrome': ['chrome.exe', None],
# #             'settings': ['ms-settings:', None]  # Windows settings URI
# #         }
        
# #         app = apps.get(app_name.lower())
# #         if not app:
# #             print(f"Unknown app: {app_name}")
# #             return False
        
# #         # Try to open native app
# #         try:
# #             if os.name == 'nt':  # Windows
# #                 if app_name.lower() == 'settings':
# #                     os.startfile(app[0])
# #                 else:
# #                     subprocess.Popen(app[0])
# #                 time.sleep(3)  # Wait for app to open
# #                 return True
# #             else:  # Mac/Linux
# #                 # Add platform-specific commands here
# #                 if app_name.lower() == 'settings':
# #                     subprocess.Popen(['gnome-control-center'])  # Ubuntu example
# #                 else:
# #                     subprocess.Popen(['open', '-a', app[0]])  # Mac example
# #                 time.sleep(3)
# #                 return True
# #         except Exception as e:
# #             print(f"Couldn't open native app: {e}")
        
# #         # Fall back to web version
# #         if app[1]:
# #             webbrowser.open(app[1])
# #             time.sleep(5)  # Wait for page to load
# #             return True
        
# #         return False
    
# #     def send_whatsapp_message(self, contact: str, message: str) -> bool:
# #         """Send a WhatsApp message."""
# #         if not self.open_app('whatsapp'):
# #             return False
        
# #         try:
# #             # Wait for WhatsApp to load
# #             time.sleep(5)
            
# #             # Search for contact (Ctrl+F in web WhatsApp)
# #             pyautogui.hotkey('ctrl', 'f')
# #             time.sleep(1)
# #             pyautogui.write(contact)
# #             time.sleep(2)
# #             pyautogui.press('enter')
# #             time.sleep(2)
            
# #             # Type and send message
# #             pyautogui.write(message)
# #             pyautogui.press('enter')
# #             return True
# #         except Exception as e:
# #             print(f"Error sending WhatsApp message: {e}")
# #             return False
    
# #     def adjust_system_setting(self, setting: str, value: int) -> bool:
# #         """Adjust system settings like volume or brightness."""
# #         try:
# #             setting = setting.lower()
# #             if setting == 'volume':
# #                 # Windows volume control
# #                 for _ in range(abs(value)):
# #                     if value > 0:
# #                         pyautogui.press('volumeup')
# #                     else:
# #                         pyautogui.press('volumedown')
# #                     time.sleep(0.1)
# #                 return True
            
# #             elif setting == 'brightness':
# #                 if os.name == 'nt':  # Windows
# #                     self.open_app('settings')
# #                     time.sleep(2)
# #                     pyautogui.write('brightness')
# #                     time.sleep(1)
# #                     pyautogui.press('enter')
# #                     time.sleep(1)
# #                     # Adjust brightness - this will depend on your screen
# #                     for _ in range(value):
# #                         pyautogui.press('right')
# #                     return True
# #                 else:  # Mac/Linux
# #                     print("Brightness adjustment requires platform-specific implementation")
# #                     return False
            
# #             elif setting in ['wifi', 'bluetooth', 'airplane mode']:
# #                 self.open_app('settings')
# #                 time.sleep(2)
# #                 pyautogui.write(setting)
# #                 time.sleep(1)
# #                 pyautogui.press('enter')
# #                 time.sleep(1)
# #                 pyautogui.press('space')  # Toggle setting
# #                 return True
            
# #             else:
# #                 print(f"Unknown setting: {setting}")
# #                 return False
                
# #         except Exception as e:
# #             print(f"Error adjusting system setting: {e}")
# #             return False
    
# #     def automate_task(self, task_description: str) -> str:
# #         """Automate a task based on natural language description."""
# #         # First, ask Groq to interpret the task
# #         prompt = f"""Analyze this task and respond with ONLY a JSON object containing:
# # - "action": one of ["send_message", "read_messages", "system_setting", "open_app"]
# # - "app": optional, app name if applicable
# # - "target": optional, contact name or setting name
# # - "value": optional, message content or setting value
# # - "confidence": your confidence in this interpretation (0-1)

# # Task: {task_description}"""
        
# #         response = self.query_groq(prompt)
# #         if not response:
# #             return "Failed to connect to Groq API. Please check your API key and internet connection."
        
# #         try:
# #             task = json.loads(response.strip())
# #             print(f"Interpreted task: {task}")
            
# #             if task.get('confidence', 0) < 0.7:
# #                 return "I'm not confident enough to perform this task"
            
# #             if task['action'] == 'send_message' and 'app' in task and 'target' in task and 'value' in task:
# #                 if task['app'].lower() == 'whatsapp':
# #                     success = self.send_whatsapp_message(task['target'], task['value'])
# #                     return "Message sent successfully" if success else "Failed to send message"
# #                 else:
# #                     return f"Messaging not implemented for {task['app']}"
            
# #             elif task['action'] == 'system_setting' and 'target' in task and 'value' in task:
# #                 success = self.adjust_system_setting(task['target'], task['value'])
# #                 return f"Adjusted {task['target']} successfully" if success else f"Failed to adjust {task['target']}"
            
# #             elif task['action'] == 'open_app' and 'app' in task:
# #                 success = self.open_app(task['app'])
# #                 return f"Opened {task['app']} successfully" if success else f"Failed to open {task['app']}"
            
# #             else:
# #                 return "Couldn't execute this task"
                
# #         except json.JSONDecodeError:
# #             return "Failed to parse Groq's response. The API might be unavailable."
# #         except KeyError as e:
# #             return f"Missing information in task interpretation: {e}"
# #         except Exception as e:
# #             return f"Error executing task: {e}"

# # # Example usage with better error handling
# # if __name__ == "__main__":
# #     automator = GroqAutomation()
    
# #     # Test Groq API connection first
# #     test_query = automator.query_groq("Hello")
# #     if not test_query:
# #         print("""
# #         Groq API connection failed. Please check:
# #         1. Your GROQ_API_KEY is correct
# #         2. You have internet connection
# #         3. The Groq API is currently available
# #         """)
# #         exit(1)
    
# #     # Example tasks
# #     tasks = [
# #         "Send a WhatsApp message to John saying hello",
# #         "Increase volume by 3 levels",
# #         "Turn on airplane mode",
# #         "Open Instagram"
# #     ]
    
# #     for task in tasks:
# #         print(f"\nExecuting: '{task}'")
# #         result = automator.automate_task(task)
# #         print(f"Result: {result}")
# #         time.sleep(2)
