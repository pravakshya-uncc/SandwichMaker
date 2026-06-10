import data
from sandwich_maker import SandwichMaker
from cashier import Cashier

# Make an instance of other classes here
resources = data.resources
recipes = data.recipes

sandwich_maker_instance = SandwichMaker(resources)
cashier_instance = Cashier()


def main():
    is_on = True

    while is_on:
        choice = input("What would you like? (small/medium/large/off/report): ").lower()

        if choice == "off":
            is_on = False
            print("Turning off the machine. Goodbye!")
        elif choice == "report":
            # Display current resource levels
            print(f"Bread: {sandwich_maker_instance.machine_resources['bread']} slice(s)")
            print(f"Ham: {sandwich_maker_instance.machine_resources['ham']} slice(s)")
            print(f"Cheese: {sandwich_maker_instance.machine_resources['cheese']} ounce(s)")
        elif choice in recipes:
            sandwich_type = recipes[choice]
            # 1. Check if there are enough resources
            if sandwich_maker_instance.check_resources(sandwich_type["ingredients"]):
                # 2. Process the payment
                coins_inserted = cashier_instance.process_coins()
                # 3. Check if the transaction is successful
                if cashier_instance.transaction_result(coins_inserted, sandwich_type["cost"]):
                    # 4. Make the sandwich
                    sandwich_maker_instance.make_sandwich(choice, sandwich_type["ingredients"])
        else:
            print("Invalid selection. Please choose small, medium, large, report, or off.")


if __name__ == "__main__":
    main()