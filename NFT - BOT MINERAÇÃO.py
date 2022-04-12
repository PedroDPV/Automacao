import pyautogui
import time

#### BIBLIOTECA DE FUNÇÕES DO BOT ####
def removerheroinas():
    pyautogui.moveTo(784, 452), pyautogui.click(784, 452), time.sleep(4)  # remover heroinas
    pyautogui.moveTo(1095, 445), pyautogui.click(1095, 445), time.sleep(4)
    pyautogui.moveTo(1410, 451), pyautogui.click(1410, 451), time.sleep(4)
def selecionarboss():
    pyautogui.click(696, 395), time.sleep(1)
    pyautogui.click(886, 389), time.sleep(1)
    pyautogui.click(981, 394), time.sleep(1)
    pyautogui.click(1196, 397), time.sleep(1)
    pyautogui.click(722, 729), time.sleep(1)
    pyautogui.click(883, 710), time.sleep(1)
    pyautogui.click(1100, 700), time.sleep(1)
    pyautogui.click(1239, 707), time.sleep(1)
def time1():
    pyautogui.moveTo(629, 565), pyautogui.click(629, 565), time.sleep(4)  # abrir aba
    pyautogui.moveTo(423, 408), pyautogui.click(423, 408), time.sleep(3)  # selecionar time 1
    pyautogui.moveTo(556, 429), pyautogui.click(556, 429), time.sleep(3)
    pyautogui.moveTo(672, 418), pyautogui.click(672, 418), time.sleep(3)
    pyautogui.moveTo(876, 562), pyautogui.click(876, 562), time.sleep(3)  # fechar aba
    pyautogui.moveTo(1382, 819), pyautogui.click(1382, 819), time.sleep(6)  # caçar boss
def time2():
    pyautogui.moveTo(629, 565), pyautogui.click(629, 565), time.sleep(4)  # abrir aba
    pyautogui.moveTo(777, 412), pyautogui.click(799, 384), time.sleep(4)  # selecionar time 2
    pyautogui.moveTo(427, 581), pyautogui.click(444, 564), time.sleep(4)
    pyautogui.moveTo(533, 583), pyautogui.click(534, 574), time.sleep(4)
    pyautogui.moveTo(876, 562), pyautogui.click(876, 562), time.sleep(3)  # fechar aba
    pyautogui.moveTo(1382, 819), pyautogui.click(1382, 819), time.sleep(6)  # caçar boss
def time3():
    pyautogui.moveTo(629, 565), pyautogui.click(629, 565), time.sleep(4)  # abrir aba
    pyautogui.moveTo(672, 579), pyautogui.click(672, 579), time.sleep(3)  # selecionar time 3
    pyautogui.moveTo(773, 584), pyautogui.click(773, 584), time.sleep(3)
    pyautogui.moveTo(430, 751), pyautogui.click(430, 751), time.sleep(3)
    pyautogui.moveTo(876, 562), pyautogui.click(876, 562), time.sleep(3)  # fechar aba
    pyautogui.moveTo(1382, 819), pyautogui.click(1382, 819), time.sleep(6)  # caçar boss

def time4():
    pyautogui.moveTo(629, 565), pyautogui.click(629, 565), time.sleep(4)  # abrir aba
    pyautogui.moveTo(534, 747), pyautogui.click(534, 747), time.sleep(3)  # selecionar time 4
    pyautogui.moveTo(672, 759), pyautogui.click(672, 759), time.sleep(3)
    pyautogui.moveTo(776, 732), pyautogui.click(776, 732), time.sleep(3)
    pyautogui.moveTo(876, 562), pyautogui.click(876, 562), time.sleep(3)  # fechar aba
    pyautogui.moveTo(1382, 819), pyautogui.click(1382, 819), time.sleep(6)  # caçar boss
def time5():
    pyautogui.moveTo(629, 565), pyautogui.click(629, 565), time.sleep(4)  # abrir aba
    pyautogui.moveTo(644, 535), time.sleep(1)
    pyautogui.scroll(-130), time.sleep(1)
    pyautogui.moveTo(435, 815), pyautogui.click(435, 815), time.sleep(3)  # selecionar time 5
    pyautogui.moveTo(563, 799), pyautogui.click(563, 799), time.sleep(3)
    pyautogui.moveTo(673, 815), pyautogui.click(673, 815), time.sleep(3)
    pyautogui.moveTo(876, 562), pyautogui.click(876, 562), time.sleep(3)  # fechar aba
    pyautogui.moveTo(1382, 819), pyautogui.click(1382, 819), time.sleep(6)  # caçar boss
def matarboss():
    pyautogui.moveTo(1382, 819), pyautogui.click(1382, 819), time.sleep(6)  # caçar boss
    pyautogui.click(1073, 726), time.sleep(60)
    pyautogui.click(1015, 792), time.sleep(3)
    pyautogui.click(1015, 792), time.sleep(3)
    pyautogui.click(1015, 792), time.sleep(3)
def entrar():
    time.sleep(15), pyautogui.click(1166, 688)  # conectar metamask
    time.sleep(15), pyautogui.click(1821, 690)  # clicar em assinar
    time.sleep(15), pyautogui.click(585, 486)  # clicar em matar boss
