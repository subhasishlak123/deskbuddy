from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Ellipse, Line
from kivy.clock import Clock
import random

class DeskBuddy(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.face_state = "happy"
        # Redraw whenever the window size changes
        self.bind(pos=self.draw_face, size=self.draw_face)

    def draw_face(self, *args):
        self.canvas.clear()
        with self.canvas:
            # Background
            Color(0.1, 0.1, 0.1, 1) # Dark gray background
            # Eyes (White part)
            Color(1, 1, 1, 1)
            eye_size = self.width * 0.15
            # Left Eye
            Ellipse(pos=(self.center_x - eye_size * 1.5, self.center_y), size=(eye_size, eye_size))
            # Right Eye
            Ellipse(pos=(self.center_x + eye_size * 0.5, self.center_y), size=(eye_size, eye_size))

            # Pupils (Black part)
            Color(0, 0, 0, 1)
            pupil_size = eye_size * 0.4
            Ellipse(pos=(self.center_x - eye_size * 1.2, self.center_y + eye_size * 0.3), size=(pupil_size, pupil_size))
            Ellipse(pos=(self.center_x + eye_size * 0.8, self.center_y + eye_size * 0.3), size=(pupil_size, pupil_size))

            # Mouth
            Color(1, 0.3, 0.3, 1) # Pinkish lips
            self.draw_mouth()

    def draw_mouth(self):
        w, h = self.width, self.height
        cx, cy = self.center_x, self.center_y
        
        if self.face_state == "happy":
            # A simple smile curve
            Line(points=[cx-50, cy-100, cx, cy-150, cx+50, cy-100], width=5, close=False)
        elif self.face_state == "surprised":
            # An 'O' shape
            Ellipse(pos=(cx-25, cy-150), size=(50, 50))
        elif self.face_state == "wink":
            # Change mouth to a flat line
            Line(points=[cx-40, cy-130, cx+40, cy-130], width=5)

    def on_touch_down(self, touch):
        # Cycle through states when touched
        states = ["happy", "surprised", "wink"]
        self.face_state = random.choice(states)
        self.draw_face()
        return True

class DeskBuddyApp(App):
    def build(self):
        return DeskBuddy()

if __name__ == '__main__':
    DeskBuddyApp().run()
