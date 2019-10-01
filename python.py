l=[(2,5),(1,2),(4,4),(2,3),(2,1)]
lenght=len(l)
for i in range(lenght):
	for j in range(lenght-i-1):
		if l[j][1]>l[j+1][1]:
			temp=l[j]
			l[j]=l[j+1]
			l[j+1]=temp
print(l)			
