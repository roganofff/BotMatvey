import requests
import bs4

def search_word_definition(word, numberOfLetters) -> str:
    response = requests.get('https://inflectonline.ru/' + word)
    page = bs4.BeautifulSoup(response.content,"html.parser")
    PageItem = page.find('p')
    return PageItem.text[:numberOfLetters]
