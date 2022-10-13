from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import time

# Reads input file and prints a list with all the lines in the file
input_file = input('Input file: ')
sentences = []

with open(input_file, 'r') as f:
    current_sentence = ''
    for line in f.readlines():
        if line == '\n': continue
        l = line
        if line[-1] == '\n': l = line[:-1]
        sentences.append(l)

print(f'\033[1;32mFound sentences: {sentences}\033[m')

# Initializes Google Chrome and goes to the following url
url = 'https://freetts.com'
driver = webdriver.Chrome('/home/gabriel/Downloads/chromedriver')
driver.get(url)

print('\033[1;32mConnected to Google Chrome\033[m')

# Ask user for the language and voice of the speech
language_select = Select(driver.find_element(By.ID, 'Language'))
voice_select = Select(driver.find_element(By.ID, 'Voice'))
language_index = -1
voice_index = -1

for i in range(len(language_select.options)):
    print(f"{str(i)} - {language_select.options[i].text}")

while not(0 <= language_index < len(language_select.options)):
    language_index = int(input('Select language: '))
    if not(0 <= language_index < len(language_select.options)):
        print('\033[1;31mUnavailable option\033[m')

language_select.select_by_index(language_index)

print(f'\033[1;32mChose {language_select.options[language_index].text} as language\033[m')

for i in range(len(voice_select.options)):
    print(f"{str(i)} - {voice_select.options[i].text}")

while not(0 <= voice_index < len(voice_select.options)):
    voice_index = int(input('Select voice: '))
    if not(0 <= voice_index < len(voice_select.options)):
        print('\033[1;31mUnavailable option\033[m')

print(f'\033[1;32mChose {voice_select.options[voice_index].text} as voice\033[m')

for i in range(len(sentences)): # Loops through all the sentences in the input file
    driver.refresh() # Refresh page
    
    language_select = Select(driver.find_element(By.ID, 'Language'))
    language_select.select_by_index(language_index) # Select language

    voice_select = Select(driver.find_element(By.ID, 'Voice'))
    voice_select.select_by_index(voice_index) # Select voice

    convert_to_audio_btn = driver.find_element(By.ID, 'btnAudio')
    audio_div = driver.find_element(By.ID, 'AudioPlayer')

    element = driver.find_element(By.ID, 'TextMessage')
    driver.execute_script("arguments[0].value = arguments[1]", element, sentences[i]) # Enters sentence to input
    convert_to_audio_btn.click() # Clickc button to convert text to speech

    audio_div = driver.find_element(By.ID, 'AudioPlayer')

    # Wait until audio is created
    wait = WebDriverWait(driver, 10)
    wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@id='AudioPlayer']/audio")))

    print(f'\033[1;32mCreated audio number {i}\033[m')

    # Find the URL of the created audio
    audio = audio_div.find_elements(By.TAG_NAME, 'audio')[0]
    source = audio.find_elements(By.TAG_NAME, 'source')[0]
    audio_url = source.get_attribute('src')

    # Copy audio to a file in the current directory
    response = requests.get(audio_url)
    open(f'audio{str(i)}.mp3', 'wb').write(response.content)

    print(f'\033[1;32mDownloaded audio number {i}\033[m')


