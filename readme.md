# Testing of DLL integrate C++ and Python

Creation libTestN.so

Para compilr *.cpp como libreria dinamica
es necesario agregar -fPIC.
ej:

Comando: g++ -fPIC -shared -o libdina.so dina.cpp

-fPIC: Cuando se compila un archivo fuente en C++ para generar una biblioteca compartida, es necesario utilizar la opción -fPIC (Position Independent Code) para indicar al compilador que el código generado debe ser independiente de la posición. Esto permite que la biblioteca compartida se cargue y ejecute correctamente en diferentes direcciones de memoria, ya que no asume una ubicación específica.

Ex:

!g++ -fPIC -shared -o libTestN.so libdinamic.cpp


