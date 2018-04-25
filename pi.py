#!/usr/bin/env python3

from ev3dev.ev3 import *
from time import sleep

#dir preto +- 5
#esq preto +- 4
#esq branco +- 55
#dir branco +- 54

KP = 10
KI = 5
TP= 100
OFFSET = 0
integral = 0

#MOTORES
esq = LargeMotor('outA')
dir = LargeMotor('outB')
motor_garra = LargeMotor('outC')
#motor_sensor = MediumMotor('outD')


#SENSORES
sensor_esq = ColorSensor(address=INPUT_1)
sensor_dir = ColorSensor(address=INPUT_2)
#sonar = UltrasonicSensor(address=INPUT_3)

sensor_esq.mode = 'COL-REFLECT'
sensor_dir.mode = 'COL-REFLECT'

def sat(giro):
    '''
    Satura o valor do giro para não ultrapassar o valor máximo do motor
    :param giro: KP*erro +ou- TP
    :return: O valor do giro saturado
    '''
    if giro > 1000:
        return 1000
    if giro < -1000:
        return -1000
    return giro

def executar():
        while True:
                erro = (sensor_dir.value() - sensor_esq.value())
                integral = integral + erro
                p=KP*erro + KI * integral
                print(p)
                giro_dir = sat(TP+p)
                giro_esq = sat(TP-p)
                print(giro_esq)
                esq.run_forever(speed_sp=giro_esq)
                dir.run_forever(speed_sp=giro_dir)
executar()