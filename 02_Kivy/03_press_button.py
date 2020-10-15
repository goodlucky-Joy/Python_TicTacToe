from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class TutorialApp(GridLayout):
    def __init__(self, **kwargs):

        super(TutorialApp, self).__init__(**kwargs)

        self.cols = 2
        self.rows = 1

        self.label = Label(text = "my App")
        self.add_widget(self.label)
    
        self.button = Button(text="Click me!", font_size=40)
        self.button.bind(on_press=lambda a:print(self.label.text))
        self.add_widget(self.button)

class MyApp(App):
    def build(self):
        return TutorialApp()

if __name__ == '__main__':
    MyApp().run()
