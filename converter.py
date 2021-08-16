import pykakasi

kks = pykakasi.kakasi()
# text = '今日の映画は面白かった'
result = ''

for line in open('./text.txt', 'r', encoding='utf-8').readlines():
    line = line.strip()
    text_trans = kks.convert(line)
    # print(text_trans)
    for item in text_trans:
        if item['orig'] == item['hira']:
            result += item['orig']
        elif item['orig'] == item['kana']:
            result += item['kana']
        else:
            if item['orig'][-1] == item['hira'][-1]:
                result += '{{photrans|' + item['orig'][:-1] + '|' + item['hira'][:-1] + '}}'
                result += item['hira'][-1]
            else:
                result += '{{photrans|' + item['orig'] + '|' + item['hira'] + '}}'
    result += '\n'

# print(result)

with open('./result.txt', 'w', encoding='utf-8') as w:
    w.write(result.strip())
