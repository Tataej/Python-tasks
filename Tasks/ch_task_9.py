##9. International Greetings
##Suppose you have a guest list of students and the country they are from,
##stored as key-value pairs in a dictionary.
##GUEST_LIST = {
##"Randy": "Germany",
##"Karla": "France",
##"Wendy": "Japan",
##"Norman": "England",
##"Sam": "Argentina"
##}
##Write a function that takes in a name and returns a name tag, that should
##read:
##"Hi! I'm [name], and I'm from [country]."
##If the name is not in the dictionary, return:
##"Hi! I'm a guest."
##Examples
##greeting("Randy") ➞ "Hi! I'm Randy, and I'm from Germany."
## 
##greeting("Sam") ➞ "Hi! I'm Sam, and I'm from Argentina."
## 
##greeting("Monti") ➞ "Hi! I'm a guest."
##

def greeting(dict, name):
    if name in dict:
        country = dict[name]
        return(print('greeting("%s") --> "Hi! I\'m %s, and I\'m from %s' %(name, name, country)))
    else:
        print('Hi! I\'m a guest')

guest_list = {}
k = True
while (k):
    data = input('Enter name & country separated by ":" ')
    if data == "#":
        k = False
    else:
        temp = data.split(':')
        guest_list[temp[0]] = str(temp[1])
      
print('GUEST_LIST: {')
for key in guest_list:
    print('"{}": "{}",'.format(key, guest_list[key]))
print('}')

greeting(guest_list, input("Input name which you are looking for: "))
 


    
