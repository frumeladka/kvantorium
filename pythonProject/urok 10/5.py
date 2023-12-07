name = input()
author = input()
pageCount = input()
price = input()
totalList = [name,author,pageCount,price]
totalList[2] = 132
totalList[1] = 'Пушкин'
totalList[3] = float(totalList[3]) * 2
print(totalList)
