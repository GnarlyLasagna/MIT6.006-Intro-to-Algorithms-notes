denominations = [1, 2, 5, 10, 20, 50, 100]
# 100p is £1

def returnChange(change, denominations):
    # make a list size of length denominations filled with 0
    toGiveBack = [0] * len(denominations)

    for pos, coin in enumerate(reversed(denominations)):
        while coin <= change:
            change = change - coin
            toGiveBack[pos] += 1
    return(toGiveBack)
            
print(returnChange(30, denominations))
# returns [0, 0, 0, 1, 1, 0, 0]
# 1x 10p, 1x 20p