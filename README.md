{{project_name}}
===============


Valiendonos de la prestación de django 1.4 para tomar un molde de proyecto, 
y con la intención de formalizar algunas prácticas que a esta altura son
rutinarias preparamos este molde.

Algunas prestaciones de este molde son:

- Incluye templates y estilos genericos.
- Incluye django debug toolbar, pagination.
- Configuraciones genericas para statics y media.
- Algunos chiches más.

Uso
---------------

Clone el paquete en algun lugar accesible:

    $ git clone git://github.com/Inventta/django-project-template.git

Cree y active un [entorno virtual](http://pypi.python.org/pypi/virtualenv) para el 
proyecto:

    $ cd ~/venvs/ # adapte este path a su preferencia
    $ virtualenv {{project_name}}
    $ source {{project_name}}/bin/activate

Instale las dependencias necesarias:

    $ cd ~/Proyectos/{{project_name}} #el directorio donde hizo el clone 
    $ pip install -r requirements.txt
    
Corra el comando de django con este proyecto como template:

    $ cd ~/Proyectos # ajuste este path a su preferencia
    $ django-admin.py startproject {{project_name}}
    
(Opcional) Sincronice la base de datos y comiense a ejecutar el proyecto:

   $ cd {{project_name}}
   $ python manage.py syncdb
   ...
   $ python runserver

> Nota: Este texto y la nota de licencia están incluidos en el molde y se 
> aplicarán a todos los proyectos que cree con este método.
> Recomendamos con énfasis modificar estos textos para adaptarlos a su entorno.


Noticia de licencia
---------------
{{project_name}} es software libre copyright 2012 de Matías Iturburu, 
Martín Onetti y Francisco Herrero, distribuido bajo la licencia BSD. Una copia 
de esta licencia se incluye en el archivo COPYING.
