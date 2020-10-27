def add_to_archive(name, lastname):
    c = open('fullname.txt', 'a')
    c.write(name + ' ' + lastname + '\n')
    c.close()

add_to_archive('Lolo', 'Cejas')