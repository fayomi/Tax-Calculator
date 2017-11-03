#command for user to input their daily wage
amount = int(raw_input(' please put in daily amount: \n'))

#define hourly wage
def hourly(h):
    p = h/8
    return p

#weekly gross amount variable defined
def week(w):
    x = w * 5
    return x
#monthly gross amount variable defined
def month(m):
    n = (m * 5) * 4
    return n


week_amount = week(amount)
month_amount = month(amount)
hour_amount = hourly(amount)

#weekly net variable after a 20% tax defined
def netw():
    a = (week_amount*80) /100
    return a

#monthly net variable after a 20% tax defined
def netm():
    d = (month_amount*80) / 100
    return d

net_month = netm()
net_week = netw()

#final output
if amount >= 110:
    print 'Congratulations! \nif your daily pay is ', amount, 'your hourly amount is ', hour_amount, '\n your gross weekly amount is ', week_amount, '\n your gross monthly amount is ', month_amount, '\n your net weekly pay is ', net_week, 'after a 20% tax' '\n your net monthly pay is ', net_month, 'after a 20% tax'
else:
    print 'you are being cheated!!!!! \nif your daily pay is ', amount, 'your hourly amount is ', hour_amount, '\n your gross weekly amount is ', week_amount, '\n your gross monthly amount is ', month_amount, '\n your net weekly pay is ', net_week, 'after a 20% tax' '\n your net monthly pay is ', net_month, 'after a 20% tax '
