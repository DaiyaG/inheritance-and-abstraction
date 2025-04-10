from abc import ABC, abstractmethod

class Sports(ABC):

    def objects(self):
        pass

class Football(Sports):

    def objects(self):
        print("I love to run around for 90 minutes kicking a ball and hoping to either score or win")

class Basketball(Sports):

    def objects(self):
        print("I love to play basketball and score buckets or win")

class Cricket(Sports):

    def objects(self):
        print("I love to bowl or bat and play for my school team")

class Table_Tennis(Sports):

    def objects(self):
        print("I love to beat others but can get very competative and challenging towards the end")

F = Football()

B = Basketball()

C = Cricket()

TT = Table_Tennis()

for sports in (F, B, C, TT):
    sports.objects()
        
            
        
            
        
        