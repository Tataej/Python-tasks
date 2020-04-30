#Створити список, що містить цифри,
#літери алфавіту (великі та малі), спеціальні символи.

myList = [2, 8, 0, 'T', 'p', '$', 3, 'C']
print('My list: ',myList)

print('')
print('*********************************')
print('')

##Розділити список на декілька, кожний з
##яких містить тільки цифри, тільки літери тощо.

digits = set()
letters = set()
symbols = []
myDigits = []
myLetters = []

for i in range(10):
    digits.add(i)
    
for j in range(65,91):
    letters.add(chr(j))

for x in range(97,123):
    letters.add(chr(x))

for y in myList:
    if y in digits:
        myDigits.append(y)
    elif y in letters:
        myLetters.append(y)
    else:
        symbols.append(y)
        
print('Digits: ',myDigits)
print('Letters: ',myLetters)
print('Symbols: ',symbols)

print('')
print('*********************************')
print('')

#Конвертувати списки в  кортежі

print('Tuple Digits: ',tuple(myDigits))
print('Tuple Letters: ',tuple(myLetters))
print('Tuple Symbols: ',tuple(symbols))

print('')
print('*********************************')
print('')


##Ввести з клавіатури посчергово цифру, літеру чи спецсимвол
##і повернути відповідно індекс входження у відповідний кортеж

a = input('Input some numbers or letters or symbols: ')
a == ''.split(a)
digits = set()
letters = set()
symbols = []
myDigits = []
myLetters = []
print(a)

for i in range(48,58):
    digits.add(chr(i))         #питання по літері 'l' та цифрі '1' -
                               # якась дивна поведінка при виборці
for j in range(65,91):
    letters.add(chr(j))

for x in range(97,123):
    letters.add(chr(x))

for y in a:
    if y in digits:
        myDigits.append(y)
    elif y in letters:
        myLetters.append(y)
    else:
        symbols.append(y)
        
print('Digits: ',myDigits)
print('Letters: ',myLetters)
print('Symbols: ',symbols)

print('')
print('*********************************')
print('')

#Відобразити реверс одного з кортежів

b = [8, 3, 'p', 9, '*', '%', 'O']
print(b)
print('My tuple is: ',tuple(b))
b = b[::-1]
print('Reversed list: ',b)
print('My reverse tuple is: ',tuple(b))
