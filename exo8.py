import random

Months_dic = {'1': 'Janvier',
          '2': 'Fevrier', 
          '3': 'Mars',
          '4': 'Avril',
          '5': 'Mai',
          '6': 'Juin',
          '7': 'Juillet',
          '8': 'Aout',
          '9': 'Septembre',
          '10': 'Octobre',
          '11': 'Novembre',
          '12': 'Decembre'}

MonthsNumbers=list(Months_dic.keys())
print('let\'s learn month number (10 rounds)')
point = 0
for i in range(10):
    MonthNumber = random.choice(MonthsNumbers)
    MonthToGuess = Months_dic[MonthNumber]
    #ask question
    answer = input("which month is %s : " %MonthNumber)
    if answer.title() == MonthToGuess:
        print ('Good answer')
        point = point+1
    else:
        print ('Wrong answer')
print ('number of good answer : ',point)