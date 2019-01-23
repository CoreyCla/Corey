class Product(object):
    def __init__(self, product_id=0, name='', price=0, quantity=0, location=''):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity
        self.location = location
        # self.product_dict = []

    def user_prompt(self):
        # Creates the initial prompt for user input and stores that input in variables.
        self.product_id = 1
        self.name = input("What is the name of the product? ")
        self.price = input("What is the price of the product? ")
        self.quantity = input("How much of the product is there? ")
        self.location = input("Where is the product located? ")

        # new_product = Products.Product(0, name, price, quantity, location)

        # Prints whatever the user entered during the prompt. Later on it would be good to have
        # functionality that lets the user recreate the object if something was accidentally
        # entered incorrectly.
        print("Id: ", self.product_id)
        print("Name: ", self.name)
        print("Price: ", self.price)
        print("Quantity: ", self.quantity)
        print("Location: ", self.location)

        return self
