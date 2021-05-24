import pytube
import os
import time

choice = input('Single (1) or Queue (2) Mode\n : ')


if choice == "1":
    url = input("Video Link (Url) \n : ")
    youtube = pytube.YouTube(url)
    video = youtube.streams.get_highest_resolution()
    location = video.download()
    os.rename(location, "downloaded.mp3")
else:
    if choice == "2":

        my_file = open("sample.txt", "r")
        content_list = my_file. readlines()

        list_good = [x.replace('\n', '') for x in content_list]

        i=0
        while i<len(list_good):
            print(f"Getting URL {list_good[0]}")
            youtube = pytube.YouTube(list_good[0])
            video = youtube.streams.get_highest_resolution()
            location = video.download()            
            os.rename(location, location.replace('.mp4', '.mp3'))
            list_good.pop(0)
            time.sleep(5)



