def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. View Items")
    print("3. Remove Item")
    print("4. Exit")

def main():
    shopping_list = []

    while True:
        display_menu()
        choice = input("Choose an option (1-4): ")

        if choice == '1':
            item = input("Enter the item to add: ")
            shopping_list.append(item)
            print(f"'{item}' has been added to your shopping list.\n")
        elif choice == '2':
            if shopping_list:
                print("Your Shopping List:")
                for idx, item in enumerate(shopping_list, start=1):
                    print(f"{idx}. {item}")
                print()
            else:
                print("Your shopping list is empty.\n")
        elif choice == '3':
            item = input("Enter the item to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' has been removed from your shopping list.\n")
            else:
                print(f"'{item}' is not in your shopping list.\n")
        elif choice == '4':
            print("Exiting Shopping List Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()