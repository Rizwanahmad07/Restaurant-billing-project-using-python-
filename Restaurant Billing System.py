# Restaurant Billing System

# Menu dictionary with item names as keys and prices as values
menu = {
    "Burger": 5.00,
    "Pizza": 8.00,
    "Pasta": 6.50,
    "Salad": 4.50,
    "Soft Drink": 1.50
}

# Function to display the menu
def display_menu():
    print("Menu:")
    for item, price in menu.items():
        print(f"{item}: ${price:.2f}")

# Function to calculate the total bill
def calculate_bill(order):
    total = 0
    for item in order:
        if item in menu:
            total += menu[item]
    return total

# Main program
if __name__ == "__main__":
    print("Welcome to the Restaurant Billing System!")

    # Display the menu
    display_menu()

    # Initialize the order list
    order = []

    # Allow the user to make selections
    while True:
        item = input("Enter the item you want to order (or 'done' to finish): ")
        
        if item.lower() == 'done':
            break
        
        if item in menu:
            order.append(item)
            print(f"{item} added to the order.")
        else:
            print("Invalid item. Please choose from the menu.")

    # Calculate and display the total bill
    total_bill = calculate_bill(order)
    print(f"\nYour order:")
    for item in order:
        print(f"- {item}: ${menu[item]:.2f}")
    print(f"Total Bill: ${total_bill:.2f}")
    
    print("\nThank you for using the Restaurant Billing System!")
