from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

user = 'username'
pw = 'password'

firefox = webdriver.Firefox()
firefox.get('https://www.athena.biblioteca.unesp.br/F')
wait = WebDriverWait(firefox, 5)

firefox.find_element_by_xpath('//*[@title="Mostra situação do usuário na biblioteca"]').click()

login = firefox.find_element_by_name('bor_id')
login.send_keys(user)

password = firefox.find_element_by_name('bor_verification')
password.send_keys(pw)
password.send_keys(Keys.ENTER)

baseUrl = firefox.current_url.strip('BOR-INFO')

loan = 'bor-loan&adm_library=UEP50'
wait.until(EC.title_is("Informações do Usuário - Resumo"))
firefox.get(baseUrl + loan)

wait.until(EC.title_is("UEP50 - Itens em Empréstimo"))
firefox.find_element_by_xpath('//*[@title="Renova todos empréstimos do usuário"]').click()


firefox.find_element_by_xpath('//*[@title="Inicia uma nova sessão"]').click()
wait.until(EC.title_is("Catálogo Athena - Encerrar sessão"))
firefox.find_element_by_xpath('//img[@alt="Confirma"]').click()