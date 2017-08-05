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
<<<<<<< HEAD

    def output(part_id):
        X1 = np.column_stack((np.ones(20), np.exp(1) + np.exp(2) * np.linspace(0.1, 2, 20)))
        Y1 = X1[:,1] + np.sin(X1[:,0]) + np.cos(X1[:,1])
        X2 = np.column_stack((X1, X1[:,1]**0.5, X1[:,1]**0.25))
        Y2 = np.power(Y1, 0.5) + Y1

        fname = part_file['srcs'][part_id-1].rsplit('.',1)[0]
        mod = __import__(fname, fromlist=[fname], level=1)
        func = getattr(mod, fname)

        if part_id == 1:
            return sprintf('%0.5f ', func())
        elif part_id == 2:
            return sprintf('%0.5f ', func(X1, Y1, np.array([0.5, -0.5])))
        elif part_id == 3:
            return sprintf('%0.5f ', func(X1, Y1, np.array([0.5, -0.5]), 0.01, 10))
        elif part_id == 4:
            return sprintf('%0.5f ', func(X2[:,1:4]))
        elif part_id == 5:
            return sprintf('%0.5f ', func(X2, Y2, np.array([0.1, 0.2, 0.3, 0.4])))
        elif part_id == 6:
            return sprintf('%0.5f ', func(X2, Y2, np.array([-0.1, -0.2, -0.3, -0.4]), 0.01, 10))
        elif part_id == 7:
            return sprintf('%0.5f ', func(X2, Y2))


    def homework(self,exercise):
        path = 'exercises/'+exercise+'/part_file.json'
        tmp = json.load(open(path))       
        homework = tmp['homework']
        return homework
=======
    
   
>>>>>>> 8c2665727775c7a4f31c0ab34c04a13df68bbcd8

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
        tmp = json.load(open(path))       
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


