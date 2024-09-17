from googletrans import Translator

translator = Translator()

def TransLate(text: str, scr: str, dest: str) -> str:
    """Translate text from scr language to dest language."""
    try:
        translation = translator.translate(text, src=scr, dest=dest)
        return translation.text
    except Exception as e:
        return f"Error: {str(e)}"

def LangDetect(text: str, set: str = "all") -> str:
    """Detect the language of a text and return the language or confidence."""
    try:
        detection = translator.detect(text)
        if set == "lang":
            return detection.lang
        elif set == "confidence":
            return detection.confidence
        else:
            return f"lang={detection.lang}, confidence={detection.confidence}"
    except Exception as e:
        return f"Error: {str(e)}"

def CodeLang(lang: str) -> str:
    """Return the code or name of a language."""
    try:
        if len(lang) == 2:
            return translator.LANGUAGES.get(lang, "Unknown code")
        else:
            for code, name in translator.LANGUAGES.items():
                if name.lower() == lang.lower():
                    return code
            return "Unknown language"
    except Exception as e:
        return f"Error: {str(e)}"

def LanguageList(out: str = "screen", text: str = None) -> str:
    """Print or save a table of all supported languages and translations."""
    try:
        supported_languages = translator.LANGUAGES
        header = f"{'N':<5} {'Language':<20} {'ISO-639 code':<10} {'Text':<20}"
        lines = [header, "-" * len(header)]

        for idx, (code, language) in enumerate(supported_languages.items(), start=1):
            translation = translator.translate(text, dest=code).text if text else ''
            lines.append(f"{idx:<5} {language:<20} {code:<10} {translation:<20}")

        if out == "screen":
            print("\n".join(lines))
        elif out == "file":
            with open("languages.txt", "w") as f:
                f.write("\n".join(lines))
        return "Ok"
    except Exception as e:
        return f"Error: {str(e)}"
