import time
import requests
import pyautogui
import pyperclip

from pynput import keyboard

IS_MAC = False
ALL_KEYS = ['ctrl', 'a'] if not IS_MAC else ['command', 'a']
COPY_KEYS = ['ctrl', 'c'] if not IS_MAC else ['command', 'c']
PASTE_KEYS = ['ctrl', 'v'] if not IS_MAC else ['command', 'v']
DELETE_KEY = ['del']

PLACEHOLDER_TEXT = "Translating"
PLACEHOLDER_LEN = len(PLACEHOLDER_TEXT)

def translate_with_llm(text: str) -> str:
    url = "http://localhost:1234/v1/chat/completions"
    payload = {
        "messages": [
            {
                "role": "user",
                "content": text
            }
        ]
    }
    headers = {"Content-Type": "application/json"}

    try:
        resp = requests.post(url, json=payload, headers=headers)
        resp.raise_for_status()
        data = resp.json()

        raw_content = data["choices"][0]["message"]["content"]

        marker = '</think>\n\n'
        if marker in raw_content:
            parts = raw_content.rsplit(marker, 1)
            raw_content = parts[-1].strip()

        return raw_content.strip()

    except Exception as e:
        return f"[Error: {e}]"


def on_activate():
    pyautogui.hotkey(*ALL_KEYS)
    time.sleep(0.3)
    pyautogui.hotkey(*COPY_KEYS)
    time.sleep(0.3)
    selected_text = pyperclip.paste().strip()
    print(selected_text)

    if not selected_text:
        return
    
    pyautogui.typewrite(PLACEHOLDER_TEXT)

    translation = translate_with_llm(selected_text)

    translation_table = str.maketrans('', '', '"¿?!¡')

    translation = translation.translate(translation_table)

    lines = translation.split('\\n') 

    pyautogui.hotkey(*ALL_KEYS)
    time.sleep(0.3)

    for line in lines:
        pyperclip.copy(line)
        pyautogui.hotkey(*PASTE_KEYS)
        time.sleep(0.5)

        pyautogui.press('enter')
        time.sleep(0.5)

        pyautogui.press('enter')
        time.sleep(0.5)

hotkey = keyboard.HotKey(
    keyboard.HotKey.parse('<alt>+t'),
    on_activate
)

def for_canonical(f):
    return lambda k: f(listener.canonical(k))

if __name__ == "__main__":
    with keyboard.Listener(
        on_press=for_canonical(hotkey.press),
        on_release=for_canonical(hotkey.release)
    ) as listener:
        listener.join()
