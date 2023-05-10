
class Order:
    all = []
    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price

        Order.all.append(self)

        coffee.orders(self)
        coffee.customers(customer)

        customer.orders(self)
        customer.coffees(coffee)

    @property
    def name(self):
        return self._price
    
    @name.setter
    def name(self, new_price):
        if new_price and 1 <len(new_price) <= 10:
            self._price = new_price
        else:
            raise Exception
        
    @property
    def customer(self):
        return self._customer
    
    @customer.setter
    def customer(self, new_customer):
        from classes.customer import Customer
        if isinstance(new_customer, Customer):
            self._customer = new_customer
        else:
            raise Exception
        return self._customer
    
    @property
    def coffee(self):
        return self._coffee
    
    @coffee.setter
    def coffee(self, new_coffee):
        from classes.coffee import Coffee
        if isinstance(new_coffee, Coffee):
            self._coffee = new_coffee
        else:
            raise Exception
        return self._coffee



