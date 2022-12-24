
print("Viteza media a unei masini")
import numpy
speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
x = numpy.mean(speed)
print(x, '\n')


#mediana
print("Valoarea mediană")
import numpy
speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
x = numpy.median(speed)
print(x, '\n')

print("Valoarea Mode")
from scipy import stats
speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
x = stats.mode(speed)
print(x, '\n')


#Abatearea standart
print("Abatearea standart, Deviatia standart")
import numpy
speed = [86,87,88,86,87,85,86]
x = numpy.std(speed)
print(x, '\n')

"""
O abatere standard scăzută înseamnă că majoritatea numerelor sunt
aproape de valoarea medie.
O abatere standard ridicată înseamnă că valorile sunt distribuite întrun interval mai larg.
"""
"""
Ce este deviația standard?
Găsiți media:
2. Pentru fiecare valoare: găsiți diferența față de
medie:
3. Pentru fiecare diferență: găsiți valoarea
pătrată:
4. Varianta este numărul mediu al acestor
diferențe pătrate:

Folosim functia var()
Rez = 1432.25 
formula pentru a găsi abaterea standard este
rădăcina pătrată a varianței:
√1432.25 = 37.85
"""
print("Folosim functia var, deviația standard")
import numpy
speed = [32,111,138,28,59,77,97]
x = numpy.var(speed)
print(x, '\n')


# Ce sunt percentilele?
"""
Percentilele sunt folosite în statistici pentru a vă oferi un număr care
descrie valoarea pe care un anumit procent din valori este mai mică
decât

Exemplu: Să presupunem că avem o serie de vârste ale tuturor
oamenilor care locuiesc pe o stradă.
ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]

Care este percentila 75? Răspunsul este 43, ceea ce înseamnă că
75% dintre oameni au 43 de ani sau mai puțin.
Modulul NumPy are o metodă pentru găsirea percentilei specificate:
"""
print("Abaterea standard")
import numpy
ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]
x = numpy.percentile(ages, 75)
print(x, '\n')

print("Metoda pentru gasirea percentilei specificate, Modulul NumPy")
import numpy
ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]
x = numpy.percentile(ages, 75)
print(x, '\n')

print("Distribuirea datelor")
import numpy
x = numpy.random.uniform(0.0, 5.0, 250)
print(x, '\n')

