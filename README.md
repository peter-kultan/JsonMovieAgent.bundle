JSON Metadata Agent for Plex
============================
Plex agent for Plex to load movie metadata from JSON located in folder with your media.

Media Structure
---------------
This agent supports only movies, agent for TV Shows is in development.

Movies Metadata should be presented in `Info.json` file in same directory as your movie(s). For Example:

```
Movies
   |- Movie Subdir
   |   |- Memento.mkv
   |   |- Fight Club.mkv
   |   |- Memento.jpg
   |   |- Fight Club.jpg
   |   \- Info.json
   |- Zombieland.mp4
   |- No Country for Old Men.mkv
   |- Zombieland.jpg
   |- No Country for Old Men.jpg
   \- Info.json
```

Example JSON
------------
The `Info.json` file is structured to follow Plex Movie Metadata Model as much as possible. It should look something like (this example is for `Movie subdir` mentioned above):

```json
{
    "Memento.mkv": {
        "title": "Memento",
        "original_title": "Memento",
        "summary": "Leonard Shelby is tracking down the man who raped and murdered his wife. The difficulty of locating his wife's killer, however, is compounded by the fact that he suffers from a rare, untreatable form of short-term memory loss. Although he can recall details of life before his accident, Leonard cannot remember what happened fifteen minutes ago, where he's going, or why.",
        "year": "2000",
        "originally_available_at": "2000-10-11",
        "rating": "8.2",
        "content_rating": "PG-13",
        "studio": "Summit Entertainment",
        "duration": "113",
        "directors": [
            "Christopher Nolan"
        ],
        "genres": [
            "Mystery",
            "Thriller"
        ],
        "roles": [
                "Guy Pearce",
                "Carrie-Anne Moss"
        ],
        "writers": [
            "Christopher Nolan",
            "Jonathan Nolan"
        ],
        "producers": [
            "Suzanne Todd",
            "Jennifer Todd"
        ],
        "collections": [
            "Movie"
        ],
        "countries": [
            "USA"
        ]
    },
    "Fight Club.mkv": {
        "title": "Fight Club",
        "original_title": "Fight Club",
        "summary": "Leonard Shelby is tracking down the man who raped and murdered his wife. The difficulty of locating his wife's killer, however, is compounded by the fact that he suffers from a rare, untreatable form of short-term memory loss. Although he can recall details of life before his accident, Leonard cannot remember what happened fifteen minutes ago, where he's going, or why.",
        "originally_available_at": "1999-10-15",
        "directors": [
            "David Fincher"
        ],
        "genres": [
            "Drama",
            "Thriller",
            "Comedy"
        ],
        "roles": [
                "Brad Pitt",
                "Edward Norton",
                "Helena Bonham Carter"
        ],
        "producers": [
            "Art Linson",
            "Ceán Chaffin"
        ],
        "countries": [
            "USA"
        ]
    }
}
```

The keys of metadata are movie media file names with suffix. All fields in metadata are optional.

Installation
-----------
1. Download the [zipped bundle](https://github.com/peter-kultan/JsonMovieAgent.bundle/archive/refs/heads/main.zip).
2. Extract it.
3. rename it to JsonMovieAgent.bundle.
4. Find the [Plex Media data directory](https://support.plex.tv/articles/202915258-where-is-the-plex-media-server-data-directory-located/).
5. move the .bundle folder to the Plug-ins directory.
6. Restart plex server.
7. You should be able to see JsonMovieAgent in Agents settings and should be able to pick it in Libraries manager settings as movie library json agent.