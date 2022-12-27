# 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия
# и восстановления данных.

# wwwwrfffzzllllllllllll --> 4w1r3f2z12l


from pathlib import Path


def rle_encode(data):
    encoding = ''
    prev_char = ''
    count = 1
    if not data:
        return ''
    for char in data:
        if char != prev_char:
            if prev_char:
                encoding += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    else:
        encoding += str(count) + prev_char
        return encoding


def rle_decode(data):
    decode = ''
    count = ''
    for char in data:
        if char.isdigit():
            count += char
        else:
            decode += char * int(count)
            count = ''
    return decode


text = 'wwwwrfffzzllllllllllll'
encode_text = rle_encode(text)


file_path = Path('zip_text.txt')

with open(file_path, 'w') as data:
    data.write(rle_encode(text))

file_path = Path('unzip_text.txt')

with open(file_path, 'w') as data:
    data.write(rle_decode(encode_text))
