class Employee:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def show(self,name):
        return f"Hi {name}!"