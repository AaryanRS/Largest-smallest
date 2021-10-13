salesprice = 200
costprice = 150

def profit() :
    profit = costprice - salesprice

    return profit

def loss() :
    loss = costprice - salesprice

    return loss

if (costprice > salesprice):
    print(loss())

else :
    print(profit())



