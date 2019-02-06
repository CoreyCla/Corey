import json


class Product(object):
    def __init__(self, product_id=0, name='', price=0, quantity=0, location=''):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity
        self.location = location

    @property
    def product_id(self):
        return self.__product_id

    @product_id.setter
    def product_id(self, product_id):
        if product_id < 0:
            print("Product ID cannot be less than 0")
            self.__product_id = 0
        else:
            self.__product_id = product_id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        self.__price = price

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, quantity):
        self.__quantity = quantity

    @property
    def location(self):
        return self.__location

    @location.setter
    def location(self, location):
        self.__location = location


class ClothingProd(object, Product):
    def __init__(self, product_id, name, price, quantity, location, size, color):
        # super() is a reference to the base class and is used in lieu of Product.__init__()
        super().__init__(self, product_id, name, price, quantity, location)
        self.size = size
        self. color = color


class FileOutput:
    @staticmethod
    def make_json(name, product_list):
        with open(name, "w+") as outfile:
            json.dump(product_list, outfile)

        print("File " + name + " has been created.")

    # In the future this ought to be able to output human-readable plain text and microsoft/google
    # spreadsheet ready file types


class Prompt:
    @staticmethod
    def new_prompt():
        prompt_bool = True
        product_list = {'products': []}

        while prompt_bool:
            print('Create new product: ')
            # Creates the initial prompt for user input and stores that input in variables.
            product_id = 1
            name = input("What is the name of the product? ")
            price = input("What is the price of the product? ")
            quantity = input("How much of the product is there? ")
            location = input("Where is the product located? ")
            size = input("What size is it? ")
            color = input("What color is it? ")

            # Creates a new product object and fills product_list with metadata from it.
            new_product = ClothingProd(product_id, name, price, quantity, location, size, color)

            product_list['products'].append({
                'id': new_product.product_id,
                'name': new_product.name,
                'price': new_product.price,
                'quantity': new_product.quantity,
                'location': new_product.location,
                'size': new_product.size,
                'color': new_product.color
            })

            # Prints whatever the user entered during the prompt. Later on it would be good to have
            # functionality that lets the user recreate the object if something was accidentally
            # entered incorrectly.
            print("Id: ", product_id)
            print("Name: ", name)
            print("Price: ", price)
            print("Quantity: ", quantity)
            print("Location: ", location)

            prompt = input('Do you wish to create another product? (y/n) ')
            if prompt == "y" or prompt == "Y":
                prompt_bool = True
            elif prompt == "n" or prompt == "N":
                prompt_bool = False
            else:
                print('Invalid input. Please indicate either \'y\' for yes or \'n\' for no. ')

        file_name = input('Creating new file. Please choose a name for your file: ')
        FileOutput.make_json(file_name, product_list)
