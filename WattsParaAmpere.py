def main():
    potencia = (input('Potencia: '))
    tensao = (input('Tensão: '))
    if not tensao.isdigit() or not potencia.isdigit():
        print('Digite apenas números inteiros')
    else:
        potencia = int(potencia)
        tensao = int(tensao)
        corrente = potencia / tensao
        print(f'Corrente {corrente:.1f}A')
        if corrente > 57:
            print('Bitola 16mm')
        elif corrente >= 41:
            print('Bitola 10mm')
        elif corrente >= 32:
            print('Bitola 6mm')
        elif corrente >= 24:
            print('Bitola 4mm')
        elif corrente >= 17.5:
            print('Bitola 2.5mm')
        elif corrente >= 0:
            print('Bitola 2.5mm')
        # Disjuntor
        if corrente >= 41:
            print('Disjuntor de 50A')
        elif corrente >= 31:
            print('Disjuntor de 40A')
        elif corrente >= 26:
            print('Disjuntor de 30A')
        elif corrente >= 21:
            print('Disjuntor de 25A')
        elif corrente >= 16:
            print('Disjuntor de 20A')
        elif corrente >= 11:
            print('Disjuntor de 15A')
        else:
            print('Disjuntor de 10A')
        print('=' * 15)
    main()


main()






def watt():
    potencia = (input('Potencia: '))
    tensao = (input('Tensão: '))
    if not tensao.isdigit() or not potencia.isdigit():
        print('Digite apenas números inteiros')
    else:
        potencia = int(potencia)
        tensao = int(tensao)
        corrente = potencia / tensao
        print(f'Corrente {corrente:.1f}A')
        if corrente > 57:
            print('Bitola 16mm')
        elif corrente >= 41:
            print('Bitola 10mm')
        elif corrente >= 32:
            print('Bitola 6mm')
        elif corrente >= 24:
            print('Bitola 4mm')
        elif corrente >= 17.5:
            print('Bitola 2.5mm')
        elif corrente >= 0:
            print('Bitola 2.5mm')
        # Disjuntor
        if corrente >= 41:
            print('Disjuntor de 50A')
        elif corrente >= 31:
            print('Disjuntor de 40A')
        elif corrente >= 26:
            print('Disjuntor de 30A')
        elif corrente >= 21:
            print('Disjuntor de 25A')
        elif corrente >= 16:
            print('Disjuntor de 20A')
        elif corrente >= 11:
            print('Disjuntor de 15A')
        else:
            print('Disjuntor de 10A')
        print('=' * 15)
    watt()