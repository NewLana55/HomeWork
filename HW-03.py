print("Сколько билетов Вы хотите приобрести на конференцию?")
n=int(input())
i=0
sum=0
while i<n:
 print("Сколько лет поситителю",i+1)
 age=int(input())
 if age<18:
  t=0
 elif 17 < age < 25:
  t=990
 elif age>24:
  t=1390
 sum+=t
 i+=1

if n>3:
 sum *= 0.9

print("Сумма покупки= ",sum)
