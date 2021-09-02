from StackUsingLL import *
s = Stack()

def StockspanStack(price,span):

    for i in range(len(price)):
        if i == 0:
            span[i] = i+1
            s.push(i)

        elif price[i] > price[s.top()]:
            s.pop()
            span[i] = i + 1
            s.push(i)

        else:
            #price[i] < price[s.top()]:
            span[i] = i - s.top()
            s.push(i)



price = [60, 70, 80, 100, 90, 75, 80, 120]
span = [0]*len(price)

StockspanStack(price,span)
print(span)