from ChatGPT import Chat
from WebScrapping import Scrapping

import eel

if __name__ == '__main__':
    chat = Chat()
    scrapping = Scrapping()

    @eel.expose
    def scrape_word(word: str):
        chatGPTReply = chat.prompt(word)
        scrapping.getPronunciation(word)
        categories = scrapping.getWordCategories(word)

        return {
            "chat_reply": chatGPTReply,
            "categories": categories
        }

    eel.init('web')
    eel.start('index.html', size=(1280, 720), port=3000, mode='chrome')
