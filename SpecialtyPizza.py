from Pizza import Pizza
from CustomPizza import CustomPizza

class SpecialtyPizza(Pizza):
    def __init__(self, size, name):
        super().__init__(size)
        self.name = name
        self.sizePrice()

    def sizePrice(self):
        if self.getSize() == "S":
            self.setPrice(12.00)
        elif self.getSize() == "M":
            self.setPrice(14.00)
        elif self.getSize() == "L":
            self.setPrice(16.00)

    def getPizzaDetails(self):
        return("SPECIALTY PIZZA\nSize: {}\nName: {}\nPrice: ${:.2f}\n")\
            .format(self.size, self.name, self.price)