from AppOpener import close, open as appopen
from webbrowser import open as webopen
from pywhatkit import search, playonyt, sendwhatmsg_instantly
from dotenv import dotenv_values
from bs4 import BeautifulSoup
from rich import print
from groq import Groq
import webbrowser
import subprocess
import requests
import keyboard
import asyncio
import os
import pyautogui
import time
import platform
import json # Import json for parsing

# --- NEW IMPORTS FOR IMAGE GENERATION ---
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, WebDriverException
# ----------------------------------------

# env_vars = dotenv_values(".env")
# GroqAPIKey = env_vars.get("GroqAPIKey")
# WhatsAppNumber = env_vars.get("WhatsAppNumber") # Added for WhatsApp
GroqAPIKey = "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"
WhatsAppNumber = "+919876543210" # Replace with an actual number or load from .env

classes = ["zCubwf", "hgKELc", "LTKOO SY7ric", "ZOLcW", "gsrt vk_bk FzvWSb YwPhnf", "pclqee", "tw-Data-text tw-text-small tw-ta",
           "IZ6rdc", "05uR6d LTKOO", "vlzY6d", "webanswers-webanswers_table_webanswers-table", "dDoNo ikb4Bb gsrt", "sXLa0e",
           "LWkfKe", "VQF4g", "qv3Wpe", "kno-rdesc", "SPZz6b"]

useragent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36'

# Initialize Groq client only if API key exists
client = None
if GroqAPIKey:
    client = Groq(api_key=GroqAPIKey)

professional_responses = [
    "Your satisfaction is my top priority; feel free to reach out if there's anything else I can help you with.",
    "I'm at your service for any additional questions or support you may need—don't hesitate to ask.",
]

messages = []

SystemChatBot = [{"role": "system", "content": f"Hello, I am {os.environ.get('Username', 'User')}, a content writer. You have to write content like letters, codes, applications, essays, notes, songs, poems, etc."}]


def GoogleSearch(topic):
    search(topic)
    return True


def Content(topic):
    def OpenNotepad(file):
        try:
            default_text_editor = 'notepad.exe'
            subprocess.Popen([default_text_editor, file])
            return True
        except Exception as e:
            print(f"Error opening notepad: {e}")
            return False

    def ContentWriterAI(prompt):
        if not client:
            print("Error: Groq API key not found. Please check your .env file.")
            return "Error: Unable to generate content - API key missing."
        
        try:
            messages.append({"role": "user", "content": f"{prompt}"})

            completion = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=SystemChatBot + messages,
                max_tokens=2048,
                temperature=0.7,
                top_p=1,
                stream=True,
                stop=None
            )

            answer = ""

            for chunk in completion:
                if chunk.choices[0].delta.content:
                    answer += chunk.choices[0].delta.content

            answer = answer.replace("</s>", "")
            messages.append({"role": "assistant", "content": answer})
            return answer
        except Exception as e:
            print(f"Error generating content: {e}")
            return f"Error: Unable to generate content - {str(e)}"

    topic = topic.replace("content", "").strip()
    content_by_ai = ContentWriterAI(topic)

    # Create Data directory if it doesn't exist
    data_dir = "Data"
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
        print(f"Created directory: {data_dir}")

    filepath = os.path.join(data_dir, f"{topic.lower().replace(' ', '_')}.txt")
    
    try:
        with open(filepath, "w", encoding="utf-8") as file:
            file.write(content_by_ai)
        print(f"Content written to: {filepath}")
        
        OpenNotepad(filepath)
        return True
    except Exception as e:
        print(f"Error writing content to file: {e}")
        return False

def YouTubeSearch(topic):
    url = f"https://www.youtube.com/results?search_query={topic}"
    webbrowser.open(url)
    return True


def PlayYoutube(query):
    try:
        playonyt(query)
        return True
    except Exception as e:
        print(f"Error playing YouTube video: {e}")
        return False


