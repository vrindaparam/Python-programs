from gensim.summarization import summarize
import requests
import re
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Automatic_summarization"

def get_page(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    return soup

def collect_text(soup):
    text = f'url: {url}\n\n'
    para_text = soup.find_all('p')
    # print(f"paragraphs text = \n {para_text}")
    for para in para_text:
        text += f"{para.text}\n\n"
    return text

def get_summary(text):
    gensim_summary_text = summarize(text, word_count=200, ratio = 0.1)
    return {
        'code': 200,
        'message': 'Summarized text',
        'summary': gensim_summary_text
    }

def main():
    text = collect_text(get_page(url))
    summary = get_summary(text)
    print(summary)

if __name__ == "__main__":
    main()

"""
Front-end 
I/p: Piece of Text inside a Textfield (Text) / Url
O/P: Summary of text (JSON)

Back-end
def get_summary(text):
    return {
        'code': 200,
        'message': Summarized text
        'summary': summary
    }
"""