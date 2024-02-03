![logo](https://github.com/kvgnx54/ghostpanel/blob/main/gplogo.jpg)
<h1 align="center">GhostPanel</h1>
> Última atualização: 03/02/2024

> Um painel de consultas simples feito 100% em python.

<h2 align="center">🔰 Instalação 🔰</h2>
<h3>⚙️ Automática(Linux/Termux)</h3>

> Não precisa ter o python instalado.

```bash
curl -o install.sh https://raw.githubusercontent.com/kvgnx54/ghostpanel/main/install.sh
bash install.sh && rm -r install.sh
```

<h3>📱 Linux/Termux</h3>

> Baixando o python e as bibliotecas.
```bash
pkg update
pkg upgrade
pkg install python
pkg install git
git clone https://github.com/kvgnx54/ghostpanel
pip install requests
```
> Quando for utilizar o GhostPanel:
```bash
cd
cd ghostpanel
python main.py
```
<h2 align="center">♻️ Atualização de código ♻️</h2>
<h3>📱 Linux/Termux</h3>

> É importante sempre verificar se há atualização disponível para o código.
> Futuramente o arquivo main.py vai ter uma opção de verificação automática.

```bash
curl -o update.sh https://raw.githubusercontent.com/kvgnx54/ghostpanel/main/update.sh
bash update.sh && rm -r update.sh
```
<h2 align="center">⚙️ Problemas ⚙️</h2>

> Se você achou algum problema no código, crie um issue na parte de issues.

<h3>❗ Problemas de tradução</h3>

> Em algumas opções de consultas, existem alguns problemas na tradução.

> Exemplo do WhoIs:

```
[-] result:
[+] domain_name: 
[+] registrar: 
[+] whois_server: 
[+] referral_url: 
[+] updated_date: 
[+] creation_date: 
```
> Esses problemas de tradução ocorrem porque o script utiliza algumas API's que não são brasileiras e como o script imprimi automaticamente no terminal, alguns problemas de tradução ocorrem. Peço desculpas por todos os problemas.
