import pykakasi
import os
from pathlib import Path

kks = pykakasi.kakasi()
# text = '今日の映画は面白かった'
result = ''

if not os.path.exists('./text.txt'):
    Path('./text.txt').touch()
else:
    for line in open('./text.txt', 'r', encoding='utf-8').readlines():
        text_trans = kks.convert(line.strip())
        # print(text_trans)
        for item in text_trans:
            if item['orig'] == item['hira']:
                result += item['orig']
            elif item['orig'] == item['kana']:
                result += item['kana']
            else:
                if item['orig'][-1] == item['hira'][-1]:
                    if item['orig'][-2] == 'っ' or item['orig'][-2] == 'し':
                        result += '{{photrans|' + item['orig'][:-2] + '|' + item['hira'][:-2] + '}}'
                        result += item['orig'][-2] + item['hira'][-1]
                    else:
                        result += '{{photrans|' + item['orig'][:-1] + '|' + item['hira'][:-1] + '}}'
                        result += item['hira'][-1]
                else:
                    result += '{{photrans|' + item['orig'] + '|' + item['hira'] + '}}'
        result += '\n'
        # print(result)

result = result.replace('|人|にん', '|人|ひと')
result = result.replace('|君|くん', '|君|きみ')

if not os.path.exists('./result.txt'):
    Path('./result.txt').touch()
else:
    with open('./result.txt', 'w', encoding='utf-8') as w:
        w.write(result.strip())
        