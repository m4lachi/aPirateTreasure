from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.uix.image import Image
from kivy.animation import Animation

kv_str = """
<IntroScreen@Screen>:
    Image:
        source: 'INTROSCREEEN.png' if root.name == 'MainMenu' else ''
        size: self.size
        pos: self.pos

<Beginning@Screen>:
    Image:
        source: 'wakingUp.jpg' if root.name == 'other_screen' else ''
        size: self.size
        pos: self.pos

<BeachIntro@Screen>:
    Image:
        source: 'Beach.png' 
        size_hint: 1, 1
        pos: self.pos

<PauseMenu@Screen>:
    canvas.before:
        Color:
            rgba: 1, 1, 1, 0.7
        Rectangle:
            size: self.size
            pos: self.pos

<FadingImage@Image>:
    canvas:
        Color:
            rgba: self.color
        Rectangle:
            size: self.size
            pos: self.pos
        Color:
            rgba: 1, 1, 1, self.opacity


MyScreenManager:
    IntroScreen:
        name: 'MainMenu'
        Button:
            background_color: 0,1,0
            size_hint: 0.2, 0.1
            pos_hint: {'center_x': 0.5, 'center_y': 0.4}
            on_release: root.current = 'other_screen'
        Button:
            background_color: 0,1,0
            size_hint: 0.2, 0.1
            pos_hint: {'center_x': 0.5, 'center_y': 0.4}
            on_release: root.current = 'other_screen'
        BoxLayout:
            Label:
                text: "Start"
                font_name: 'RetroGaming.ttf'  # Replace with your font file name
                font_size: 24
                color: 1,1,1
                size_hint: 0.2, 0.1
                pos_hint: {'center_x': 0.5, 'center_y': 0.4}

    Beginning:
        name: 'other_screen'
        Button:
            text: 'Go Back'
            size_hint: 0.2, 0.1
            pos_hint: {'top': 1, 'right': 1}
            on_release: root.current = 'PauseMenu'
        Button:
            text: '>'
            size_hint: 0.05, 0.05
            pos_hint: {'bottom': 1, 'right': 1}
            background_color: 1,1,1,0.5
            on_release: root.current = 'BeachIntro'
        BoxLayout:
            Label:
                text: "*you wake up alone on beach*"
                font_name: 'RetroGaming.ttf' 
                font_size: 16
                color: 1,1,1
                size_hint: 0.2, 0.1
                pos_hint: {'center_x': 0.5, 'center_y': 0.15}
        
    PauseMenu:
        name: 'PauseMenu'
        Button:
            size_hint: 0.4, 0.1
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            on_release: root.current = 'MainMenu'
        BoxLayout:
            Label:
                text: "Back To Start Menu"
                font_name: 'RetroGaming.ttf'  # Replace with your font file name
                font_size: 21
                color: 1,1,1
                size_hint: 0.2, 0.1
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}

    BeachIntro:
        name: 'BeachIntro'
        Button:
            text: 'Go Back'
            size_hint: 0.2, 0.1
            pos_hint: {'top': 1, 'right': 1}
            on_release: root.current = 'PauseMenu'
        Button:
            text: '>'
            size_hint: 0.05, 0.05
            pos_hint: {'bottom': 1, 'right': 1}
            background_color: 1,1,1,0.5
            on_release: root.current = 'BeachIntro1'
        BoxLayout:
            Label:
                text: "*your memory is fade only remembering your name*"
                font_name: 'RetroGaming.ttf' 
                font_size: 16
                color: 1,1,1
                size_hint: 0.2, 0.1
                pos_hint: {'center_x': 0.5, 'center_y': 0.15}
    
    BeachIntro:
        name: 'BeachIntro1'
        Button:
            text: 'Go Back'
            size_hint: 0.2, 0.1
            pos_hint: {'top': 1, 'right': 1}
            on_release: root.current = 'PauseMenu'
        BoxLayout:
            Label:
                text: "*wait what is your name*"
                font_name: 'RetroGaming.ttf' 
                font_size: 16
                color: 1,1,1
                size_hint: 0.2, 0.1
                pos_hint: {'center_x': 0.5, 'center_y': 0.15}
        BoxLayout: 
            Button:
                text: 'Submit'
                size_hint: 0.2, 0.05
                pos_hint: {'left': 0} 
                on_release: 
                    root.user_input = user_input.text
                    root.current = 'BeachIntro2'   
            TextInput:
                id: user_input
                size_hint: 0.4, 0.05
                pos_hint: {'center_x': 0.4,}
                hint_text: 'Enter your name'

    BeachIntro:
        name: 'BeachIntro2'
        Button:
            text: 'Go Back'
            size_hint: 0.2, 0.1
            pos_hint: {'top': 1, 'right': 1}
            on_release: root.current = 'PauseMenu'
        Button:
            text: '>'
            size_hint: 0.05, 0.05
            pos_hint: {'bottom': 1, 'right': 1}
            background_color: 1,1,1,0.5
            on_release: root.current = 'BeachIntro3'
        BoxLayout:
            Label:
                text: "*right i'm " + root.user_input
                font_name: 'RetroGaming.ttf' 
                font_size: 16
                color: 1,1,1
                size_hint: 0.2, 0.1
                pos_hint: {'center_x': 0.5, 'center_y': 0.15}
                
    BeachIntro:
        name: 'BeachIntro3'
        Button:
            text: 'Go Back'
            size_hint: 0.2, 0.1
            pos_hint: {'top': 1, 'right': 1}
            on_release: root.current = 'PauseMenu'
        Image:
            source: 'Lothar The Pirate.png' 
            size_hint: 0.3, 0.3
            pos_hint: {"x":0.2 , "y": 0.2}

        Button:
            text: '>'
            size_hint: 0.05, 0.05
            pos_hint: {'bottom': 1, 'right': 1}
            background_color: 1,1,1,0.5
            on_release: root.current = 'BeachIntro3'
        BoxLayout:
            Label:
                text: "HEY YOU"
                font_name: 'RetroGaming.ttf' 
                font_size: 16
                color: 1,1,1
                size_hint: 0.2, 0.1
                pos_hint: {'center_x': 0.5, 'center_y': 0.15}
           

                
"""
class MyScreenManager(ScreenManager):
    user_input = StringProperty("")
    def submit_name(self):
        user_input = self.get_screen('BeachIntro1').ids.user_input.text
        # Do something with the user input, e.g., store it in a variable or process it
        print("User entered:", user_input)
        # You can replace the 'print' statement with any logic to handle the input.



class FINAL_SCREEN(Screen):
    previous = StringProperty()

class MAINApp(App):
    def build(self):
        return Builder.load_string(kv_str)
    

if __name__ == '__main__':
    MAINApp().run()
