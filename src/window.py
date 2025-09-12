from kivy.uix.widget import Widget
from kivy.uix.popup import Popup
from kivy.properties import StringProperty

class WarningPopup(Popup):
    title = StringProperty("Titulo")
    message = StringProperty("Mensagem")

class Window(Widget):
    def save_day(self) -> None:
        print("SALVO!")
        print(self.ids.diary_input.text)
        for emotion in self.ids.emotions_box.children:
            if emotion.state == "down":
                print(emotion.emotion_id)
                break
        
        self.show_warning("Titulo", "Mensagem")

    def show_warning(self, title: str, message) -> None:
        popup = WarningPopup(title=title, message=message)
        popup.open()