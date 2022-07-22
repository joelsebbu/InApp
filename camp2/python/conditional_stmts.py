#using if elif ladder

month = int(input('Enter the month no of your birth: '))

if(month==1):
    print('Personality: Bold and Alert\nBirth Stone: Garnet')
elif(month==2):
    print('Personality: Lucky and Loyal\nBirth Stone: Amethyst')
elif(month==3):
    print('Personality: Naughty and Genius\nBirth Stone: Aquamarine')
elif(month==4):
    print('Personality: Caring and Strong\nBirth Stone: Diamond')
elif(month==5):
    print('Personality: Loving and Practical\nBirth Stone: Emerald')
elif(month==6):
    print('Personality: Romantic and Curious\nBirth Stone: Alexandrite')
elif(month==7):
    print('Personality: Adventurous and Honest\nBirth Stone: Ruby')
elif(month==8):
    print('Personality: Active and Hardworking\nBirth Stone: Peridot')
elif(month==9):
    print('Personality: Sensitive and Pretty\nBirth Stone: Sapphire')
elif(month==10):
    print('Personality: Stylish and Friendly\nBirth Stone: Tourmaline')
elif(month==11):
    print('Personality: Nice and Creative\nBirth Stone: Citrine')
elif(month==12):
    print('Personality: Confident and Freedom loving\nBirth Stone: Zicron')
else:
    print("Wrong month!")



#using match
num = int(input(('Enter the month of your birth: ')))
def month(num):
      match num:
        case 1:
            return'Personality: Bold and Alert\nBirth Stone: Garnet'
        case 2:
            return'Personality: Lucky and Loyal\nBirth Stone: Amethyst'
        case 3:
            return'Personality: Naughty and Genius\nBirth Stone: Aquamarine'
        case 4:
            return'Personality: Caring and Strong\nBirth Stone: Diamond'
        case 5:
            return'Personality: Loving and Practical\nBirth Stone: Emerald'
        case 6:
            return'Personality: Romantic and Curious\nBirth Stone: Alexandrite'
        case 7:
            return'Personality: Adventurous and Honest\nBirth Stone: Ruby'
        case 8:
            return'Personality: Active and Hardworking\nBirth Stone: Peridot'
        case 9:
            return'Personality: Sensitive and Pretty\nBirth Stone: Sapphire'
        case 10:
            return'Personality: Stylish and Friendly\nBirth Stone: Tourmaline'
        case 11:
            return'Personality: Nice and Creative\nBirth Stone: Citrine'
        case 12:
            return'Personality: Confident and Freedom loving\nBirth Stone: Zicron'
        case _:
            return'Wrong month'
print(month(num))
