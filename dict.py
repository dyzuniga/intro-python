persona_1 = {
  'nombre': 'Sara',
  'edad': 27,
  'cedula': '115820287'
}
persona_2 = {
  'nombre': 'Oscar',
  'edad': 35,
  'cedula': '112310501'
}
persona_3 = {
  'nombre': 'Mario',
  'edad': 40,
  'cedula': '111020253'
}

persona_4 = {
  'nombre': 'Daye',
  'edad': 29,
  'cedula': '503900224'
}
persona_5 = {
  'nombre': 'Rafa',
  'edad': 45,
  'cedula': '112310501'
}
persona_6 = {
  'nombre': 'Ale',
  'edad': 36,
  'cedula': '112510899'
}

personas = [persona_1, persona_2, persona_3]
personas1 = [persona_4, persona_5, persona_6]

#for p in personas:
    #print(p['nombre'], 'tiene', p['edad'], 'años y su cédula es', p['cedula'])

def info(p):
    return p['nombre'] + ' tiene ' + str(p['edad']) + ' años y su cédula es ' + p['cedula']

#for persona in personas:
    #print(info(persona))

for persona in personas1:
    print(info(persona))