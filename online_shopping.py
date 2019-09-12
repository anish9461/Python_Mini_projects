class HomeAppliances:
    def __init__(self, productName, productCost):
        self.productName = productName
        self.productCost = productCost
    
    def displayProduct(self):
        print(" "+ self.productName+"   ",self.productCost)


class ElectronicProducts:
    def __init__(self, productName, productCost):
        self.productName = productName
        self.productCost = productCost
    
    def displayProduct(self):
        print(" "+ self.productName+"   ",self.productCost)

class HomeDecor:
    def __init__(self, productName, productCost):
        self.productName = productName
        self.productCost = productCost
    
    def displayProduct(self):
        print(" "+ self.productName+"   ",self.productCost)

def getProductValue(dictproducts,product):
    return dictproducts[product].productCost        

#function to display the exit message
def exitMessage():
    print(">----------------< Thankyou! For shopping Online on our portal >-------------------<")

def main():
    print(">-------------< Welcome to online shopping portal >--------------<")
    
    laptop = ElectronicProducts("laptop",100)
    phone = ElectronicProducts("phone",50)
    watch = ElectronicProducts("watch",25)

    television = HomeAppliances("television",1000)
    microwave = HomeAppliances("microwave",500)
    heater = HomeAppliances("heater",300)

    
    listofProducts = [laptop,phone,watch,television,microwave,heater]

    #Dictionary Comprehension from the list
    dictionaryOfProducts = {f.productName:f for f in listofProducts}
    for i in listofProducts:
        i.displayProduct()
    cost = input("Enter a number to see items below that price: ")
    listOfUpdatedProducts = [item for item in listofProducts if item.productCost < int(cost)]
    dictionaryOfUpdatedProducts = {listOfUpdatedProducts.index(f):f.productName for f in listOfUpdatedProducts}
    itemsInTheCart = []
    totalinCart = 0
    while(True):
        try:
            if dictionaryOfUpdatedProducts != {}:
                print("-----------------------------------------------")
                print("Items Available : ",dictionaryOfUpdatedProducts)
                print("-----------------------------------------------")
                index = input("Select the index of the item to purchase : ")
                totalinCart += getProductValue(dictionaryOfProducts,dictionaryOfUpdatedProducts[int(index)])
                print("Selected Item : ",dictionaryOfUpdatedProducts[int(index)])
                print(">--------------------------------------------<")
                print("Total amount in the cart : ",totalinCart)
                itemsInTheCart.append(dictionaryOfUpdatedProducts[int(index)])
                print("Items in the cart : ",itemsInTheCart)
                print(">--------------------------------------------<")
            else:
                print(">===============< Cart empty. Checking Out >===============<")
                break
            
        except Exception:
            print("\nXXXXXXXXXXXXXXXXXXXXXXXX No such item for that index in the list XXXXXXXXXXXXXXXXXXXXXXXXXXX\n")
            continue
        del dictionaryOfUpdatedProducts[int(index)]
    exitMessage()        

if __name__ == "__main__":
    main()


