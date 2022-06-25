import kivy
from kivy.app import App
from kivy.uix import dropdown

import dataPlotter

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
Window.clearcolor = (0.9, 0.9, 0.9, 1)

from imgprocess import resizeimage

class CameraClick(BoxLayout):
    def capture(self):
            camera = self.ids['camera']
            camera.export_to_png("capture.png")
            resizeimage()
            print("Captured")
            #analyze here




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
   		 text: "By Jeffrey Lam, Jack Wei, and Linda Xue"
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

        Button:

            text: "Select Graph Type To Display.."
            on_release: root.run()
            pos: 250, 250
            size: 100, 100
            size_hint: None, None

        DropDown:

            Button:
                text: 'Bar Graph'
                size_hint_y: None
                height: '48dp'
                on_press:

            Button:
                text: 'Pie Chart'
                size_hint_y: None
                height: '48dp'
                on_press: dropdown.select('Pie Chart')

            Button:
                text: 'Line Graph'
                size_hint_y: None
                height: '48dp'
                on_press: dropdown.select('Line Graph')


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
        Label:
            id: description_label
            text:
                "Manual Input(if ai is not accurate), overwrites file"
            pos: 0, 300
            font_size: 16
            color: 0, 0, 0, 1
        TextInput:
            id: clothingID
            hint_text:'Enter ID'
            pos: 100, 620
            size: 300, 50
            size_hint: None, None


        TextInput:
            id: typeID
            hint_text:'Enter type of clothing'
            pos: 100, 550
            size: 300, 50
            size_hint: None, None
        TextInput:
            id: statusID
            hint_text:'Enter status'
            pos: 100, 480
            size: 300, 50
            size_hint: None, None
        TextInput:
            id: priceID
            hint_text:'Enter price'
            pos: 100, 410
            size: 300, 50
            size_hint: None, None
        TextInput:
            id: sizeID
            hint_text:'Enter size'
            pos: 100, 340
            size: 300, 50
            size_hint: None, None
        TextInput:
            id: descriptionID
            hint_text:'Enter description'
            pos: 100, 270
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
from machinelearning import ml_imageprediction

global predictedClothingType

predictedClothingType = ""

def predictCapture():
    #    from machinelearning import ml_imageprediction
        resizeimage()
        predictedClothingType = ml_imageprediction("capture2.png")
        #print(x)

class ScreenTwo(Screen):
	def runCamera(self):
            print("hi")

	def capture(self):
        	camera = self.ids['camera']
        	camera.export_to_png("capture.png")
        	predictCapture()
        #    predictCapture()
        	print("Captured")
        #    from machinelearning import ml_imageprediction
        #    x = ml_imageprediction("capture.png")
        #    print(x)

class ScreenThree(Screen):
	pass

class ScreenFour(Screen):
	def run(self):
            dropdown.open()
	def graph1(self):
            dataPlotter.bar_graph()
	def graph2(self):
            dataPlotter.pie_graph()
	def graph3(self):
            dataPlotter.line_graph()




class ScreenFive(Screen):
	pass

class ScreenSix(Screen):
	def process(self):
            clothingID = self.ids.clothingID.text
            typeID = self.ids.typeID.text
            statusID = self.ids.statusID.text
            priceID = self.ids.priceID.text
            sizeID = self.ids.sizeID.text
            descriptionID = self.ids.descriptionID.text
            favID = self.ids.favID.text
            favID = favID.lower()
            from csvWorker import append_data
            if favID == "t":
                favID = True
            else:
                favID = False
            y = append_data(typeID, statusID, priceID, sizeID, descriptionID, favID)
            import shutil
            original = 'capture.png'
            target = 'pictures/' + y + '.png'
            shutil.copyfile(original, target)

screen_manager = ScreenManager()

screen_manager.add_widget(ScreenOne(name ="screen_one"))
screen_manager.add_widget(ScreenTwo(name ="screen_two"))
screen_manager.add_widget(ScreenThree(name ="screen_three"))
screen_manager.add_widget(ScreenFour(name ="screen_four"))
screen_manager.add_widget(ScreenThree(name ="screen_five"))
screen_manager.add_widget(ScreenSix(name ="screen_six"))

class ScreenApp(App):

	def build(self):
    	   return screen_manager



# run the app
sample_app = ScreenApp()
sample_app.run()
