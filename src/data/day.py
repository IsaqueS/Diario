import tomli_w, uuid
from pathlib import Path
from datetime import datetime, timezone
from src.settings import settings

class Day():
    def __init__(self, message: str, emotion: str, media: tuple[Path,...] | None = None) -> None:
        assert isinstance(message, str), "MESSAGE IS NOT STRING!"
        assert isinstance(emotion, str), "EMOTION IS NOT STRING!"

        self.message: str = message
        self.emotion: str = emotion
        self.time: datetime = datetime.now(timezone.utc)
    
    def write(self) -> None:
        data_to_save = {

            "id": str(uuid.uuid4()),
            "version": settings["app"]["save-version"],
            
            "data": {
                "message": self.message,
                "emotion": self.emotion,
                "time": self.time
            }
            
        }

        toml_str: str = tomli_w.dumps(data_to_save,multiline_strings=True) + "\n\n# Diary app made By IsaqueS"

        # print(toml_str)

        save_folder: Path = settings["path"]["save"] / str(self.time.year) / str(self.time.month) / str(self.time.day)
        file_path = save_folder / settings["file-name"]["day"]

        # print(save_folder)

        save_folder.mkdir(parents=True, exist_ok=True)

        with open(file_path, "w", encoding="utf8") as file:
            file.write(toml_str)
