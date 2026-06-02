pt = int(input('PT: '))
labs = int(input('Labs: '))
assignment = int(input('Assignment: '))
pe = int(input('PE: '))
fe = int(input('FE: '))

avg = (pt*(15/100) + labs*(10/100) + assignment*(15/100) + pe*(30/100) + fe*(30/100))


if (pt <= 0 or labs <= 0 or assignment <= 0 or pe <= 0 or fe < 4 or avg < 5):
    print ('Not Passed')
else:
    print('Passed')    

