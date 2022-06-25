from kivy.app import App
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.spinner import Spinner

KV = """
<MainScreen>:
    BoxLayout:
        orientation: 'vertical'
        Button:
            text: 'Edit'
            on_press: app.show(name='edit')
        Label:
            text: 'Main Screen'

<HelpScreen>:
    Label:
        text: 'Help Screen'

<SettingsScreen>:
    Label:
        text: 'Settings Screen'

<EditScreen>:
    Label:
        text: 'Edit Screen'

<ScreenMenu>:
    text: 'main'
    values: ('main', 'help', 'settings')
    size_hint: None, None
    size: 200, 44
"""


class MainScreen(FloatLayout):
    pass


class HelpScreen(FloatLayout):
    pass


class SettingsScreen(FloatLayout):
    pass


class EditScreen(FloatLayout):
    pass


class ScreenMenu(Spinner):
    pass


class MyApp(App):

    def build(self):
        Builder.load_string(KV)
        self.screen = None
        self.root = FloatLayout()
        self.screen_layout = FloatLayout()
        self.menu = ScreenMenu()
        self.root.add_widget(self.screen_layout)
        self.root.add_widget(self.menu)

        self.menu.bind(text=self.select_screen)
        self.show('main')
        return self.root

    def select_screen(self, *args):
        self.show(self.menu.text)

    def show(self, name='main'):
        if self.screen is not None:
            self.screen_layout.remove_widget(self.screen)
            self.screen = None
        if name == 'main':
            screen = MainScreen()
        elif name == 'help':
            screen = HelpScreen()
        elif name == 'settings':
            screen = SettingsScreen()
        elif name == 'edit':
            screen = EditScreen()
        else:
            raise Exception('Invalid screen name')
        self.screen = screen
        self.screen_layout.add_widget(screen)


if __name__ == "__main__":
    MyApp().run()
