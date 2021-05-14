import random
import os


def generatesRandomPosition(maximum, direction):
    if direction == 'horizontal':
        return random.randint(0, len(ocean) - 1), random.randint(0, maximum)
    else:
        return random.randint(0, maximum), random.randint(0, len(ocean) - 1)


def positionVesselHelper(vesselSize):
    ok = False
    HORIZONTAL = 0
    VERTICAL = 1

    if random.randint(0, 1) == HORIZONTAL:
        direction = 'horizontal'
    else:
        direction = 'vertical'

    while not ok:
        sortedLine, sortedColumn = generatesRandomPosition((len(ocean) - 1) - vesselSize, direction)

        if direction == 'horizontal':
            for column in range(sortedColumn, sortedColumn + vesselSize, 1):
                if ocean[sortedLine][column] == 'a':
                    ok = True
                else:
                    ok = False
                    break
        else:
            for line in range(sortedLine, sortedLine + vesselSize, 1):
                if ocean[line][sortedColumn] == 'a':
                    ok = True
                else:
                    ok = False
                    break
    return sortedLine, sortedColumn, direction


def positionVessel(strikeGroup):
    for vessel in strikeGroup:
        for i in range(vessel.get("amount")):
            # tupla
            sortedLine, sortedColumn, direction = positionVesselHelper(vessel.get('size'))
            if direction == 'horizontal':
                for column in range(sortedColumn, sortedColumn + vessel.get('size')):
                    ocean[sortedLine][column] = vessel.get('initials')
            else:
                for line in range(sortedLine, sortedLine + vessel.get('size')):
                    ocean[line][sortedColumn] = vessel.get('initials')


def showBattleLattice():
    # os.system('cls')
    for line in range(len(ocean)):
        for column in range(len(ocean[line])):
            if column == 9:
                print(ocean[line][column])
            else:
                print(ocean[line][column], end=' ')


ocean = [['a' for i in range(10)] for j in range(10)]

strikeGroup = []
portaAvioes = {'name': 'Porta-aviões',
               'size': 5,
               'initials': 'P',
               'amount': 1}
strikeGroup.append(portaAvioes)

cruzadores = {'name': 'Cruzador',
              'size': 4,
              'initials': 'C',
              'amount': 2}
strikeGroup.append(cruzadores)

destroyers = {'name': 'Destroyer',
              'size': 3,
              'initials': 'D',
              'amount': 3}
strikeGroup.append(destroyers)

submarinos = {'name': 'Submarino',
              'size': 2,
              'initials': 'S',
              'amount': 3}
strikeGroup.append(submarinos)

positionVessel(strikeGroup)

showBattleLattice()
