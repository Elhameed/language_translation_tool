#!/usr/bin/python3

import requests

def translate_text(source_text, target_lang):
    url = "https://google-translate105.p.rapidapi.com/v1/rapid/translate"

    payload = {
        "text": source_text,
        "to_lang": target_lang,
        "from_lang": "en"
    }

    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "X-RapidAPI-Key": "e3535b60a0msha8c2f34a6673a0ep17349ajsn3641377a2b5e",
        "X-RapidAPI-Host": "google-translate105.p.rapidapi.com"
    }

    try:
        response = requests.post(url, data=payload, headers=headers)
        response_data = response.json()

        if "data" in response_data:
            translated_text = response_data["data"]["translations"][0]["translatedText"]
            return translated_text
        else:
            return "Translation error occurred."

    except Exception as e:
        return f"An error occurred: {str(e)}"

def main():
    print("Welcome to the Language Translation Tool!")
    source_text = input("Enter the text to translate: ")
    target_lang = input("Enter the target language code (e.g., 'es' for Spanish): ")

    translated_text = translate_text(source_text, target_lang)
    print(f"Translated Text: {translated_text}")

if __name__ == "__main__":
    main()


