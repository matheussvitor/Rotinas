from selenium import webdriver
import time

# Criar instância do navegador
firefox = webdriver.Firefox(executable_path='/home/matheus/geckodriver-v0.24.0-linux64/geckodriver')

# Abrir a página do Python Club
firefox.get('https://www.espn.com/soccer/transfers')

# Para descer até o bottom da página
SCROLL_PAUSE_TIME = 1

# Get scroll height
last_height = firefox.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    firefox.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = firefox.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

# Seleciono todos os elementos que possuem a class Table2__tr
posts = firefox.find_elements_by_class_name("Table2__tr")
print(posts.__len__())

'''for i in range(posts.__len__()):
    print(posts[i].text)
    i+=1
'''
# Criando lista para receber os outputs




# Fechar navegador
firefox.quit()

