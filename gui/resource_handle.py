import pypandoc

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



    def files(self,excercise):
        path = 'res/'+excercise+'/sources.txt'
        filehandler = open(path)
        filelist=[]
        while True:
            try:
                filelist.append(filehandler.next())
            except Exception, e:
                return filelist
    def manual(self, excercise):
        path = 'res/'+excercise+'/manual.md'
        return pypandoc.convert(path,'rst')

    def writeFile(self,excercise,filename):
        path = '../'+excercise+'/'+filename
        f=open(path,'w')
        return f

    def readFile(self,excercise,filename):
        path = '../'+excercise+'/'+filename
        #print 'Opening ',path
        f=open(path,'r')
        return f.read()
