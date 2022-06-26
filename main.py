import kivy
from kivy.app import App
kivy.require('1.9.0')
import csv

from kivy.lang import Builder
from kivy.uix.screenmanager import (ScreenManager, Screen, NoTransition,
SlideTransition, CardTransition, SwapTransition,
FadeTransition, WipeTransition, FallOutTransition, RiseInTransition)


from kivy.config import Config
Config.set('graphics', 'width', '440')
Config.set('graphics', 'height', '800')
Config.set('graphics', 'resizable', False)

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.core.window import Window
import tkinter


Window.clearcolor = (0.9, 0.9, 0.9, 1)

#analyze code here
def analyzeAI():
    return "shirt"


Builder.load_string("""
<ScreenOne>:
	FloatLayout:
        Label:
            id: description_label
            text:
                "Alfashion"
            pos: 0, 300
            font_size: 16
            color: 0, 0, 0, 1

    	Image:
        	source: 'Alfashion.png'
        	keep_ratio: False
        	allow_stretch: True
        	opacity: 0.8
        	size_hint: 0.6, 0.3
        	pos_hint: {'center_x': 0.5, 'center_y': 0.75}

    	Label:
   		 id: name_label
   		 text: "By Jeffrey Lam, Jack Wei, Linda Xue, and Linden Zheng"
        	pos: 0, 0
   		 font_size: 16
        	keep_ratio: False
        	allow_stretch:
        	color: 0, 0, 0, 1
    BoxLayout:

        Button:
            background_normal: 'camera.png'
            size: 110, 110
            size_hint: None, None
            on_press:
                # You can define the duration of the change
                # and the direction of the slide
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 1
                root.manager.current = 'screen_two'
        Button:
            background_normal: 'closet.png'
            size: 110, 110
            size_hint: None, None
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 1
                root.manager.current = 'screen_three'
        Button:
            background_normal: 'graphicon.png'
            size: 110, 110
            size_hint: None, None
            on_press:
                # You can define the duration of the change
                # and the direction of the slide
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 1
                root.manager.current = 'screen_four'

        Button:
            background_normal: 'weather.png'

            size: 110, 110
            size_hint: None, None
            on_press:
                # You can define the duration of the change
                # and the direction of the slide
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 1
                root.manager.current = 'screen_five'

<ScreenTwo>:
	FloatLayout:
        Button:
            background_normal: 'backbutton.png'
            pos: 0, 710
            size: 100, 100
            size_hint: None, None

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
            size: 480, 300
    BoxLayout:

        ToggleButton:
            text: 'Play'
            on_press: camera.play = not camera.play
            size_hint_y: None
            height: '48dp'
        Button:
            text: 'Capture'
            size_hint_y: None
            height: '48dp'
            on_press:
                root.capture()
                root.manager.transition.direction = 'left'
                root.manager.current = 'screen_six'
        Button:
            text: 'Select Image'
            size_hint_y: None
            height: '48dp'
            on_press:
                root.imageselect()
                root.manager.transition.direction = 'left'
                root.manager.current = 'screen_six'

<ScreenThree>:
    FloatLayout:
        Button:

            background_normal: 'backbutton.png'
            pos: 0, 710
            size: 100, 100
            size_hint: None, None
            on_press:
                # You can define the duration of the change
                # and the direction of the slide
                root.manager.transition.direction = 'right'
                root.manager.transition.duration = 1
                root.manager.current = 'screen_one'
<ScreenFour>:
    FloatLayout:
        Button:

            background_normal: 'backbutton.png'
            pos: 0, 710
            size: 100, 100
            size_hint: None, None
            on_press:
                # You can define the duration of the change
                # and the direction of the slide
                root.manager.transition.direction = 'right'
                root.manager.transition.duration = 1
                root.manager.current = 'screen_one'



<ScreenFive>:
    FloatLayout:
        Button:

            background_normal: 'backbutton.png'
            pos: 0, 710
            size: 100, 100
            size_hint: None, None
            on_press:
                # You can define the duration of the change
                # and the direction of the slide
                root.manager.transition.direction = 'right'
                root.manager.transition.duration = 1
                root.manager.current = 'screen_one'

        Button:

            text: "Check the Weather!"
            pos: 100, 710
            size: 300, 50
            size_hint: None, None
            background_color: 1, 0.75, 0.95, 1
            on_press:
                root.weatherstuff()

        Button:

            text: "Get Weather Advice!"
            pos: 100, 400
            size: 300, 50
            size_hint: None, None
            background_color: 1, 0.75, 0.95, 1
            on_press:
                root.recommendstuff()

<ScreenSix>:
    FloatLayout:
        Button:

            background_normal: 'backbutton.png'
            pos: 0, 710
            size: 100, 100
            size_hint: None, None
            on_press:
                # You can define the duration of the change
                # and the direction of the slide
                root.manager.transition.direction = 'right'
                root.manager.transition.duration = 1
                root.manager.current = 'screen_two'
        Button:

            text: "Analyze"
            pos: 100, 710
            size: 300, 50
            size_hint: None, None
            background_color: 1, 0.75, 0.95, 1
            on_press:
                root.analyze()
        Label:
            id: description_label
            text:
                "Manual Input(if ai is not accurate), overwrites file"
            pos: 0, 300
            font_size: 16
            color: 0, 0, 0, 1

        TextInput:
            id: typeID
            hint_text:"Enter type"
            pos: 100, 600
            size: 300, 50
            size_hint: None, None
        TextInput:
            id: statusID
            hint_text:'Enter status'
            pos: 100, 520
            size: 300, 50
            size_hint: None, None
        TextInput:
            id: priceID
            hint_text:'Enter price'
            pos: 100, 440
            size: 300, 50
            size_hint: None, None
        TextInput:
            id: sizeID
            hint_text:'Enter size'
            pos: 100, 360
            size: 300, 50
            size_hint: None, None
        TextInput:
            id: descriptionID
            hint_text:'Enter description'
            pos: 100, 280
            size: 300, 50
            size_hint: None, None
        TextInput:
            id: favID
            hint_text:'Enter favorite(T or F)'
            pos: 100, 200
            size: 300, 50
            size_hint: None, None

        Button:

            text: "Confirm Values"
            pos: 100, 100
            size: 300, 50
            size_hint: None, None
            background_color: 1, 0.75, 0.95, 1
            on_press:
                # You can define the duration of the change
                # and the direction of the slide
                root.process()

""")

