#Home appliances class
class HomeAppliances:
    def __init__(self, productName, productCost):
        self.productName = productName
        self.productCost = productCost
   #display product function
    def displayProduct(self):
        print(" "+ self.productName+"   ",self.productCost)

#Electronic products class
class ElectronicProducts:
    def __init__(self, productName, productCost):
        self.productName = productName
        self.productCost = productCost
    #display product function
    def displayProduct(self):
        print(" "+ self.productName+"   ",self.productCost)

#Home decor class
class HomeDecor:
    def __init__(self, productName, productCost):
        self.productName = productName
        self.productCost = productCost
    #display product function
    def displayProduct(self):
        print(" "+ self.productName+"   ",self.productCost)

#Musical instruments class
class MusicalInstruments:
    def __init__(self, productName, productCost):
        self.productName = productName
        self.productCost = productCost
    #display product function
    def displayProduct(self):
        print(" "+ self.productName+"   ",self.productCost)

#Sports class
class Sports:
    def __init__(self, productName, productCost):
        self.productName = productName
        self.productCost = productCost
    #display product function
    def displayProduct(self):
        print(" "+ self.productName+"   ",self.productCost)
        
#function to get the product value 
def getProductValue(dictproducts,product):
    return dictproducts[product].productCost        

#function to display the exit message
def exitMessage(Cost,Cart):
    print("\n>----------------------------------------------------------------------------------<")
    print("Items purchased -> ",Cart)
    print("Checkout Bill : $%i"%Cost)
    print(">----------------< Thankyou! For shopping Online on our portal >-------------------<\n")

#Main function
def main():
    print(">-------------< Welcome to online shopping portal >--------------<\n")
    
    laptop = ElectronicProducts("laptop",100)
    phone = ElectronicProducts("phone",50)
    watch = ElectronicProducts("watch",25)
    
    television = HomeAppliances("television",1000)
    microwave = HomeAppliances("microwave",500)
    heater = HomeAppliances("heater",300)
    curtains = HomeDecor("curtains", 50)
    sheets = HomeDecor('sheets',25)
    pillows = HomeDecor('pillows',15)
    guitar = MusicalInstruments("guitar", 125)
    piano = MusicalInstruments('piano',100)
    violin = MusicalInstruments('violin',75)
    bat = Sports("bat", 75)
    football = Sports('football',60)
    diceGame = Sports('diceGame',25)

    listofProducts = [laptop,phone,watch,television,microwave,heater, curtains, sheets, pillows, guitar, piano, violin, bat, football, diceGame]

    #Dictionary Comprehension from the list
    dictionaryOfProducts = {f.productName:f for f in listofProducts}
    #for loop to display all the products
    print('>-------------< Electronic Products >-----------<')
    for i in listofProducts[0:3]:
        i.displayProduct()
    print('>-------------< Home Appliances >---------------<')
    for i in listofProducts[3:6]:
        i.displayProduct()
    print('>--------------< Home Decor >-------------------<')
    for i in listofProducts[6:9]:
        i.displayProduct()
    print('>--------------< Musical Instruments >-------------------<')
    for i in listofProducts[9:12]:
        i.displayProduct()
    print('>--------------< Sports >-------------------<')
    for i in listofProducts[12:15]:
        i.displayProduct()
    while True:
        
        cost = input("Enter a number to see items below that price: ")
        try:
             #List comprehension for updated list of products
            listOfUpdatedProducts = [item for item in listofProducts if item.productCost < int(cost)]
            if listOfUpdatedProducts == []:
                print(">----------< No items below that value >-------<")
                print(">============< Re-enter the amount >===========<")
                continue
            dictionaryOfUpdatedProducts = {listOfUpdatedProducts.index(f):f.productName for f in listOfUpdatedProducts}
            break
        except Exception:
            print("XXXXXXXXXXXXXXX Invalid Entry XXXXXXXXXXXXXXXX")
   
    
    itemsInTheCart = []
    totalinCart = 0
    #Infinite while loop to interact with the python program
    while(True):
        #Try except block to catch exception
        try:
            #if else block to to check items in the cart
            if dictionaryOfUpdatedProducts != {}:
                print("-----------------------------------------------")
                print("Items Available : ",dictionaryOfUpdatedProducts)
                print("-----------------------------------------------")
                #input statement to take input from the user
                index = input("Select the index of the item to purchase : ")
                totalinCart += getProductValue(dictionaryOfProducts,dictionaryOfUpdatedProducts[int(index)])
                print("Selected Item : ",dictionaryOfUpdatedProducts[int(index)])
                print(">--------------------------------------------<")
                print("Total amount in the cart : $%i"%totalinCart)
                itemsInTheCart.append(dictionaryOfUpdatedProducts[int(index)])
                print("Items in the cart : ",itemsInTheCart)
                print(">--------------------------------------------<")            
            else:
                print(">===============< Cart empty >===============<")
                continue
        #Exception to catch if the user input is incorrect    
        except Exception:
            print("\nXXXXXXXXXXXXXXXXXXXXXXXX No such item for that index in the list XXXXXXXXXXXXXXXXXXXXXXXXXXX\n")
            continue
        del dictionaryOfUpdatedProducts[int(index)]
        while(1):
            cont = input("Enter Y to continue and N to check out : ")
            if(cont == 'y' or cont == 'Y'):
                flag = True
                break
            elif(cont == 'n' or cont == 'N'):
                flag = False
                break
            else:
                print("Invalid Entry")
                continue
        if flag == True:
            continue
        else:
            break
    exitMessage(totalinCart,itemsInTheCart)        

#main module
if __name__ == "__main__":
    main()


