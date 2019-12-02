prices = {"banana": 4,
"apple": 2,
"orange": 1.5,
"pear": 3}
stocks = {"banana": 3,
"apple": 0,
"orange": 1,
"pear": 2}
for item in prices:
    print(item)
    print(item + "\nprices:" + str(prices[item]) + "\nstocks:" + str(stocks[item]))
total = 0
for item in prices:
    total = total + (prices[item] * stocks[item])
print(total)
