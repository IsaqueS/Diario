import json, locale, os
from pathlib import Path
from kivy.logger import Logger

LANG_PATH = Path("res/lang/")
DEFAULT_LANG = "en"

class Lang():
    def __init__(self) -> None:
        locate_info: tuple[str | None, str | None] = locale.getdefaultlocale()

        # lang_code will be something like 'en_US', 'pt_BR', etc.
        Logger.info(f"Detected language code: {locate_info[0]}")

        lang: str = "en"
        if locate_info[0]:
            lang = locate_info[0].split("_")[0]
        # lang = "jp" # to test language fall back
        
        self.switch_language(lang)

    def switch_language(self, lang: str):
        self.text: dict[str,str] = {}

        if not os.path.exists(LANG_PATH / f"{lang}.json"):
            Logger.warning(f"'{lang}' language code not found, using: {DEFAULT_LANG}")
            lang = DEFAULT_LANG

        with open(LANG_PATH / f"{lang}.json", "r", encoding="utf8") as file:
            self.text = json.load(file)
        
        Logger.info("Language selected: %s"%lang)
    def __call__(self, id: str) -> str:
        return self.text.get(id,id)




