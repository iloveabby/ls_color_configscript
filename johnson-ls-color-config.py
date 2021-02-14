'''
This is a pretty simple script in python that configures your Ls colors. 
Be warned this will over write you .bashrc. So please back it up before doing this.
Especially if you have a custon PS2 vaule. This scricpt is a bit bloated.
I migh try to make a lua script and bash version of this.
- Samuel Johnson aka iloveabby email:iloveabby@mailfence.com 
'''
rcs = '.bashrc' #this sets the file all of the open fucntions will li
inserts = 'LSCOLOR' # this is the bash config option that sets the color
inserts1 = "alias ls='ls --color'" #this alises ls to be ls --color so it is automaticly set to dispslay the color with out other modifcation 
texttype1 = '1'# sets the text to be bold if applied 
texttype2 ='0' #sets the text to be plan text if apllied 
color1 = '32' # all of these are the color variables that I used to make remember the colors a bit easier.
color2 = '31'
color3 = '36'
color4 = '34'
color5 = '33'
color6 = '37'
write0 = open(rcs,'w')# this inserts the alias so it wipes the bashrc so there can be no conflictions 
write0.write(inserts1)
write0.close()
print('Welcome to johnson ls color config!')


print('Choose Directory colors')

user = input('1 Green .2 Red 3 Cyan .4 Blue .5 Yellow .6 White') #this is where the user gives their input.

if user == '1':  # All of these blocks are the code that checks the user input and puts 
    write1 = open(rcs,'a')
    write1.write('\n'+inserts +'='+'"'+'di='+texttype1+';'+color1+':'+'"') 
    write1.close()
elif user == '2':
    write1 = open(rcs,'a')
    write1.write('\n'+inserts +'='+'"'+'di='+texttype1+';'+color2+':'+'"') 
    write1.close()
elif user == '3':
    write1 = open(rcs,'a')
    write1.write('\n'+inserts +'='+'"'+'di='+texttype1+';'+color3+':'+'"') 
    write1.close() 
elif user == '4':
    write1 = open(rcs,'a')
    write1.write('\n'+inserts +'='+'"'+'di='+texttype1+';'+color4+':'+'"')
    write1.close()
elif user == '5':
    write1 = open(rcs,'a')
    write1.write('\n'+inserts +'='+'"'+'di='+texttype1+';'+color5+':'+'"')
    write1.close()
elif user == '6':
    write1 = open(rcs,'a')
    write1.write('\n'+inserts +'='+'"'+'di='+texttype1+';'+color6+':'+'"')
    write1.close()
else:
    print('Invaild input')
print('Choose file colors')
user = input('1 Green .2 Red 3 Cyan .4 Blue .5 Yellow .6 White')


if user == '1':
    write1 = open(rcs,'a')
    write1.write('\n'+inserts +'='+'"'+'fi='+texttype1+';'+color1+':'+'"') 
    write1.close()
elif user == '2':
    write1 = open(rcs,'a')
    write1.write('\n'+inserts +'='+'"'+'fi='+texttype1+';'+color2+':'+'"') 
    write1.close()
elif user == '3':
    write1 = open(rcs,'a')
    write1.write('\n'+inserts +'='+'"'+'fi='+texttype1+';'+color3+':'+'"') 
    write1.close() 
elif user == '4':
    write1 = open(rcs,'a')
    write1.write('\n'+inserts +'='+'"'+'fi='+texttype1+';'+color4+':'+'"')
    write1.close()
elif user == '5':
    write1 = open(rcs,'a')
    write1.write('\n'+inserts +'='+'"'+'fi='+texttype1+';'+color5+':'+'"')
    write1.close()
elif user == '6':
    write1 = open(rcs,'a')
    write1.write('\n'+inserts +'='+'"'+'fi='+texttype1+';'+color6+':'+'"')
    write1.close()
else:
    print('Invaild input')

print('Change executable colors ')
user = input('1 Green .2 Red 3 Cyan .4 Blue .5 Yellow .6 White')


if user == '1':
    write1 = open(rcs,'a')
    write1.write('\n'+inserts +'='+'"'+'ex='+texttype1+';'+color1+':'+'"') 
    write1.close()
elif user == '2':
    write1 = open(rcs,'a')
    write1.write('\n'+inserts +'='+'"'+'ex='+texttype1+';'+color2+':'+'"') 
    write1.close()
elif user == '3':
    write1 = open(rcs,'a')
    write1.write('\n'+inserts +'='+'"'+'ex='+texttype1+';'+color3+':'+'"') 
    write1.close() 
elif user == '4':
    write1 = open(rcs,'a')
    write1.write('\n'+inserts +'='+'"'+'ex='+texttype1+';'+color4+':'+'"')
    write1.close()
elif user == '5':
    write1 = open(rcs,'a')
    write1.write('\n'+inserts +'='+'"'+'ex='+texttype1+';'+color5+':'+'"')
    write1.close()
elif user == '6':
    write1 = open(rcs,'a')
    write1.write('\n'+inserts +'='+'"'+'ex='+texttype1+';'+color6+':'+'"')
    write1.close()
else:
    print('Invaild input')
print('Change block device colors')
user = input('1 Green .2 Red 3 Cyan .4 Blue .5 Yellow .6 White')

if user == '1':
    write1 = open(rcs,'a')
    write1.write('\n'+inserts +'='+'"'+'bd='+texttype1+';'+color1+':'+'"') 
    write1.close()
elif user == '2':
    write1 = open(rcs,'a')
    write1.write('\n'+inserts +'='+'"'+'bd='+texttype1+';'+color2+':'+'"') 
    write1.close()
elif user == '3':
    write1 = open(rcs,'a')
    write1.write('\n'+inserts +'='+'"'+'bd='+texttype1+';'+color3+':'+'"') 
    write1.close() 
elif user == '4':
    write1 = open(rcs,'a')
    write1.write('\n'+inserts +'='+'"'+'bd='+texttype1+';'+color4+':'+'"')
    write1.close()
elif user == '5':
    write1 = open(rcs,'a')
    write1.write('\n'+inserts +'='+'"'+'bd='+texttype1+';'+color5+':'+'"')
    write1.close()
elif user == '6':
    write1 = open(rcs,'a')
    write1.write('\n'+inserts +'='+'"'+'bd='+texttype1+';'+color6+':'+'"')
    write1.close()
else:
    print('Invaild input')

print('Ls color config complete!')
