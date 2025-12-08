my_dict = {
    'tuple': (1000, 'tuple', False, 1, 'one'),
    'list': [2000, 'list', True, 2, 'two'],
    'dict': {'a': 3000, 'b': 'dict', 'c': False, 'd': 3, 'i': 'three'},
    'set': {4000, 'set', True, 4, 'four'}
}

# действия с tuple
last_element_dict = my_dict['tuple'][-1]
print(f"Последний элемент из tuple: {last_element_dict}")

# действия с list
my_dict['list'].append('newElement')
print("Добавлен новый элемент в list:", my_dict['list'])
my_dict['list'].pop(1)
print("Удалён второй элемент из list:", my_dict['list'])

# действия с dict
my_dict['dict']['i am a tuple'] = 'hi'
print("Добавлен новый элемент с новым ключом в dict", my_dict['dict'])
my_dict['dict'].pop('a')
print("Удалён элемент с ключом 'a' из dict", my_dict['dict'])

# действия с set
my_dict['set'].add('newElement')
print("Добавлен новый элемент в set", my_dict['set'])
my_dict['set'].remove(True)
print("Удалён элемент из set", my_dict['set'])
