from os import listdir
from os.path import isfile, join
from mutagen.mp3 import MP3
music_path = 'D:\\Music\\lofi\\lofi\\' # Music file path
music_names = [f for f in listdir(music_path) if isfile(join(music_path, f))]
for music in music_names:
    k = music.split('.')
    if k[1] == 'jpg' or k[1] == 'py' or k[1] == 'm3u':
        music_names.remove(music)
ur_playlist = 'lofi-music'
f = open(ur_playlist+'.m3u','w+')
f.writelines('#EXTM3U\n')
for music in music_names:
    audio = MP3('D:\\Music\\lofi\\lofi\\'+music)
    audio_time = int(audio.info.length)
    f.writelines('#EXTINF:'+str(audio_time)+",Lofi music - "+music.strip('.mp3')+"\n")
    f.writelines(music+'\n')
