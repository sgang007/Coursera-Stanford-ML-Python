import pypandoc
import os
import json
import subprocess
import sys
import StringIO
import contextlib


@contextlib.contextmanager
def stdoutIO(stdout=None):
    old = sys.stdout
    if stdout is None:
        stdout = StringIO.StringIO()
    sys.stdout = stdout
    yield stdout
    sys.stdout = old

class resourceHandler():
    def __init__(self, **args):
        pass
    
   

    def read_token(self,instance):
        path = '../'+instance.current_ex+'/token.txt'
        try:
            credentials = open(path)
            instance.email = credentials.readline().strip()
            instance.token = credentials.readline().strip()
            return True
        except Exception, e:
            return False


    def exercises(self):
        path = 'exercises/params.json'
        exercises = json.load(open(path))['exercises']
        return exercises
    
    def files(self,exercise):
        path = 'exercises/'+exercise+'/part_file.json'
        filehandler = open(path)
        tmp = json.load(filehandler)       
        filelist = tmp['srcs']
        return filelist
    
    def manual(self, exercise):
        path = 'exercises/'+exercise+'/manual.md'
        return pypandoc.convert(path,'rst')

    def writeFile(self,exercise,filename):
        path = 'exercises/'+exercise+'/'+filename
        f=open(path,'w')
        return f

    def readFile(self,exercise,filename):
        path = 'exercises/'+exercise+'/'+filename
        #print 'Opening ',path
        f=open(path,'r')
        return f.read()

    def run_ex(self,exercise,filename):
        #redirect and change system streams
        # os.chdir('exercises/'+exercise)
        # os.system('export PYTHONPATH=../..')
        
        path = 'exercises/'+exercise+'/'+filename
        split_ex = open(path).read().split('raw_input("Program paused. Press Enter to continue...")')
        #redirected_output = sys.stdout = StringIO()code = split_ex[0]
        
        # with stdoutIO() as s:
        #     exec(code)
        # #output = subprocess.Popen(code, stdout=subprocess.PIPE)
        # #restore system streams
        # os.chdir('../..')

        # output = codeOut.getvalue()
        # error = codeErr.getvalue()
        
        #print 'output: ',s.getvalue(),''
        return split_ex[0]


