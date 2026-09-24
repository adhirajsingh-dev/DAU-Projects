# Initial book inventory
inventory = {
    "The Guide": 4,
    "Godan": 2,
    "The Room on the Roof": 5,
    "The Complete Adventures of Feluda": 3
}

# Function to check out a book
def checkout_book(title):
    if inventory[title]>0:
        inventory[title]-=1
        print('Checking out:',title)
        print('Remaining copies:',inventory[title])
    else:
        print('The title is not available.')

# Function to display all books and their quantities
def display_inventory():
    print("Current book inventory:")
    for id, (title, quantity) in enumerate(inventory.items(), start=1):
        print(f"{id}. {title}: {quantity} copies")

def main():
    while True:
        # Display the current inventory
        display_inventory()
        
        # Prompt user for a book to check out
        book_number = input("Enter the number of the book to check out (or 'quit' to exit): ").strip()
        
        if book_number.lower() == 'quit':
            print("Exiting the program.")
            break

        if not book_number.isdigit() or int(book_number) < 1 or int(book_number) > len(inventory):
            print("Invalid input. Please enter a valid book number.")
            continue
        
        book_index = int(book_number) - 1
        book_title = list(inventory.keys())[book_index]
        
        # Attempt to check out the book
        checkout_book(book_title)

main()