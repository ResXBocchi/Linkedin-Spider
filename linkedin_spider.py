from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
import parameters
from parsel import Selector

driver = webdriver.Chrome(executable_path=parameters.driver_path)
driver.maximize_window()
sleep(0.5)

driver.get('https://linkedin.com/')
sleep(3)

driver.find_element_by_xpath('//a[text()="Sign in"]').click()
sleep(3)

user_field = driver.find_element_by_xpath('//input[@name="session_key"]')
user_field.send_keys(parameters.username)

password_field = driver.find_element_by_xpath('//input[@name="session_password"]')
password_field.send_keys(parameters.password)

driver.find_element_by_xpath("//button[text()='Sign in']").click()
sleep(3)

driver.get('https://www.google.com/')

search_input = driver.find_element_by_name('q')
search_input.send_keys(parameters.search_query)
sleep(1)
search_input.send_keys(Keys.RETURN)
sleep(3)

profiles = driver.find_elements_by_xpath("//div[@class='yuRUbf']/a[1]") 
profiles = [profile.get_attribute('href') for profile in profiles]

for profile in profiles:
    driver.get(profile)
    sleep(2)
    try:
        if driver.find_element_by_xpath('//button[@class="pv-s-profile-actions pv-s-profile-actions--connect ml2 artdeco-button artdeco-button--2 artdeco-button--primary ember-view"]'):
            driver.find_element_by_xpath('//button[@class="pv-s-profile-actions pv-s-profile-actions--connect ml2 artdeco-button artdeco-button--2 artdeco-button--primary ember-view"]').click()
            sleep(1)
            driver.find_element_by_xpath('//button[@class="mr1 artdeco-button artdeco-button--muted artdeco-button--3 artdeco-button--secondary ember-view"]').click()
            sleep(1)
            driver.find_element_by_xpath('//div[@class="relative"]/textarea').send_keys('Olá, {}! Seu perfil foi localizado automáticamente pelos parâmetros que passei para o robo que desenvolvi com Python e Selenium! Se quiser saber mais como ele funciona, ou até mesmo usá-lo, posso te explicar! Apesar de ainda não te conhecer, espero que possamos construir um ótimo relacionamento! Abraço!'.format(driver.find_element_by_xpath('//li[@class="inline t-24 t-black t-normal break-words"]').text))
            driver.find_element_by_xpath('//button[@class="ml1 artdeco-button artdeco-button--3 artdeco-button--primary ember-view"]').click()
       

    except:
        pass

    sleep(1)

driver.quit()