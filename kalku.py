from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class Calculator(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 1
        self.output = TextInput(multiline=False, readonly=True, font_size=32)
        self.add_widget(self.output)

        tombol = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            ["C", "0", "=", "+"]
        ]

        for baris in tombol:
            row = GridLayout(cols=4)
            for label in baris:
                button = Button(text=label, font_size=24)
                button.bind(on_press=self.on_button_press)
                row.add_widget(button)
            self.add_widget(row)

    def on_button_press(self, instance):
        text = instance.text
        if text == "C":
            self.output.text = ""
        elif text == "=":
            try:
                self.output.text = str(eval(self.output.text))
            except:
                self.output.text = "Error"
        else:
            self.output.text += text

class CalculatorApp(App):
    def build(self):
        return Calculator()

if __name__ == "__main__":
    CalculatorApp().run()
