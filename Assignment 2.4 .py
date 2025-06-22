items = []
prices = []

while True:
    print("\n--- Billing Menu ---")
    print("1. Create Bill")
    print("2. Display Items and Total")
    print("3. Display Total Only")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        item_name = input("Enter item name: ")
        item_price = float(input("Enter item price: "))
        items.append(item_name)
        prices.append(item_price)
        print("Item added!")

    elif choice == '2':
        print("\n--- Bill Items ---")
        total = 0
        for i in range(len(items)):
            print(items[i], "-> Rs.", prices[i])
            total += prices[i]
        print("Total Amount = Rs.", total)

    elif choice == '3':
        total = sum(prices)
        print("Total Amount = Rs.", total)

    elif choice == '4':
        print("Exiting billing system. Thank you!")
        break

    else:
        print("Invalid choice. Please select again.")
