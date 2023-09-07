"""
ctypes: ctypes es una biblioteca de funciones foráneas para Python. Proporciona tipos de datos compatibles con C y permite llamar a funciones en archivos DLL o bibliotecas compartidas. Se puede utilizar para envolver estas bibliotecas en Python puro.

time: Este módulo proporciona varias funciones relacionadas con el tiempo. Para la funcionalidad relacionada, consulte también los módulos datetime y calendar.

"""
import ctypes 
import time

"""
Objetivo: Observar la integración de lenguajes en pro del rendimiento
"""
def performancePython(n):
    var = 0
    for i in range(0,n):
        var = var + 1
    print("Result Python", var)

if __name__ == "__main__":
    print("Start....")
    
    time_i = 0
    time_f = 0
    
    cases = 4294967290 #10.000.000.000 Diez Mil

    libTest = ctypes.CDLL("./libTestN.so") #Se obtiene la dll que sera .so o .dll dependiendo el OS
    performanceTest = libTest.testPerformance #Se selecciona la función o método

    """
    C++ Performance Test
    """
    print("Start performance test C++")
    time_i = time.time()
    performanceTest(cases)
    time_f = time.time()
    print("C++ time: ",time_f - time_i)

    """
    Python Performance Test
    """
    print("Start performance test Python")
    time_i = time.time()
    performancePython(cases)
    time_f = time.time()

    print("Python time: ",time_f - time_i)
    
