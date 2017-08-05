#!python
#!/usr/bin/env python
from kivy.app import App
from kivy.clock import Clock
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from functools import partial

class Test(App):
    def create_clock(self, widget, touch, *args):
        callback = partial(self.menu, touch)
        Clock.schedule_once(callback, 1)
        touch.ud['event'] = callback

    def delete_clock(self, widget, touch, *args):
        Clock.unschedule(touch.ud['event'])

    def menu(self, touch, *args):
        menu = BoxLayout(
                size_hint=(None, None),
                orientation='vertical',
                center=touch.pos)
        menu.add_widget(Button(text='a'))
        menu.add_widget(Button(text='b'))
        close = Button(text='close')
        close.bind(on_release=partial(self.close_menu, menu))
        menu.add_widget(close)
        self.root.add_widget(menu)

    def close_menu(self, widget, *args):
        self.root.remove_widget(widget)

    def build(self):
        self.root = FloatLayout()
        self.root.bind(
            on_touch_down=self.create_clock,
            on_touch_up=self.delete_clock)

if __name__ == '__main__':
    Test().run()
