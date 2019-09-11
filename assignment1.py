class Test1:
    t1text = "This is Test 1 class"
    #List Comprehension for creating a list of cubes
    cubes = []
    cubes = [x**3 for x in range(10)]
    def func1():
        print("This is funtion 1 in class test 1")

class Test2:
    t2text = "This is Test 2 class"
    #List Comprehension for creating a list of cubes
    squares = []
    squares = [x**2 for x in range(10)]
    def func1():
        f1text = "This is funtion 1 in class test 2"


class product:
    def __init__(self, productName, productCost):
        self.productName = productName
        self.productCost = productCost
    
    def displayProduct(self):
        print(" "+ self.productName+"   ",self.productCost)

def getProductValue(dictproducts,product):
    return dictproducts[product].productCost        

def main():
    print(">-------------< Welcome to online shopping portal >--------------<")
    
    laptop = product("laptop",100)
    phone = product("phone",50)
    watch = product("watch",25)

    listofProducts = [laptop,phone,watch]

    #Dictionary Comprehension from the list
    dictionaryOfProducts = {f.productName:f for f in listofProducts}
    print(dictionaryOfProducts)
    for i in listofProducts:
        i.displayProduct()
    cost = input("Enter a number to see items below that price: ")
    listOfUpdatedProducts = [item for item in listofProducts if item.productCost < int(cost)]
    
    dictionaryOfUpdatedProducts = {listOfUpdatedProducts.index(f):f.productName for f in listOfUpdatedProducts}
    
    print(dictionaryOfUpdatedProducts[0])
    
    totalinCart = 0
    while(True):
        try:
            if dictionaryOfUpdatedProducts != {}:
                print(dictionaryOfUpdatedProducts)
                index = input("Select the index of the item to purchase:")
                totalinCart += getProductValue(dictionaryOfProducts,dictionaryOfUpdatedProducts[int(index)])
                del dictionaryOfUpdatedProducts[int(index)]
                print(totalinCart)
            else:
                print("No items in this range")
            
        except KeyError:
            print("index error")
            

if __name__ == "__main__":
    main()


