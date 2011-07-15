#!/usr/bin/env python
# -*- coding: utf-8 -*-

# En este fichero se implementan las funciones que construyen las
# respuestas AJAX en html para que el proceso principal pueda acceder
# a ellas. Utiliza las funciones definidas en mp3functions.py para 
# obtener los datos en bruto

import mp3functions

#Devuelve una tabla html con los albumes de un artista
def getAlbumsFromArtistTable(artista):
	albums = mp3functions.getAlbumsFromArtist(artista)

	tabla = ""
	tabla +=(
u'''<table class="display" id="album_table">	
<thead>
	<tr>
		<th id="album_table_header">Álbum</th>
	</tr>
	</thead>
	
	<tbody>
	<tr>
		<td id="all_albums">*** Todos los álbumes ***</td>
	</tr>
''')
	
	for album in albums:
		tabla += ('<tr><td class="album_row">' + album + "</td></tr>")
	
	tabla += ("</tbody></table>")
	
	return tabla


#Devuelve una tabla html con los generos de un artista
def getGenresFromArtistTable(artista):
	genres = mp3functions.getGenresFromArtist(artista)

	tabla = ""
	tabla +=(
u'''<table class="display" id="genre_table">	
<thead>
	<tr>
		<th id="genre_table_header">Género</th>
	</tr>
	</thead>
	
	<tbody>
	<tr>
		<td id="all_genres">*** Todos los géneros ***</td>
	</tr>
''')
	
	for genre in genres:
		tabla += ('<tr><td class="genre_row">' + genre + "</td></tr>")
	
	tabla += ("</tbody></table>")
	
	return tabla
	

#Devuelve una tabla html con las canciones de un artista
def getSongsFromArtistTable(artista):
	songs = mp3functions.getSongsFromArtist(artista)

	tabla = ""
	tabla +=(
u'''<table class="display" id="song_table">	
<thead>
	<tr>
		<th class="track_column_header">#</th>
		<th class="name_column_header">Canción</th>
		<th class="artist_column_header">Artista</th>
		<th class="album_column_header">Álbum</th>
		<th class="genre_column_header">Género</th>
		<th class="path_column_header" style="display:none">Path</th>
	</tr>
	</thead>
	
	<tbody>
''')
	
	for song in songs:
		tabla += (u'<tr class="song_row"><td class="track_column">')
		tabla += (unicode(song[3]))
		tabla += (u'</td><td class="name_column">')
		tabla += (unicode(song[4]))
		tabla += (u'</td><td class="artist_column">')
		tabla += (unicode(song[0]))
		tabla += (u'</td><td class="album_column">')
		tabla += (unicode(song[1]))
		tabla += (u'</td><td class="genre_column">')
		tabla += (unicode(song[2]))
		tabla += (u'</td><td class="res_url" style="display:none">')
		tabla += (unicode(song[5]))
		tabla += (u'</td></tr>')
	
	tabla += (u"</tbody></table>")
	
	return unicode(tabla)


#Devuelve una tabla html con los artistas de un album
def getArtistsFromAlbumTable(album):
	artists = mp3functions.getArtistsFromAlbum(album)

	tabla = ""
	tabla +=(
u'''<table class="display" id="artist_table">	
<thead>
	<tr>
		<th id="artist_table_header">Artista</th>
	</tr>
	</thead>
	
	<tbody>
	<tr>
		<td id="all_artists">*** Todos los artistas ***</td>
	</tr>
''')
	
	for artist in artists:
		tabla += ('<tr><td class="artist_row">' + artist + "</td></tr>")
	
	tabla += ("</tbody></table>")
	
	return tabla


#Devuelve una tabla html con los generos de un album
def getGenresFromAlbumTable(album):
	genres = mp3functions.getGenresFromAlbum(album)

	tabla = ""
	tabla +=(
u'''<table class="display" id="genre_table">	
<thead>
	<tr>
		<th id="genre_table_header">Género</th>
	</tr>
	</thead>
	
	<tbody>
	<tr>
		<td id="all_genres">*** Todos los géneros ***</td>
	</tr>
''')
	
	for genre in genres:
		tabla += ('<tr><td class="genre_row">' + genre + "</td></tr>")
	
	tabla += ("</tbody></table>")
	
	return tabla
	

#Devuelve una tabla html con las canciones de un album
def getSongsFromAlbumTable(album):
	songs = mp3functions.getSongsFromAlbum(album)

	tabla = ""
	tabla +=(
u'''<table class="display" id="song_table">	
<thead>
	<tr>
		<th class="track_column_header">#</th>
		<th class="name_column_header">Canción</th>
		<th class="artist_column_header">Artista</th>
		<th class="album_column_header">Álbum</th>
		<th class="genre_column_header">Género</th>
		<th class="path_column_header" style="display:none">Path</th>
	</tr>
	</thead>
	
	<tbody>
''')
	
	for song in songs:
		tabla += (u'<tr class="song_row"><td class="track_column">')
		tabla += (unicode(song[3]))
		tabla += (u'</td><td class="name_column">')
		tabla += (unicode(song[4]))
		tabla += (u'</td><td class="artist_column">')
		tabla += (unicode(song[0]))
		tabla += (u'</td><td class="album_column">')
		tabla += (unicode(song[1]))
		tabla += (u'</td><td class="genre_column">')
		tabla += (unicode(song[2]))
		tabla += (u'</td><td class="res_url" style="display:none">')
		tabla += (unicode(song[5]))
		tabla += (u'</td></tr>')
	
	tabla += (u"</tbody></table>")
	
	return unicode(tabla)


