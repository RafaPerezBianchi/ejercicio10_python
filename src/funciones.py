def find_winner_and_update_chart(round, chart): # Revisa la ronda para retornar al ganador y tambien actualiza las estadisticas de todos los jugadores.
    winner = ''
    max = -1
    for i in round['scores'].keys():
        N = 0
        for j in round['scores'][i].values():
            N += j
        if N > max:
            max = N
            winner = i
        chart[i]['Score'] += N
        if N > chart[i]['Best round']:
            chart[i]['Best round'] = N
    chart[winner]['Rounds won'] += 1
    return (winner, max) # Retorna también los puntos del ganador para no calcularlos luego.


def show_chart(chart):
    print(''.center(75,'-'))
    print('Cocinero/a'.ljust(15) + 'Puntaje')
    for i in chart.keys():
        print(i.ljust(15) + str(chart[i]['Score']))
    print(''.center(75,'-'))


def get_score(tuple):
    return tuple[1]['Score']


def get_sorted_chart(chart):
    sorted_list = list(chart.items())
    sorted_list.sort(key= get_score)
    sorted_list.reverse()
    return dict(sorted_list)


def show_final_chart(chart):
    sorted_chart = get_sorted_chart(chart)
    print(''.center(75,'='))
    print('Tabla de posiciones final')
    print(''.center(75,'.'))
    print('Cocinero/a'.ljust(15) + 'Puntaje'.ljust(15) + 'Rondas ganadas'.ljust(15) + 'Mejor ronda'.ljust(15) + 'Promedio')
    print(''.center(75,'_'))
    for i in sorted_chart.keys():
        print(i.ljust(15) + str(sorted_chart[i]['Score']).ljust(15) + str(sorted_chart[i]['Rounds won']).ljust(15) + str(sorted_chart[i]['Best round']).ljust(15) + str(round((sorted_chart[i]['Score'] / 5), 1)))
    print(''.center(75,'='))