def hi(name):
    if name == 'ian':
        print('Hello, ' + name + ' baby!')
    else:
        print('sup ' + name + '!')

hi('ian')

girls = ['Rachel', 'Monica', 'Phoebe', 'Ola', 'Yara']
for name in girls: 
    hi(name)
    print('Next girl')

for i in range(1, 6):
    print('Number: ' + str(i))
