import sys
import json
import threading

# def custom_threading_excepthook(args):
#     if isinstance(args.exc_value, json.JSONDecodeError):
#         print("[Warning] JSONDecodeError während des Empfangs ignoriert.")
#     else:
#         sys.__excepthook__(args)

def custom_threading_excepthook(args):
    # Ignoriere JSONDecodeError vollständig
    if not isinstance(args.exc_value, json.JSONDecodeError):
        sys.__excepthook__(args)

# Setze Excepthook direkt nach dem Import der Module
threading.excepthook = custom_threading_excepthook
