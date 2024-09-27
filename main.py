import data
from sandwich_maker import SandwichMaker
from cashier import Cashier

# Create instances of classes
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMaker(resources)
cashier_instance = Cashier()


def main():
    while True:
        # Ask user what size sandwich they want
        choice = input("What size sandwich would you like? (small/medium/large): ").lower()

        if choice in recipes:
            # Check if resources are available
            order_ingredients = recipes[choice]["ingredients"]
            if sandwich_maker_instance.check_resources(order_ingredients):
                # Ask user to insert coins
                total_cost = recipes[choice]["cost"]
                print(f"The cost is ${total_cost}")
                inserted_coins = cashier_instance.process_coins()

                # Process transaction
                if cashier_instance.transaction_result(inserted_coins, total_cost):
                    # Make the sandwich
                    sandwich_maker_instance.make_sandwich(choice, order_ingredients)

        # Ask if the user wants another sandwich
        continue_order = input("Would you like to make another sandwich? (yes/no): ").lower()
        if continue_order != 'yes':
            break


if __name__ == "__main__":
    main()
