d={}


sent="We tried list and we tried dicts also we tried Zen"
for word in sent.split(' '):
	if word in d:
		d[word]=d[word]+1
	else:
		d[word]=1
print d