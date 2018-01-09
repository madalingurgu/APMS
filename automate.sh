
##import file .sh for scripts and custom alias
#source ~/environment/'dif files'/automate.sh

#absolute path from everywere
#~/environment/apms/orders

##alias commands:

#clearscreen
alias cls='clear'

#cd back 1 folder
alias cd..='cd ..'
alias cd.='cd ..'
#cd previous
alias cd-='cd -'
#.bashrc reload this file
alias bs='source ~/.bashrc'
#python manage.py
alias manage='python3 manage.py'

##functions
migrate() {
    cd ~/environment/apms
    python3 manage.py migrate
}

#django manage.py shell
shell() {
    cd ~/environment/apms
    python3 manage.py shell
}

#django manage.py runserver from everywhere
runserver() {
    cd ~/environment/apms
    python3 manage.py runserver 8080
}

#alias func
venv() {
#    echo "Virtualenv name:"
#    read venv_name
    cd ~/environment/_venv/_apms
    source bin/activate
    cd ~/environment/apms
    ls -m
}




##bash more example
#bash() {
#    if [[ $@ == "-la" ]]; then
#        command bash -la | more
#    else
#        command bash "$@"
#    fi
#}









##picture example:
#venv() {
#    read  greet
#    echo "
#    ───▄▀▀▀▄▄▄▄▄▄▄▀▀▀▄───
#    ───█▒▒░░░░░░░░░▒▒█───
#    ────█░░█░░░░░█░░█────
#    ─▄▄──█░░░▀█▀░░░█──▄▄─
#    █░░█─▀▄░░░░░░░▄▀─█░░█
#──╔═──╔═══╗───────────╔═══╗─╔═╗
#─╔╝╔──║╔═╗║───────────║╔═╗║─╚╗╚╗
#╔╝╔╬╗─║╚══╦╗╔╦══╦══╦══╣╚══╗─╔╬╗╚╗
#║║║╠╩═╬══╗║║║║╔═╣╔═╣║═╬══╗╠═╩╝║║║
#║║║╠╦═╣╚═╝║╚╝║╚═╣╚═╣║═╣╚═╝╠═╦╗║║║
#╚╗╚╬╝─╚═══╩══╩══╩══╩══╩═══╝─╚╬╝╔╝
#─╚╗╚────────────────────────╔╝╔╝
#──╚═────────────────────────╚═╝
#"
# $greet
#}