import re

def extract_first_session(log_file_path):
    try:
        with open(log_file_path, 'r') as file:
            content = file.read()
            session_match = re.search(r"var SessionId='([a-zA-Z0-9\-]+)';", content)
            if session_match:
                session_value = session_match.group(1)
                print(f"[Info] Erster gefundener Session-Wert: {session_value}")
                return session_value
            else:
                print("Kein Session-Wert gefunden.")
    except FileNotFoundError:
        print("Die angegebene Log-Datei wurde nicht gefunden.")
    except Exception as e:
        print(f"Es ist ein Fehler aufgetreten: {e}")
