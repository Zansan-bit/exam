inte =list(map(int, input('整数を入力してください').split()))

tnte1=(max(inte))
tnte2=(min(inte))
Anwer = sum(inte)/len(inte)
def deta(tntet):
	for i in tntet:
		date = (i - Anwer)
		date = (i * 2 )
	return print(f'分散 {date}')

def deta2(date):
	for i in inte:
		data = ( i -Anwer)
		data = (i * 2)
		data = (data **2)
	return print(f'標準偏差　{data}')

deta(inte)
deta2(inte)