a = [
        ['高小一',18,30000,'北京'],
        ['高小二',19,20000,'上海'],
        ['高小三',20,10000,'深圳'],
        ['高小二',19,20000],
    ]
for m in range(len(a)):
    for n in range(len(a[m])):
        print(a[m][n],end='\t')
    print()#打印完一行，换行