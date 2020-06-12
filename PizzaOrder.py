from Pizza import Pizza
from CustomPizza import CustomPizza
from SpecialtyPizza import SpecialtyPizza

class PizzaOrder:
    def __init__(self, time):
        self.time = time
        self.pizzas = []
        self.total = 0.0

    def getTime(self):
        return self.time

    def setTime(self, time):
        self.time = time

    def getTotal(self):
        return self.total
    
    def setTotal(self, total):
        self.total = total

    def addPizza(self, pizza):
        self.pizzas.append(pizza)
        self.setTotal(self.getTotal() + Pizza.getPrice(pizza))

    def getOrderDescription(self):
        details = "******\nOrder Time: {}\n".format(self.getTime())
        for pizza in self.pizzas:
            if type(pizza) == CustomPizza:
                details = details + "{}\n----\n".format(CustomPizza.getPizzaDetails(pizza))
            elif type(pizza) == SpecialtyPizza:
                details = details + "{}\n----\n".format(SpecialtyPizza.getPizzaDetails(pizza))
        details = details + "TOTAL ORDER PRICE: ${:.2f}\n******\n".format(self.getTotal())
        return details

    def __repr__(self):
        return self.getOrderDescription()


cp1 = CustomPizza("S")
cp1.addTopping("extra cheese")
cp1.addTopping("sausage")
sp1 = SpecialtyPizza("S", "Carne-more")
order = PizzaOrder(123000) #12:30:00PM
order.addPizza(cp1)
order.addPizza(sp1)

# print (order.getOrderDescription())

assert order.getOrderDescription() == \
"******\n\
Order Time: 123000\n\
CUSTOM PIZZA\n\
Size: S\n\
Toppings:\n\
\t+ extra cheese\n\
\t+ sausage\n\
Price: $9.00\n\
\n\
----\n\
SPECIALTY PIZZA\n\
Size: S\n\
Name: Carne-more\n\
Price: $12.00\n\
\n\
----\n\
TOTAL ORDER PRICE: $21.00\n\
******\n"