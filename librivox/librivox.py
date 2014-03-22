import urllib2
import simplejson

librivox_audiobook_url = "https://librivox.org/api/feed/audiobooks/?%s&format=json"
librivox_author_url = "https://librivox.org/api/feed/authors/?%s&format=json"

class Librivox(dict):
    pass

class Author(dict):
    pass

def retrieve_all_audiobooks():
    url = librivox_audiobook_url % "extended=1"
    json = urllib2.urlopen(url).read()
    json = simplejson.loads(json)
    return [Librivox(x) for x in json['books']]

def retrieve_audiobook(book_id):
    url = librivox_audiobook_url % ("id=" + str(book_id),)
    json = urllib2.urlopen(url).read()
    json = simplejson.loads(json)
    return [Librivox(x) for x in json['books']]

def retrieve_author(author_id):
    url = librivox_author_url % ("id=" + str(author_id),)
    json = urllib2.urlopen(url).read()
    json = simplejson.loads(json)
    return [Author(x) for x in json['authors']]

def search_audiobooks(since = None, author = None, title = None, genre = None):
    searchterm = []
    if since:
        searchterm.append("since=" + since)
    if author:
        searchterm.append("author=" + author)
    if title:
        searchterm.append("title=" + title)
    if genre:
        searchterm.append("genre=" + genre)
    if not searchterm:
        raise TypeError
    searchterm = "&".join(searchterm)
    url = librivox_audiobook_url % (searchterm,)
    print(url)
    json = urllib2.urlopen(url).read()
    json = simplejson.loads(json)
    return [Librivox(x) for x in json['books']]
