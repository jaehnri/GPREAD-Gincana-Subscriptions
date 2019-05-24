import gspread 
from oauth2client.service_account import ServiceAccountCredentials
import pprint
import re

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

sheet = client.open('Inscrição Provas gincana  (respostas)').sheet1

pp = pprint.PrettyPrinter()
subscribers = sheet.get_all_records()

def phone_model(string):
    string = ''.join([n for n in str(string) if n.isdigit()])   
    
    if (string [0:2] == '55'):
        string = string[2:]
    return string[0:2] + ' ' + string[2:7] + '-' + string[7:]

def mostrar_codigos():
    print('Provas Disponíveis: \n')
    print('00) League of Legends')
    print('01) Video da instituição')
    print('02) Logo')
    print('03) Bandeira da equipe')
    print('04) Video')
    print('05) Artes Visuais')
    print('06) Artes: Teatro')
    print('07) Artes: Dança')
    print('08) Damas')
    print('09) Xadrez')
    print('10) O que eu posso fazer por você agora?')
    print('11) Show de talentos: Musicais')
    print('12) Mini ONU')
    print('13) Calouro 2019 (Camiseta)')
    print('14) Magic')
    print('15) You-gi-oh')
    print('16) Pokémon')
    print('17) Rescue robot (MEC)')
    print('18) Forró')
    print('19) Escape Room')
    print('20) Just Dance')
    print('21) Prova de Busca')
    print('22) Quem sabe, sabe')
    print('23) Qual é a musica')
    print('24) FIFA')
    print('25) Volei')
    print('26) Futebol')
    print('27) Cubo Mágico')
    print('28) Unreal')
    print('29) Counter Strike')

print('|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|')
print('|================================== BEM VINDO ==================================|')
print('|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|\n')
print("(Para ver o código de todas as provas, apenas pressione [ENTER]\n")
print('Digite o código da prova: ')

codigo = input()

if (codigo == ''):
    mostrar_codigos()
    print("\n(Para ver o código de todas as provas, apenas pressione [ENTER]\n")
    print('Digite o código da prova: ') 

if (codigo != ''):
    for sub in range(0,len(subscribers)):
        if ("LOL" in subscribers[sub]['Quais provitchas o senhor irá participar?']):
            pp.pprint(' '.join(subscribers[sub]['Fala o nominho (COMPLETO ) pra mim'].split()[0:3]).ljust(25)[:25])
            pp.pprint(subscribers[sub]['Qual sua sala?'])
            pp.pprint(phone_model("".join(str(subscribers[sub]['manda o zap com ddd']).split())))
            
            print()

