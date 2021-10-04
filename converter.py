import pykakasi
import os
from pathlib import Path

kks = pykakasi.kakasi()
# text = '今日の映画は面白かった'
result = ''

def file_exist(file_name):
    os.path.exists(file_name)

def file_write(file_name, str0):
    with open(file_name, 'w', encoding='utf-8') as w:
        w.write(str0.strip())

def file_create(file_name):
    Path(file_name).touch()

def photrans(str0, str1):
    return '{{photrans|' + str0 + '|' + str1 + '}}'

def str_add(var0, str0):
    var0 += str0

def str_replace(var0, str0, str1):
    var0 = var0.replace(str0, str1)

if not file_exist('./text.txt'):
    file_create('./text.txt')
else:
    for line in open('./text.txt', 'r', encoding='utf-8').readlines():
        text_trans = kks.convert(line.strip())
        # print(text_trans)
        for item in text_trans:
            if item['orig'] == item['hira']:
                str_add(result, item['orig'])
            elif item['orig'] == item['kana']:
                str_add(result, item['kana'])
            else:
                if item['orig'][-1] == item['hira'][-1]:
                    if item['orig'][-2] == 'っ' or item['orig'][-2] == 'し':
                        str_add(result, photrans(item['orig'][:-2], item['hira'][:-2]) + item['orig'][-2] + item['hira'][-1])
                    else:
                        str_add(result, photrans(item['orig'][:-1], item['hira'][:-1]) + item['hira'][-1])
                else:
                    str_add(result, photrans(item['orig'], item['hira']))
        str_add(result, '\n')
        # print(result)

    str_replace(result, '人|にん', '人|ひと')
    str_replace(result, '君|くん', '君|きみ')

    if not file_exist('./result.txt'):
        file_create('./result.txt')
    file_write('./result.txt', result)
