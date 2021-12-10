japon = ['Toyota', 'Honda', 'Nissan']
corea = ['Hyundai', 'Kia']
alemania = ['BMW', 'Audi', 'Mercedes-Benz']
usa = ['Ford', 'GMC', 'Tesla']

# print('\nCarros japoneses:')
# for carro in japon:
#     print('-',carro)

# print('\nCarros coreanos:')
# for carro in corea:
#     print('-',carro)

# print('\nCarros alemanes:')
# for carro in alemania:
#     print('-',carro)

# print('\nCarros estadounidenses:')
# for carro in usa:
#     print('-',carro)

carros = [japon, corea, alemania, usa]

for pais in carros:
    print('Modelos:')
    for carro in pais:        
        print('-',carro)
