import product
import json


def main():
    def jsonify(name, list):
        with open(name, "w+") as outfile:
            json.dump(list, outfile)

        print("File " + name + " has been created.")

    def prompt():
        prompt_bool = True
        product_list = {'products': []}

        while prompt_bool:
            print('Create new product: ')
            # Creates a new product object and fills product_list with metadata from it.
            new_product = product.Product.user_prompt(product.Product())

            product_list['products'].append({
                'id': new_product.product_id,
                'name': new_product.name,
                'price': new_product.price,
                'quantity': new_product.quantity,
                'location': new_product.location
            })

            prompt = input('Do you wish to create another product? (y/n) ')
            if prompt == "y" or prompt == "Y":
                prompt_bool = True
            elif prompt == "n" or prompt == "N":
                prompt_bool = False
            else:
                print('Invalid input. Please indicate either \'y\' for yes or \'n\' for no. ')

        file_name = input('Creating new file. Please choose a name for your file: ')
        jsonify(file_name, product_list)

    prompt()


main()
