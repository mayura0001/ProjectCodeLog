priceList = []

no = 1
for i in range(3):
    answer = input("Enter the Price of the item " + str(no) + ": ")
    no += 1
    priceList.append(answer)

priceList.append(input('Enter price of an existuing item: '))

priceList[1] = input('Enter a new price for the second item: ')

total = 0
for price in priceList:
    total += float(price)

del priceList[0]

print("Final Price List:", priceList)
print("Total Cost: " ,total)

print(f"jdsjfdsjfidj{priceList[2]}")