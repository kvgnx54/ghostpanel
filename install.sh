#!/bin/bash
# pode nao funcionar muito bem, e meu primeiro script em shell

reuse="\e[1m[\e[94m+\e[0m\e[1m]\e[94m"
clear
echo -e "$reuse Atualizando apt\e[0m"
sleep 2
clear
apt update
apt upgrade
clear
echo -e "$reuse Instalando python\e[0m"
sleep 2
clear
apt install python -y
clear

while true; do
    clear
    echo -e "$reuse Deseja iniciar o GhostPanel?\e[0m [\e[94ms/\e[91mn\e[0m\e[1m]\e[0m"
    read -n 1 opt
    clear
    if [ $opt == "s" ];then
        break
    elif [ $opt == "n" ];then
        exit
    else
        echo -e "\e[1m[\e[91m!\e[0m\e[1m] \e[91mEscreva s ou n.\e[0m"
        sleep 2
    fi
done
python main.py
