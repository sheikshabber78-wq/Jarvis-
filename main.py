from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView

class JarvisApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        self.scroll = ScrollView(size_hint=(1, 0.85))
        self.chat_history = Label(
            text="Jarvis: Hello! I am your AI Assistant.",
            size_hint_y=None,
            valign='top',
            color=(0, 1, 0.8, 1)
        )
        self.chat_history.bind(texture_size=lambda instance, value: setattr(instance, 'height', value[1]))
        self.scroll.add_widget(self.chat_history)
        self.layout.add_widget(self.scroll)
        
        self.input_layout = BoxLayout(orientation='horizontal', size_hint=(1, 0.15), spacing=5)
        self.user_input = TextInput(hint_text="Ask Jarvis...", multiline=False)
        self.send_btn = Button(text="Send", size_hint_x=0.3, background_color=(0, 0.6, 1, 1))
        self.send_btn.bind(on_press=self.ask_jarvis)
        
        self.input_layout.add_widget(self.user_input)
        self.input_layout.add_widget(self.send_btn)
        self.layout.add_widget(self.input_layout)
        
        return self.layout

    def ask_jarvis(self, instance):
        text = self.user_input.text.strip()
        if not text:
            return
        self.chat_history.text += f"\n\nYou: {text}\nJarvis: I am running directly on your Android phone!"
        self.user_input.text = ""

if __name__ == '__main__':
    JarvisApp().run()