def OpenApp(app, sess=requests.session()):
    """
    Attempts to open an application locally using AppOpener.
    If AppOpener fails, it falls back to searching and opening via Chrome.
    """
    try:
        print(f"Attempting to open '{app}' using AppOpener (local search)...")
        appopen(app, match_closest=True, output=True, throw_error=True)
        print(f"Successfully opened '{app}' locally.")
        return True

    except Exception as e:
        print(f"AppOpener failed to open '{app}' locally: {e}. Falling back to web search...")
        
        def extract_links(html):
            if html is None:
                return []
            soup = BeautifulSoup(html, 'html.parser')
            links = soup.find_all('a', href=True)
            return [link.get('href') for link in links]
            
        def search_microsoft(query):
            url = f"https://www.microsoft.com/en-us/search?q={query}"
            headers = {"User-Agent": useragent}
            try:
                response = sess.get(url, headers=headers, timeout=10)
                if response.status_code == 200:
                    return response.text
                else:
                    print(f"Failed to retrieve search results from Microsoft (Status: {response.status_code}).")
                    return None
            except requests.exceptions.RequestException as req_e:
                print(f"Network error during Microsoft search for '{query}': {req_e}")
                return None

        def open_in_chrome_beta(url):
            """Open URL specifically in Google Chrome Beta, fallback to stable Chrome, then default."""
            system = platform.system()
            chrome_paths = []

            if system == "Windows":
                chrome_paths = [
                    r"C:\Program Files\Google\Chrome Beta\Application\chrome.exe",
                    os.path.expanduser(r"~\AppData\Local\Google\Chrome Beta\Application\chrome.exe"),
                    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
                    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
                    os.path.expanduser(r"~\AppData\Local\Google\Chrome\Application\chrome.exe")
                ]
            elif system == "Darwin":  # macOS
                chrome_paths = ["/Applications/Google Chrome Beta.app/Contents/MacOS/Google Chrome Beta", "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"]
            elif system == "Linux":
                chrome_paths = ["google-chrome-beta", "google-chrome"]

            for path in chrome_paths:
                try:
                    if system == "Windows" and os.path.exists(path):
                        subprocess.Popen([path, url])
                        print(f"Opened '{url}' in Chrome/Chrome Beta via explicit path.")
                        return True
                    elif system in ["Darwin", "Linux"]:
                        subprocess.Popen([path, url])
                        print(f"Opened '{url}' in Chrome/Chrome Beta via command.")
                        return True
                except FileNotFoundError:
                    continue
                except Exception as ex:
                    print(f"Error opening with specific Chrome path '{path}': {ex}")
                    continue

            print("Chrome/Chrome Beta not found via common paths. Opening in default browser.")
            webbrowser.open(url)
            return True

        print(f"Attempting web search for '{app}'...")
        html = search_microsoft(app)
        if html:
            links = extract_links(html)
            if links:
                for link in links:
                    if app.lower() in link.lower() and ("download" in link.lower() or "app" in link.lower() or "store" in link.lower()):
                        print(f"Found potentially relevant link: {link}")
                        open_in_chrome_beta(link)
                        return True
                if links:
                    print(f"No specific app download link found, opening first search result: {links[0]}")
                    open_in_chrome_beta(links[0])
                    return True
            else:
                print(f"No links found in web search results for '{app}'.")
        else:
            print(f"Web search for '{app}' returned no HTML content.")
        return False
    
def CloseApp(app):
    if "chrome" in app.lower():
        try:
            subprocess.run(["taskkill", "/f", "/im", "chrome.exe"], check=True, creationflags=subprocess.DETACHED_PROCESS)
            print(f"Closed all Chrome processes using taskkill.")
            return True
        except subprocess.CalledProcessError as e:
            print(f"Taskkill failed for Chrome: {e}")
        except Exception as e:
            print(f"Error during Chrome taskkill: {e}")
            
    try:
        close(app, match_closest=True, output=True, throw_error=True)
        print(f"Closed {app} using AppOpener")
        return True
    except Exception as e:
        print(f"Error closing {app}: {e}. App might not be running or AppOpener couldn't find it.")
        return False


def System(command):
    def mute():
        keyboard.press_and_release("volume mute")

    def unmute():
        keyboard.press_and_release("volume mute")

    def volume_up():
        keyboard.press_and_release("volume up")

    def volume_down():
        keyboard.press_and_release("volume down")

    try:
        if command == "mute":
            mute()
        elif command == "unmute":
            unmute()
        elif command == "volume up":
            volume_up()
        elif command == "volume down":
            volume_down()
        else:
            print(f"Unknown system command: {command}")
            return False
        
        print(f"Executed system command: {command}")
        return True
    except Exception as e:
        print(f"Error executing system command {command}: {e}")
        return False

