num = input()

def claps(text):
    return text.count('3') + text.count('6') + text.count('9')


result = claps(num)
if result == 0:
    print(num)
else:
    print('짝' * result)
