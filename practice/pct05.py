inte  = [int(input('整数を入力してください')) for i in range(10)]
tnte1=(max(inte))
tnte2=(min(inte))
Anwer = sum(inte)/len(inte)

for i in inte:
	ti =(i - Anwer)*2
	date =sum(inte)/(ti)


print(f'{date}分散')
date= date**0.5
print(f'{date} 標準偏差')