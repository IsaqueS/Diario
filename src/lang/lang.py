import json
from pathlib import Path
from kivy.event import EventDispatcher
from kivy.logger import Logger
from kivy.properties import DictProperty

lang_path = Path("src/lang/")

class Lang(EventDispatcher):

    strings = DictProperty({})

    def __init__(self) -> None:
        self.switch_language()

    def switch_language(self):
        self.text: dict[str,str] = {}

        with open(lang_path / "pt.json", "r", encoding="utf8") as file:
            self.text = json.load(file)
        
        Logger.info("Switch langiages")
    def __call__(self, id: str) -> str:
        return self.text.get(id,id)

if __name__ == "__main__":
    import csv, os

    with open(lang_path / "lang.csv", "r", encoding="utf8") as file:
        reader = csv.reader(file,delimiter=";")
        # print("FIle")

        languages = next(reader)
        languages = languages[1:]
        # print(languages)

        text  = {}

        for language in languages:
            text[language] = {}

        # print(text)

        for row in reader:
            # print(row)
            for id in range(1,len(row)):
                text[languages[id -1]][row[0]] = row[id]
        
        for language_text in text.keys():
            with open(lang_path / f"{language_text}.json", "w", encoding="utf8") as file:
                json.dump(text[language_text], file,separators=(',', ':'), ensure_ascii=False)

        def remove_language(path: Path) -> None:
            if not path.stem in languages:
                os.remove(path)
                print("Removed: %s"%path.stem)

        [remove_language(item) for item in lang_path.rglob("*.json")]

        print("Lang file updated!")


