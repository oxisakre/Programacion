def astrologia():

    dia = int(input('dia: '))
    mes = input('mes, (ejemplo diciembre):')

    if mes == 'diciembre':
        astro_signo = 'Sagitario' if (dia < 22) else 'Capricornio'
    elif mes == 'enero':
        astro_signo = 'Capricornio' if (dia < 20) else 'Acuario'
    elif mes == 'feberro':
        astro_signo = 'Acuario' if (dia < 19) else 'Picis, como justin'
    elif mes == 'marzo':
        astro_signo = 'Picis, como justin' if (dia < 21) else 'Aries'
    elif mes == 'abril':
        astro_signo = 'Aries' if (dia < 20) else 'Tauro'
    elif mes == 'mayo':
        astro_signo = 'Tauro' if (dia < 21) else 'Geminis'
    elif mes == 'junio':
        astro_signo = 'Geminis' if (dia < 21) else 'Cancer'
    elif mes == 'julio':
        astro_signo = 'Cancer' if (dia < 23) else 'Leo'
    elif mes == 'agosto':
        astro_signo = 'Leo' if (dia < 23) else 'Virgo'
    elif mes == 'septiembre':
        astro_signo = 'Virgo' if (dia < 23) else 'Libra'
    elif mes == 'octubre':
        astro_signo = 'Libra' if (dia < 23) else 'Scorpio'
    elif mes == 'noviembre':
        astro_signo = 'Scorpio' if (dia < 22) else 'Sagitario'
    print("Tu signo es: ",astro_signo)  
        


astrologia()