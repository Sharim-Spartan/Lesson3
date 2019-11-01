
ship1=['A1','A2','A3']
ship2=['C1','D1','E1']

ship_damaged=zip(ship1,ship2)

user_attack=input('Where would to attack?\n Enter coordinates:')

counter=20
ship_hp=6
for coor in ship_damaged:
    while user_attack== coor:
        ship_hp=ship_hp-1
        if user_attack != coor:
            counter=counter-1
        elif counter==0:
            print ('Game Over')
        elif ship_hp==0:
            print('You won')
        else:
            'something did work'

