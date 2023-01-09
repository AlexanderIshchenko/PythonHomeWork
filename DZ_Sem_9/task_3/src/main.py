from pytube import YouTube

print('\n*** Эта программа поможет вам скачать видео или аудио с YOUTUBE ***')
url = input('\nВведите URL --> ')


def download_from_yt(url):
    try:
        v = YouTube(url)
        streams = v.streams
        count = 1

        for stream in streams:
            print(f'\n{count}: {stream}\n')
            count += 1

        choice = int(input('Выберите вариант для скачивания (введите номер) --> '))
        streams[choice-1].download()

        print('\nСкачивание успешно завершено!\n')

    except:
        print('\nОшибка ввода!\n')


download_from_yt(url)

# pip freeze > requirements.txt - создать

# pip install -r requirements.txt - установить

# pip install -U -r requirements.txt - установить и обновить все, что можно

# aiogram - боты телеграмм

# --no-check-certificate

# https://youtu.be/2zXg8CbymYc
