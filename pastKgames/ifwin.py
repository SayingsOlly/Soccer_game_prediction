import csv
from phrasingData import footballData

filename = 'E2014.csv'


class PastKGames():
	"""docstring for PastKGames"""
	def __init__(self):
		self.trainSet = []
		
	def set_trainData(self,filename):

		self.trainSet=self.load_data(filename)

	def find_fiveth_winning_pre(self,team,game_num):
		k=0
		ftr=[]	#full time result 
		for item in self.trainSet:
			if item[2]==team:
				k=k+1
				if item[6]=='H':
					ftr.append(1)
				elif item[6]=='A':
					ftr.append(-1)
				else:
					ftr.append(0)
			if item[3]==team:
				k=k+1
				if item[6]=='A':
					ftr.append(1)
				elif item[6]=='H':
					ftr.append(-1)
				else:
					ftr.append(0)
			if k>=game_num:
				return k,ftr
		return None	

	# def load_data(self,filename):
	# 	data=[]
	# 	with open(filename,'rb') as file:
	# 		season14=csv.reader(file,delimiter=' ',quotechar = '|')
	# 		for row in enumerate(season14):
	# 			if row[0]!=0:
	# 				t = '-'.join(row[1])
	# 				a = t.split(',')
	# 				self.trainSet.append(a)

	# 	return self.trainSet



pastKgame = PastKGames()
pastKgame.set_trainData(filename)
kk, result=pastKgame.find_fiveth_winning_pre('Sunderland',6)
print pastKgame.trainSet[5][2], pastKgame.trainSet[5][3]
print result


	 
