class Coffee:
    def __init__(self, name):
        self.name = name
        self._orders = []
        self._customers = []


    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if new_name:
            self._name = new_name
        else:
            raise Exception
        
    def orders(self, new_order=None):
        from classes.order import Order
        if new_order and isinstance(new_order, Order):
            self._orders.append(new_order)
            
        return self._orders
        
    
    def customers(self, new_customer=None):
        from classes.customer import Customer
        if new_customer not in self._customers and isinstance(new_customer, Customer):
            self._customers.append(new_customer)

        return self._customers
    
    def num_orders(self):
        return len(self._orders)
    
    def average_price(self):
        return sum([order.price for order in self._orders]) / len(self._orders)
