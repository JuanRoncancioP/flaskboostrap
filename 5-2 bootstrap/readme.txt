El ejemplo utiliza Blueprints, boostrap y jinja2 para presentar un sitio con un menu principal donde cada una de las llaves de un diccionario es un enlace a una pagina donde se visualiza el dato del diccionario.

Se presentaron dos dificultades. una fue a manera en que se hacia referencia a las hojas de estilos y a los archivos boostrap
y la otra fue la configuracion del registro de windows que hacia que el navegador presentara un erro al cargar las hojas de estilo por Mime type.
Para solucionarlos se ingres[o al registro y e rootkeys se cambio la llave css para que tubiera el valor text/html. inicialmente tenía el valor aplication/cx o algo asi.