class ScreenOne(Screen):
	pass
   	# Replace the given image source value:


class ScreenTwo(Screen):
    global type
    def runCamera(self):
            print("hi")
    def capture(self):
            type = "shirt"
            print(type)
            camera = self.ids['camera']
            camera.export_to_png("capture.png")
            print("Captured")
    def imageselect(self):
        from selectionanalysis import selectImageandAnalyze
        selectImageandAnalyze()

class ScreenThree(Screen):
	pass

class ScreenFour(Screen):
	pass

class ScreenFive(Screen):

    def weatherstuff(self):
        from locationweatherget import locationweather2
        x = locationweather2()
        #print(x)
    #    print("locationweather")
        y = "The current temperature is " + str(x[0]) + "F, humidity is " + str(x[1]) + "%, and the forecast is " + str(x[2])
        print(y)
        return y

    def recommendstuff(self):
        from locationweatherget import recommendations
        x = recommendations()
        #print(x)
        y = ""
        y = "It is recommended that you wear: "+str(x[0])+", "+str(x[1])+", or "+str(x[2])
        print(y)
        return y
#        print("recommendations")

class ScreenSix(Screen):
    def analyze(self):
        holder = analyzeAI()
        print(holder)
        self.ids.typeID.text = holder

    def process(self):

            typeID = self.ids.typeID.text
            statusID = self.ids.statusID.text
            priceID = self.ids.priceID.text
            sizeID = self.ids.sizeID.text
            descriptionID = self.ids.descriptionID.text
            favID = self.ids.favID.text


screen_manager = ScreenManager()


screen_manager.add_widget(ScreenOne(name ="screen_one"))
screen_manager.add_widget(ScreenTwo(name ="screen_two"))
screen_manager.add_widget(ScreenThree(name ="screen_three"))
screen_manager.add_widget(ScreenFour(name ="screen_four"))
screen_manager.add_widget(ScreenFive(name ="screen_five"))
screen_manager.add_widget(ScreenSix(name ="screen_six"))

class ScreenApp(App):

	def build(self):
    	   return screen_manager



# run the app
sample_app = ScreenApp()
sample_app.run()
