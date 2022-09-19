# конструкция контекстный менеджер
# запись в файл
with open('example.txt', 'w') as f:
    # 'w' - открыть файл на запись
    f.write('Hello world\nnew text')

# f.write('Try')

# Закрывать файл вручную = антипаттерн
# f = open('example2.txt', 'w')
# f.write('Hello2')
# f.close()
# f.write('Try')

# чтение из файла
with open('example.txt', 'r') as f:
    file = f.read()
    print(file)
    assert file == 'Hello world\nnew text'
    assert 'new' in file

# чтение построчно из файла
# def test_rows():
#     with open('example2.txt') as file:
#         for i in file:
#             assert i == 'Hello1'
#             print(i)

# создание/дописывание в файл
with open('example3.txt', 'a') as file:
    file.write('\nHello')