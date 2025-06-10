from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
import datetime

class FinanceApp(App):
    def build(self):
        self.data = []
        layout = BoxLayout(orientation='vertical')
        self.label = Label(text="Digite: Ex: 'gastei 50 gasolina'")
        self.input = TextInput(multiline=False)
        btn = Button(text="Salvar")
        btn.bind(on_press=self.salvar_dado)
        layout.add_widget(self.label)
        layout.add_widget(self.input)
        layout.add_widget(btn)
        return layout

    def salvar_dado(self, instance):
        texto = self.input.text
        if texto:
            self.data.append(f"{datetime.datetime.now()}: {texto}")
            with open("dados.txt", "a") as f:
                f.write(f"{self.data[-1]}\n")
            self.label.text = "Salvo!"
            self.input.text = ""

if __name__ == '__main__':
    FinanceApp().run()
