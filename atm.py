def atm_bills(num):
    count ={}
    if isinstance(num, int):
        for i in range(len(bills_variety)):
            money = bills_variety[i]
            """Divmode"""
            if num >= money:
                div,num, = divmod(num,money) #div = result of division, num = remainder
                count[money] = (div)
        return count
    else:
        print('Type Error: Enter integer number')
bills_variety = [2000, 500, 200, 50, 20, 10,2,1]
if __name__ == '__main__':
    xd = atm_bills(4470)
    print((xd))
