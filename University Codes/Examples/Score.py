arsenal=int(input('Enter a score: '))
man_utd=int(input('Enter a score: '))
if arsenal>man_utd:
    print('Manchester United lose!')
    if man_utd<arsenal:
        print ('Manchester United need to change tactics')
    else:
        print ('Arsenal need to change tactics')
else:    
    print('Arsenal lose!')
    
