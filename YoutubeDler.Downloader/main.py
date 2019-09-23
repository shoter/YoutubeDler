from __future__ import unicode_literals
from urllib.parse import urlparse, parse_qs
import sys, getopt
import youtube_dl

url = ''
output = ''

try:
    opts, args = getopt.getopt(sys.argv[1:],"u:o:")
    if not opts:
        print("main.py -u <inputfile> -o <outputfile>")
        exit(3)
except getopt.GetoptError as err:
    print('main.py -u <inputfile> -o <outputfile>')
    print(err)
    sys.exit(2)
for opt, arg in opts:
    if opt in ("-u"):
        url = arg
    elif opt in ("-o"):
        output = arg


parsed = urlparse(url)
qs = parse_qs(parsed.query)

url = "https://youtube.com/watch?v=" + qs['v'][0]


ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '640',
    }],
}
if output:
    ydl_opts["outtmpl"] = output

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])