def WhatsApp(message):
    """
    Sends a WhatsApp message instantly to a predefined number.
    The 'sendwhatmsg_instantly' function from pywhatkit handles opening WhatsApp Web
    and sending the message.
    """
    if not WhatsAppNumber:
        print("Error: WhatsApp number not configured. Please set 'WhatsAppNumber' in your .env file.")
        return False
    
    try:
        print(f"Sending WhatsApp message: '{message}' to {WhatsAppNumber}")
        sendwhatmsg_instantly(WhatsAppNumber, message, wait_time=20, tab_close=True, close_time=5) 
        print("WhatsApp message sent successfully.")
        return True
    except Exception as e:
        print(f"Error sending WhatsApp message: {e}. Common issues: WhatsApp Web not logged in, browser focus, slow internet, multiple monitors.")
        return False

def GenerateImage(prompt: str, save_directory="GeneratedImages"):
    """
    Generates an image using a free online AI image generator (e.g., Craiyon/DALL-E mini)
    and attempts to save it.

    NOTE: This function is highly dependent on the target website's structure.
    It's an example and will require frequent updates if the website changes.
    You MUST inspect the website and update the locators.
    """
    
    # URL of a free AI image generator (Example: Craiyon's simplified interface)
    # >>> CRITICAL: YOU MIGHT NEED TO CHANGE THIS URL AND THE LOCATORS BELOW <<<
    IMAGE_GENERATOR_URL = "https://www.craiyon.com/" # As of July 2024, this is a working example.

    if not os.path.exists(save_directory):
        os.makedirs(save_directory)
        print(f"Created directory: {save_directory}")

    driver = None
    try:
        print(f"Attempting to generate image for prompt: '{prompt}' on {IMAGE_GENERATOR_URL}")
        
        # Initialize Chrome WebDriver
        options = webdriver.ChromeOptions()
        # options.add_argument("--headless") # Uncomment for headless browser (no GUI)
        options.add_argument("--log-level=3") # Suppress console logs
        options.add_experimental_option("detach", True) # Keep browser open after script finishes (useful for debugging)
        
        driver = webdriver.Chrome(options=options)
        driver.maximize_window()
        driver.get(IMAGE_GENERATOR_URL)

        # --- LOCATORS FOR CRAIYON (AS OF JULY 2024 - SUBJECT TO CHANGE) ---
        PROMPT_INPUT_SELECTOR = "textarea[placeholder*='Enter your prompt'], input[placeholder*='Enter your prompt'], #promptInput"
        GENERATE_BUTTON_XPATH = "//button[contains(., 'Draw')] | //button[contains(., 'Generate')] | //button[@id='generateButton']"
        IMAGE_ELEMENT_SELECTOR = "div.grid.grid-cols-3.gap-2.mt-4 img, #gallery img, .image-grid img"
        DOWNLOAD_BUTTON_XPATH = "//button[contains(., 'Download Image')]"
        # ------------------------------------------------------------------
        
        # Wait for the prompt input field
        prompt_input = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, PROMPT_INPUT_SELECTOR))
        )
        print("Found prompt input field.")
        prompt_input.send_keys(prompt)
        print("Typed prompt into input field.")
        
        # Find and click the generate button
        generate_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, GENERATE_BUTTON_XPATH))
        )
        print("Found generate button.")
        generate_button.click()
        print("Clicked generate button. Waiting for image...")

        # Wait for the images to load. This can take a while.
        first_image = WebDriverWait(driver, 90).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, IMAGE_ELEMENT_SELECTOR))
        )
        print("First image element detected and is visible.")
        time.sleep(3)

        try:
            download_button = driver.find_element(By.XPATH, DOWNLOAD_BUTTON_XPATH)
            print("Found a dedicated download button. Clicking it...")
            download_button.click()
            time.sleep(5)
            print("Download button clicked. Check your browser's download folder.")
            return True
        except NoSuchElementException:
            print("No dedicated download button found. Attempting direct image URL download.")
            image_src = first_image.get_attribute("src")
            if image_src and image_src.startswith("http"):
                print(f"Attempting to download image from: {image_src}")
                try:
                    response = requests.get(image_src, stream=True, timeout=30)
                    if response.status_code == 200:
                        filename = "".join(c for c in prompt if c.isalnum() or c in (' ', '_')).replace(' ', '_').lower()[:50]
                        filepath = os.path.join(save_directory, f"{filename}_{int(time.time())}.png")
                        with open(filepath, 'wb') as f:
                            for chunk in response.iter_content(8192):
                                f.write(chunk)
                        print(f"Image saved successfully to: {filepath}")
                        return True
                    else:
                        print(f"Failed to download image from {image_src}. Status code: {response.status_code}.")
                except requests.exceptions.RequestException as req_e:
                    print(f"Network error during direct image download: {req_e}")
            else:
                print(f"Image src '{image_src}' is not a valid direct URL for download.")

            print("Direct image URL download failed or not applicable. Image generation command may not have fully succeeded.")
            return False

    except WebDriverException as wd_e:
        print(f"WebDriver error: Ensure Chromedriver is correctly installed and its version matches your Chrome browser. Error: {wd_e}")
        return False
    except TimeoutException:
        print("Timeout: Element not found or image generation took too long. Check locators and internet connection.")
        return False
    except NoSuchElementException:
        print("No such element: The website structure might have changed. Please inspect the website and update the locators.")
        return False
    except Exception as e:
        print(f"An unexpected error occurred during image generation: {e}")
        return False
    finally:
        if driver:
            print("Browser session finished (may remain open if 'detach' option is true or for debugging).")
            # driver.quit() # Uncomment to force close browser


