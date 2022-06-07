def a_hms(segundos):
    
    segundos= int(input('dame los segundos papi:'))
    h = (segundos // 3600)
    m = (segundos % 3600) // 60
    s = (segundos % 3600) % 60
    print(h, m, s)

    a_hms(segundos)
