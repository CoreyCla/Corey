class Product:
    product_id = 0
    name = ''
    price = 2
    quantity = 0
    location = ''

    def __init__(self, product_id, name, price, quantity, location):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity
        self.location = location
