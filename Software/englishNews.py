from audioplayer import AudioPlayer
import os
from gtts import gTTS
from bs4 import BeautifulSoup
import requests
import requests
def enews():
    res = requests.get('https://www.60secondsnow.com/')
    soup = BeautifulSoup(res.text, 'lxml')
    data = soup.find('div', {"class": "listingpage"})
    article = data.find('article')
    adds = article.find('div', {'class': 'photos-add'})
    postcontainer = article.find('div', {"class": "post-container"})
    article_content = postcontainer.find('div', {'class': 'post-header clearfix'})

    article_content = article_content.find('div', {'class': 'article-content'})
    header = article_content.find('h2')

    updated_time = article_content.find('div', {'class': 'article-datetime'})

    categories = updated_time.find('a')

    article_desc = article_content.find('div', {'class': 'article-desc'})
    article_desc = article_desc.find('p')
    updated_time = updated_time.text
    if '-' in updated_time:
        updated_time = updated_time.replace('-', '')
    article_desc = article_desc.text
    categories = categories.text
    print(
        f"\n\n\nHeadlines: {header.text}\n\nCategory: {categories[23:]}\n\nNews updated time: {updated_time[40:]}\n")
    print("*************************************************************************Article*************************************************************************************************************************")
    print(f"\n{article_desc}\n")
    print("*********************************************************************************************************************************************************************************************************\n\n\n")

    updates_readerInEnglish = f"""Category {categories[23:]}, the news was uploaded {updated_time[40:]}, The article says {article_desc}"""

    language = 'en'
    myobj = gTTS(text=updates_readerInEnglish,
                lang=language, slow=False)
    file = "english reader.mp3"
    myobj.save(file)
    AudioPlayer(file).play(loop=False, block=True)
    os.remove(file)

