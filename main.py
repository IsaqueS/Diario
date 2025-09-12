from kivy.app import App
from src.lang.lang import Lang
from src.window import Window

class DiaryApp(App):
    def build(self):
        return Window()
    
    _ = Lang()


if __name__ == "__main__":
    DiaryApp().run()
