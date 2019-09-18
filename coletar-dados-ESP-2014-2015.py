from selenium import webdriver
import pandas as pd

# Criar instância do navegador
firefox = webdriver.Firefox(executable_path='/home/matheus/geckodriver-v0.24.0-linux64/geckodriver')

# Abrir a página do Python Club
firefox.get('https://www.soccernews.com/soccer-transfers/spanish-la-liga-transfers-2014-2015/')


# Seleciono todos os elementos que possuem a class Table2__tr
date = firefox.find_elements_by_class_name("date")
player = firefox.find_elements_by_class_name("player-deals")
team_to = []
for i in range(1, date.__len__()-9):
    a = firefox.find_elements_by_xpath('//*[@id="epl"]/table/tbody/tr[{}]/td[6]'.format(i))
    team_to.append(a[0].text)
    i+=1
team_from = []
for i in range(1, date.__len__()-9):
    a = firefox.find_elements_by_xpath('//*[@id="epl"]/table/tbody/tr[{}]/td[4]'.format(i))
    team_from.append(a[0].text)
    i+=1
price = firefox.find_elements_by_class_name("price-status")

#print(team_to[2])
#print(date[0].text)

# Criando lista para receber os outputs

dados = {'Data':[], 'Nome':[],'Saída':[], 'Destino':[], 'Preço':[]}

for i in range(date.__len__()):
    dados['Data'].append(date[i].text)
    a = player[i].text
    b = a.split("\n")
    dados['Nome'].append(b[0])
    dados['Preço'].append(price[i].text)
for i in range(team_from.__len__()):
    dados['Saída'].append(team_from[i])
    dados['Destino'].append(team_to[i])
for i in range(team_from.__len__(), date.__len__()):
    dados['Saída'].append(i)
    dados['Destino'].append(i)

df = pd.DataFrame(dados)
df.to_csv(r'/home/matheus/Transferências/transferencias.csv')
# Fechar navegador
firefox.quit()
