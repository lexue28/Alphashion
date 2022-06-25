import kivy
from kivy.app import App
kivy.require('1.9.0')

from kivy.lang import Builder
from kivy.uix.screenmanager import (ScreenManager, Screen, NoTransition,
SlideTransition, CardTransition, SwapTransition,
FadeTransition, WipeTransition, FallOutTransition, RiseInTransition)


from kivy.config import Config
Config.set('graphics', 'width', '441')
Config.set('graphics', 'height', '800')
Config.set('graphics', 'resizable', False)

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.core.window import Window
#Window.clearcolor = (0.3, 0.5, 0.2, 0.8)

class CameraClick(BoxLayout):
    def capture(self):
            '''
            Function to capture the images and give them the names
            according to their captured time and date.
            '''
            camera = self.ids['camera']
            timestr = time.strftime("%Y%m%d_%H%M%S")
            camera.export_to_png("IMG_{}.png".format(timestr))
            print("Captured")

Builder.load_string("""
<ScreenOne>:
    FloatLayout:
        Label:
            id: description_label
            text:
                "Schoolfed"
            pos: 0, 300
            font_size: 32
        Image:
            id: logo
            source: 'Alfashion.png'
            size: 50, 50
            pos: 320,630
            allow_stretch: True
            keep_ratio: True
            opacity: 0.8
            size_hint: 0.2, 0.2

<ScreenTwo>:
    BoxLayout:
        Button:
            text: "Back"
            orientation: 'vertical'
            size_hint: None, None
            pos_hint: {"x":0.5, "top":1}
            size: 110, 50
            background_color : 0.9, 0.7, 0.2, 10
            on_press:
                # You can define the duration of the change
                # and the direction of the slide
                root.manager.transition.direction = 'right'
                root.manager.transition.duration = 1
                root.manager.current = 'screen_one'
        Camera:
            id: camera
            resolution: (640, 480)
            play: False
            size: 640, 480
        ToggleButton:
            text: 'Play'
            on_press: camera.play = not camera.play
            size_hint_y: None
            height: '48dp'
        Button:
            text: 'Capture'
            size_hint_y: None
            height: '48dp'
            on_press: root.capture()
        Button:
            text: 'Select Image'
            size_hint_y: None
            height: '48dp'
            on_press: root.imageselect()
""")

screen_manager = ScreenManager()


screen_manager.add_widget(ScreenOne(name ="screen_one"))
screen_manager.add_widget(ScreenTwo(name ="screen_two"))

class ScreenApp(App):

    def build(self):
        return screen_manager



# run the app
sample_app = ScreenApp()
sample_app.run()
