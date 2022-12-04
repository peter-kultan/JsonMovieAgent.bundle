import os, json
from dateutil.parser import parse

load_file = Core.storage.load

class JsonAgent(Agent.Movies):

    name = 'JsonMovieAgent'
    primary_provider = True
    languages = [Locale.Language.NoLanguage]
    accepts_from = [
        'com.plexapp.agents.localmedia',
        'com.plexapp.agents.opensubtitles',
        'com.plexapp.agents.podnapisi',
        'com.plexapp.agents.subzero'
    ]

    contributes_to = [
        'com.plexapp.agents.themoviedb',
        'com.plexapp.agents.imdb',
        'com.plexapp.agents.none'
    ]

    def search(self, results, media, lang):
        part = media.items[0].parts[0]
        path = os.path.join(os.path.dirname(part.file), 'Info.json')

        if not os.path.exists(path):
            return

        info = json.loads(load_file(path))

        info = info[os.path.basename(part.file)]

        try: title = info['title']
        except: pass

        if os.path.exists(path):
            results.Append(MetadataSearchResult(id=media.id, name=title, lang=lang, score=100))

    def update(self, metadata, media, lang):
        part = media.items[0].parts[0]
        path = os.path.join(os.path.dirname(part.file), 'Info.json')

        info = json.loads(load_file(path))

        info = info[os.path.basename(part.file)]

        try: metadata.title = info['title']
        except: pass

        try: metadata.original_title = info['original_title']
        except: pass

        try: metadata.summary = info['summary']
        except: pass

        try: metadata.year = info['year']
        except: pass

        try: metadata.originally_available_at = parse(info['originally_available_at'])
        except: pass

        try: metadata.rating = info['rating']
        except: pass

        try: metadata.content_rating = info['content_rating']
        except: pass

        try: metadata.studio = info['studio']
        except: pass

        try: metadata.duration = info['duration']
        except: pass

        metadata.directors.clear()
        
        try:
            for r in info['directors']:
                try: metadata.directors.new().name = r
                except: pass
                
        except:
            pass

        metadata.genres.clear()

        try:
            for g in info['genres']:
                metadata.genres.add(g)
        except:
            pass

        metadata.roles.clear()

        try:
            for r in info['roles']:
                role = metadata.roles.new()

                try: role.name = r
                except: pass
        except:
            pass

        metadata.writers.clear()

        try:
            for w in info['writers']:
                try: metadata.writers.new().name = w
                except: pass
        except: 
            pass

        metadata.producers.clear()

        try:
            for p in info['producers']:
                try: metadata.producers.new().name = p
                except: pass
        except:
            pass


        metadata.collections.clear()

        try:
            for c in info['collections']:
                metadata.collections.add(c)
        except:
            pass
        
        
        metadata.countries.clear()

        try:
            for d in info['countries']:
                metadata.countries.add(d)
        except:
            pass

movieAgent = JsonAgent