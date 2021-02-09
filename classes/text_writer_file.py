class text_writer:
    #This parameter is set as an attribute for the class
    param=2
    def __init__(self,content,name="text"):
        # This parameters can be changed by instance
        self.a=name
        self.b=content
    def attack(self):
        out=open(self.a+".txt","w+") 
        # in=open("text.txt","r") would read a file
        out.write(self.b)