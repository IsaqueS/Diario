from kivy.app import App
from kivy.core.text import LabelBase
from src.lang.lang import Lang
from src.window import Window

LabelBase.register(name="ChakraPetch", 
                   fn_regular="res/ChakraPetch-Medium.ttf",
                   fn_bold="res/ChakraPetch-Bold.ttf",
                   fn_italic="res/ChakraPetch-MediumItalic.ttf")

class DiaryApp(App):
    def build(self):
        return Window()
    
    _ = Lang()


if __name__ == "__main__":
    DiaryApp().run()
