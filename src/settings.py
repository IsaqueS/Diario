import tomllib
from pathlib import Path

class Settings():
    def __init__(self) -> None:
        with open("res/defaults.toml", "rb") as file:
            self.data = tomllib.load(file)
            # print(self.data)

            if self.data.get("path", None):
                for path in self.data["path"].keys():
                    new_path = self.data["path"][path]
                    new_path = Path(new_path).expanduser().absolute()
                    self.data["path"][path] = new_path
            
            print(self.data)
        
    def __getitem__(self, arg):
        return self.data[arg]

settings = Settings()