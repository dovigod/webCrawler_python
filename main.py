



class car():
    def __init__(self,*args,**kwargs):
        self.wheels = 4
        self.color = kwargs.get("color")
        self.price = kwargs.get("price")
        self.seats = 4
    
    def __str__(self):
        return (f"price of this car is {self.price}")
    

class convertible(car):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.time = kwargs.get("time",10)
    def take_off(self):
        return f'taking off...'
    

porche = convertible( color = "green" , price = "$40")


print(porche)