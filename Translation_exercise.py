from translate import Translator

translator = Translator(to_lang = 'ja')

with open('exercise.txt') as myfile:
    text = myfile.read()
    translation = translator.translate(text)
    with open('japanese.txt', mode='w') as japfile:
        japfile.write(translation)
