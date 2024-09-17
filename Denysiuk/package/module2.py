from deep_translator import GoogleTranslator
from langdetect import detect, detect_langs

def TransLate(text: str, scr: str, dest: str) -> str:
    """Translate text using Deep Translator."""
    try:
        translator = GoogleTranslator(source=scr, target=dest)
        return translator.translate(text)
    except Exception as e:
        return f"Error: {str(e)}"

def LangDetect(text: str, set: str = "all") -> str:
    """Detect the language using langdetect."""
    try:
        detection = detect_langs(text)
        if set == "lang":
            return detection[0].lang
        elif set == "confidence":
            return detection[0].prob
        else:
            return f"lang={detection[0].lang}, confidence={detection[0].prob}"
    except Exception as e:
        return f"Error: {str(e)}"

def CodeLang(lang: str) -> str:
    """Map language code to name and vice versa."""
    try:
        # Implement the logic here for code-name mapping
        return "Function implementation needed"
    except Exception as e:
        return f"Error: {str(e)}"

def LanguageList(out: str = "screen", text: str = None) -> str:
    """List supported languages in Deep Translator."""
    try:
        supported_languages = GoogleTranslator.get_supported_languages(as_dict=True)
        header = f"{'N':<5} {'Language':<20} {'ISO-639 code':<10} {'Text':<20}"
        lines = [header, "-" * len(header)]

        for idx, (code, language) in enumerate(supported_languages.items(), start=1):
            translation = GoogleTranslator(source='auto', target=code).translate(text) if text else ''
            lines.append(f"{idx:<5} {language:<20} {code:<10} {translation:<20}")

        if out == "screen":
            print("\n".join(lines))
        elif out == "file":
            with open("deep_languages.txt", "w") as f:
                f.write("\n".join(lines))
        return "Ok"
    except Exception as e:
        return f"Error: {str(e)}"
