#!/usr/bin/python3

import http.client

def translate_text(source_text, source_lang, target_lang):
    conn = http.client.HTTPSConnection("google-translate105.p.rapidapi.com")

    payload = f"text={source_text}&to_lang={target_lang}&from_lang={source_lang}"

    headers = {
        'content-type': "application/x-www-form-urlencoded",
        'X-RapidAPI-Key': "e3535b60a0msha8c2f34a6673a0ep17349ajsn3641377a2b5e",
        'X-RapidAPI-Host': "google-translate105.p.rapidapi.com"
    }

    conn.request("POST", "/v1/rapid/translate", payload, headers)

    res = conn.getresponse()
    data = res.read().decode("utf-8")

    translated_text = None
    if "translated_text" in data:
        translated_text = data.split('"translated_text":"')[1].split('"}')[0]

    return translated_text if translated_text else "Translation error occurred."

def main():
    print("Welcome to the Language Translation Tool!")
    source_lang = input("Enter the source language code (e.g., 'en' for English): ")
    source_text = input("Enter the text to translate: ")
    target_lang = input("Enter the target language code (e.g., 'es' for Spanish): ")

    translated_text = translate_text(source_text, source_lang, target_lang)

    print("\nTranslation Result:")
    print("-------------------")
    print(f"Source Text: {source_text}")
    print(f"Translated Text: {translated_text.encode('utf-8').decode('unicode-escape')}")

if __name__ == "__main__":
    main()


