cm =list(map(int, input('身長').split()))
kg =list(map(int, input('体重').split()))
cm1=(max(cm))
kg1=(max(kg))
print(f'身長の最大値{cm1}')
print(f'体重の最大値{kg1}')
cm2=(min(cm))
kg2=(min(kg))
print(f'身長の最小値{cm2}')
print(f'体重の最小値{kg2}')
Anwercm = sum(cm)/len(cm)
Anwerkg = sum(kg)/len(kg)
print(f'身長の平均{Anwercm} ,体重の平均 {Anwerkg}')
def cmvar(cm):
	for i in cm:
		cm = (i - Anwercm)
		cm = (i * 2)
	return(f'身長の分散　{cm}')
def kgvar(kg):
	for i in kg:
		kg = (i - Anwerkg)
		kg = (i *2)
	return print(f'体重の分散　{kg}')

def kgdd(cm):
		for i in cm:
			cm = (i - Anwercm)
			cm = (i * 2)
			cm  = (cm**2)
		return print(f'体重の標準偏差 { cm}')
def cmdd(kg):
		for i in kg:
			kg = (i - Anwerkg)
			kg = (i *2)
			kg = (kg**2) 
		return print(f'体重の標準偏差　{kg}')
cmvar(cm)
kgvar(kg)
cmdd(cm)
kgdd(kg)
