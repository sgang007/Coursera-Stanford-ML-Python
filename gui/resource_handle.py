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
