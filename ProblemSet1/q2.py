s = 'bblnpobobogbobobbfbobb'
b='bob'
v=0
for i in range(0,len(s)):
	x=0
	for j in range(0,len(b)):
		if i <= len(s) -3:
			if s[i+j]==b[j]:
				x=x+1
				if x==len(b):
					v=v+1		
			else:
				break
print "Number of times bob occurs is: "+str(v)				
