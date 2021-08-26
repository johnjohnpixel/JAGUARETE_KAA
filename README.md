# JAGUARETE_KAA
Projecto Final del Curso de Desarrollo Web FullStack de PoloTIC

 [CURSO-DESWEB-PYTHON-JS-2021-TPFINAL.pdf](https://github.com/jonathan-messina/JAGUARETE_KAA/files/7052057/CURSO-DESWEB-PYTHON-JS-2021-TPFINAL.pdf)

 1 
 
 
CURSO DE DESARROLLO WEB FULL STACK 
CON PYTHON Y JAVASCRIPT 

TRABAJO INTEGRADOR FINAL 2021 (v1.0) 
 
ENUNCIADO 

La empresa JAGUARETE KAA S.A. quiere realizar un sitio web para exponer los productos  que tiene 
para  venderlos  aprovechando  el  auge  del  eCommerce  y  dentro  de  sus  requerimientos  está  lo 
siguiente. 
La  empresa  quiere  que  todas  las  páginas  del  sitio  sean  homogéneas  además  de  que  puedan  verse 
bien en computadoras de escritorio, tablets o teléfonos celulares.  



ESTRUCTURA DEL SITIO WEB 


Se desea tener una sección de encabezado, que incluya el logo de la empresa y botones de acceso 
rápido para el login del usuario, el registro y el carrito. Además de contar con el botón de desconectar 
en caso de estar logueado. 
Una sección de menú, donde se pueda ir siempre al home o pagina principal, un botón desplegable 
que muestre todas las categorías de los productos, un botón de acerca de.. que lleve hacia una página 
con los datos de la empresa, un botón de contacto que sea un enlace al mail de la empresa, un botón 
de agregar producto (que solo vean los moderadores) y una caja de búsqueda para buscar productos. 
Una  sección  de  footer  o  pie  de  página  donde  aparezca  el  nombre  de  la  empresa,  el  copyright  y  el 
nombre del desarrollador.  
Lo único que cambiará de página en página es el contenido que haya en la sección media o cuerpo 
del sitio web como se muestra en la imagen a continuación: 
  
 2 
 
El cuerpo variará según la URL y serán las siguientes: 
• Pantalla principal 
• Pantalla de acerca de... 
• Pantalla de resultado de busqueda 
• Pantalla del producto 
• Pantalla de login 
• Pantalla de registro 
• Pantalla del carrito 
ENCABEZADO 
El encabezado contará con un logo a la izquierda y en la parte superior derecha tres botones, uno de 
login hacia la pantalla de acceso, uno de registro para nuevos usuarios y otro de carrito para visualizar 
el  carrito  de  compras.  Si  el  usuario  esta  logueado  no  podrá  ver  el  botón  login  y  tampoco  el  botón 
registro. Solo podrá ver un botón para desconectar y el de carrito. 
Si es moderador solo podrá ver el botón de desconectar. El moderador no tiene carrito. 
 
  
 3 
 
MENU 


El menú contará con las siguientes opciones: 
• Home: dirige a la página principal; 
• Categorias: es un desplegable que muestra todas las categorías y luego lleva a la página de 
búsqueda (con los productos filtrados por la categoría seleccionada) 
• Acerca de..: Lleva a una pagina estatica con información de la empresa 
• Contacto: Es simplemente un botón de enlace al mail de la compañía (un hyperlink de tipo 
mailto:) 
• Nuevo producto: Solo lo ve el moderador y lleva a la página de alta de producto. 
• Una caja de buscador, que cuando se presiona intro lleva a la página de búsqueda filtrando 
con la palabra que se ingresó. 
 
 
 
PANTALLA PRINCIPAL 

En todas las pantallas el encabezado, el menú y el footer son iguales.  
En el cuerpo de la página principal aparecerán los 10 ultimos productos. Los primeros 3 en el 
formato que se muestra en el prototipo a continuación, y los demás simplemente con una lista (al 
clicar en ellos los lleva a la página de ver el producto). 
 
  
 4 
 
 
PANTALLA ACERCA DE 


Una página estática con información de la empresa. Pueden poner la información que quieran, 
imágenes, texto, etc. 
 
 
PANTALLA DE RESULTADO DE BUSQUEDA 


A esta página se llega de dos maneras. La primera es buscando con la cajita del menú. Y la segunda 
es eligiendo una categoría.  
En la primera se filtra por cualquier cosa que aparezca en el titulo o la descripción, en la segunda 
solamente por la categpría. 
Esta página es un listado simple. 
 
  
 5 
 
 
PANTALLA DEL PRODUCTO 

VISUALIZACION (Solo usuario comunes) 

Se pueden ver todos los detalles del producto y se puede agregar al carrito del usuario logueado. Si 
el usuario no esta logueado se lo lleva a la pantalla de login cuando apreta el botón. 
 
NUEVO

(Solo moderadores, podrán ver el botón nuevo producto en el menú). Todos los campos son 
obligatorios. 
 
 
  
 6 
 
 
EDITAR/BORRAR (Solo moderadores) 

Solo los moderadores podrán editar los datos del producto. Todos los campos son obligatorios. 
 
PANTALLA DE LOGIN 
Es la misma para usuarios comunes o moderadores. 
 
  
 7 
 
 
PANTALLA DE REGISTRO 

A la pantalla de registro no pueden acceder usuarios ya registrados. Todos los campos son 
obligatorios. 
 
PANTALLA DE CARRITO 

Solo usuarios comunes. Podran ver un listado de los productos que agregaron al carrito, podrán 
sacarlos de a uno, vaciarlo completamente o finalizar la compra. El botón de finalización de compra 
no se implementará en este trabajo final. 
 
  
 8 
 
MODELOS ELEMENTALES 

Para desarrollar el presente trabajo serán obligatorios los modelos siguientes modelos para la lógica 
de negocios: 
• Categorias: 
o Descripcion 
• Productos: 
o Titulo 
o Imagen 
o Descripcion 
o Precio 
o Categoria a la que pertenece 
• Carrito: 
o Usuario 
o Lista de productos del usuario. 
o Total del carrito. 


El modelo para el Usuario será el mismo que utiliza Django por defecto, lo mismo para los grupos. 
Los grupos de usuarios serán dos, usuario común, y moderador. El usuario común podrá ver el sitio 
web completo a excepción de las páginas de Carga y Edición del Producto. También podrá ver la 
página de carrito con los productos que fue cargando. 
El usuario moderador podrá ver todo el sitio web, pero en lugar de ver la página de producto verá la 
página de edición. Y en la página principal podrá ver un botón de Agregar Producto que le llevará a 
la página de carga de Producto. 


BASES DE DATOS 
Pueden presentar el trabajo solamente con la base por defecto de Django (SQLite) 

FRONT END 
El sitio web debe ser responsivo, se debe implementar Bootstrap (o alguna librería similar). 
