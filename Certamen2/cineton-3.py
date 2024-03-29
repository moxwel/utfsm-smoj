cartelera = [# (mes, pais, nombre_pelicula, annio_filmacion, [sala1, sala2, ...])
            ('febrero', 'FRANCIA' , 'El muelle'          , 1962, ['sala1', 'sala3']),
            ('febrero', 'FRANCIA' , 'La dama de honor'   , 2004, ['sala1', 'sala4']),
            ('abril'  , 'RUSIA'   , 'Padre del soldado'  , 1964, ['sala3', 'sala2', 'sala4']),
            ('enero'  , 'CHILE'   , 'Gloria'             , 2013, ['sala1', 'sala2']),
            ('mayo'   , 'MEXICO'  , 'Cumbres'            , 2013, ['sala3', 'sala2']),
            ('julio'  , 'FRANCIA' , 'Melo'               , 1986, ['sala3', 'sala1']),
            ('junio'  , 'BELGICA' , 'Rondo'              , 2012, ['sala4', 'sala2']),
            ('marzo'  , 'ALEMANIA', 'Tiempo de Canibales', 2014, ['sala1', 'sala2']),
            ('marzo'  , 'ALEMANIA', 'Soul Kitchen'       , 2009, ['sala3', 'sala4'])]

menor    = 3000
pelicula = 0
pais     = 0

for x in cartelera:
    if x[3] < menor:
        menor    = x[3]
        pelicula = x[2]
        pais     = x[1]

print((pelicula, pais))