from mutagen.easyid3 import EasyID3
import os
from os import listdir
from os.path import isfile,join

#import json
#import urllib,urllib2

import lyricwikia
import requests
import config

cwd = os.getcwd()
result_file = open('lyrics.txt','w')
extension = False
noFetch = False

for f in listdir(cwd):
    ext = f[f.rfind('.'):]
    try:
        if(not (ext == '.mp3' or ext == '.MP3')):
            extension = True
            raise Exception()
        audio = EasyID3(f)
        if(audio == {}):
            noFetch = True
            raise Exception()
        else:
            title = audio['title'][0]
            flag = title.find('-')
            if(flag>title.find('(') and not title.find('(') == -1 or flag == -1):
                flag = title.find('(')
            title = title[:flag if(flag>-1) else len(title)]
            artist = audio['artist'][0]
            flag = artist.find('(')
            if(flag>artist.find('-') and not artist.find('-') == -1 or flag == -1):
                flag = artist.find('-')
            artist = artist[:flag if(flag>-1) else len(artist)]
            artist = artist.split('&')[0]
            artist = artist.split(',')[0]
            print(artist)
            print(title)
            lyrics = lyricwikia.get_lyrics(artist,title)
            result_file.write('Artist:'+artist+' '+'Title: '+title+'\n\n'+'Lyrics:\r\n'+lyrics+'\n\n-------\n\n\n')

        #query = {'q_track':title,'apikey':config.apikey}
        #query = urllib.urlencode(query)
        #url = "http://api.musixmatch.com/ws/1.1/track.search?"+query
        #request = urllib2.Request(url)
        #response = urllib2.urlopen(request)
        #response = json.loads(response.read())
        #track_id = response["message"]["body"]["track_list"][0]["track"]["track_id"]
        #query = {'track_id':track_id,'apikey':config.apikey}
        #query = urllib.urlencode(query)
        #url = "http://api.musixmatch.com/ws/1.1/track.lyrics.get?"+query
        #request = urllib2.Request(url)
        #response = urllib2.urlopen(request)
        #response = json.loads(response.read())
        #url = response["message"]["body"]["lyrics"]["backlink_url"]
        #url =str(url)
        #request = requests.get(url)
        #print(request)
    #except urllib2.HTTPError as err:
        #print err
        
    except:
        if(extension):
            extension = False
            print "Please provide .mp3 extension"
        elif(noFetch):
            noFetch = False
            print "Not fetching.."
        else:
            print "Error"
        pass
result_file.close()

