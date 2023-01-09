from pytube import YouTube


def download_audio():
    url = input('Введите URL --> ')
    yt = YouTube(url)
    yt.streams.filter(only_audio=True).first().download()
    print('Аудио успешно скачано!')


def download_video():
    url = input('Введите URL --> ')
    yt = YouTube(url)
    yt.streams.filter(only_video=True).first().download()
    print('Видео успешно скачано!')


choice = int(input('\n1 - скачать видео\n2 - скачать аудио\n\nВыберите действие --> '))
while choice != 1 and choice != 2:
    choice = int(input('\nВведите 1 или 2 --> '))

if choice == 1:
    download_video()
if choice == 2:
    download_audio()
