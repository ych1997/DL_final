import csv
def label(index,key,text):
	#print(len(key))
	#index=key[0][0]
	for i in range(len(key)):
		key[i][1]=int(key[i][1])
		key[i][2]=int(key[i][2])
		#key[i][4]=str.upper(key[i][4])
		#print(key)
	j=0
	with open('output2.csv', 'a', newline='') as csvfile:
		writer = csv.writer(csvfile)
		j=0
	#fw.write("article"+index+"\n")
		for i in range(len(text)):
			a=[]
			if text[i]=='，':
				index+=1
			a.append(index)
			a.append(str(text[i]))
			if i==key[j][1]:
				a.append("B-"+str(key[j][4]))
			elif key[j][1]<i<key[j][2]:
				a.append("I-"+str(key[j][4]))
			else:
				a.append("O")
			writer.writerow(a)
			if key[j][2]-1==i:
				j+=1
				if j>=len(key):
					j=0
	return index
f = open("output2.csv", "w")
f.close()
with open('output2.csv', 'a', newline='') as csvfile:
	writer = csv.writer(csvfile)
	a=['Sentence #','Word','Tag']
	writer.writerow(a)
#fw = open('file_io.data', 'w')
#fw.close()
f = open("train_2.txt", "r")
key=[]
space=0
temp=""
text=f.readline()
text=text.rstrip('\n')
title=f.readline()
temp=f.readline()
max_len=len(text)
index=0
while space!=3:
	#print(temp)
	if len(temp)==1:
		space+=1
		temp=f.readline()
	elif temp=='--------------------\n':
		space+=1
		#print(key)
		#print(text)
		index=label(index,key,text)
		index+=1
		text=""
		key.clear()
		text=f.readline()
		text=f.readline()
		text=text.rstrip('\n')
		if len(text)==0:
			break
		else:
			if len(text)>max_len:
				max_len=len(text)
			temp=f.readline()
			temp=f.readline()
	else:
		space=0
		temp=temp.rstrip('\n')
		temp=temp.split('\t')
		key.append(temp)
		temp=f.readline()
f.close()
print(max_len)