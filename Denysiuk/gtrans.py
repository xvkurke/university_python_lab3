from package.module1 import TransLate, LangDetect, CodeLang, LanguageList

text = "Добрий день. Як справи?"
source_lang = "auto"  
target_lang = "en"    

print("Original text:", text)

detected = LangDetect(text, set="all")
print(f"Detected language and confidence: {detected}")

translated_text = TransLate(text, scr=source_lang, dest=target_lang)
print(f"Translated text: {translated_text}")

lang_code = CodeLang("English")
print(f"Language code for 'English': {lang_code}")

print("\nSupported Languages and Translations:")
LanguageList(out="screen", text=text)
