#!/usr/bin/env python
# -*- coding: utf-8 -*-

# En este fichero se implementan todas las funciones necesarias para
# tratar los mp3 que se reproduciran en jukloud

import sqlite3

'''Devuelve una lista de albumes de un determinado artista'''
def getAlbumsFromArtist(artist):
	albums = list()
	
	# Nos conectamos a la BD
	connection = sqlite3.connect("mp3.db")

	# Creamos un cursor
	cursor = connection.cursor()
	artist = artist.replace("'", "''");
	cursor.execute("SELECT DISTINCT album FROM songs WHERE artist = '" + artist + "' ORDER BY album, track")

	for tupla in cursor:
		albums.append(tupla[0])

	# Cerramos cursor
	cursor.close()
	# Cerramos conexion a la BD
	connection.close()
	
	return albums

	
'''Devuelve una lista de generos de un determinado artista'''
def getGenresFromArtist(artist):
	genres = list()
	
	# Nos conectamos a la BD
	connection = sqlite3.connect("mp3.db")

	# Creamos un cursor
	cursor = connection.cursor()
	artist = artist.replace("'", "''");
	cursor.execute("SELECT DISTINCT genre FROM songs WHERE artist = '" + artist + "' ORDER BY album, track")

	for tupla in cursor:
		genres.append(tupla[0])

	# Cerramos cursor
	cursor.close()
	# Cerramos conexion a la BD
	connection.close()
	
	return genres

	
'''Devuelve una lista de canciones de un determinado artista'''
def getSongsFromArtist(artist):
	songs = list()
	
	# Nos conectamos a la BD
	connection = sqlite3.connect("mp3.db")

	# Creamos un cursor
	cursor = connection.cursor()
	artist = artist.replace("'", "''");
	cursor.execute("SELECT artist, album, genre, track, title, path FROM songs WHERE artist = '" + artist + "'ORDER BY artist, album, track")

	# Construimos la lista
	for tupla in cursor:
		songs.append([tupla[0],tupla[1],tupla[2],tupla[3],tupla[4],tupla[5]])

	# Cerramos cursor
	cursor.close()
	# Cerramos conexion a la BD
	connection.close()
	
	return songs
	
'''Devuelve una lista de artistas de un determinado album'''
def getArtistsFromAlbum(album):
	artists = list()
	
	# Nos conectamos a la BD
	connection = sqlite3.connect("mp3.db")

	# Creamos un cursor
	cursor = connection.cursor()
	album = album.replace("'", "''");
	cursor.execute("SELECT DISTINCT artist FROM songs WHERE album = '" + album + "' ORDER BY artist")

	for tupla in cursor:
		artists.append(tupla[0])

	# Cerramos cursor
	cursor.close()
	# Cerramos conexion a la BD
	connection.close()
	
	return artists

'''Devuelve una lista de generos de un determinado album'''
def getGenresFromAlbum(album):
	genres = list()
	
	# Nos conectamos a la BD
	connection = sqlite3.connect("mp3.db")

	# Creamos un cursor
	cursor = connection.cursor()
	album = album.replace("'", "''");
	cursor.execute("SELECT DISTINCT genre FROM songs WHERE album = '" + album + "' ORDER BY artist")

	for tupla in cursor:
		genres.append(tupla[0])

	# Cerramos cursor
	cursor.close()
	# Cerramos conexion a la BD
	connection.close()
	
	return genres


'''Devuelve una lista de canciones de un determinado album'''
def getSongsFromAlbum(album):
	songs = list()
	
	# Nos conectamos a la BD
	connection = sqlite3.connect("mp3.db")

	# Creamos un cursor
	cursor = connection.cursor()
	album = album.replace("'", "''");
	cursor.execute("SELECT artist, album, genre, track, title, path FROM songs WHERE album = '" + album + "'ORDER BY album, track")

	# Construimos la lista
	for tupla in cursor:
		songs.append([tupla[0],tupla[1],tupla[2],tupla[3],tupla[4],tupla[5]])

	# Cerramos cursor
	cursor.close()
	# Cerramos conexion a la BD
	connection.close()
	
	return songs


