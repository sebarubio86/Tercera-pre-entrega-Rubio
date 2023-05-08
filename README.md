# Tercera-pre-entrega-Rubio


# Pagina de Gestion de Medicos, pacientes y turnos
Hará las siguientes funciones:
* Agregar medicos, pacientes y turnos
* Listar medicos, pacientes y turnos
* Buscar medicos y pacientes


## Pasos
1. Creo los modelos en models.py para la base de datos
2. Hago la migracion de los modelos de tablas de models.py con ```python manage.py makemigrations``` 
3. Generamos el sql correspondiente a las migraciones con ```python manage.py sqlmigrate App1 0001```
4. Migro las tablas a sqlite con ```python manage.py migrate```
5. Creo la aplicacion  con ```python manage.py startapp App1```
6. Añado la aplicacion a la lista de aplicaciones instaladas en settings.py
7. Verifico que se han instalado correctamente con ```python manage.py check App1```
8. Corremos el servidor web con ```python manage.py runserver```


Web disponible tras ejecutar el servidor en http://127.0.0.1:8000/App1/