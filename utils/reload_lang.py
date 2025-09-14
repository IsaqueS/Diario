import csv, os, tomli_w
from pathlib import Path

CSV_PATH = Path("utils/")
LANG_PATH = Path("res/lang")

if __name__ == "__main__":

    with open(CSV_PATH / "lang.csv", "r", encoding="utf8") as file:
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
            with open(LANG_PATH / f"{language_text}.toml", "w", encoding="utf8") as file:
                toml: str = tomli_w.dumps(text[language_text], multiline_strings=True)
                file.write(toml)

        def remove_language(path: Path) -> None:
            if not path.stem in languages:
                os.remove(path)
                print("Removed: %s"%path.stem)

        [remove_language(item) for item in CSV_PATH.rglob("*.toml")]

        print("Lang file updated!")