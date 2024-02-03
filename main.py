# - Imports -
# ☇ It was used to get the screen size and clean the console
import os

# ☇ Only the sleep function was used
from time import sleep

# ☇ Used to jsonify the requests
import json

# ☇ Used to make requests
from requests import get

# - Reusable variables -
# ☇ List of options that is reused in the _menu function
options = [
    "localizar IP",
    "localizar DDD",
    "Consultar CNPJ",
    "localizar CEP",
    "Consulta WhoIS",
    "Verificar Telefone"
]
_options = [0, 1, 2, 3, 4, 5, 6, 99]

R="\033[1;31m";G="\033[1;32m";B="\033[1;34m";Y="\033[1;33m";r="\033[0m";n="\033[1m"

def cls():
    # - Function to clean the console

    os.system('cls' if os.name=='nt' else 'clear')

# ☇ "[+]" colored
start = f"{n}[{B}+{r}{n}] "

# - Main code -

class metodos:
    def whois():
        domain=input("%s%sDigite o dominio que deseja consultar:%s "%(start,B,r));cls()
        headers={"apikey": "2nY2gxtScwH6mPVmOSYstS8oVmF4ltbb"}
        rsp=get(url=f"https://api.apilayer.com/whois/query?domain={domain}",headers=headers)
        rspj=rsp.json()
        match rsp.status_code:
            case 200:
                metodos.ndict(rspj)
                print("%s%sPeço desculpas por não traduzir as respostas, veja porque não traduzir em: https://github.com/kvgnx54/ghostpanel%s"%(start,Y,r))
                input("\n%s%sAperte a tecla %s%sEnter%s%s para voltar.%s"%(start,B,r,G,r,B,r))
            case _:
                print("%s[%s!%s%s] %s%s%s"%(n,R,r,n,R,str(rspj["message"]),r));print("%sSe o site começa com https:// remova essa parte.%s"%(start,r));input("\n%s%sAperte a tecla %s%sEnter%s%s para voltar.%s"%(start,B,r,G,r,B,r))
    def cep():
        _cep=input("%s%sDigite o cep que deseja localizar:%s "%(start,B,r));cls()
        cep=[]
        for remove in _cep:
            if remove.isnumeric:cep.append(remove)
            else:pass
        cep="".join(cep)
        if cep=="":print();input("\n%s%sAperte a tecla %s%sEnter%s%s para voltar.%s"%(start,B,r,G,r,B,r))
        else:
            rsp=get("https://cep.awesomeapi.com.br/%s"%(cep))
            rspj=rsp.json()
            match rsp.status_code:
                case 200:
                    print("%sCep: %s%s"%(start,str(rspj["cep"]),r))
                    print("%sTipo do endereço: %s%s"%(start,str(rspj["address_type"]),r))
                    print("%sNome do endereço: %s%s"%(start,str(rspj["address_name"]),r))
                    print("%sEndereço completo: %s%s"%(start,str(rspj["address"]),r))
                    print("%sEstado: %s%s"%(start,str(rspj["state"]),r))
                    print("%sCidade: %s%s"%(start,str(rspj["city"]),r))
                    print("%sBairro: %s%s"%(start,str(rspj["district"]),r))
                    print("%sCódigo IBGE: %s%s"%(start,str(rspj["city_ibge"]),r))
                    print("%sDDD: %s%s"%(start,str(rspj["ddd"]),r))
                    print("%sLatitude: %s%s"%(start,str(rspj["lat"]),r))
                    print("%sLongitude: %s%s"%(start,str(rspj["lng"]),r))
                    print("%s%sLink do Google maps: https://www.google.com/maps/place/%s,%s%s"%(start,Y,str(rspj["lat"]),str(rspj["lng"]),r))
                    input("\n%s%sAperte a tecla %s%sEnter%s%s para voltar.%s"%(start,B,r,G,r,B,r))
                case _:
                    print("%s[%s!%s%s] %s%s%s"%(n,R,r,n,R,str(rspj["message"]),r));input("\n%s[%s+%s%s%s] %sAperte a tecla %s%sEnter%s%s para voltar.%s"%(start,B,r,G,r,B,r))
    def vt():
        _cll=input("%s%sDigite o telefone que deseja verificar:%s "%(start,B,r))
        cls()
        cll=[]
        for remove in _cll:
            if remove.isnumeric:cll.append(remove)
            else:pass
        cll="".join(cll)
        if cll == "":print();input("\n%s%sAperte a tecla %s%sEnter%s%s para voltar.%s"%(start,B,r,G,r,B,r))
        else:
            rsp=get("https://phonevalidation.abstractapi.com/v1/?api_key=b8d6fe3c1915403989b5e28416c75fbc&phone=%s"%(cll))
            rspj=rsp.json()
            if rsp.status_code != 200:
                rsp=get(url="https://api.apilayer.com/number_verification/validate?number=%s"%(cll),headers={'apikey': '2nY2gxtScwH6mPVmOSYstS8oVmF4ltbb'})
                rspj=rsp.json()
            
            metodos.ndict(rspj)
            print("%sSe a requisição retornou o codigo erro use o numero no formato +00 00 00000-0000%s"%(start,r))
            input("\n%s%sAperte a tecla %s%sEnter%s%s para voltar.%s"%(start,B,r,G,r,B,r))
    # Função para usar quando eu tiver com preguiça de fazer print manualmente
    def nlist(LIST):
        for value in range(0, len(LIST)):
            if isinstance(LIST[value], dict):
                metodos.ndict(LIST[value])
            elif isinstance(LIST[value], list):
                metodos.nlist(LIST[value])
            else:
                print("%s%s%s"%(start,LIST[value],r))
    # Função para usar quando eu tiver com preguiça de fazer print manualmente
    def ndict(DICT):
        for key, value in DICT.items():
            if isinstance(value, dict):
                print("%s[%s-%s%s] %s: %s"%(n,B,r,n,key,r))
                metodos.ndict(value)
            elif isinstance(value, list):
                print("%s[%s-%s%s] %s: %s"%(n,B,r,n,key,r))
                metodos.nlist(value)
            else:
                print("%s%s: %s%s"%(start,key,value,r))
    def cnpj():
        _cnpj=input("%s%sDigite o CNPJ que deseja consultar%s: "%(start,B,r));cls()
        cnpj=[]
        for remove in _cnpj:
            if remove.isnumeric():cnpj.append(remove)
            else:pass
        _cnpj="".join(cnpj)
        cnpj=[]
        cnpj.append(_cnpj)
        if cnpj=="":print();input("\n%s%sAperte a tecla %s%sEnter%s%s para voltar.%s"%(start,B,r,G,r,B,r))
        else:
            rsp=get("https://brasilapi.com.br/api/cnpj/v1/%s"%(cnpj))
            rspj=rsp.json()
            if rsp.status_code!=200:print("%s[%s!%s%s] %s%s%s"%(n,R,r,n,R,str(rspj["message"]),r))
            else:metodos.ndict(rspj)
            input("\n%s%sAperte a tecla %s%sEnter%s%s para voltar.%s"%(start,B,r,G,r,B,r))
    def ddd():
        ddd=input("%s%sDigite o DDD que deseja consultar%s: "%(start,B,r));cls()
        rsp=get("https://brasilapi.com.br/api/ddd/v1/%s"%(ddd))
        rspj=rsp.json()
        match rsp.status_code:
            case 200:
                print("%s%sEstado: %s%s"%(start,Y,str(rspj["state"]),r))
                if type(rspj["cities"])==list:
                    for i in range(0, len(rspj["cities"])):
                        print("%sCidade %s: %s%s"%(start,i+1,str(rspj["cities"][i]),r))
                else:pass
                input("\n%s%sAperte a tecla %s%sEnter%s%s para voltar.%s"%(start,B,r,G,r,B,r))
            case _:print("%s[%s!%s%s] %s%s%s"%(n,R,r,n,R,str(rspj["message"]),r));input("\n%s[%s+%s%s%s] %sAperte a tecla %s%sEnter%s%s para voltar.%s"%(start,B,r,G,r,B,r))
    def ip():
        ip=input("%s%sDigite o IP que deseja localizar%s: "%(start,B,r));cls()
        rsp=get("http://ip-api.com/json/%s"%(ip))
        rspj=rsp.json()
        if rspj["status"]=="success":
            print("%sStatus: sucesso%s"%(start,r))
            print("%sPaís: %s%s"%(start,str(rspj["country"]),r))
            print("%sSigla País: %s%s"%(start,str(rspj["countryCode"]),r))
            print("%sEstado: %s%s"%(start,str(rspj["regionName"]),r))
            print("%sCidade: %s%s"%(start,str(rspj["city"]),r))
            print("%sCódigo ZIP: %s%s"%(start,str(rspj["zip"]),r))
            print("%sLatitude: %s%s"%(start,str(rspj["lat"]),r))
            print("%sLongitude: %s%s"%(start,str(rspj["lon"]),r))
            print("%sIP: %s%s"%(start,str(rspj["query"]),r))
            print("%sLink do Google maps: https://www.google.com/maps/place/%s,%s%s"%(start,str(rspj["lat"]),str(rspj["lon"]),r))
            input("\n%s%sAperte a tecla %s%sEnter%s%s para voltar.%s"%(start,B,r,G,r,B,r))
        else:print("%s[%s!%s%s] %sOcorreu um erro na requisição. Status:  %s%s%s"%(n,R,r,n,R,r,rspj["status"],r));input("%s%sAperte a tecla %s%sEnter%s%s para voltar.%s"%(start,B,r,G,r,B,r))

