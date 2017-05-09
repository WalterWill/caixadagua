# Biblioteas

import time

# Declaração dos Objetos

status = str('on')  # Define que o sistema esta ligado

caixa = float(100.000)  # Metragem da caixa d'Agua
caixaStatus = str('')  # Status da caixa d'Agua
nivelStatus = float(0.000)  # NIvel da agua em tempo real
nivelMin = float(50.000)  # Nivel de agua minimo na caixa d'Agua
nivelMax = float(caixa*1)  # Nivel de agua maximo na caixa d'Agua

motor = float(1.000)  # Vazão da bomba d'Agua
motorStatus = str('')  # Status do motor

chuveiro = float('0.800')  # Vazão do chuveiro
chuveiroStatus = str('')  # Status do chuveiro

# ===================================================================

# Leitura dos sensores

nivelStatus = float(input('Digite o nivel da agua(0L - 100L): '))

# ===================================================================

# Loop Infinito

while status == 'on':

    # Desliga o motor quando a caixa esta cheia
    if nivelStatus >= nivelMax:
        motorStatus = str('off')
        caixaStatus = str('Cheio')

    #Status Esvaziando
    if nivelStatus < nivelMax and nivelStatus > nivelMin:
        caixaStatus = str('Esvaziando')

    # Liga o motor quando o nivel da agua chega no nivel minimo
    if nivelStatus <= nivelMin:
        motorStatus = str('on')
        caixaStatus = str('Minimo')

    # Adiciona agua na caixa quando o motor esta ligado
    if motorStatus == 'on':
        nivelStatus += motor

    # Retira agua da caixa quando o chuveiro esta ligado
    if chuveiroStatus == 'on':
        nivelStatus = nivelStatus - chuveiro

    #Simulação
    if motorStatus == 'off' :
        chuveiroStatus = str('on')

    # Mostra as informações
    print('Nivel Caixa:', nivelStatus)
    print('Motor:', motorStatus)
    print('Chuveiro:',chuveiroStatus)


    #Espera 1 segundo para atualizar
    time.sleep(0.2)
