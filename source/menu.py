# menu.py

# IMPORTS
import os, sys,json
from time import sleep
from requests import get

# VARIAVEIS
clear=lambda:os.system('cls' if os.name=='nt' else 'clear')
R="\033[1;31m";G="\033[1;32m";B="\033[1;34m";Y="\033[1;33m";r="\033[0m";n="\033[1m"



# INICIO DO MENU
class menu():
    clear()
    def whois():
        domain=input("%s[%s+%s%s] %sDigite o dominio que deseja consultar:%s "%(n,B,r,n,B,r));clear()
        headers={"apikey": "2nY2gxtScwH6mPVmOSYstS8oVmF4ltbb"}
        rsp=get(url="https://api.apilayer.com/whois/query?domain=%s"%(domain),headers=headers)
        rspj=rsp.json()
        match rsp.status_code:
            case 200:
                menu.ndict(rspj)
                print("%s[%s+%s%s]%s Peço desculpas por não traduzir as respostas, veja porque não traduzir em: https://github.com/kvgnx54/ghostpanel%s"%(n,Y,r,n,Y,r))
                input("\n%s[%s+%s%s] %sAperte a tecla %s%sEnter%s%s para voltar.%s"%(n,B,r,n,B,r,G,r,B,r))
            case _:
                print("%s[%s!%s%s] %s%s%s"%(n,R,r,n,R,str(rspj["message"]),r));input("\n%s[%s+%s%s%s] %sAperte a tecla %s%sEnter%s%s para voltar.%s"%(n,B,r,n,B,r,G,r,B,r))
    def cep():
        _cep=input("%s[%s+%s%s] %sDigite o cep que deseja localizar:%s "%(n,B,r,n,B,r));clear()
        cep=[]
        for remove in _cep:
            if remove.isnumeric:cep.append(remove)
            else:pass
        cep="".join(cep)
        if cep=="":print();input("\n%s[%s+%s%s] %sAperte a tecla %s%sEnter%s%s para voltar.%s"%(n,B,r,n,B,r,G,r,B,r))
        else:
            rsp=get("https://cep.awesomeapi.com.br/%s"%(cep))
            rspj=rsp.json()
            match rsp.status_code:
                case 200:
                    print("%s[%s+%s%s] %sCep: %s%s"%(n,B,r,n,Y,str(rspj["cep"]),r))
                    print("%s[%s+%s%s] %sTipo do endereço: %s%s"%(n,B,r,n,Y,str(rspj["address_type"]),r))
                    print("%s[%s+%s%s] %sNome do endereço: %s%s"%(n,B,r,n,Y,str(rspj["address_name"]),r))
                    print("%s[%s+%s%s] %sEndereço completo: %s%s"%(n,B,r,n,Y,str(rspj["address"]),r))
                    print("%s[%s+%s%s] %sEstado: %s%s"%(n,B,r,n,Y,str(rspj["state"]),r))
                    print("%s[%s+%s%s] %sCidade: %s%s"%(n,B,r,n,Y,str(rspj["city"]),r))
                    print("%s[%s+%s%s] %sBairro: %s%s"%(n,B,r,n,Y,str(rspj["district"]),r))
                    print("%s[%s+%s%s] %sCódigo IBGE: %s%s"%(n,B,r,n,Y,str(rspj["city_ibge"]),r))
                    print("%s[%s+%s%s] %sDDD: %s%s"%(n,B,r,n,Y,str(rspj["ddd"]),r))
                    print("%s[%s+%s%s] %sLatitude: %s%s"%(n,B,r,n,Y,str(rspj["lat"]),r))
                    print("%s[%s+%s%s] %sLongitude: %s%s"%(n,B,r,n,Y,str(rspj["lng"]),r))
                    input("\n%s[%s+%s%s] %sAperte a tecla %s%sEnter%s%s para voltar.%s"%(n,B,r,B,r,G,r,B,r))
                case _:
                    print("%s[%s!%s] %s%s%s"%(n,R,r,R,str(rspj["message"]),r));input("\n%s[%s+%s%s%s] %sAperte a tecla %s%sEnter%s%s para voltar.%s"%(n,B,r,n,B,r,G,r,B,r))
    def vt():
        _cll=input("%s[%s+%s%s] %sDigite o telefone que deseja verificar:%s "%(n,B,r,B,r))
        clear()
        cll=[]
        for remove in _cll:
            if remove.isnumeric:cll.append(remove)
            else:pass
        cll="".join(cll)
        if cll == "":print();input("\n%s[%s+%s%s] %sAperte a tecla %s%sEnter%s%s para voltar.%s"%(n,B,r,B,r,G,r,B,r))
        else:
            rsp=get("https://phonevalidation.abstractapi.com/v1/?api_key=b8d6fe3c1915403989b5e28416c75fbc&phone=%s"%(cll))
            rspj=rsp.json()
            menu.ndict(rspj)
            input("\n%s[%s+%s%s] %sAperte a tecla %s%sEnter%s%s para voltar.%s"%(n,B,r,B,r,G,r,B,r))
    # Função para usar quando eu tiver com preguiça de fazer print manualmente
    def nlist(LIST):
        for value in range(0, len(LIST)):
            if isinstance(LIST[value], dict):
                menu.ndict(LIST[value])
            elif isinstance(LIST[value], list):
                menu.nlist(LIST[value])
            else:
                print("%s[%s+%s%s] %s%s%s"%(n,B,r,n,Y,LIST[value],r))
    # Função para usar quando eu tiver com preguiça de fazer print manualmente
    def ndict(DICT):
        for key, value in DICT.items():
            if isinstance(value, dict):
                print("%s[%s-%s%s] %s%s: %s"%(n,B,r,n,Y,key,r))
                menu.ndict(value)
            elif isinstance(value, list):
                print("%s[%s-%s%s] %s%s: %s"%(n,B,r,n,Y,key,r))
                menu.nlist(value)
            else:
                print("%s[%s+%s%s] %s%s: %s%s"%(n,B,r,n,Y,key,value,r))
    def cnpj():
        _cnpj=input("%s[%s+%s%s] %sDigite o CNPJ que deseja consultar%s: "%(n,B,r,n,B,r));clear()
        cnpj=[]
        for remove in _cnpj:
            if remove.isnumeric():cnpj.append(remove)
            else:pass
        _cnpj="".join(cnpj)
        cnpj=[]
        cnpj.append(_cnpj)
        if cnpj=="":print();input("\n%s[%s+%s%s] %sAperte a tecla %s%sEnter%s%s para voltar.%s"%(n,B,r,n,B,r,G,r,B,r))
        else:
            rsp=get("https://brasilapi.com.br/api/cnpj/v1/%s"%(cnpj))
            rspj=rsp.json()
            if rsp.status_code!=200:print("%s[%s!%s%s] %s%s%s"%(n,R,r,n,R,str(rspj["message"]),r))
            else:menu.ndict(rspj)
            input("\n%s[%s+%s%s] %sAperte a tecla %s%sEnter%s%s para voltar.%s"%(n,B,r,n,B,r,G,r,B,r))
    def ddd():
        ddd=input("%s[%s+%s%s] %sDigite o DDD que deseja consultar%s: "%(n,B,r,n,B,r));clear()
        rsp=get("https://brasilapi.com.br/api/ddd/v1/%s"%(ddd))
        rspj=rsp.json()
        match rsp.status_code:
            case 200:
                print("%s[%s+%s%s] %sEstado: %s%s"%(n,B,r,n,Y,str(rspj["state"]),r))
                if type(rspj["cities"])==list:
                    for i in range(0, len(rspj["cities"])):
                        print("%s[%s+%s%s] %sCidade %s: %s%s"%(n,Y,r,n,Y,i+1,str(rspj["cities"][i]),r))
                else:pass
                input("\n%s[%s+%s%s] %sAperte a tecla %s%sEnter%s%s para voltar.%s"%(n,B,r,n,B,r,G,r,B,r))
            case _:print("%s[%s!%s%s] %s%s%s"%(n,R,r,n,R,str(rspj["message"]),r));input("\n%s[%s+%s%s%s] %sAperte a tecla %s%sEnter%s%s para voltar.%s"%(n,B,r,n,B,r,G,r,B,r))
    def ip():
        ip=input("%s[%s+%s%s] %sDigite o IP que deseja localizar%s: "%(n,B,r,n,B,r));clear()
        rsp=get("http://ip-api.com/json/%s"%(ip))
        rspj=rsp.json()
        if rspj["status"]=="success":
            print("%s[%s+%s%s] %sStatus: sucesso%s"%(n,Y,r,n,Y,r))
            print("%s[%s+%s%s] %sPaís: %s%s"%(n,Y,r,n,Y,str(rspj["country"]),r))
            print("%s[%s+%s%s] %sSigla País: %s%s"%(n,Y,r,n,Y,str(rspj["countryCode"]),r))
            print("%s[%s+%s%s] %sEstado: %s%s"%(n,Y,r,n,Y,str(rspj["regionName"]),r))
            print("%s[%s+%s%s] %sCidade: %s%s"%(n,Y,r,n,Y,str(rspj["city"]),r))
            print("%s[%s+%s%s] %sCódigo ZIP: %s%s"%(n,Y,r,n,Y,str(rspj["zip"]),r))
            print("%s[%s+%s%s] %sLatitude: %s%s"%(n,Y,r,n,Y,str(rspj["lat"]),r))
            print("%s[%s+%s%s] %sLongitude: %s%s"%(n,Y,r,n,Y,str(rspj["lon"]),r))
            print("%s[%s+%s%s] %sIP: %s%s"%(n,Y,r,n,Y,str(rspj["query"]),r))
            input("\n%s[%s+%s%s] %sAperte a tecla %s%sEnter%s%s para voltar.%s"%(n,B,r,n,B,r,G,r,B,r))
        else:print("%s[%s!%s%s] %sOcorreu um erro na requisição. Status:  %s%s%s"%(n,R,r,n,R,r,rspj["status"],r));input("%s[%s+%s%s%s] %sAperte a tecla %s%sEnter%s%s para voltar.%s"%(n,B,r,n,B,r,G,r,B,r))
    def inicio():
        while True:
            clear()
            opt=input("""

%s█▀▀ █░█ █▀█ █▀ ▀█▀ █▀█ ▄▀█ █▄░█ █▀▀ █░░
█▄█ █▀█ █▄█ ▄█ ░█░ █▀▀ █▀█ █░▀█ ██▄ █▄▄%s
%s╔╦═════════════════════════════════════
║║%s「1」%sLocalizar IP%s
%s║║%s「2」%sLocalizar DDD%s
%s║║%s「3」%sConsultar CNPJ%s
%s║║%s「4」%sLocalizar CEP%s
%s║║%s「5」%sConsulta Whois%s
%s║║%s「6」%sVerificação telefone%s
%s║║
║║%s「0」%sSair%s
%s╠╩═════════════════════════════════════
╚> %s"""%(n,r,B,r,Y,r,B,r,Y,r,B,r,Y,r,B,r,Y,r,B,r,Y,r,B,r,Y,r,B,r,R,r,B,r))
            try:opt=int(opt)
            except:opt="erro"
            clear()
            match opt:
                case 1:menu.ip()
                case 2:menu.ddd()
                case 3:menu.cnpj()
                case 4:menu.cep()
                case 5:menu.whois()
                case 6:menu.vt()
                case 0:exit()
                case _:print("%s[%s!%s]%s Digite o número da opção desejada.%s"%(n,R,r,R,r));sleep(2)

if __name__=="__main__":
    menu.inicio()