def _menu(txt:list = "",rst=False):
    """
    - This function prints all available options to select from the menu
    - Explanation:
    - - Basically the function will take a list called "options" and add the option to the menu.
    """

    if txt == "":
        txt = options
    size = os.get_terminal_size().columns
    contagem = 0
    for item in txt:
        contagem += 1
        strcont = f"[{contagem}] "
        if rst == True:
            strcont = ""
        if len(item) > (size-6):
            print(" │",strcont+str(item)[:(size-6-len(strcont))],"│")
            _menu(txt=[str(item)[(size-6):]],rst=True)
        else:
            print(" │",strcont+str(item),"│".rjust(size-5-len(str(item))-len(strcont)))

def menu():
    """
    - Function that creates the menu
    """
    while True:
        # ☇ Screen Size
        size = os.get_terminal_size().columns
        size = size - 4
        # ☇ Clear console
        cls()
        print(" ╭"+"─"*(size)+"╮")
        print(" │"+str("GhostPanel").center(size)+"│")
        print(" ╞"+"═"*(size)+"╡")
        _menu()
        print(" │","│".rjust(size))
        print(" │","[99] Api's","│".rjust(size-11))
        print(" │","[0] Sair","│".rjust(size-9))
        print(" ├"+"─"*(size)+"╯")
        ipt = input(f" ├({start}Numero da opção{r}) ")
        cls()
        try:
            ipt = int(ipt)
            if ipt not in _options:
                cls()
                print(f"{start}Escolha uma opção válida{r}")
                sleep(2)
                cls()
        except:
            cls()
            print(f"{start}Escolha uma opção válida{r}")
            sleep(2)
            cls()
        match ipt:
            case 1:
                metodos.ip()
            case 2:
                metodos.ddd()
            case 3:
                metodos.cnpj()
            case 4:
                metodos.cep()
            case 5:
                metodos.whois()
            case 6:
                metodos.vt()
            case 0:
                exit("%sObrigado por usar o GhostPanel!%s"%(start,r))
            case 99:
                apisusadas={
                    "IP": "ip-api.com",
                    "DDD": "brasilapi.com.br",
                    "CNPJ": "brasilapi.com.br",
                    "Cep": "cep.awesomeapi.com.br",
                    "WhoIS": "apilayer.com",
                    "Verificação de telefone": "apilayer.com",
                    "Verificação de telefone 2": "phonevalidation.abstractapi.com"}
                metodos.ndict(apisusadas)
                input("\n%s%sAperte a tecla %s%sEnter%s%s para voltar.%s"%(start,B,r,G,r,B,r))


            case _:
                print(f"{start}Escolha uma opção válida{r}")


if __name__ == "__main__":
    menu()
