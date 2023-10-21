!!!!! IMPORTANTE !!!!!!!
Bom, no codigo todo é necessario que você altere o x e y de tudo, vai demorar um pouco mas como eu não sabia onde ficava cada botão na sua tela nem a proporção nem resolução da tela, de todo jeito você teria que descobrir e me mandar, então só descobrir e trocar a informação no proprio codio.

Exemplo:

NO ARQUIVO AutoDelphin.py temos este seguinte codigo no incio: 
    x_create_profile = 1350  # Substitua pelo valor correto
    y_create_profile = 48  # Substitua pelo valor correto

        # Mova o cursor do mouse para as coordenadas do botão "Create Profile" e clique
    pyautogui.moveTo(x_create_profile, y_create_profile)
    pyautogui.click()
Aqui basta alterar as variaveis x_create_profile que seria onde está o x do botão create profile do dolphin na sua tela e a variavel y dele

No incio do arquivo AutoDelphin ele tem esses seguintes codigos: 
    caminho_executavel_dolphin = r'C:/Users/heito/AppData/Local/Programs/Dolphin Anty/Dolphin Anty.exe'
Neste codigo é necessario que você troque para o caminho do seu executavel dolphin, para achar esse caminho basta abrir o explorador de arquivos clicar com o botão direito no executavel do dolphin e selecionar a opção 'Copiar como caminho' em seguida só colar no codigo. Certifique-se de que ele não contenha contra barras '\' e sim  barras normais '/'.

Ja neste codigo aqui;
    subprocess.Popen(caminho_executavel_dolphin, shell=True)
ele automaticamente abre o dolphin sozinho pra você então antes de iniciar o arquivo certifique-se de que o dolphin esta fechado.

Explicar agora o time.sleep:

Bom o time.sleep que tem em seguida da maioria dos codigos é para ter um intervalo o numero dentro dos colchetes (1) é o numero em segundos de quanto tempo de intervalo tera para executar a proxima linha de codigo, ajuste para o tempo que você preferir.

Falando agora do arquivo Deposito.py bom nele é necessario tambem alterar as posições x e y de tudo, dentro do arquivo tem tudo comentado e tambem é preciso que você mantenha o site da Tech play aberto no outro monitor e passe a posição dele na codigo do Deposito.py. O resto esta explicado no arquivo do codigo.
5

!!!!! IMPORTANTE !!!!!!!