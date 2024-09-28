"""

TASK 5: INVENTORY MANAGEMENT SYSTEM

"""
availableProducts = {
    'bean': {
        'kilos': 30,
        'buying price': 55,
        'selling price': 65,
    },
    'chickpea': {
        'kilos': 20,
        'buying price': 45,
        'selling price': 55,
    },
   'macaroni': {
        'kilos': 40,
        'buying price': 50,
        'selling price': 60,
    },
    'rice': {
        'kilos': 35,
        'buying price': 35,
        'selling price': 45,
    },
    'red meat': {
        'kilos': 25,
        'buying price': 250,
        'selling price': 350,
   },
    'chicken': {
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
    
    try:
        userChoice = int(input("\nPlease choose an operation above: "))
        
        if (userChoice == 1):
            print("\nAvailable Products: ")
            print(availableProducts)
    
        elif(userChoice == 2):
            add_product = True
            while add_product:
                newProducts = {}
                name = input("\nName: ")
                amount = input("Kilos: ")
                buyingPrice = input("Buying Price: ")
                sellingPrice = input("Selling Price: ")
                newProducts["Name"] = name
                newProducts["Amount"] = amount 
                newProducts["Buying Price"] = buyingPrice
                newProducts["Selling Price"] = sellingPrice
                print(newProducts)
                print("\nSuccessfully added!")
                break
                
                """anotherProduct = input("\nYes or no for another product?")
                
                if (anotherProduct == "yes"):
                    add_product = True
                else:
                    add_product = False"""
            
        elif (userChoice == 3):
            remove_product = True
            while remove_product:
                removingProduct = input("\nName: ")
                if removingProduct in  availableProducts:
                    del availableProducts[removingProduct]
                    print(f"\n{removingProduct} removed successfully.")
                    print("\nUpdated Inventory:", availableProducts)
                    
                    anotherRemoving = input("\nYes or no for another removing?")
                    
                    if (anotherRemoving == "yes"):
                        remove_product = True
                    else:
                        remove_product = False
                else:
                    print(f"\n{removingProduct} does not exist in the inventory.")
                    
                    """anotherRemoving = input("\nYes or no for another removing?")
                    
                    if (anotherRemoving == "yes"):
                        remove_product = True
                    else:
                        remove_product = False"""
        else:
            print("Geçersiz seçim.Tekrar deneyiniz.")
    except ValueError:
        print("Lütfen sadece rakam giriniz.")
        
    






