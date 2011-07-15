#!/usr/bin/env python
# -*- coding: utf-8 -*-

import web
import songsdb
import webfunctions
import random
from web import form
import urllib
import sqlite3


# Asocia una url (en este caso "/" a una clase)
urls = (
	'/', 'main_player',
	'/ajax/getalbumsfromartist', 'get_albums_from_artist',
	'/ajax/getgenresfromartist', 'get_genres_from_artist',
	'/ajax/getsongsfromartist', 'get_songs_from_artist',
	'/ajax/getartistsfromalbum', 'get_artists_from_album',
	'/ajax/getgenresfromalbum', 'get_genres_from_album',
	'/ajax/getsongsfromalbum', 'get_songs_from_album',
	'/ajax/getartistsfromgenre', 'get_artists_from_genre',
	'/ajax/getalbumsfromgenre', 'get_albums_from_genre',
	'/ajax/getsongsfromgenre', 'get_songs_from_genre',
	'/ajax/getallartists', 'get_all_artists',
	'/ajax/getallalbums', 'get_all_albums',
	'/ajax/getallgenres', 'get_all_genres',
	'/ajax/getallsongs', 'get_all_songs'
	)


# Crea la aplicacion web. La instancia actua de mediador 
# entre python y la web. urls referencia las urls
# definidas arriba, y True hace que no sea necesario
# reiniciar el servidor para ver los cambios en la web
app = web.application(urls, globals(), True)

# Pasa al renderizador el directorio de las plantillas
# para poder usarlas. Ademas le dice que use base como
# plantilla base
render = web.template.render('templates/', base='base')

# Las siguientes clases estan enlazadas con la páginas que hemos definido
# en la variable "urls", se ha sobreescrito su método get para que devuelvan
# los datos apropiados
 
 
'''Clase que construye la aplicacion jukloud'''
class main_player:
	def GET(self):
		canciones = songsdb.obtener_tabla_canciones()
		artistas = songsdb.obtener_tabla_artistas()
		albumes = songsdb.obtener_tabla_albumes()
		generos = songsdb.obtener_tabla_generos()
		
		return render.jukloud("Jukloud", "Manuel Pedrero Luque",canciones,artistas,albumes,generos)		


'''Clase que construye una tabla con todos los albumes de un artista determinado'''
class get_albums_from_artist:
	def GET(self):
		# Extraemos el nombre del artista
		user_data = web.input(_unicode=False)
		artista = user_data.artist
		albums = webfunctions.getAlbumsFromArtistTable(artista)
		return albums
	
		
'''Clase que construye una tabla con todos los generos de un artista determinado'''
class get_genres_from_artist:
	def GET(self):
		# Extraemos el nombre del artista
		user_data = web.input(_unicode=False)
		artista = user_data.artist
		generos = webfunctions.getGenresFromArtistTable(artista)
		return generos


'''Clase que construye una tabla con todos las canciones de un artista determinado'''
class get_songs_from_artist:
	def GET(self):
		# Extraemos el nombre del artista
		user_data = web.input(_unicode=False)
		artista = user_data.artist
		
		canciones = webfunctions.getSongsFromArtistTable(artista)
		return canciones


'''Clase que construye una tabla con todos los artistas de un album determinado'''
class get_artists_from_album:
	def GET(self):
		# Extraemos el nombre del album
		user_data = web.input()
		album = user_data.album
		
		artistas = webfunctions.getArtistsFromAlbumTable(album)
		return artistas
		
		
'''Clase que construye una tabla con todos los generos de un album determinado'''
class get_genres_from_album:
	def GET(self):
		# Extraemos el nombre del album
		user_data = web.input()
		album = user_data.album
		
		generos = webfunctions.getGenresFromAlbumTable(album)
		return generos
		
		
'''Clase que construye una tabla con todos las canciones de un album determinado'''
class get_songs_from_album:
	def GET(self):
		# Extraemos el nombre del album
		user_data = web.input()
		album = user_data.album
		
		canciones = webfunctions.getSongsFromAlbumTable(album)
		return canciones
		
	
'''Clase que construye una tabla con todos los artistas de un genero determinado'''
class get_artists_from_genre:
	def GET(self):
		# Extraemos el nombre del genero
		user_data = web.input()
		genero = user_data.genre
		
		artistas = webfunctions.getArtistsFromGenreTable(genero)
		return artistas
		

'''Clase que construye una tabla con todos los albumes de un artista determinado'''
class get_albums_from_genre:
	def GET(self):
		# Extraemos el nombre del genero
		user_data = web.input()
		genero = user_data.genre
		
		albums = webfunctions.getAlbumsFromGenreTable(genero)
		return albums
		

'''Clase que construye una tabla con todos las cancinoes de un genero determinado'''	
class get_songs_from_genre:
	def GET(self):
		# Extraemos el nombre del album
		user_data = web.input()
		genero = user_data.genre
		
		canciones = webfunctions.getSongsFromGenreTable(genero)
		return canciones	
		

'''Clase que construye una tabla con todos los artistas de la base de datos'''
class get_all_artists:
	def GET(self):	
		artistas = webfunctions.getAllArtistsTable()
		return artistas
		

'''Clase que construye una tabla con todos los albumes de la base de datos'''
class get_all_albums:
	def GET(self):	
		albums = webfunctions.getAllAlbumsTable()
		return albums
		
		
'''Clase que construye una tabla con todos los artistas de la base de datos'''
class get_all_genres:
	def GET(self):	
		generos = webfunctions.getAllGenresTable()
		return generos
		

'''Clase que construye una tabla con todos los canciones de la base de datos'''	
class get_all_songs:
	def GET(self):	
		canciones = webfunctions.getAllSongsTable()
		return canciones	
		
		
'''Si se ejecuta este archivo directamente, arranca la aplicacion y el servidor web'''
if __name__ == "__main__":
	app.run()
