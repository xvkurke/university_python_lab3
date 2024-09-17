import os
from package.module1 import TransLate, LangDetect

def load_config(config_file):
    try:
        with open(config_file, "r") as f:
            config = {}
            for line in f:
                key, value = line.strip().split("=")
                config[key.strip()] = value.strip()
        return config
    except FileNotFoundError:
        print(f"Configuration file {config_file} not found.")
        return None

def read_text_file(file_name, char_limit=None, word_limit=None, sentence_limit=None):
    try:
        with open(file_name, "r") as f:
            text = f.read()

            if char_limit and len(text) > int(char_limit):
                text = text[:int(char_limit)]
            if word_limit:
                words = text.split()
                if len(words) > int(word_limit):
                    text = " ".join(words[:int(word_limit)])
            if sentence_limit:
                sentences = text.split(".")
                if len(sentences) > int(sentence_limit):
                    text = ". ".join(sentences[:int(sentence_limit)])

            return text
    except FileNotFoundError:
        print(f"Text file {file_name} not found.")
        return None

def translate_file():
    config_file = "config.txt"
    config = load_config(config_file)

    if not config:
        return

    text_file = config.get("text_file")
    target_lang = config.get("target_language", "en")
    output_type = config.get("output", "screen")
    char_limit = config.get("char_limit")
    word_limit = config.get("word_limit")
    sentence_limit = config.get("sentence_limit")

    text = read_text_file(text_file, char_limit, word_limit, sentence_limit)

    if not text:
        return

    detected_lang = LangDetect(text, set="lang")
    print(f"Detected language: {detected_lang}")

    translated_text = TransLate(text, scr="auto", dest=target_lang)

    if output_type == "screen":
        print(f"Translated text to {target_lang}:")
        print(translated_text)
    elif output_type == "file":
        output_file = f"{os.path.splitext(text_file)[0]}_{target_lang}.txt"
        with open(output_file, "w") as f:
            f.write(translated_text)
        print(f"Translation saved to {output_file}")

translate_file()
