import os
import re


def file_splitter():
    file_list = os.listdir('mid_rus_conll')
    for filename in file_list:
        filepath = os.path.join('mid_rus_conll', filename)
        with open(filepath, encoding='utf-8') as f:
            text = f.readlines()

        for line in text:
            if 'newdoc id' in line:
                filepath = re.search(r'texts/.+', line)
                if filepath:
                    filepath = filepath.group()
                    filepath = filepath.split('/')
                    if len(filepath) == 2:
                        dirpath = filepath[0]
                        filename = filepath[1] + '.txt'
                    else:
                        dirpath = os.path.join(filepath[0], filepath[1])
                        filename = filepath[2] + '.txt'
                    os.makedirs(dirpath, exist_ok=True)
                    f = open(os.path.join(dirpath, filename), 'w', encoding='utf-8')
                    continue
            f.write(line + '\n')
    f.close()


if __name__ == '__main__':
    file_splitter()
