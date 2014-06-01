s ='abcdefghbcdefijklmnqxy'
substring=s[0]
longest=s[0]
for i in range(1,len(s)):
	if substring[-1] <= s[i]:
		substring+=s[i]
	else :
		substring=s[i]
	
	if len(substring)>len(longest):
			longest=substring	
print longest	
	
