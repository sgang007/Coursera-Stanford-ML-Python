import subprocess
import kivy
kivy.require('1.8.0')
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.codeinput import CodeInput
from kivy.uix.label import Label
from kivy.uix.rst import RstDocument
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.splitter import Splitter
from kivy.uix.scrollview import ScrollView
from kivy.uix.popup import Popup
from kivy.clock import Clock
from functools import partial
from kivy.animation import Animation
from Submission import Submission
from resource_handle import resourceHandler



class MainScreen(BoxLayout,Submission):

    def __init__(self, welcome=False, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        self.orientation='vertical'
        self.current_ex = 'ex1'
        self.current_file = 'warmUpExercise.py'
        self.element=resourceHandler()
        #self.= Submission()
        if welcome:
            welcome_popup = Popup(title='Coursera ML in Python', content=Label(text='Coursera Assignment App'),size_hint=(1, 1))
            self.add_widget(welcome_popup)
            welcome_popup.open()
            Clock.schedule_once(self.start_app,3)
        else:
            self.bind(size=self.draw_mainscreen)
  
    def start_app(self,*args):
        self.draw_mainscreen()
        self.bind(size=self.draw_mainscreen)

    def draw_mainscreen(self,*args):
        self.clear_widgets()
        self.add_widget(self.titlebar())
        self.add_widget(self.maineditor('e'))
        self.add_widget(self.filebar())
        self.add_widget(self.console())

    def draw_runscreen(self,*args):
        self.clear_widgets()
        self.add_widget(self.titlebar())
        self.add_widget(self.maineditor('r'))


    def titlebar(self):
        layout=BoxLayout(padding='2sp',size_hint=(1,None),height='65sp')
        layout.orientation='horizontal'

        #credentials = self.login_prompt()
        self.submit_popup = Popup(title='Enter credentials',content=self.login_prompt(),size_hint=(0.6, 0.35))
        #credentials.children[1].bind(on_press=self.submit_popup.dismiss)

        submit = Button(text='Submit',size_hint=(0.4,1))
        # if self.element.read_token(self):
        #     submit.bind(on_press=partial(self.submit_assignment))
        # else:
        #     submit.bind(on_press=self.submit_popup.open)
        submit.bind(on_press=partial(self.submit_assignment))
        run = Button(text='Run',size_hint=(0.4,1))
        run.bind(on_press=self.run)

        ex_dropdown = Spinner(text=self.current_ex,size_hint=(1,1))
        ex_dropdown.values = self.element.exercises()
        ex_dropdown.bind(text=self.updateExercise)

        layout.add_widget(run)
        layout.add_widget(ex_dropdown)
        layout.add_widget(submit)

        return layout


    def console(self):
        layout = FloatLayout(size_hint=(1,None),height=0)
        self.info_label = TextInput(size_hint=(1,None),readonly=True,background_color=(0,0,0,1),foreground_color=(1,1,1,1),opacity=0)
        self.info_label.text_size = self.size
        self.info_label.text = 'console'
        self.info_label.height = '150pt'
        self.info_label.top = 0
        layout.add_widget(self.info_label)
        return layout


    def login_prompt(self):
        main_layout= BoxLayout(padding='2sp')
        main_layout.orientation='vertical'
        layout=GridLayout(padding='2sp')
        layout.cols=2
        layout.add_widget(Label(text='Email id:'))
        email = TextInput(multiline=False)
        layout.add_widget(email)
        token = TextInput(multiline=False)
        layout.add_widget(Label(text='Submission Token:'))
        layout.add_widget(token)
        main_layout.add_widget(layout)
        submit = Button(text='Submit',size_hint=(1,0.4))
        submit.bind(on_press=partial(self.submit_assignment,email,token))
        main_layout.add_widget(submit)
        return main_layout

    def submit_assignment(self,*largs):
        #Make local if not used anywhere else 
        super(MainScreen).__homework = self.element.homework(self.current_ex)

        self.submit()
        if len(largs)>1:
            self.__login = largs[0].text
            self.__password = largs[1].text
        else:
            self.__login=self.email
            self.__password=self.token

        print 'Email',self.__login
        print 'Token', self.__password
        self.submit_popup.dismiss()

        #TODO: save token and give submission call
        # command = ["python","exercises/"+self.current_ex+"/"+"submit.py"]

        # process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        # output,error= process.communicate()
        # #self.show_error(output)
        # if not error == '':
        #     self.show_error(error)
        #self.show_error(self.submit())


    def updateExercise(self,spinner,text):
        self.current_ex=text
        current_file = self.element.files(self.current_ex)[0]
        if current_file.endswith('\n'):
            current_file=current_file[:-1]
        self.current_file= current_file
        self.draw_mainscreen()
        print 'Current Exercise changed to: ', self.current_ex



    def run(self,instance):
        #TODO: Display output in popup
        #output = subprocess.check_output(["python","../"+self.current_ex+"/"+self.current_ex+".py"],stderr=subprocess.PIPE)
        command = ["python","../"+self.current_ex+"/"+self.current_ex+".py"]
        #self.show_message('Running Exercise',1)
        print "Running"
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        
        output , error= process.communicate()
        #self.show_error(output)
        if not error == '':
            self.show_error(error)
        
        #while True:
        #     #Bind self.info_label.text to output.stdout.readline()
        #    self.show_error(process.stdout.readline())
        #    if process.poll() is not None:
        #        break
        print('The button <%s> is being pressed' % instance.text)

    
   
        
    def maineditor(self,*args):
        layout=BoxLayout()
        if self.width < self.height:
            layout.orientation='vertical'
        else:
            layout.orientation='horizontal'
        #self.bind(self.current_ex=self.update_currentFile)
        man = self.element.manual(self.current_ex)
        codeFile = self.element.readFile(self.current_ex,self.current_file)
        code = CodeInput(text=codeFile)
        code.bind(focus =self.schedule_reload)
        splitter = Splitter()
        if layout.orientation == 'vertical':
            splitter.sizable_from='bottom'
        else:
            splitter.sizable_from='right'
        splitter.add_widget(code)
        layout.add_widget(splitter)

        if args[0]=='e':
            layout.add_widget(RstDocument(text=man))
        else:

            layout.add_widget(terminal)
        return layout

    def saveAssignment(self,assignment,*largs):
        self.show_message('Autosaved',1)
        try:
            if not self.element.readFile(self.current_ex,self.current_file)==assignment.text:
                filehandler = self.element.writeFile(self.current_ex,self.current_file)
                filehandler.write(assignment.text)
                print 'INFO: Autosaved file'
        except Exception, e:
            raise e
            self.show_error(e)


    def schedule_reload(self,instance,value):
        if value:
            #Schedule Update
            self.callback = partial(self.saveAssignment,instance)
            Clock.schedule_interval(self.callback,5)
        else:
            #TODO:When clicking on another file, both focus=False and filebar button callbacks are executed simultaneously leading to deadlock
            Clock.unschedule(self.callback)
            #self.saveAssignment(instance)
            #Update now
            
    
    def filebar(self):

        layout = GridLayout(rows=1, size_hint=(None,None))
        layout.bind(minimum_width=layout.setter('width'))

        files = list(set(self.element.files(self.current_ex)))
        for f in files:
            if f.strip() == self.current_file:
                button = ToggleButton(text=f,group = self.current_ex,state='down')
            else:
                button = ToggleButton(text=f,group = self.current_ex,state='normal')
            if self.width/len(files) < 200:
                button.width=200
            else:
                button.width = int(self.width/len(files))
            button.size_hint=(None,1)
            button.bind(on_press=self.update_currentFile)
            layout.add_widget(button)

        filebar = ScrollView(size_hint=(1,None), do_scroll_x=True, do_scroll_y=False )
        filebar.add_widget(layout)
        return filebar


    def update_currentFile(self,instance):
        if instance.text.endswith('\n'):
            instance.text=instance.text[:-1]
        self.current_file = instance.text
        self.draw_mainscreen()
        print 'Current file changed to: ', self.current_file

    def show_message(self, msg,duration):
        self.info_label.text = msg
        anim = Animation(top=30.0, opacity=0.5, d=1) +\
            Animation(top=30.0, d=duration) +\
            Animation(top=0, opacity=0, d=1)        
        anim.start(self.info_label)

    def show_error(self, e):
        self.info_label.text = str(e)
        duration = len(self.info_label.text)/50
        anim = Animation(top=190.0, opacity=1, d=0.5) +\
            Animation(top=190.0, d=duration) +\
            Animation(top=0, opacity=0, d=2)        
        anim.start(self.info_label)



class CourseraApp(App):

    def build(self):
        return MainScreen(welcome=False)
    def on_pause(self):
        return True


if __name__ == '__main__':	
    CourseraApp().run()
