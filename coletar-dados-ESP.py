from selenium import webdriver
import pandas as pd
import calendar

# Criar instância do navegador
firefox = webdriver.Firefox(executable_path='/home/matheus/geckodriver-v0.24.0-linux64/geckodriver')


for i in range(2007,2019):
    print('https://www.soccernews.com/soccer-transfers/spanish-la-liga-transfers-{}-{}/'.format(i, i + 1))
    # Abrir a página do Python Club
    firefox.get('https://www.soccernews.com/soccer-transfers/spanish-la-liga-transfers-{}-{}/'.format(i, i+1))

    # Seleciono todos os elementos que possuem a class Table2__tr
    date = firefox.find_elements_by_class_name("date")
    player = firefox.find_elements_by_class_name("player-deals")
    team_to = []
    for j in range(1, date.__len__()-9):
        a = firefox.find_elements_by_xpath('//*[@id="epl"]/table/tbody/tr[{}]/td[6]'.format(j))
        team_to.append(a[0].text)
        j+=1
    team_from = []
    for j in range(1, date.__len__()-9):
        a = firefox.find_elements_by_xpath('//*[@id="epl"]/table/tbody/tr[{}]/td[4]'.format(j))
        team_from.append(a[0].text)
        j+=1
    price = firefox.find_elements_by_class_name("price-status")

    # Criando lista para receber os outputs

    dados = {'Data':[], 'Nome':[],'Saída':[], 'Destino':[], 'Preço':[], 'Mês':[], 'Dia':[], 'Ano':[]}

    for j in range(date.__len__()):
        dados['Data'].append(date[j].text)
        a = player[j].text
        b = a.split("\n")
        dados['Nome'].append(b[0])
        dados['Preço'].append(price[j].text)
    for j in range(team_from.__len__()):
        dados['Saída'].append(team_from[j])
        dados['Destino'].append(team_to[j])
    for j in range(team_from.__len__(), date.__len__()):
        dados['Saída'].append(j)
        dados['Destino'].append(j)
    for j in range(date.__len__()-10):
        dados['Mês'].append(list(calendar.month_abbr).index(dados['Data'][j].split(' ')[0]))
        dados['Dia'].append(int(dados['Data'][j].split(' ')[1]))
        if dados['Mês'][j] in [5,6,7,8,9,10,11,12]:
            dados['Ano'].append(i)
        else:
            dados['Ano'].append(i+1)
    for j in range  (dados['Mês'].__len__(), dados['Mês'].__len__() + 10):
        dados['Mês'].append(0)
        dados['Dia'].append(0)
        dados['Ano'].append(0)


    df = pd.DataFrame(dados)
    df.to_csv(r'/home/matheus/Transferências/transferencias-ESP-{}-{}.csv'.format(i, i+1))
    print(i)
# Fechar navegador
firefox.quit()

