<h1 align="center">☠️ GhostPanel ☠️</h1>

> Um painel de consultas simples feito 100% em python.

<h2 align="center">🔰 Instalação 🔰</h2>
<h3>⚙️ Automática</h3>

> Funciona em qualquer máquina que o bash tiver instalado.

> Não precisa ter o python instalado.

```bash
apt install git -y
git clone https://github.com/kvgnx54/ghostpanel
cd ghostpanel
bash install.sh
```

<h3>📱 Termux</h3>

> Baixando o python e as bibliotecas.
```bash
pkg update
pkg upgrade
pkg install python
pkg install git
git clone https://github.com/kvgnx54/ghostpanel
```
> Quando for utilizar o GhostPanel:
```bash
cd ghostpanel
python main.py
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
