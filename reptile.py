from animal import *
class reptile(animal):
    def __init__(self):
        super().__init__()
        self.coldblood=True
        self.tetrapod=True
        self.heart_chambers=[3,4]
        self.amniotoc_eggs=None
        self.scales=True

    def seek_heat(self):
        print ('Need the Heat boi')
    def hunt(self):
        print('I would like a Number one Large, a Number two with extra dip')
    def use_venom(self):
        print ('spit spit')
    def shedding (self):
        print ('Looking good boiiiiiii')

Bob_Reptile= reptile()

print(Bob_Reptile.excrement())
Bob_Reptile.shedding()


print (Bob_Reptile.scales)





