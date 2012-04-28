import pymongo
import gzip

connection = pymongo.Connection('mongodb://admin:4A5buhckPFSw@127.6.89.1:27017/'
db = connection.six

aFile = gzip.open('../data/testactors.list.gz')

startParsing = 0 
actor = ''


def sanitize(movie):
    #movie = movie.split('<')[0].split('[')[0]
    try:
        title = movie.split(' (')[0].strip('"')
        year = movie.split(' (')[1].split(')')[0]    
    except Exception, e:
        print movie;
        raise e;
    finally:
        return { "title" : title, "year" : year};

x = 1;
y = 0;
xend = 12454936
actors = {}
print xend;
for line in aFile:
    y += 1
    if( xend / y == x ):
        print "%s percent done" % x
        x += 1
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

    
    if(words[0] == '----' and words[-1] == '------\n'):
        startParsing =1;
        print


print '%s actors found' % len(actors)
adb = db.actors
print '%s actors inserted' % len(adb.insert(actors.itervalues()))