#Devuelve una tabla html con los artistas de un genero
def getArtistsFromGenreTable(genre):
	artists = mp3functions.getArtistsFromGenre(genre)

	tabla = ""
	tabla +=(
u'''<table class="display" id="artist_table">	
<thead>
	<tr>
		<th id="artist_table_header">Artista</th>
	</tr>
	</thead>
	
	<tbody>
	<tr>
		<td id="all_artists">*** Todos los artistas ***</td>
	</tr>
''')
	
	for artist in artists:
		tabla += ('<tr><td class="artist_row">' + artist + "</td></tr>")
	
	tabla += ("</tbody></table>")
	
	return tabla


#Devuelve una tabla html con los albumes de un genero
def getAlbumsFromGenreTable(genre):
	albums = mp3functions.getAlbumsFromGenre(genre)

	tabla = ""
	tabla +=(
u'''<table class="display" id="album_table">	
<thead>
	<tr>
		<th id="album_table_header">Álbum</th>
	</tr>
	</thead>
	
	<tbody>
	<tr>
		<td id="all_albums">*** Todos los álbumes ***</td>
	</tr>
''')
	
	for album in albums:
		tabla += ('<tr><td class="album_row">' + album + "</td></tr>")
	
	tabla += ("</tbody></table>")
	
	return tabla


#Devuelve una tabla html con las canciones de un genero
def getSongsFromGenreTable(genre):
	songs = mp3functions.getSongsFromGenre(genre)

	tabla = ""
	tabla +=(
u'''<table class="display" id="song_table">	
<thead>
	<tr>
		<th class="track_column_header">#</th>
		<th class="name_column_header">Canción</th>
		<th class="artist_column_header">Artista</th>
		<th class="album_column_header">Álbum</th>
		<th class="genre_column_header">Género</th>
		<th class="path_column_header" style="display:none">Path</th>
	</tr>
	</thead>
	
	<tbody>
''')
	
	for song in songs:
		tabla += (u'<tr class="song_row"><td class="track_column">')
		tabla += (unicode(song[3]))
		tabla += (u'</td><td class="name_column">')
		tabla += (unicode(song[4]))
		tabla += (u'</td><td class="artist_column">')
		tabla += (unicode(song[0]))
		tabla += (u'</td><td class="album_column">')
		tabla += (unicode(song[1]))
		tabla += (u'</td><td class="genre_column">')
		tabla += (unicode(song[2]))
		tabla += (u'</td><td class="res_url" style="display:none">')
		tabla += (unicode(song[5]))
		tabla += (u'</td></tr>')
	
	tabla += (u"</tbody></table>")
	
	return unicode(tabla)


#Devuelve una tabla html con todos los artistas
def getAllArtistsTable():
	artists = mp3functions.getAllArtists()

	tabla = ""
	tabla +=(
u'''<table class="display" id="artist_table">	
<thead>
	<tr>
		<th id="artist_table_header">Artista</th>
	</tr>
	</thead>
	
	<tbody>
	<tr>
		<td id="all_artists">*** Todos los artistas ***</td>
	</tr>
''')
	
	for artist in artists:
		tabla += ('<tr><td class="artist_row">' + artist + "</td></tr>")
	
	tabla += ("</tbody></table>")
	
	return tabla



#Devuelve una tabla html con todos los albumes 
def getAllAlbumsTable():
	albums = mp3functions.getAllAlbums()

	tabla = ""
	tabla +=(
u'''<table class="display" id="album_table">	
<thead>
	<tr>
		<th id="album_table_header">Álbum</th>
	</tr>
	</thead>
	
	<tbody>
	<tr>
		<td id="all_albums">*** Todos los álbumes ***</td>
	</tr>
''')
	
	for album in albums:
		tabla += ('<tr><td class="album_row">' + album + "</td></tr>")
	
	tabla += ("</tbody></table>")
	
	return tabla


#Devuelve una tabla html con todos los generos
def getAllGenresTable():
	genres = mp3functions.getAllGenres()

	tabla = ""
	tabla +=(
u'''<table class="display" id="genre_table">	
<thead>
	<tr>
		<th id="genre_table_header">Género</th>
	</tr>
	</thead>
	
	<tbody>
	<tr>
		<td id="all_genres">*** Todos los géneros ***</td>
	</tr>
''')
	
	for genre in genres:
		tabla += ('<tr><td class="genre_row">' + genre + "</td></tr>")
	
	tabla += ("</tbody></table>")
	
	return tabla
	

#Devuelve una tabla html con todas las canciones
def getAllSongsTable():
	songs = mp3functions.getAllSongs()

	tabla = ""
	tabla +=(
u'''<table class="display" id="song_table">	
<thead>
	<tr>
		<th class="track_column_header">#</th>
		<th class="name_column_header">Canción</th>
		<th class="artist_column_header">Artista</th>
		<th class="album_column_header">Álbum</th>
		<th class="genre_column_header">Género</th>
		<th class="path_column_header" style="display:none">Path</th>
	</tr>
	</thead>
	<tbody class="scrollable">
''')
	
	for song in songs:
		tabla += (u'<tr class="song_row"><td class="track_column">')
		tabla += (unicode(song[3]))
		tabla += (u'</td><td class="name_column">')
		tabla += (unicode(song[4]))
		tabla += (u'</td><td class="artist_column">')
		tabla += (unicode(song[0]))
		tabla += (u'</td><td class="album_column">')
		tabla += (unicode(song[1]))
		tabla += (u'</td><td class="genre_column">')
		tabla += (unicode(song[2]))
		tabla += (u'</td><td class="res_url" style="display:none">')
		tabla += (unicode(song[5]))
		tabla += (u'</td></tr>')
	
	tabla += (u"</tbody></table>")
	
	return unicode(tabla)

