import json
import requests
from bs4 import BeautifulSoup

url = 'https://portal.ifba.edu.br/conquista/noticias-2/noticias-campus-vitoria-da-conquista'
api_url = 'http://ff-web:5000'

def get_dat_publish(article):
    data_modification = article.header.find(class_='documentByLine').getText().replace("  ", "").replace('\n', "")
    date = data_modification[data_modification.find('modificação') + 11:]
    return date

def crawler(page_url: str, verify: bool):
    page = requests.get(page_url, verify=verify)
    soup = BeautifulSoup(page.text, 'html.parser').find_all('article', class_='entry')
    posts = []
    for article in soup:
        summary = article.header.find(class_='summary')
        article = {
            'title': summary.a.getText(),
            'link': summary.a['href'],
            'date': get_dat_publish(article)
        }
        posts.append(article)
        # print(article)
    return posts


def get_posts(start=1) -> list:
    b_start = 0 if start == 1 else 30 * (start - 1)
    page_url = '{}?b_start:int={}'.format(url, b_start)
    posts = crawler(page_url, verify=True)
    return posts

def send_to_api(posts):
    headers = {
    'Content-Type':'application/json'
    }
    
    r = requests.post(api_url, data=json.dumps(posts), headers=headers)
    # r = requests.get('http://localhost:5000')
    print(r.content)
    
if __name__ == "__main__":
    posts = get_posts()
    send_to_api(posts)
    