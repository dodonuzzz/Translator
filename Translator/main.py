from translate import Translator

translator = Translator(to_lang="tr")

sentence = "I think ordinary people may also be extraordinary."
translation = translator.translate(sentence)

print(translation)
