# In python , all the tkinter classes like label,pack have  properties and attributes as kwargs.So we can pass arguments
# by ourself and value will be assigned to those predefined properties but option willnot be shown when we hover over it

class Car:
    def __init__(self, **kwargs):
        self.model = kwargs.get("model")
        self.speed = kwargs.get("speed")  # when we use get method

tesla = Car(model="new")
print(tesla.model)
print(tesla.speed)
