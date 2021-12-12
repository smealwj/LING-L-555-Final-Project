Lat = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
Кир = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ь', 'Ю', 'Я', 'а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ь', 'ю', 'я']

sum_lat=0
sum_cy=0
bgstats = open ('bgrecreationalclean.txt', 'r')
data = bgstats.read()
for j in range(len(Lat)):
	k=data.count(Lat[j])
			
	print(str(Lat[j])+'\t'*2+str(k))
	sum_lat=sum_lat+k
print("Sum of latin: "+str(sum_lat)+"\n")

for p in range(len(Кир)):
	n = data.count(Кир[p])
	sum_cy=sum_cy+n
	print(str(Кир[p])+'\t'*2+str(n))

print("Sum of Cyrillic: "+str(sum_cy)+"\n")
total=sum_cy+sum_lat
print("Total is "+str(total))
print('Latin percentage: ' +str(sum_lat/total))
print('Cyrillic percentage: ' +str(sum_cy/total))



#stats_list = {k:int(v) for (v,k) in [i.strip().split(' ') for i in bgstats.read$

#[i.strip() for i in bgstats.readlines()]
#print(stats_list)

#print(sum(stats_list.values()))






#bgstats = open ('bgstats.txt', 'r')
#stats_list = {k:int(v) for (v,k) in [i.strip().split(' ') for i in bgstats.read$

#[i.strip() for i in bgstats.readlines()]
#print(stats_list)

#print(sum(stats_list.values()))
