def multiplica_a_soma(multiplicador, *args):
    return multiplicador * sum(args)


resultado2 = multiplica_a_soma(9, 8, 7, 6, 5, 4, 3, 2, 1)
print(resultado2)


def killer(sword, *args, desvantagem=0, **kwargs):
    pessoa = kwargs

    killed = multiplica_a_soma(sword, *args)
    if killed > desvantagem:
        killed -= desvantagem

    pessoa.update({
        "killed": killed,
        "killed2": killed,
        "killed3": killed
    })
    
    return pessoa


pessoa = killer(2,
                3, 4, 5, 6, 7, 5,
                desvantagem=2,
                nome='John', sobrenome='Snow', idade='36', familia='Targaryen'
                )
print(pessoa)
