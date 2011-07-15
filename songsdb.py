#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3
import eyeD3
from eyeD3.tag import genres, TagException
from eyeD3 import InvalidAudioFormatException

import os
import posixpath
import hashlib
import stat
import urllib
import sys

''' Esta funcion recorre recursivamente los directorios que cuelgan del
 directorio top y devuelve una lista de ellos'''
def walktree (top = u"./static/songs", depthfirst = True):
    names = os.listdir(top)
    if not depthfirst:
        yield top, names
    for name in names:
        try:
            st = os.lstat(posixpath.join(top, name))
        except os.error:
            continue
        if stat.S_ISDIR(st.st_mode):
            for (newtop, children) in walktree (posixpath.join(top, name), depthfirst):
                yield newtop, children
    if depthfirst:
        yield top, names


'''Esta fucion devuelve un cursor con la lista de canciones de la base de datos'''
def obtener_tabla_canciones():
	connection = sqlite3.connect("mp3.db")
	cursor = connection.cursor()
	cursor.execute("SELECT artist, album, genre, track, title, path FROM songs ORDER BY artist, album, track")
	return cursor;
	

'''Esta fucion devuelve un cursor con la lista de artistas de la base de datos'''
def obtener_tabla_artistas():
	connection = sqlite3.connect("mp3.db")
	cursor = connection.cursor()
	cursor.execute("SELECT DISTINCT artist FROM songs ORDER BY artist")
	return cursor


'''Esta fucion elimina todos los datos de la base de datos'''
def borrar_db():
	connection = sqlite3.connect("mp3.db")
	cursor = connection.cursor()
	cursor.execute("DELETE FROM songs")
	cursor.execute("VACUUM")
	connection.commit()
	return cursor


'''Esta fucion devuelve un cursor con la lista de albums de la base de datos'''
def obtener_tabla_albumes():
	connection = sqlite3.connect("mp3.db")
	cursor = connection.cursor()
	cursor.execute("SELECT DISTINCT album FROM songs ORDER BY album")
	return cursor
	

'''Esta fucion devuelve un cursor con la lista de generos de la base de datos'''
def obtener_tabla_generos():
	connection = sqlite3.connect("mp3.db")
	cursor = connection.cursor()
	cursor.execute("SELECT DISTINCT genre FROM songs ORDER BY genre")
	return cursor
	
	
'''Esta fucion devuelve un cursor con la lista de canciones de la base de datos'''
def obtener_canciones():
	canciones = list()
	
	# Nos conectamos a la BD
	connection = sqlite3.connect("mp3.db")

	# Creamos un cursor
	cursor = connection.cursor()
	cursor.execute("SELECT title, path FROM songs ORDER BY artist, album, track")

	for tupla in cursor:
		canciones.append([tupla[0],urllib.pathname2url(tupla[1])])

	# Cerramos cursor
	cursor.close()
	# Cerramos conexion a la BD
	connection.close()
	
	return canciones
	
	
'''Esta fucion devuelve un cursor con la lista de canciones de un determinado autor de la base de datos'''
def obtener_canciones_autor(autor):
	canciones = list()
	
	# Nos conectamos a la BD
	connection = sqlite3.connect("mp3.db")

	# Creamos un cursor
	cursor = connection.cursor()
	cursor.execute("SELECT title, path FROM songs WHERE artist = '?' ORDER BY artist, album, track",autor)

	for tupla in cursor:
		canciones.append([tupla[0],urllib.pathname2url(tupla[1])])

	# Cerramos cursor
	cursor.close()
	# Cerramos conexion a la BD
	connection.close()
	
	return canciones
	
	
'''Esta fucion devuelve un cursor con la lista de autores de la base de datos'''
def obtener_autores():
	autores = list()

	# Nos conectamos a la BD
	connection = sqlite3.connect("mp3.db")

	# Creamos un cursor
	cursor = connection.cursor()
	cursor.execute("SELECT DISTINCT artist FROM songs ORDER BY artist;")

	for tupla in cursor:
		autores.append(tupla[0])

	# Cerramos cursor
	cursor.close()
	# Cerramos conexion a la BD
	connection.close()

	return autores


