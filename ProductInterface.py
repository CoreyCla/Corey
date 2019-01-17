import Products
import json


def create_product():
    # Whenever a new product object is created, this ID gets incremented by 1.
    product_id = 0
    # Creates the initial prompt for user input and stores that input in variables.
    name = input("What is the name of the product? ")
    price = input("What is the price of the product? ")
    quantity = input("How much of the product is there? ")
    location = input("Where is the product located? ")

    # Instantiates a product object with the user input stored.
    product = Products.Product(product_id, name, price, quantity, location)

    product.product_id = product_id + 1
    product.name = name
    product.price = price
    product.quantity = quantity
    product.location = location

    # Prints whatever the user entered during the prompt. Later on it would be good to have
    # functionality that lets the user recreate the object if something was accidentally
    # entered incorrectly.
    print("Id: ", product.product_id)
    print("Name: ", product.name)
    print("Price: ", product.price)
    print("Quantity: ", product.quantity)
    print("Location: ", product.location)

    return product


def main():
    # This bool is used for when a user wishes to add another product to their list.
    prompt_bool = True

    # This dictionary is used for creating a JSON-ready dictionary with dictionary elements.
    product_list = {}
    product_list['products'] = []

    # Uses the nested dictionary setup and adds the user input to key-value pairs for storage
    # in a new JSON file.
    while prompt_bool:
        print("Create new product. ")
        new_product = create_product()
        product_list['products'].append({
            'id': new_product.product_id,
            'name': new_product.name,
            'price': new_product.price,
            'quantity': new_product.quantity,
            'location': new_product.location
        })

        prompt = input("Do you wish to create another product? (y/n) ")

        if prompt == "y" or prompt == "Y":
            prompt_bool = True
        elif prompt == "n" or prompt == "N":
            prompt_bool = False
        else:
            print("Invalid input. Please indicate either 'y' for yes or 'n' for no. ")

    # Allows user to create a file with a chosen name.
    file_name = input("Creating new file. Please choose a name for your file: ")
    with open(file_name, "w+") as outfile:
        json.dump(product_list, outfile)

    print("Your output file is located at " + file_name)


main()
