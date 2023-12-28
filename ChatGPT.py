import json
import openai
import os
openai.api_key = "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"


class Chat:
    __messages = [{"role": "system", "content":
                   """Since now your are my English assistant, I will give you words in English. Your job is to:
- show the word itself (In English).
- show the different meanings of that word in Spanish (ordered by most used). Without the parenthesis.
- show the IPA pronunciation of that word (American Accent). Without the parenthesis.
- show a common sentence using the word.
- show the translation in spanish of the sentence.
- show a list of the main synonyms of the word in English (do not exceed 3).
- show a url of the search "{{word}} images" ONLY on Google Images, not in normal search
Note that {{word}} refers to the word in english"""},
                  {
        "role": "user",
        "content": "dawn"
    }, {
        "role": "assistant",
        "content": """Word: dawn

Meanings: amanecer - inicio - comienzo

IPA Pronunciation: /dɔn/

Example sentence: I woke up at dawn to watch the sunrise.

Traducción: Me desperté al amanecer para ver el amanecer.

Synonyms: daybreak - sunrise - morning twilight

Google Images search: https://www.google.com/search?q=dawn+images&tbm=isch"""
    }
    ]

    def prompt(self, word: str) -> str:
        self.__messages.append({"role": "user", "content": word})
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=self.__messages)
        reply = chat.choices[0].message.content
        self.__messages.append({"role": "assistant", "content": reply})
        return reply


"""
    def __read_json_file(self):
        with open(self.__json_path, 'r') as file:
            data = json.load(file)
        return data["data"]

    # Write JSON data to a file
    def __write_json_file(self, data):
        with open(self.__json_path, 'w') as file:
            json.dump({"data": data}, file, indent=4)
"""