# --- MODIFIED get_task_details FUNCTION ---
def get_task_details(user_input, groq_api_key):
    headers = {
        "Authorization": f"Bearer {groq_api_key}",
        "Content-Type": "application/json"
    }
    
    # Updated prompt to define the new JSON structure
    prompt = f"""
You are a smart assistant. Analyze the user's request and extract the necessary details into a JSON object.
Focus on identifying the core command type and its specific parameters.

Available command types and their parameters:
- "open_app": {{ "app_name": "string" }} (e.g., "open notepad")
- "close_app": {{ "app_name": "string" }} (e.g., "close chrome")
- "whatsapp_message": {{ "message_content": "string" }} (sends to a predefined number) (e.g., "send whatsapp message saying hello")
- "play_youtube": {{ "query": "string" }} (e.g., "play despacito on youtube")
- "Google Search": {{ "query": "string" }} (e.g., "google search for latest news")
- "Youtube": {{ "query": "string" }} (e.g., "Youtube for funny cats")
- "generate_content": {{ "topic": "string" }} (e.g., "write an essay on AI", "content about quantum physics")
- "generate_image": {{ "prompt": "string" }} (e.g., "create an image of a futuristic city", "make an image of a red dragon")
- "system_command": {{ "command": "string" }} (e.g., "mute volume", "volume up", "unmute", "volume down")

If the input does not match any of the above, return {{ "command_type": "unrecognized" }}.
Only return valid JSON with no explanation or extra text.

Input: "{user_input}"

Return JSON in this format:
{{
  "command_type": "string",
  "app_name": "string (if open/close app)",
  "message_content": "string (if whatsapp message)",
  "query": "string (if play/search youtube/google)",
  "topic": "string (if generate content)",
  "prompt": "string (if generate image)",
  "command": "string (if system command)"
}}
"""

    body = {
        "model": "llama3-8b-8192", # Using a smaller model for faster responses, can switch to 70b
        "messages": [{"role": "user", "content": prompt}],
        "response_format": {"type": "json_object"} # Ensure JSON output
    }

    try:
        response = requests.post("https://api.groq.com/openai/v1/chat/completions", headers=headers, json=body, timeout=15) # Added timeout
        response.raise_for_status() # Raise an exception for HTTP errors
        json_string = response.json()["choices"][0]["message"]["content"]
        # Groq might sometimes wrap the JSON in markdown code blocks, try to parse it
        if json_string.startswith("```json") and json_string.endswith("```"):
            json_string = json_string[7:-3].strip()
        
        return json.loads(json_string) # Parse the JSON string into a Python dictionary
    except requests.exceptions.RequestException as e:
        print(f"API request failed: {e}")
        return {"command_type": "error", "message": f"API request failed: {e}"}
    except json.JSONDecodeError as e:
        print(f"Failed to decode JSON from API response: {e}\nRaw response content: {json_string}")
        return {"command_type": "error", "message": f"Invalid JSON response: {e}"}
    except KeyError as e:
        print(f"Unexpected API response structure: Missing key {e}\nRaw response: {response.json()}")
        return {"command_type": "error", "message": f"Unexpected API response: Missing data."}


