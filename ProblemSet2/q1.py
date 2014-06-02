balance=3629 
annualInterestRate=0.15
monthlyPaymentRate=0.05
total_paid=0.0
for i in range(0,12):

	Monthly_interest_rate= (annualInterestRate) / 12.0
	Minimum_monthly_payment = (monthlyPaymentRate) * (balance)
	Monthly_unpaid_balance = (balance) - (Minimum_monthly_payment)
	balance = (Monthly_unpaid_balance) + (Monthly_interest_rate * Monthly_unpaid_balance) 
	print "Month: "+str(i+1)
	print "Minimum monthly payment: "+str(round(Minimum_monthly_payment,2))
	print "Remaining balance: "+str(round(balance,2))	
	total_paid+=Minimum_monthly_payment

print "Total paid: "+str(round(total_paid,2))
print "Remaining balance: "+str(round(balance,2))	
