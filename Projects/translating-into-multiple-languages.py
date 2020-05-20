from translate import Translator

with open('test.txt',mode='r') as my_file:
  file=my_file.read()
  
  translator=Translator(to_lang="en")
  translate=translator.translate(file)
  print(translate)
  translator=Translator(to_lang="es")
  translate=translator.translate(file)
  print(translate)
  translator=Translator(to_lang="zh")
  translate=translator.translate(file)
  print(translate)
  translator=Translator(to_lang="pt")
  translate=translator.translate(file)
  print(translate)