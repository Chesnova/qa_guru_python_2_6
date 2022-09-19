import os


def test_file_size():
    picture_size = os.path.getsize('./resources/sampleFile.jpeg')
    # print(picture_size)
    assert picture_size == 4096

    print(os.path.abspath('./resources/sampleFile.jpeg'))
    print(os.path.dirname(os.path.abspath('./resources/sampleFile.jpeg')))

    current_dir = os.path.dirname(os.path.abspath(__file__))
    # позволяет склеивать пути для запуска тестов на разных операционных системах
    resource = os.path.join(current_dir, 'resources')
    print(resource)
    resource_tmp = os.path.join(current_dir, 'resources', 'tmp')
    print(resource_tmp)
