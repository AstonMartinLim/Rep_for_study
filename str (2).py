# Напишем строку. Причем после обратного слеша, он не будет экранировать
# строку, т.к. после него нет служебного символи
url = 'https:\www.youtube.com'
print (url)
print('\n')

# НО если записать и после com поставить обратный слеш, произойдет экранирование
# на другую строку
url1 = 'https:\www.youtube.com\new'
print (url1)
# для таких случаев нужно писать два слеша, чтобы экранировал только 1-й
print('\n')

# you shold disolay yours code

# Пример:
url2 = 'https:\www.youtube.com\\new'
url3 = 'https://github.com/Alexandr-Romanenko/Rep_for_study/edit/master/str%20(2).py'
print (url2)
# Также мы можем использовать специальный ЛИТЕРАЛ r, который означает
# только для чтения, с ним запись будет работать без 2-х слешэй
url3 = r'https:\www.youtube.com\new'
print (url3)

# Пример 2:
# Нужно написать передать ф-и аргумент
## os.walk('D:\')
# Интерпритатор будет выдавать ошибку т.к. после первого слеша он думает,
# что строка продолжается (экранируетс) поэтому правильная запись:
# через два слеша
##os.walk('D:\\')

print("Hello my friend!")








