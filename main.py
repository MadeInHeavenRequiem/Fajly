#1 Открываю и закрываю файл
text_file = open("/Users/admin/Documents/Misha's Folder/PytonProject.txt", "r", encoding='utf-8')
text_file.read()
text_file.close()
#2 Читаю файл полностью
text_file = open("/Users/admin/Documents/Misha's Folder/PytonProject.txt", "r", encoding='utf-8')
whole = text_file.read()
print(whole)
text_file.close()
#3 Меняю все символы на новые
text_file = open("/Users/admin/Documents/Misha's Folder/PytonProject.txt", "w", encoding='utf-8')
new = text_file.write('''Я изменил текст
вот так вот''')
text_file.close()
#4 Читаю определённое количество символов
text_file = open("/Users/admin/Documents/Misha's Folder/PytonProject.txt", "r", encoding='utf-8')
print(text_file.readline(5))
text_file.close()
#5 Читаю все строки
text_file = open("/Users/admin/Documents/Misha's Folder/PytonProject.txt", "r", encoding='utf-8')
print(text_file.readlines())
text_file.close()
print('ok')
