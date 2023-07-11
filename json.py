def __init__():
    print("Js in Python")
    
class console:
    def __init__(self):
        print("do console.log() for fun")
    
    @staticmethod
    def log(*text, **k):
        print(*text, **k)

    @staticmethod 
    def pizza():
        print("Italy!")

    @staticmethod 
    def Help():
        print(""" """)
