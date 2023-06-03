# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
import requests

KV = """
MyBL:
    orientation: "vertical"
    size_hint: (0.95, 0.95)
	pos_hint: {"center_x": 0.5, "center_y":0.5}
	Label:
		font_size: "15sp"
		multiline: True
		text_size: self.width*0.98, None
		size_hint_x: 1.0
		size_hint_y: None
		height: self.texture_size[1] + 15
		text: root.data_label
		markup: True
	TextInput:
		id: Inp
		multiline: False
		padding_y: (5,5)
		size_hint: (1, 0.5)
		text: "Введите слово"		
		on_text: app.process()
	Button:
		text: "Русско-алтайский"
		bold: True
		background_color:'#00FFCE'
		size_hint: (1,0.5)
		on_press: root.callback()
	Button:
		text: "Алтайско-русский"
		bold: True
		background_color:'#00FFCE'
		size_hint: (1,0.5)
		#on_press: root.callback()	
	Button:
		text: "О приложении"
		bold: True
		background_color:'#00FFCE'
		size_hint: (1,0.5)
		on_press: root.aboutapp()	
			
"""

class MyBL(BoxLayout):
    #data_label = StringProperty("Треугольник!\n")
    data_label = StringProperty("")

    def callclear(self):
        self.ids.Inp.text = ""
    def callback(self):
        r = requests.get("https://joomla.sozlik.ru/kadval.php?termin="+self.ids.Inp.text)
        print(r.text)

        yyy = "жизнь - Jÿрÿм, jадын - jÿрÿм / Life <br /> духовная жизнь человека - кижиниҥ кöгÿсjÿрÿми"
        self.data_label=""
        self.data_label += str(r.text.replace("<br />","\n")) + "\n"
        #self.data_label += str(yyy) + "\n"
        #self.data_label = self.ids.Inp.text
    def aboutapp(self):
        self.data_label = "Алтайские словари онлайн 1.0\nПеревод слов по базе сайта sozlik.ru\nКонтакты: megalex2003@ya.ru"
class MyApp(App):
    running = True

    def process(self):
        text = self.root.ids.Inp.text
    def build(self):
        return Builder.load_string(KV)

    def on_stop(self):
        self.running = False

MyApp().run()

