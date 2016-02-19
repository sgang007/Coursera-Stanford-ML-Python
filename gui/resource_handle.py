import pypandoc
import os
import json


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
        path = 'exercises/'
        return os.listdir(path)
    
    def files(self,excercise):
        path = 'exercises/'+excercise+'/part_file.json'
        filehandler = open(path)
        tmp = json.load(filehandler)       
        filelist = tmp['srcs']
        return filelist
    
    def manual(self, excercise):
        path = 'exercises/'+excercise+'/manual.md'
        return pypandoc.convert(path,'rst')

    def writeFile(self,excercise,filename):
        path = 'exercises/'+excercise+'/'+filename
        f=open(path,'w')
        return f

    def readFile(self,excercise,filename):
        path = 'exercises/'+excercise+'/'+filename
        #print 'Opening ',path
        f=open(path,'r')
        return f.read()