async def TranslateAndExecute(commands_data: list[dict]): # Accepts list of dicts now
    funcs = []

    for command_detail in commands_data: # Iterate through the parsed command details
        command_type = command_detail.get("command_type")
        
        print(f"Processing command type: {command_type} with details: {command_detail}")
        
        if command_type == "open_app":
            app_name = command_detail.get("app_name")
            if app_name: funcs.append(asyncio.to_thread(OpenApp, app_name))
        elif command_type == "close_app":
            app_name = command_detail.get("app_name")
            if app_name: funcs.append(asyncio.to_thread(CloseApp, app_name))
        elif command_type == "whatsapp_message":
            message_content = command_detail.get("message_content")
            if message_content: funcs.append(asyncio.to_thread(WhatsApp, message_content))
        elif command_type == "play_youtube":
            query = command_detail.get("query")
            if query: funcs.append(asyncio.to_thread(PlayYoutube, query))
        elif command_type == "Google Search":
            query = command_detail.get("query")
            if query: funcs.append(asyncio.to_thread(GoogleSearch, query))
        elif command_type == "Youtube":
            query = command_detail.get("query")
            if query: funcs.append(asyncio.to_thread(YouTubeSearch, query))
        elif command_type == "generate_content":
            topic = command_detail.get("topic")
            if topic: funcs.append(asyncio.to_thread(Content, topic))
        elif command_type == "generate_image":
            prompt = command_detail.get("prompt")
            if prompt: funcs.append(asyncio.to_thread(GenerateImage, prompt))
        elif command_type == "system_command":
            command = command_detail.get("command")
            if command: funcs.append(asyncio.to_thread(System, command))
        elif command_type == "unrecognized":
            print(f"Unrecognized command: {command_detail}. No action will be taken.")
        elif command_type == "error":
            print(f"Error parsing command: {command_detail.get('message', 'Unknown error')}")
        else:
            print(f"Unknown command_type encountered: {command_type}")

    if funcs:
        results = await asyncio.gather(*funcs, return_exceptions=True)
        for i, result in enumerate(results):
            if isinstance(result, Exception):
                print(f"Command {i+1} failed with exception: {result}")
            else:
                print(f"Command {i+1} result: {result}")
            yield result
    else:
        print("No valid commands to execute")


async def Automation(commands: list[str]): # `commands` here is still raw user input strings
    print(f"Starting automation with raw commands: {commands}")
    parsed_commands = []
    for cmd_str in commands:
        # Here's where get_task_details is called to parse each command string
        parsed_detail = get_task_details(cmd_str, GroqAPIKey)
        parsed_commands.append(parsed_detail)
        print(f"Parsed '{cmd_str}' into: {parsed_detail}")

    results = []
    # Now pass the list of parsed command details to TranslateAndExecute
    async for result in TranslateAndExecute(parsed_commands):
        results.append(result)
    print(f"Automation completed. Results: {results}")
    return True


if __name__ == "__main__":
    test_commands = [
        "open notepad",
        # "send whatsapp message saying how are you doing to chiku?",
        "write content about the history of the internet",
        "google search for latest AI trends",
        "play bohemian rhapsody on youtube",
        "create an image of a cute robot playing chess",
        "system volume up",
        "close chrome",
        "tell me a joke" # This should be unrecognized
    ]
    
    print("Testing automation with Groq parsing...")
    asyncio.run(Automation(test_commands))