import time

def handle_network_event(**kwargs):
    print("Network Event Captured")
    print("Event Type:", kwargs.get("type", "Unknown"))
    print("Request:", kwargs.get("request", {}))
    print("Response:", kwargs.get("response", {}))
    print("Additional Data:", kwargs)
    print("-" * 50)


# def print_page_source(tab, log_file):
#     try:
#         time.sleep(10)
#         result = tab.call_method("DOM.getDocument")
#         node_id = result['root']['nodeId']
#         html_data = tab.call_method("DOM.getOuterHTML", nodeId=node_id)
#         site_content = html_data['outerHTML']
#         with open(log_file, 'w', encoding='utf-8') as datei:
#             try:
#                 datei.write(site_content)
#                 print(f"[DEV] Schreibe Quelltext in Log Datei: '{log_file}'")
#             except Exception as e:
#                 print(f"[Error] Fehler beim Schreiben in Log Datei: {e}")
#     except Exception as e:
#         print(f"[Error] Fehler beim Abrufen des Quelltexts: {e}")

def print_page_source(tab, log_file):
    try:
        time.sleep(10)
        # Ruft den Quelltext der aktuellen Seite ab
        result = tab.call_method("DOM.getDocument")
        node_id = result['root']['nodeId']
        html_data = tab.call_method("DOM.getOuterHTML", nodeId=node_id)  # Verwende eindeutige Variablennamen
        print("[Dev] Quelltext der Seite:")
        
        site_content = html_data['outerHTML']  # Korrekt: Verwende das Modul
        
        # Optional: Speichere den Inhalt in einer Datei
        with open(log_file, 'w', encoding='utf-8') as datei:
            try:
                datei.write(site_content)
                print(f"[Dev] Schreibe Quelltext in Log Datei: '{log_file}'")
            except Exception as e:
                print(f"[Error] Fehler beim Schreiben in Log-Datei: {e}")
        
    except Exception as e:
        print(f"[Error] Fehler beim Abrufen des Quelltexts: {e}")
