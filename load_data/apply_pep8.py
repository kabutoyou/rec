import os

user_path = os.path.expanduser('~')


def apply_pep8_to_file(filename, pip_path=user_path +
                       '/Library/Python/2.7/lib/python/site-packages/'):
    '''
    1.  before you use this module, please install autopep8
        pip install --upgrade autopep8
    2.  apply this function to the file in this project
        apply_pep8_to_file('load_data.py')
    '''

    search_space = r'../'
    absolute_path = ''
    for root, dirs, files in os.walk(search_space):
        for name in files:
            if name == filename:
                absolute_path = os.path.abspath(os.path.join(root, name))
                break

    if absolute_path == '':
        raise NameError('No such file ' + filename)

    system_call = 'python ' + pip_path + 'autopep8.py ' + \
                  '--in-place --aggressive --aggressive ' + absolute_path
    os.system(system_call)


def apply_pep8_to_dir(path, pip_path=user_path +
                      '/Library/Python/2.7/lib/python/site-packages/'):

    search_space = r'../'
    for root, dirs, files in os.walk(search_space):
        for dir in dirs:
            if dir == path:
                absolute_path = os.path.abspath(os.path.join(root, dir))
                file_list = os.listdir(absolute_path)
                for f in file_list:
                    apply_pep8_to_file(f, pip_path)
            else:
                raise NameError('No such directory ' + path)
