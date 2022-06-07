def domino():
  fichas = input('dar piezas dos piezas (ejemplo: 2-5 4-2):')
  pieza = fichas.split()
  
  if len(pieza) == 2:
    if pieza[0][2] == pieza[1][0]:
      print('encajan')
    else:
      print('no encajan')
  else:
    print('solo dos piezas bro')



domino()
