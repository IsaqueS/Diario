from kivy.uix.widget import Widget
from kivy.app import App
from kivy.uix.popup import Popup
from kivy.properties import StringProperty
from kivy.uix.togglebutton import ToggleButton

from pathlib import Path
from datetime import datetime, timezone
import os, tomllib

from src.settings import settings
from src.data.day import Day

class WarningPopup(Popup):
    title = StringProperty("Titulo")
    message = StringProperty("Mensagem")

class Window(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.app: App = App.get_running_app() # type: ignore

        self.emotion_buttons: dict[str, ToggleButton] = {}

        for emotion_button in self.ids.emotions_box.children:
            self.emotion_buttons[emotion_button.emotion_id] = emotion_button
        
        # print(self.emotion_buttons)

        time: datetime = datetime.now(timezone.utc)

        save_folder: Path = settings["path"]["save"] / str(time.year) / str(time.month) / str(time.day)
        file_path = save_folder / settings["file-name"]["day"]

        if os.path.exists(file_path):
            print("EXIST!")

            with open(file_path, "rb") as file:
                data = tomllib.load(file)
                self.ids.diary_input.text = data["data"]["message"]
                emotion: str = data["data"]["emotion"]
                emotion_button_found: ToggleButton | None = self.emotion_buttons.get(emotion, None)
                if emotion_button_found:
                    emotion_button_found.state = "down"
                    # print(emotion)
                    # print(emotion_button_found.text)

    def text_changed(self, text: str) -> None:
        if text:
            self.ids.diary_display.text = text
        else:
            self.ids.diary_display.text = self.app._("text-style-tip")
    
    def return_day(self, time: datetime = datetime.now()) -> str:
        return time.strftime("%d/%m/%Y")

    def save_day(self) -> None: 
        # print("SALVO!")

        can_save: bool = False
        emotion_found: str = ""

        for emotion in self.ids.emotions_box.children:
            if emotion.state == "down":
                emotion_found = emotion.emotion_id
                break
        
        if self.ids.diary_input.text and emotion_found:
            can_save = True

        if not can_save:
            self.show_warning(self.app._("warning"), self.app._("finish-text"))
        
        else:
            day = Day(
                self.ids.diary_input.text,
                emotion_found
            )

            day.write()

    def show_warning(self, title: str, message) -> None:
        popup = WarningPopup(title=title, message=message)
        popup.open()