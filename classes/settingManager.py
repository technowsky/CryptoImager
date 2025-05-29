import json
import os
from pathlib import Path

class settingManager:
    _instance = None
    _settings_path = "setting.json"



    def __init__(self):
        raise 'Singleton class. Call function ".get_instance()" method'
    
    def get_instance(cls):
        if cls._instance == None:
            cls._instance = cls.__new__(cls)
            cls._instance._load_settings()
        return cls._instance

 
    def _load_settings(self):
        try:
            with open(self._settings_path, "r") as f:
                self._json_settings = json.load(f)
                print(self._json_settings)
        except:
            self._json_settings = {
                "save_dir": str(Path("./").resolve()) + os.sep,
                "coding_method": 0,  # 0 - diagonal, 1 - From first to last, 2 - "Random", 3 - "Spiral from center"
                "save_custom_name": 1, # 0 - global, 1 - Ask every time, 2 - Same as selected image
                "save_prefix": ""
            }
            with open(self._settings_path, "w") as f:
                json.dump(self._json_settings, f)
        
    def __str__(self):
        print(self._json_settings)



        


test = settingManager().get_instance()
print(test)