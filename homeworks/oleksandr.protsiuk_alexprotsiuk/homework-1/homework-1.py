#! usr/bin/env Python3

print ('Hello !')  # collect users data
name = str(input('what is your name ?'))
surname = str(input('what is your surname ?'))
age = str(input('Ok! how old are you ?'))
city = str(input('Where are you from ?'))
mind = str(input('What do your think about Masters Academy ?'))

full_name = name +' '+surname  # create users data
data = 'Name: '+full_name + '\n' +'Age:'+age+ '\n' +'City: '+city+ '\n' +'My mind about Masters Academy : '+mind+ '\n'

print('Ok! your data is:')  # printing users data
print(data)

a_file = open('data.txt','w') # open file and save data in txt-file
a_file.write(data)
a_file.close()

print ('Your data saved in file "data.txt".')
