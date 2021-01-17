#1 Read line from Console
import sys
for line in sys.stdin:
     line=line.strip()
words=line.split()
for word in words:
	print( '%s\t%s' %(word,'1'))


#2 Using List for input to mapper
x=["am","am","you","t",1]
for word in x:
	print( '%s\t%s' %(word,'1'))


#3 Using file for input to mapper
f=open("data.txt","r")
s=f.readlines()
for line in s:
   words=line.split()
   for word in words:
      print( '%s\t%s' %(word,'1'))
