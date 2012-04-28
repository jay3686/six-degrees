import pymongo
import gzip

connection = pymongo.Connection('mongodb://admin:4A5buhckPFSw@127.6.89.1:27017/')
db = connection.six

aFile = gzip.open('../data/factors_1.list.gz')

actor = ''


def sanitize(movie):
    try:
        title = movie.split(' (')[0].strip('"')
        year = movie.split(' (')[1].split(')')[0]    
    except Exception, e:
        print movie;
        raise e;
    finally:
        return { "title" : title, "year" : year};

actors = {}

for line in aFile:
    words = line.split('\t')
    firstWord = words[0]
    wurds = line.strip(firstWord).strip('\t').strip('\n')
    if(startParsing):
        if(words[0] != ''):
            actor = words[0]
        if(len(words) > 1):
            #print '%s was in %s.' % (actor, words[-1])
            try:
                movie = sanitize(wurds)
            except Exception, e:
                print words
                raise e
            if (actors.has_key(actor)):
                    actors[actor]["movies"] += [movie,]
                    actors[actor]["mkey"] += [movie["title"] + movie["year"],]
            else:
                actors[actor] = {"name" : actor, "movies" : [movie,], "mkey" : [movie["title"] + movie["year"],]}


print '%s actors found' % len(actors)
adb = db.actors
print '%s actors inserted' % len(adb.insert(actors.itervalues()))