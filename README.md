![HenryLogo](https://d31uz8lwfmyn8g.cloudfront.net/Assets/logo-henry-white-lg.png)

 En este repositorio podran encontrar el primer proyecto individual de Federico acedo para el bootcamp "soy Henry" de la carrera data scientist.

El proyecto consta de dos etapas, una primera dónde tomamos el rol de data engineer. teniendo que realizar un sistema de consulta de las distintas plataformas de stream digitales ( Hulu,netflix,amazon y Disney ) para lograr este objetivo , recibimos distintas bases de datos en formato .csv para así con ellas realizar el proceso de ETL y luego subir una api con su sistema de consulta adecuado.
y una segunda etapa donde nuestro rol es ahora el de un data scientist, aplicando un sistema de recomendación de películas , según el interés de un nuevo consumidor.

proceso de ETL.
las siglas significa ( extraction,transformation anda loading) extracción , transforma y cargado.
por lo que iniciamos cargado las bases de datos entregadas a nuestro editor de texto , en este caso visual studio code.
una vez cargado concatenamos los diferentes datasets quedando así un solo datasets lo que nos permite trabajar de manera más ordenada y poder empezar  la transformación de ese bases de datos. 
está parte del proceso la subdividió en varios pasos a seguís
1er: examinó el datasets para entender en profundidad como está integrado y detectar errores o elementos de poco interés.
2da: una vez examinado el datasets, nos centramos en aplicar las modificiones necesarias y pedidas para la aprobación del proyecto.
ellas son: 
1.Generar campo id: Cada id se compondrá de la primera letra del nombre de la plataforma, seguido del show_id ya presente en los datasets (ejemplo para títulos de Amazon = as123)
2.Los valores nulos del campo rating deberán reemplazarse por el string “G” (corresponde al maturity rating: “general for all audiences”
3.De haber fechas, deberán tener el formato AAAA-mm-dd
4.Los campos de texto deberán estar en minúsculas, sin excepciones
5.El campo duration debe convertirse en dos campos: duration_int y duration_type. El primero será un integer y el segundo un string indicando la unidad de medición de duración: min (minutos) o season (temporadas)
3ero: una vez realizada las modificaciones pedidas y necesarias, se procede con la limpieza de datos nulos en caso de ser necesario y reemplazo de valores faltantes.
ahora sí con el data sets ya listos procedemos a levantar la api para hacer el sistema de consulta.
este sistema de consultas lo van a poder realizar desde este link que les comparto aquí: 
el mismo contá de 4 consultas diferentes.

**Película con mayor duración con filtros opcionales de AÑO, PLATAFORMA Y TIPO DE DURACIÓN. (la función debe llamarse get_max_duration(year, platform, duration_type))
**Cantidad de películas por plataforma con un puntaje mayor a XX en determinado año (la función debe llamarse get_score_count(platform, scored, year))
**Cantidad de películas por plataforma con filtro de PLATAFORMA. (La función debe llamarse get_count_platform(platform))
**Actor que más se repite según plataforma y año. (La función debe llamarse get_actor(platform, year))


https://pi1fa.onrender.com
