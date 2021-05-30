def atm_bills(num):
    count = {bill_value: 0 for bill_value in bills_variety}
    if isinstance(num, int):
        for i in range(len(bills_variety)):
            money = bills_variety[i]
            while(num>=money):
                if num >= money:
                    num = num-money
                    count[money] = (count[money] + 1)

        return count
    else:
        print('Type Error: Enter integer number')
bills_variety = [2000, 500, 200, 50, 20, 10,2,1]
if __name__ == '__main__':
    xd = atm_bills(4470)
    #print((xd))
    print({bill_key: xd[bill_key] for bill_key in xd.keys() if xd[bill_key]})
