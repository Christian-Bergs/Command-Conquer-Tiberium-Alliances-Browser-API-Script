import sys
import subprocess
import time
import pychrome

def start_chrome():
    try:
        if sys.platform.startswith('win'):  # Windows
            chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
        elif sys.platform.startswith('linux'):  # Linux
            chrome_path = '/usr/bin/google-chrome'
        elif sys.platform.startswith('darwin'):  # macOS
            chrome_path = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
        subprocess.Popen([chrome_path, r"--remote-debugging-port=9222"])
        time.sleep(5)
    except FileNotFoundError:
        print("[Error] Chrome wurde nicht gefunden. Stelle sicher, dass Chrome installiert ist und der Pfad korrekt ist.")
        sys.exit(1)


def initialize_browser():
    print('[DEV] Initialisiere pychrome mit dem Chrome Browser Debugging Modus (Port: 9222)')
    browser = pychrome.Browser(url="http://localhost:9222")
    try:
        tabs = browser.list_tab()
        if not tabs:
            print("[Dev] Keine Tabs gefunden. Stelle sicher, dass ein Tab geöffnet ist.")
            sys.exit(1)
        return browser, tabs[0]
    except Exception as e:
        print(f"[Error] Fehler beim Abrufen der Tabs: {e}")
        sys.exit(1)