def minerar():
    contador = 1
    for n in range(3):
        if contador == 1:
            time.sleep(5), removerheroinas()
            time.sleep(1), time1()
            for a in range(3):
                time.sleep(1), matarboss()
                time.sleep(1), selecionarboss()
            contador += 1

        elif contador == 2:
            time.sleep(5), removerheroinas()
            time.sleep(1), time2()
            for a in range(3):
                time.sleep(1), matarboss()
                time.sleep(1), selecionarboss()
            contador += 1

        elif contador == 3:
            time.sleep(5), removerheroinas()
            time.sleep(1), time3()
            for a in range(3):
                time.sleep(1), matarboss()
                time.sleep(1), selecionarboss()
            contador += 1

        elif contador == 4:
            time.sleep(5), removerheroinas()
            time.sleep(1), time4()
            for a in range(3):
                time.sleep(1), matarboss()
                time.sleep(1), selecionarboss()
            contador += 1

        elif contador == 5:
            time.sleep(5), removerheroinas()
            time.sleep(1), time5()
            for a in range(3):
                time.sleep(1), matarboss()
                time.sleep(1), selecionarboss()
            contador += 1
        else:
            pass
def primeiraacc():
    time.sleep(2), pyautogui.hotkey('win')
    time.sleep(2), pyautogui.write('chrome')
    time.sleep(2), pyautogui.press('enter')
    time.sleep(2), pyautogui.hotkey('win', 'up')
    time.sleep(2), pyautogui.click(1156, 615)
    time.sleep(6), pyautogui.click(1726, 66)  # clicar na metamask
    time.sleep(6), pyautogui.write('sua senha aqui')
    time.sleep(3), pyautogui.press('enter')
    time.sleep(3), pyautogui.click(491, 63)
    time.sleep(3), pyautogui.write('https://app.lunarush.io/')
    time.sleep(1), pyautogui.press('enter')
def abrirchrome():
    time.sleep(2), pyautogui.hotkey('win')
    time.sleep(2), pyautogui.write('chrome')
    time.sleep(2), pyautogui.press('enter')
    time.sleep(2), pyautogui.hotkey('win', 'up')
    time.sleep(6), pyautogui.click(1156, 615)
def abriracc2():
    time.sleep(1), pyautogui.click(1855, 63) #clicar no perfil
    time.sleep(1), pyautogui.click(1633, 525) #clicar na acc 2
    time.sleep(6), pyautogui.click(1726, 66)  # clicar na metamask
    time.sleep(15), pyautogui.write('sua senha aqui')
    time.sleep(1), pyautogui.press('enter')
    time.sleep(3), pyautogui.click(491, 63)
    time.sleep(3), pyautogui.write('https://app.lunarush.io/')
    time.sleep(1), pyautogui.press('enter')
def abriracc3():
    time.sleep(1), pyautogui.click(1855, 63)  # clicar no perfil
    time.sleep(1), pyautogui.click(1641, 566)  # clicar na acc 3
    time.sleep(7), pyautogui.click(1726, 66)  # clicar na metamask
    time.sleep(15), pyautogui.write('sua senha aqui')
    time.sleep(4), pyautogui.press('enter')
    time.sleep(3), pyautogui.click(491, 63)
    time.sleep(3), pyautogui.write('https://app.lunarush.io/')
    time.sleep(3), pyautogui.press('enter')
def abriracc4():
    time.sleep(1), pyautogui.click(1855, 63)  # clicar no perfil
    time.sleep(1), pyautogui.click(1685, 605)  # clicar na acc 4
    time.sleep(5), pyautogui.click(1726, 66)  # clicar na metamask
    time.sleep(15), pyautogui.write('sua senha aqui')
    time.sleep(3), pyautogui.press('enter')
    time.sleep(3), pyautogui.click(491, 63)
    time.sleep(3), pyautogui.write('https://app.lunarush.io/')
    time.sleep(1), pyautogui.press('enter')

    time.sleep(1), pyautogui.click(1855, 63)
#######################################################################################################
# 1ª conta = LUNA 1 (SEU ENDEREÇO DE WALLET) -> email : seu_email@gmail.com
# user1 = ' seu_email@gmail.com'
# senha1 = 'sua senha'
pyautogui.hotkey('alt','tab')
conta = 1

while True:

    contador = 1
    if conta == 1:
        primeiraacc()
        time.sleep(15), entrar()
        time.sleep(15), selecionarboss()
        time.sleep(1), minerar()
        conta = 2

    if conta == 2:
        abriracc2()
        time.sleep(15), entrar()
        time.sleep(1), selecionarboss()
        time.sleep(1), minerar()
        time.sleep(3), pyautogui.hotkey('alt', 'f4')
        conta = 3

    if conta == 3:
        abriracc3()
        time.sleep(15), entrar()
        time.sleep(1), selecionarboss()
        time.sleep(1), minerar()
        time.sleep(3), pyautogui.hotkey('alt', 'f4')
        conta = 4

    if conta == 4:
        abriracc4()
        time.sleep(15), entrar()
        time.sleep(1), selecionarboss()
        time.sleep(1), minerar()
        time.sleep(3) , pyautogui.hotkey('alt', 'f4')
        conta = 1

    time.sleep(6000)

# 2ª conta = LUNA 2  ( SEU ENDEREÇO DE WALLET)  -> email : seu_email@gmail.com
# 3ª conta = lUNA 3 (SEU ENDEREÇO DE WALLET) -> email :  seu_email@gmail.com
# 4ª conta = LUNA 4  (SEU ENDEREÇO DE WALLET)  -> email :  seu_email@gmail.com