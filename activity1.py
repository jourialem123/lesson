class cat:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def make_sound(self):
        print("meow") 
    def info(self):
        print("I am a cat my name is {} and I am {} years old".format(self.name,self.age))  

class dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def make_sound(self):
        print("bark")
    def info(self):
        print("I am a dog my name is {} and I am {} years old".format(self.name,self.age))

cat1= cat("Mimi",10)
dog1=dog("Roger",6)

for animal in (cat1,dog1): 
   animal.make_sound()
   animal.info()