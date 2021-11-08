Funcion regresa <- funcion_python(nombre)
	regresa <- 1
	Escribir 'Ejecutando una funcion de python llamada ',nombre
FinFuncion

Funcion archivo <- crear_directorio (nombre_archivo)
	Si funcion_python('os.path.exists') Entonces
		archivo <- funcion_python('open')
	SiNo
		archivo <- funcion_python('open')
		archivo <- funcion_python('archivo.write')
		archivo <- funcion_python('archivo.close')
		archivo <- funcion_python('open')
	FinSi
FinFuncion

Funcion menu()
	Escribir '  ----- Menu Principal ------'
	Escribir '1. Listar todo el directorio.'
	Escribir '2. Agregar al directrio.'
	Escribir '3. Borrar del directrio.'
	Escribir '4. Modificar del directorio.'
	Escribir '5. Salir'
	Escribir ''
FinFuncion

Funcion listar_directorio(archivo)
	archivo <- funcion_python('archivo.seek')
	Para linea<-1 Hasta archivo Hacer
		archivo <- funcion_python('linea.split')
		Escribir 'Nombre, telefono, email'
	FinPara
FinFuncion

Funcion archivo <- borrar_del_directorio(nombre_archivo)
	Escribir '¿Que nombre quieres borrar?'
	Leer nombre
	archivo <- funcion_python('nuevo = open')
	archivo <- funcion_python('archivo = open')
	Para linea<-1 Hasta archivo Hacer
		archivo <- funcion_python('split')
		Si funcion_python('lower')=funcion_python('nombre.lower') Entonces
			Escribir 'Se borro ',nombre
			archivo <- funcion_python('continue')
		FinSi
		archivo <- funcion_python('nuevo.write')
	FinPara
	archivo <- funcion_python('archivo.close')
	archivo <- funcion_python('nuevo.close')
	archivo <- funcion_python('os.remove')
	archivo <- funcion_python('os.rename')
	archivo <- funcion_python('archivo = open')
FinFuncion

Funcion archivo <- modificar_del_directorio(nombre_archivo)
	Escribir '¿Que nombre quieres modificar?'
	Leer nombre
	archivo <- funcion_python('nuevo = open')
	archivo <- funcion_python('archivo = open')
	Para linea<-1 Hasta archivo Hacer
		archivo <- funcion_python('split')
		Si funcion_python('lower')=funcion_python('nombre.lower') Entonces
			Escribir 'Escribe el nombre'
			Leer nombre
			Escribir 'Escribe el telefono'
			Leer telefono
			Escribir 'Escribe el correo electronico'
			Leer correo_e
			archivo <- funcion_python('nuevo.write')
		SiNo
			archivo <- funcion_python('nuevo.write')
		FinSi
	FinPara
	archivo <- funcion_python('archivo.close')
	archivo <- funcion_python('nuevo.close')
	archivo <- funcion_python('os.remove')
	archivo <- funcion_python('os.rename')
	archivo <- funcion_python('archivo = open')
FinFuncion

Funcion regresa <- agregar_al_directorio(nombre_archivo)
	regresa <- 1
	Escribir 'Escribe el nombre'
	Leer nombre
	Escribir 'Escribe el telefono'
	Leer telefono
	Escribir 'Escribe el correo electronico'
	Leer correo_e
	archivo <- funcion_python('open')
	archivo <- funcion_python('archivo.write')
	archivo <- funcion_python('archivo.close')
	archivo <- funcion_python('open')
FinFuncion

Algoritmo directorio_telefonico
	opcion_menu <- 1
	archivo <- crear_directorio('directorio.csv')
	Mientras opcion_menu<>5 Hacer
		menu()
		Escribir 'Opcion: '
		Leer opcion_menu
		Segun opcion_menu  Hacer
			1:
				listar_directorio(archivo)
			2:
				archivo <- funcion_python('archivo.close')
				archivo <- agregar_al_directorio('directorio.csv')
			3:
				archivo <- funcion_python('archivo.close')
				archivo <- borrar_del_directorio('directorio.csv')
			4:
				archivo <- funcion_python('archivo.close')
				archivo <- modificar_del_directorio('directorio.csv')
			5:
				Escribir 'Saliendo de programa...'
			De Otro Modo:
				Escribir 'Opcion Invalida'
		FinSegun
	FinMientras
FinAlgoritmo
