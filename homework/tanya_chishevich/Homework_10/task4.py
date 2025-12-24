PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''

parts = PRICE_LIST.splitlines()
my_dict = {
    key.strip(): value.strip()
    for line in parts
    for key, value in [line.split(' ', 1)]
}

print(my_dict)
