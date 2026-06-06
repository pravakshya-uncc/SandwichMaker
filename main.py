### Data ###

recipes = {
    "small": {
        "ingredients": {
            "bread": 2,  ## slice
            "ham": 4,  ## slice
            "cheese": 4,  ## ounces
        },
        "cost": 1.75,
    },
    "medium": {
        "ingredients": {
            "bread": 4,  ## slice
            "ham": 6,  ## slice
            "cheese": 8,  ## ounces
        },
        "cost": 3.25,
    },
    "large": {
        "ingredients": {
            "bread": 6,  ## slice
            "ham": 8,  ## slice
            "cheese": 12,  ## ounces
        },
        "cost": 5.5,
    }
}

resources = {
    "bread": 12,  ## slice
    "ham": 18,  ## slice
    "cheese": 24,  ## ounces
}


### Complete functions ###

class SandwichMachine:

    def __init__(self, machine_resources):
        """Receives resources as input.
           Hint: bind input variable to self variable"""
        self.machine_resources = machine_resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        for item, amount in ingredients.items():
            if self.machine_resources.get(item, 0) < amount:
                print(f"Sorry there is not enough {item}.")
                return False
        return True

    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        print("Please insert coins.")
        try:
            dollars = int(input("how many large dollars?: ") or 0)
            half_dollars = int(input("how many half dollars?: ") or 0)
            quarters = int(input("how many quarters?: ") or 0)
            nickels = int(input("how many nickels?: ") or 0)
        except ValueError:
            print("Invalid input. Assuming 0 for that coin type.")
            return 0.0

        total = (dollars * 1.0) + (half_dollars * 0.5) + (quarters * 0.25) + (nickels * 0.05)
        return total

    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        if coins >= cost:
            change = round(coins - cost, 2)
            print(f"Here is ${change:.2f} in change.")
            return True
        else:
            print("Sorry that's not enough money. Money refunded.")
            return False

    def make_sandwich(self, sandwich_size, order_ingredients):
        """Deduct the required ingredients from the resources.
           Hint: no output"""
        for item, amount in order_ingredients.items():
            self.machine_resources[item] -= amount
        print(f"{sandwich_size} sandwich is ready. Bon appetit!")


### Make an instance of SandwichMachine class and write the rest of the codes ###

def main():
    # Instantiate the sandwich machine with global resources
    machine = SandwichMachine(resources)
    is_on = True

    while is_on:
        # Prompt the user for choice
        choice = input("What would you like? (small/medium/large/off/report): ").strip().lower()

        if choice == "off":
            is_on = False
        elif choice == "report":
            # Display current resources matching the expected formatting
            print(f"Bread: {machine.machine_resources['bread']} slice(s)")
            print(f"Ham: {machine.machine_resources['ham']} slice(s)")
            # Note: The PDF switches text between ounces and pound(s) for cheese formatting, 
            # but matches numerical inventory logic.
            print(f"Cheese: {machine.machine_resources['cheese']} pound(s)") 
        elif choice in recipes:
            sandwich_data = recipes[choice]
            ingredients = sandwich_data["ingredients"]
            cost = sandwich_data["cost"]

            # Step 1: Check if there are enough ingredients
            if machine.check_resources(ingredients):
                # Step 2: Request and process currency
                coins_inserted = machine.process_coins()
                
                # Step 3: Verify payment and give change or refund
                if machine.transaction_result(coins_inserted, cost):
                    # Step 4: Construct sandwich and deduct inventory
                    machine.make_sandwich(choice, ingredients)
        else:
            print("Invalid choice. Please select small, medium, large, report, or off.")

if __name__ == "__main__":
    main()