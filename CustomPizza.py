from Pizza import Pizza

class CustomPizza(Pizza):
    def __init__(self, size):
        super().__init__(size)
        self.toppings = []
        self.sizePrice()

    def sizePrice(self):
        if self.getSize() == "S":
            self.setPrice(8.00)
        elif self.getSize() == "M":
            self.setPrice(10.00)
        elif self.getSize() == "L":
            self.setPrice(12.00)

    def getNumberOfToppings(self):
        return len(self.toppings)


    def toppingPrice(self):
        if self.getSize() == "S":
            return 0.50
        elif self.getSize() == "M":
            return 0.75
        elif self.getSize() == "L":
            return 1.00

    def addTopping(self, topping):
        self.toppings.append(topping)
        self.setPrice(self.getPrice() + self.toppingPrice())

    def getPizzaDetails(self):
        details = "CUSTOM PIZZA\nSize: {}\nToppings:\n"\
            .format(self.getSize())
        for top in self.toppings:
            details = details + "\t+ {}\n".format(top)
        details = details + "Price: ${:.2f}\n".format(self.getPrice())
        return details


    # def setTotalPrice(self):
    #     if self.getSize() == "S":
    #         tprice = 0.50
    #         price = tprice * self.getNumberOfToppings()
    #         self.setPrice(8.00 + price)
    #     elif self.getSize() == "M":
    #         tprice = 0.75
    #         price = tprice * self.getNumberOfToppings()
    #         self.setPrice(10.00 + price)
    #     elif self.getSize() == "L":
    #         tprice = 1.00
    #         price = tprice * self.getNumberOfToppings()
    #         self.setPrice(12.00 + price)

    # def addTopping(self,topping):
    #     self.toppings.append(topping)
    #     if self.getSize() == "S":
    #         tprice = 0.50
    #         self.setPrice(8.00 + tprice)
    #     elif self.getSize() == "M":
    #         tprice = 0.75
    #         self.setPrice(10.00 + tprice)
    #     elif self.getSize() == "L":
    #         tprice = 1.00
    #         self.setPrice(12.00 + tprice)