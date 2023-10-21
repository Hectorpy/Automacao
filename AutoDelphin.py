import subprocess
import time
import pyautogui

# Especifique o caminho completo para o executável do Dolphin
caminho_executavel_dolphin = r'C:/Users/heito/AppData/Local/Programs/Dolphin Anty/Dolphin Anty.exe'

# Número de vezes que você deseja executar o código
num_execucoes = 9

# Variável de contagem
execucoes_realizadas = 0

caixa_name = 1

sleep_incial = 30

subprocess.Popen(caminho_executavel_dolphin, shell=True)

while execucoes_realizadas < num_execucoes:
        # Aguarde alguns segundos para que o Dolphin seja carregado completamente
    time.sleep(sleep_incial)

        # Coordenadas do botão "Create Profile"
    x_create_profile = 1350  # Substitua pelo valor correto
    y_create_profile = 48  # Substitua pelo valor correto

        # Mova o cursor do mouse para as coordenadas do botão "Create Profile" e clique
    pyautogui.moveTo(x_create_profile, y_create_profile)
    pyautogui.click()

        # Aguarde um segundo para a próxima etapa
    time.sleep(1)

        # Escreva o número "1" na caixa "Input Name"
    pyautogui.write(str(caixa_name))

        # Coordenadas do botão "NEW FINGERPRINT"
    x_new_fingerprint = 1250  # Substitua pelo valor correto
    y_new_fingerprint = 100  # Substitua pelo valor correto

        # Mova o cursor do mouse para as coordenadas do botão "NEW FINGERPRINT" e clique duas vezes
    pyautogui.moveTo(x_new_fingerprint, y_new_fingerprint)
    pyautogui.click()
    time.sleep(0.5)
    pyautogui.click()

        # Aguarde um segundo para a próxima etapa
    time.sleep(0.5)

        # Coordenadas do botão "USER DATA"
    x_user_data = 1350  # Substitua pelo valor correto
    y_user_data = 180  # Substitua pelo valor correto

        # Mova o cursor do mouse para as coordenadas do botão "USER DATA" e clique
    pyautogui.moveTo(x_user_data, y_user_data)
    pyautogui.click()

        # Aguarde um segundo para a próxima etapa
    time.sleep(0.5)

        # Coordenadas do botão "Do not track"
    x_do_not_track = 530  # Substitua pelo valor correto
    y_do_not_track = 620  # Substitua pelo valor correto

        # Mova o cursor do mouse para as coordenadas do botão "Do not track" e clique
    pyautogui.moveTo(x_do_not_track, y_do_not_track)
    pyautogui.click()

        # Aguarde um segundo para a próxima etapa
    time.sleep(0.5)

        # Coordenadas do botão "Create"
    x_create = 1530  # Substitua pelo valor correto
    y_create = 100  # Substitua pelo valor correto

        # Mova o cursor do mouse para as coordenadas do botão "Create" e clique
    pyautogui.moveTo(x_create, y_create)
    pyautogui.click()

        # Incrementa a variável de contagem
    execucoes_realizadas += 1
    caixa_name += 1
    sleep_incial = 0.5
    
    if execucoes_realizadas == 9:
        time.sleep(2)
        # Iniciar os 9 navegadores em ordem
        pyautogui.moveTo(600, 170) # Botão de inciar do primeiro 
        pyautogui.click()
        time.sleep(0.1)
        pyautogui.moveTo(600, 220) # Botão de inciar do Segundo
        pyautogui.click()
        time.sleep(0.1)
        pyautogui.moveTo(600, 290) # Botão de inciar do Terceiro 
        pyautogui.click()
        time.sleep(0.1)
        pyautogui.moveTo(600, 340) # Botão de inciar do Quarto 
        pyautogui.click()
        time.sleep(0.1)
        pyautogui.moveTo(600, 400) # Botão de inciar do Quinto 
        pyautogui.click()
        time.sleep(0.1)
        pyautogui.moveTo(600, 470) # Botão de inciar do Sexto 
        pyautogui.click()
        time.sleep(0.1)
        pyautogui.moveTo(600, 530) # Botão de inciar do Setimo 
        pyautogui.click()
        time.sleep(0.1)
        pyautogui.moveTo(600, 590) # Botão de inciar do Oitavo 
        pyautogui.click()
        time.sleep(0.1)
        pyautogui.moveTo(600, 645) # Botão de inciar do Nono 
        pyautogui.click()
        time.sleep(35)
        contagem = 1
        numero_final = 9
        while contagem < numero_final:
            # Onde sera posto os usuarios por ordem
            usuarios = 'Utmal'
            senhas = 'Bravo123@'
            if contagem == 2:
                usuarios = 'Gagodfc'
                senhas = 'Bravo123@'
            elif contagem == 3:
                usuarios = 'Terceiro usuario'
                senhas = 'Terceira senha'
            elif contagem == 4:
                usuarios = 'Quarto usuario'
                senhas = 'Quarta senha'
            elif contagem == 5:
                usuarios = 'Quinto usuario'
                senhas = 'Quinta senha'
            elif contagem == 6:
                usuarios = 'Sexto usuario'
                senhas = 'Sexta senha'
            elif contagem == 7:
                usuarios = 'Setimo usuario'
                senhas = 'Setima senha'
            elif contagem == 8:
                usuarios = 'Oitavo usuario'
                senhas = 'Oitavo senha'
            elif contagem == 9:
                usuarios = 'Nono usuario'
                senhas = 'Nona senha'
            # Iniciar o login na betano e abrir ela
            pyautogui.write("https://br.betano.com")
            pyautogui.press("enter")
            time.sleep(11)
            # Mover para o botão inicar sessão na betano
            pyautogui.moveTo(1200, 190) 
            pyautogui.click()
            time.sleep(1)
            pyautogui.click()
            time.sleep(3)
            # Clicar no não sou um robô
            pyautogui.moveTo(430, 465)
            pyautogui.click()
            time.sleep(8)
            # Escrever o primeiro usuario da primeira conta
            pyautogui.write(usuarios)
            time.sleep(1)
            # Mover para o campo de senha
            pyautogui.moveTo(800, 480)
            pyautogui.click()
            time.sleep(0.2)
            # Escrever a senha da primeira conta
            pyautogui.write(senhas)
            time.sleep(0.3)
            # Mover para o botão de entrar na conta
            pyautogui.moveTo(800, 550)
            pyautogui.click()
            time.sleep(5)
            # Clicar na barra de pesquisa para trocar o link do site
            pyautogui.moveTo(800, 90)
            pyautogui.click()
            pyautogui.write('br.betano.com/myaccount/marketingbonus') #Link da aba pra colocar o bonus
            pyautogui.press("enter")
            time.sleep(4)
            pyautogui.moveTo(430, 465) # Caixa pra escrever o codigo bonus
            pyautogui.click()
            time.sleep(2)
            pyautogui.write('OGOLVIP') # Assim que entrar na aba ja escrever o bonus
            pyautogui.press("enter")
            # Minimizar a primeira aba e fazer tudo dnv na segunda
            time.sleep(5)
            pyautogui.moveTo(1158, 30)
            pyautogui.click()
            contagem += 1

print("Execução concluída.")