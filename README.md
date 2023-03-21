# PI1FA

primer proyecto individual de Federico acedo para el bootcamp "soy Henry" de la carrera data scientist.

el proyecto consta de dos etapas, una primera dónde tomamos el rol de data engineer. teniendo que realizar un sistema de consulta de las distintas plataformas de stream digitales ( Hulu,netflix,amazon y Disney ) para lograr este objetivo , recibimos distintas bases de datos en formato .csv para así con ellas realizar el proceso de ETL y luego subir una api con su sistema de consulta adecuado.
y una segunda etapa donde nuestro rol es ahora el de un data scientist, aplicando un sistema de recomendación de películas , según el interés de un nuevo consumidor.

proceso de ETL.
las siglas significa ( extraction,transformation anda loading) extracción , transforma y cargado.
por lo que iniciamos cargado las bases de datos entregadas a nuestro editor de texto , en este caso visual studio code.
una vez cargado concatenamos los diferentes datasets quedando así un solo datasets lo que nos permite trabajar de manera más ordenada y poder empezar  la transformación de ese bases de datos. 
está parte del proceso la subdividió en varios pasos a seguís
1er: examinó el datasets para entender en profundidad como está integrado y detectar errores o elementos de poco interés.
2da: una vez examinado el datasets, nos centramos en aplicar las modificiones necesarias y pedidas para la aprobación del proyecto.
ellas son:





3ero: una vez realizada las modificaciones pedidas y necesarias, se procede con la limpieza de datos nulos en caso de ser necesario y reemplazo de valores faltantes.

ahora sí con el data sets ya listos procedemos a levantar la api para hacer el sistema de consulta.

este sistema de consultas lo van a poder realizar desde este link que les comparto aquí: LINK
el mismo contá de 4 consultas diferentes.
1° consulta: devuelve la película de mayor duración de una plataforma seleccionada y de un año específico. ejemplo : 'la película más larga de netflix en el 2019'. 
con solo escribir plataforma = Netflix tipo= pilicula (min ) o serie ( season) y año : 2019 , te va a responder :

2° consulta: devuelve la valoración promedio de una película en tal año.
3er consulta: devuelve la cantidad de películas por año en cada plataforma
4° consulta: 
