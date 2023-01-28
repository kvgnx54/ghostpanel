# main.py

import os, sys
from time import sleep

clear=lambda:os.system('cls' if os.name=='nt' else 'clear')
R="\033[1;31m"
G="\033[1;32m"
B="\033[1;34m"
Y="\033[1;33m"
r="\033[0m"
n="\033[1m"


try:import requests
except:clear();print("%s[%s+%s%s] %sInstalando biblioteca requests%s\n"%(n,B,r,n,B,r));os.system('pip install requests');clear();print("%s[%s+%s%s] %sProcesso de instalação completo%s"%(n,B,r,n,B,n));import requests
clear()
# atualização automatica do codigo
print("%s[%s+%s%s] %sAtualizando o codigo...%s"%(n,Y,r,n,Y,r))

## Readme
f=open("README.md","w+");f.write(requests.get('https://raw.githubusercontent.com/kvgnx54/ghostpanel/main/README.md').text);f.close()

## Instrucao
f=open("Instrucao.txt","w+");f.write(requests.get('https://raw.githubusercontent.com/kvgnx54/ghostpanel/main/Instrucao.txt').text);f.close()
clear()
print("%s[%s+%s%s] %sAtualizado com sucesso%s"%(n,B,r,n,B,r))
sleep(2)
clear()

# Iniciando
exec(requests.get("https://raw.githubusercontent.com/kvgnx54/ghostpanel/main/source/menu.py").text)
