import csv
from sklearn.cluster import KMeans
a = []
team_names=['Tottenham','Everton','Liverpool','Sunderland','Arsenal','Southampton','Stoke','Newcastle','Chelsea','Swansea'
,'West-Ham','West-Brom','Man-City','Aston-Villa','Crystal-Palace','Leicester','Man-United','Norwich','Watford','Bournemouth']
team_features = []
with open('E1.csv','rb') as file:
	spamreader = csv.reader(file,delimiter=' ',quotechar = '|')
	for row in spamreader:
		t = '-'.join(row)
		a1 = t.split(',')
		a.append(a1)

print '---------'
#print a
count = 0
for names in team_names:
	features = [0,0,0,0,0]
	for temp in a:
		if temp[2] == names:
			for i in range(11,20,2):
				#print int(i)%11/2
				#print str(features[int(i)%11/2])+'='+str(features[int(i)%11/2])+'+'+str(int(temp[i]))
				features[int(i)%11/2] = features[int(i)%11/2] + int(temp[i])
		if temp[3] == names:
			for i in range(12,20,2):
				#print int(i)%11/2
				#print str(features[int(i)%11/2])+'='+str(features[int(i)%11/2])+'+'+str(int(temp[i]))
				features[int(i)%12/2] = features[int(i)%12/2] + int(temp[i])
	team_features.append(features)
K = 5
km = KMeans(n_clusters = K)
km.fit(team_features)
centers = km.cluster_centers_
centers[centers<0] = 0 #the minimization function may find very small negative numbers, we threshold them to 0
centers = centers.round(2)
print('\n--------Centers of the four different clusters--------')
print('Deal\t Cent1\t Cent2\t Cent3\t Cent4 \t Cent5')
for i in range(5):
    print(i+1,'\t',centers[0,i],'\t',centers[1,i],'\t',centers[2,i],'\t',centers[3,i],'\t',centers[4,i])

prediction = km.predict(team_features)
print('\n--------Which cluster each customer is in--------')
print('{:<15}\t{}'.format('Customer','Cluster'))
for i in range(len(prediction)):
    print('{:<15}\t{}'.format(team_names[i],prediction[i]+1))


print team_features
			#print count