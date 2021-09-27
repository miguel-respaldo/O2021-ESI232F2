Algoritmo calificaciones
	
	Escribir "Ingresa una calificación"
	Leer calificacion
	
	Si calificacion >= 90 Entonces
		grado <- "A"
	SiNo
		Si calificacion >= 80 Entonces
			grado <- "B"
		SiNo
			Si calificacion >= 70 Entonces
				grado <- "C"
			SiNo
				Si calificacion >= 60 Entonces
					grado <- "D"
				SiNo
					grado <- "R"
				Fin Si
			Fin Si
		Fin Si
	Fin Si
	
	Escribir "El grado es: ", grado
	
FinAlgoritmo
