"""OpenTrackr Takedown Transparency
https://github.com/Kiwi-Torrent-Research
04/09/2023
"""


import re
import requests
import sqlite3


DATABASE = 'dump_30_08_2023.sqlite'


connection = sqlite3.connect('file:' + DATABASE + '?mode=ro', uri=True)
cursor = connection.cursor()


def main():
    for url in get_takedown_urls():
        hashes_url = url[:-5] + '_hash.html'
        for infohash in get_takedown_infohashes(hashes_url):
            title = get_title_from_database(infohash)
            print(infohash, title)


def opentrackr_get(url):
    return requests.get('https://opentrackr.org/' + url).content.decode()


def get_takedown_urls():
    takedowns_page = opentrackr_get('transparency.html')
    takedown_urls = re.findall('transparency/[A-Z0-9_]+.html', takedowns_page)
    
    print('number of links:', takedowns_page.count('<a href="'))
    print('number of urls: ', len(takedown_urls), '(should be the same)')
    
    return takedown_urls


def get_takedown_infohashes(url):
    page = opentrackr_get(url)
    infohashes = re.findall('[A-F0-9]{40}', page)
    
    print(url)
    print('number of infohashes:', len(infohashes))

    return infohashes


def get_title_from_database(infohash):
    db_result = cursor.execute('SELECT name FROM torrents WHERE infohash = ?', (bytes.fromhex(infohash),)).fetchone()
    if db_result:
        return db_result[0]
    else:
        return 'NOT FOUND IN DATABASE'


main()
