balance=3232
annualInterestRate=0.18
minmonthlypayment=10.0;
Monthly_interest_rate = (annualInterestRate) / 12.0
while 1:
	balancecopy=balance
	for i in range(0,12):
		
		Monthly_unpaid_balance = (balancecopy) - minmonthlypayment
		balancecopy= (Monthly_unpaid_balance) + (Monthly_interest_rate * Monthly_unpaid_balance) 
	if balancecopy > 0:
		minmonthlypayment +=10
	else :
		break	
print minmonthlypayment
