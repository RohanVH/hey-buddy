from audioplayer import AudioPlayer
import os
from gtts import gTTS
from bs4 import BeautifulSoup
import requests
import requests
def knews():
    res = requests.get('https://www.60secondsnow.com/kn/')
    soup = BeautifulSoup(res.text, 'lxml')
    data = soup.find('div', {"class": "listingpage"})
    articles = data.find('article')
    article = data.find('article')
    adds = article.find('div', {'class': 'photos-add'})
    postcontainer = article.find('div', {"class": "post-container"})
    article_content = postcontainer.find(
        'div', {'class': 'post-header clearfix'})

    article_content = article_content.find('div', {'class': 'article-content'})
    header = article_content.find('h2')

    updated_time = article_content.find('div', {'class': 'article-datetime'})

    categories = updated_time.find('a')

    article_desc = article_content.find('div', {'class': 'article-desc'})
    article_desc = article_desc.find('p')
    updated_time = updated_time.text
    if '-' in updated_time:
        updated_time = updated_time.replace('-', '')
    if 'min ago' in updated_time:
        updated_time = updated_time.replace(
            'min ago', 'ನಿಮಿಷದ ಹಿಂದೆ')
    article_desc = article_desc.text
    categories = categories.text
    print(f"\n\n\nHeadlines: {header.text}\n\nCategory: {categories[23:]}\n\nNews updated time: {updated_time[40:]}\n")
    print("*************************************************************************Article*************************************************************************************************************************")
    print(f"\n{article_desc}\n")
    print("*********************************************************************************************************************************************************************************************************\n\n\n")

    updates_readerInkannada = f"""ವರ್ಗ, {categories[23:]}. ಅಪ್‌ಲೋಡ್ ಅಧಾ ಸಮಯ, {updated_time[38:]}. {article_desc}. ಈ ರೀತಿ ಬರಹಗಾರ ಹೇಳುತ್ತಾರೆ"""
    language = 'kn'
    myobj = gTTS(text=updates_readerInkannada,
                    lang=language, slow=False)
    file = "kannada reader.mp3"
    myobj.save(file)
    AudioPlayer(file).play(loop=False, block=True)
    os.remove(file)


