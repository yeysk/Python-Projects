
# TASK 5: INVENTORY MANAGEMENT SYSTEM

availableProducts = {
    'product1': {
        'name': 'bean',
        'kilos': 30,
        'buying price': 55,
        'selling price': 65,
     },  
    'product2': {
        'name': 'chickpea',
        'kilos': 20,
        'buying price': 45,
        'selling price': 55,
    },
   'product3': {
         'name': 'macaroni',
        'kilos': 40,
        'buying price': 50,
        'selling price': 60,
    },
    'product4': {
        'name': 'rice',
        'kilos': 35,
        'buying price': 35,
        'selling price': 45,
    },
    'product5': {
        'name': 'red meat',
        'kilos': 25,
        'buying price': 250,
        'selling price': 350,
   },
    'product6': {
        'name': 'chicken',
        'kilos': 50,
        'buying price': 150,
        'selling price': 200,
   }
}

while True:
    
    print("\n******* INVENTORY MANAGEMENT SYSTEM *******")
    print("\n1. Show available products")
    print("2. Add Products")
    print("3. Remove Products")
    print("4. Quit")
    
    try:
        userChoice = int(input("\nPlease choose an operation above: "))
        
        if (userChoice == 1):
            print("\nAvailable Products: ")
            for product_key, product in availableProducts.items():
                print(f"Product Name: {product['name']}, Amount: {product['kilos']}, Buying price: {product['buying price']}, Selling Price : {product['selling price']}")
    
        elif(userChoice == 2):
           
                
            name = input("\nName: ")
            amount = input("Kilos: ")
            buyingPrice = input("Buying Price: ")
            sellingPrice = input("Selling Price: ")
                
            product_id = 'product' + str(len(availableProducts) + 1)
            availableProducts[product_id] = {'name': name, 'kilos': amount, 'buying price': buyingPrice, 'selling price': sellingPrice}
            print("\nSuccessfully added!")
            print(availableProducts)
                
            
        elif (userChoice == 3):
            removingProduct = input("\nName: ").lower()
            book_found = False
            for product_key, product in list(availableProducts.items()):
                if product['name'].lower() == removingProduct:
                    del availableProducts[product_key]
                    book_found = True
                    print(f"\n{product['name']} removed successfully.")
                    print("\nUpdated Inventory:", availableProducts)
                    break
                
            if not book_found:
                print(f"\n{removingProduct} does not exist in the inventory.")
                    
        elif (userChoice == 4):
            print("Quitting...")
            break
        else:
            print("Invalid choice.Try again.")
    except ValueError:
        print("Input numbers only.")
        
    






