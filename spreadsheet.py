import gspread 
from oauth2client.service_account import ServiceAccountCredentials
import pprint

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

sheet = client.open('Inscrição Provas gincana  (respostas)').sheet1

pp = pprint.PrettyPrinter()
subscribers = sheet.get_all_records()

def phone_model(string):
    return string[0:2] + ' ' + string[2:7] + '-' + string[7:]


for sub in range(0,len(subscribers)):
    if ("LOL" in subscribers[sub]['Quais provitchas o senhor irá participar?']):
        pp.pprint(' '.join(subscribers[sub]['Fala o nominho (COMPLETO ) pra mim'].split()[0:3]).ljust(25)[:25])
        pp.pprint(subscribers[sub]['Qual sua sala?'])
        pp.pprint(phone_model("".join(str(subscribers[sub]['manda o zap com ddd']).split())))
        
        print()

    