infile=open('high_temperatures.txt','r')
days=infile.readlines()
max=0
maxp=0
for i in range(len(days)-30):
    x,y=days[i].split(' ')
    x2,y2=days[i+30].split(' ')
    if abs(int(y2)-int(y))>max:
        max=abs(int(y2)-int(y))
        maxp=i
x,y=days[maxp].split(' ')
x2,y2=days[maxp+30].split(' ')
print('30-day period over which there is the biggest increase in the average high temperature is:-')
print(x,'to',x2)
print('Increase is',max)