'''Si se ejecuta directamente este fichero, buscará nuevos ficheros mp3
en el directorio "songs" de la carpeta "static" y añadirá las canciones
nuevas y sus etiquetas a la base de datos'''
if __name__== "__main__":
	songs = []

	# Importamos md5
	md5 = hashlib.md5()

	# Comprobamos si hay que reinicializar la tabla
	if len(sys.argv) > 1 and sys.argv[1] == "reset":
		borrar_db()
		print "Base de datos reinicializada"

	# Escaneo de archivos para formar la BD

	# Recorremos todos los directorios de forma recursiva
	for (basepath, children) in walktree(u".",False):
		for child in children:
			# Obtenemos la ruta a cada archivo
			song_path = unicode(posixpath.join(basepath, child))
			try:
				print song_path
			except (UnicodeEncodeError):
				print "Error de Unicode, se salta la cancion"
			else:
				# Si el archivo tiene extension mp3 lo procesamos
				if song_path[-4:] == ".mp3":
					# Obtenemos metadatos
					tag = eyeD3.Tag()
					tag.link(song_path)
					
					# Comprobamos que esten los metadatos esenciales
					try:
						id3_artista = tag.getArtist()
						id3_album = tag.getAlbum()
						id3_titulo = tag.getTitle()
						id3_genero = tag.getGenre().getName()
						id3_track = tag.getTrackNum()
					except (TagException):
						print "Error en el ID3 del archivo, se salta al siguiente"
					except (InvalidAudioFormatException):
						print "El fichero procesado no es un mp3, se salta al siguiente"
					except (eyeD3.GenreException):
						print "Error al leer el genero del archivo, se salta al siguiente"
					except (Exception):
						print "Error desconocido al procesar etiquetas ID3"
					else:
						# Calculamos hash
						f = open(song_path,'rb')
						m = hashlib.md5()
						while True:
							## Don't read the entire file at once...
							data = f.read(10240)
							if len(data) == 0:
								break
							m.update(data)
						song_hash = m.hexdigest()
						f.close()
											
					
						# Construimos la tupla a insertar
						songs.append((unicode(id3_track[0]),unicode(id3_artista),unicode(id3_album),unicode(id3_titulo),unicode(id3_genero),unicode(song_hash),unicode(song_path)))
						print "Procesada cancion:",id3_titulo,"hash",song_hash


	# Nos conectamos a la BD
	connection = sqlite3.connect("mp3.db")

	# Creamos un cursor
	cursor = connection.cursor()
	cursor2 = connection.cursor()

	# Iniciamos el contador de canciones
	songcount = 0

	# Para cada tupla, verificamos que no este ya en la BD a traves del hash
	for tupla in songs:
		newhash = (tupla[5],) 
		cursor.execute("SELECT COUNT(*) FROM songs WHERE hash = ?",newhash)
		cursor2.execute("SELECT title FROM songs WHERE hash = ?",newhash)
		# Si no esta anadida la anadimos
		print "nuevo hash",newhash
		mismohash = cursor.fetchone()[0]
		print mismohash
		
		if mismohash == 0:
			cursor.execute("INSERT INTO songs (track, artist, album, title, genre, hash, path) VALUES (?,?,?,?,?,?,?)", tupla)
			print "Cancion",tupla[3],"añadida"
			songcount += 1
		else:
			print cursor2.fetchone()[0]
			print "La cancion:",tupla[3],"esta repetida, por lo que no se añadira"
		
	# Validamos los cambios
	connection.commit()
	print "Se han añadido",songcount,"canciones a la Base de Datos"

	# Cerramos cursor
	cursor.close()
	# Cerramos conexion a la BD
	connection.close()
