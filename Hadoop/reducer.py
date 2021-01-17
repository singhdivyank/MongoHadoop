import sys

wc={}

for line in sys.stdin:
	line=line.strip()
	word, count=line.split('\t',1)
	try:
		count=int(count)
	except ValueError:
		continue
	try:
		wc[word]=wc[word] + count
	except:
		wc[word]=count

for word in wc.keys():
	print('%s\t%s' %(word, wc[word]))

#to run the program - python mapper.py | sort | python reducer.py
