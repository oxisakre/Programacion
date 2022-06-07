def fecha():
    dia = int(input('dia:'))
    mes = int(input('mes:'))
    año = int(input('año:'))
    Bisiesto = año % 4 == 0 and (año % 100 != 0 or año % 400 == 0)

    
    if Bisiesto and mes == 2 and dia > 29:
        return print('fecha no valida')
    if not Bisiesto and mes ==2 and dia > 28:
        return print('fecha no valida')
    
    if mes > 12 :
        return print('fecha no valida')
    if dia > 31:
        return print('fecha no valida')
    if dia <= 0 or mes <= 0 or año < 0:
        return print('fecha no valida')
    else:
        print(f'{dia}/{mes}/{año}')

        if año % 4 == 0 and (año % 100 != 0 or año % 400 == 0):
            print('es bisiesto')
        else:
            print('no es bisiesto')
    
        fin_de_mes = 31 - dia

        if mes == 2:
            if año % 4 == 0 and (año % 100 != 0 or año % 400 == 0):
                fin_de_mes = 29 - dia
        if mes == 2:
                fin_de_mes = 28 - dia
        
        print('fin de mes en:', fin_de_mes,'dias')

        if mes == 1:
            fin_año = 365 - dia
        if mes == 2:
                fin_año = 365 - (dia + 31)
        if mes == 3 and Bisiesto:
                fin_año = 366 - (dia + 60)
        if mes == 3 and not Bisiesto:
                fin_año = 365 - (dia + 59)
        if mes == 4 and Bisiesto:
                fin_año = 366 - (dia + 91)
        if mes == 4 and not Bisiesto:
                fin_año = 365 - (dia + 90)
        if mes == 5 and Bisiesto:
                fin_año = 366 - (dia + 121)
        if mes == 5 and not Bisiesto:
                fin_año = 365 - (dia + 120)
        if mes == 6 and Bisiesto:
                fin_año = 366 - (dia + 152)
        if mes == 6 and Bisiesto:
                fin_año = 365 - (dia + 151)
        if mes == 7 and Bisiesto:
                fin_año = 366 - (dia + 182)
        if mes == 7 and not Bisiesto:
                fin_año = 365 - (dia + 181)
        if mes == 8 and Bisiesto:
                fin_año = 366 - (dia + 213)
        if mes == 8 and not Bisiesto:
                fin_año = 365 - (dia + 212)
        if mes == 9 and Bisiesto:
                fin_año = 366 - (dia + 244)
        if mes == 9 and not Bisiesto:
                fin_año = 365 - (dia + 243)
        if mes == 10 and Bisiesto:
                fin_año = 366 - (dia + 274)
        if mes == 10 and not Bisiesto:
                fin_año = 365 - (dia + 273)
        if mes == 11 and Bisiesto:
                fin_año = 366 - (dia + 305)
        if mes == 11 and not Bisiesto:
                fin_año = 365 - (dia + 304)
        if mes == 12 and Bisiesto:
                fin_año = 366 - (dia + 335)
        if mes == 12 and not Bisiesto:
                fin_año = 365 - (dia + 334)
    
        print('fin de año en:', fin_año,'dias')

        dias_transcurridos = 365 - fin_año
        if Bisiesto:
            dias_transcurridos = 366 - fin_año
        print('dias transcurridos:', abs(dias_transcurridos))

fecha()
