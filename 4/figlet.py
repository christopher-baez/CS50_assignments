from pyfiglet import figlet
import random
import sys

figlet = figlet()

if len(sys.argv) == 1:
    RanFont = True
elif len(sys.argv) == 3 and (sys.argv[1] == '-f' or sys.argv[1] == '--font'):
    RanFont = False
else:
    sys.exit()

figlet.getFonts()

if RanFont == False:
    try:
        figlet.setFontt(font=sys.argv[2])
    except:
        print('Invalid usage')
        sys.exit(1)
else:
    font = random.choice(figlet.getFonts())


text = input('Input:')


print(f'Output: {figlet.renderText(text)}')
