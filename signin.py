from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class SigninWindow(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def validate_user(self):
        user = self.ids.username_field
        pwd = self.ids.pwd_field
        info = self.ids.info
        uname = user.text
        password = pwd.text
        if uname == '' or passw == '':
            info.text = '[color=#FF0000]username and/ or passwird required[/color]'

class SigninApp(App):
    def build(self):
        return SigninWindow()

if __name__ == '__main__':
    sa = SigninApp()
    sa.run()