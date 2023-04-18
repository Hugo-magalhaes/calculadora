
'''
pyinstaller
--name='Calculadora' # ? Nome da aplicação
--noconfirm # ? Não pedir confirmação durante a execução
--onefile # ? Uma arquivo só para a aplicação
--add-data= # ? Adiciona a pasta ao arquivo
--icon= # ? Coloca icone geral da aplicação
--noconsole # ? Não inicializar console durante o executável
--clean # ? Limpa tudo
--log-level=WARN # ? Só apresentar os avisos
"./calculadora/main.py" # ? Roda o arquivo que inicializa a aplicação
--distpath # ? Local do arquivo de dist(ribuição)
--workpath # ? Local do arquivo de build
--specpath # ? Local do arquivo exec
'''


'''
pyinstaller 
--name='Calculadora' 
--noconfirm 
--onefile 
--add-data='../calcudora//files/;files/' 
--icon='../calculadora/files/icone_calculadora.png' 
--noconsole 
--clean 
--log-level=WARN 
--distpath="pasta_log/dist" 
--workpath="pasta_log/build" 
--specpath="pasta_log/" 
"calculadora/main.py"

'''