'''Devuelve una lista de artistas de un determinado genero'''
def getArtistsFromGenre(genre):
	artists = list()
	
	# Nos conectamos a la BD
	connection = sqlite3.connect("mp3.db")

	# Creamos un cursor
	cursor = connection.cursor()
	genre = genre.replace("'", "''");
	cursor.execute("SELECT DISTINCT artist FROM songs WHERE genre = '" + genre + "' ORDER BY artist")

	for tupla in cursor:
		artists.append(tupla[0])

	# Cerramos cursor
	cursor.close()
	# Cerramos conexion a la BD
	connection.close()
	
	return artists


'''evuelve una lista de albumes de un determinado genero'''
def getAlbumsFromGenre(genre):
	albums = list()
	
	# Nos conectamos a la BD
	connection = sqlite3.connect("mp3.db")

	# Creamos un cursor
	cursor = connection.cursor()
	genre = genre.replace("'", "''");
	cursor.execute("SELECT DISTINCT album FROM songs WHERE genre = '" + genre + "' ORDER BY album")

	for tupla in cursor:
		albums.append(tupla[0])

	# Cerramos cursor
	cursor.close()
	# Cerramos conexion a la BD
	connection.close()
	
	return albums


'''Devuelve una lista de canciones de un determinado genero'''
def getSongsFromGenre(genre):
	songs = list()
	
	# Nos conectamos a la BD
	connection = sqlite3.connect("mp3.db")

	# Creamos un cursor
	cursor = connection.cursor()
	genre = genre.replace("'", "''");
	cursor.execute("SELECT artist, album, genre, track, title, path FROM songs WHERE genre = '" + genre + "'ORDER BY album, track")

	# Construimos la lista
	for tupla in cursor:
		songs.append([tupla[0],tupla[1],tupla[2],tupla[3],tupla[4],tupla[5]])

	# Cerramos cursor
	cursor.close()
	# Cerramos conexion a la BD
	connection.close()
	
	return songs


'''Devuelve una lista de todos los artistas'''
def getAllArtists():
	artists = list()
	
	# Nos conectamos a la BD
	connection = sqlite3.connect("mp3.db")

	# Creamos un cursor
	cursor = connection.cursor()
	cursor.execute("SELECT DISTINCT artist FROM songs ORDER BY artist")

	for tupla in cursor:
		artists.append(tupla[0])

	# Cerramos cursor
	cursor.close()
	# Cerramos conexion a la BD
	connection.close()
	
	return artists


'''Devuelve una lista de todos los albumes'''
def getAllAlbums():
	albums = list()
	
	# Nos conectamos a la BD
	connection = sqlite3.connect("mp3.db")

	# Creamos un cursor
	cursor = connection.cursor()
	cursor.execute("SELECT DISTINCT album FROM songs ORDER BY album")

	for tupla in cursor:
		albums.append(tupla[0])

	# Cerramos cursor
	cursor.close()
	# Cerramos conexion a la BD
	connection.close()
	
	return albums

	
'''Devuelve una lista de todos los generos'''
def getAllGenres():
	genres = list()
	
	# Nos conectamos a la BD
	connection = sqlite3.connect("mp3.db")

	# Creamos un cursor
	cursor = connection.cursor()
	cursor.execute("SELECT DISTINCT genre FROM songs ORDER BY genre")

	for tupla in cursor:
		genres.append(tupla[0])
		#~ print genres[0]

	# Cerramos cursor
	cursor.close()
	# Cerramos conexion a la BD
	connection.close()
	
	return genres

	
'''Devuelve una lista de todas las canciones'''
def getAllSongs():
	songs = list()
	
	# Nos conectamos a la BD
	connection = sqlite3.connect("mp3.db")

	# Creamos un cursor
	cursor = connection.cursor()
	cursor.execute("SELECT artist, album, genre, track, title, path FROM songs ORDER BY album, track")

	# Construimos la lista
	for tupla in cursor:
		songs.append([tupla[0],tupla[1],tupla[2],tupla[3],tupla[4],tupla[5]])

	# Cerramos cursor
	cursor.close()
	# Cerramos conexion a la BD
	connection.close()
	
	return songs



if __name__== "__main__":
	pass
