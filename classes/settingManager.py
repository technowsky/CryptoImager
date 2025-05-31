import json
import os
from pathlib import Path


SETTINGS_PATH = Path("settings.json")
DEFAULT_JSON_SETTINGS = {                                           #defult data settings
            "save_dir": str(Path("./").resolve()) + os.sep,
            "coding_method": 0,  # 0 - diagonal, 1 - From first to last, 2 - "Random", 3 - "Spiral from center"
            "save_custom_name": 1, # 0 - global, 1 - Ask every time, 2 - Same as selected image
            "save_prefix": ""
        }

current_json_settings = DEFAULT_JSON_SETTINGS.copy()

def save_settings():
    global current_json_settings
    try:
        with open(SETTINGS_PATH, "w", encoding="utf-8") as f:
            json.dump(current_json_settings, f)
    except (IOError, PermissionError):
            print("Saving/Loading settings.json file failed due to permission error. Check creating file permissions.")


def load_settings():
    global current_json_settings

    try:
        with open(SETTINGS_PATH, "r", encoding="utf-8") as f:
            current_json_settings = json.load(f)
    except FileNotFoundError:
        save_settings()
    except (IOError, json.JSONDecodeError) as e:
        raise json.JSONDecodeError("Failed to decode json data from file")

def validate_settings():
    ...
    #for future validation of data in settings.json. Comperes setting.json data to  DEFAULT_JSON_SETTINGS

def display_settings():
    setting_keys = list(current_json_settings.keys())
    for setting_name in setting_keys:
        print(f"{setting_name} : {current_json_settings.get(setting_name)}")

def get_setting(key:str):
    if key not in current_json_settings:
        raise KeyError(f"{key} not found")
    return current_json_settings[key]

def set_setting(key:str, value):
    if key not in current_json_settings:
        raise KeyError(f"{key} not found")
    current_json_settings[key] = value

load_settings()     