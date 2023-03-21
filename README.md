![HenryLogo](https://d31uz8lwfmyn8g.cloudfront.net/Assets/logo-henry-white-lg.png)

 En este repositorio podran encontrar el primer proyecto individual de Federico acedo para el bootcamp "soy Henry" de la carrera data scientist.

El proyecto consta de dos etapas, una primera dónde tomamos el rol de data engineer. teniendo que realizar un sistema de consulta de las distintas plataformas de stream digitales ( Hulu,netflix,amazon y Disney ) para lograr este objetivo, recibimos distintas bases de datos en formato .csv para realizar el proceso de ETL.
Y una segunda etapa donde nuestro rol es ahora el de un data scientist, aplicando un sistema de recomendación de películas para un cliente.

***proceso de ETL.***
Las siglas significa ( extraction,transformation anda loading) extracción, transformacion y cargado.
por lo que iniciamos ingestando los archivos .csv  a nuestro editor de texto , en este caso visual studio code.
una vez cargado concatenamos los diferentes archivos quedando así un solo dataFrame lo que nos permite trabajar de manera más ordenada y poder empezar  la transformación de ese bases de datos. 
PASOS QUE SE SIGUIERON PARA REALIZAR UN BUEN PROCESO DE TRANSFORMACION:
***1er:***  Se examina el DataFrame para entender en profundidad como está integrado y detectar outliers o elementos de poco interés.
***2da:*** una vez examinado el datasets, nos centramos en aplicar las modificiones necesarias y pedidas para la aprobación del proyecto.
ellas son: 

**'1.Generar campo id: Cada id se compondrá de la primera letra del nombre de la plataforma, seguido del show_id ya presente en los datasets (ejemplo para títulos de Amazon = as123)'**

**'2.Los valores nulos del campo rating deberán reemplazarse por el string “G” (corresponde al maturity rating: “general for all audiences”'**

**'3.De haber fechas, deberán tener el formato AAAA-mm-dd'**

**'4.Los campos de texto deberán estar en minúsculas, sin excepciones'**

**'5.El campo duration debe convertirse en dos campos: duration_int y duration_type. El primero será un integer y el segundo un string indicando la unidad de medición de duración: min (minutos) o season (temporadas)'**

***3ero:*** una vez realizada las modificaciones pedidas y necesarias, se procede con la limpieza de datos nulos en caso de ser necesario y reemplazo de valores faltantes.

ahora sí con el dataFrame ya listos procedemos generar los codigos necesarios y levantar la api para hacer el sistema de consulta.
el mismo contá de 4 puntos diferentes.

**'Película con mayor duración con filtros opcionales de AÑO, PLATAFORMA Y TIPO DE DURACIÓN. (la función debe llamarse get_max_duration(year, platform, duration_type))'**

**'Cantidad de películas por plataforma con un puntaje mayor a XX en determinado año (la función debe llamarse get_score_count(platform, scored, year))'**

**'Cantidad de películas por plataforma con filtro de PLATAFORMA. (La función debe llamarse get_count_platform(platform))'**

**'Actor que más se repite según plataforma y año. (La función debe llamarse get_actor(platform, year))'**

Una vez realizado en codigo las 4 consultas procedemos a levantar la API (Application Programming Interface) que nos permiten mover y brindar acceso simple a los datos que se quieran disponibilizar a través de los diferentes endpoints(consultas), o puntos de salida de la API. para esto se utilizo FASTAPI ,un web framework moderno y de alto rendimiento para construir APIs con Python. a continuacion les dejo un link de render, una plataforma que nos permite ralizar un deployment y asi hacer publica nuestro sistema. [link](https://pi1fa.onrender.com)

Con la api funcionando estamos listos para consumirla y asi pasar al segundo punto del este proyecto.
ahora tomamos el rol de un data science, y desarrollamos un sistema de recomendacion de peliculas.
para esto primero se realiza un EDA (exploratory datos analysis) esto nos guiara hacia el modelo que buscamos entrenar y luego aplicar .


*** MODELO DE RECOMEDACION***
Este modelo busca aprobar o desaprobar la recomendacion de una pelicula a un usuario , en funcion de la valoracion (puntuacion) del mismo hacia otras peliculas. en el video acontinuacion busco desplayar mas esta idea y muestro como funciona el modelo . [link video](https://drive.google.com/file/d/1ffjxeAcBWD9bbA4XnaxdMsEYWAw_C3RV/view?usp=share_link)
