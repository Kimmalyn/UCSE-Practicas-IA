POSICIONES = ['posicion1','posicion2','posicion3','posicion4','posicion5','posicion6','posicion7']

domains = {
    'posicion1':['Alber','Bomber','Destre','Fire','Gun'] ,
    'posicion2':['Alber','Bomber','Destre','Fire','Gun','Camina'] ,
    'posicion3':['Alber','Bomber','Destre','Fire','Gun','Camina'] ,
    'posicion4':['Alber','Bomber','Destre','Fire','Gun','Camina', 'Electro'] ,
    'posicion5':['Alber','Bomber','Destre','Fire','Gun','Camina', 'Electro'] ,
    'posicion6':['Alber','Bomber','Destre','Fire','Gun','Camina', 'Electro'] ,
    'posicion7':['Alber','Bomber','Destre','Fire','Gun','Camina', 'Electro'] ,
}

ROBOTS = {
    'Alber':['ruedas'],
    'Bomber':['ruedas', 'paredes'],
    'Camina':['piernas','paredes'],
    'Destre':['piernas'],
    'Electro':['ruedas','paredes'],
    'Fire':['ruedas','paredes'],
    'Gun': ['piernas','paredes']

}

if  'ruedas' in ROBOTS['Bomber']:
    print('funca')

print(POSICIONES.index('posicion1'))
