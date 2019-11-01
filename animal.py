#The four pillars of object oriented programming
#Abstraction means hiding the complexity and showing the essential
#features of the object

#Inhertance inherts attributes from the parent class, it is not a copy,
#it add to the attributes. find example.
#it allows us to define a clsss that inherits all the mehtods and properties(attributes)
# from another parent class

#Encapsulation is the internal resperesentation of an object
#that will not be show to the user

#polymorhusm  refers to the ability of an object to adpat the code


class animal():
    def __init__(self):
        self.alive=True
        self.spine=True
        self.eyes=True
        self.lungs=True
        self.bloods=True
        self.bones=True


    def eat(self):
        return ('nomnomnom')
    def breathe(self):
        return ('Breathing')
    def move(self):
        return 'movy movy '
    def communicate(self):
        return 'nice to see that your are alive'
    def sleep(self):
        return 'Zzzzzz'
    def excrement(self):
        return 'mind looking away'

