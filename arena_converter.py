from data import *

def converter_arena(arena_antiga):
    arena_antiga = arena_antiga.split(',')
    arena_final = ''

    for parte in arena_antiga:
        parte = parte.strip()
        if parte[0].isnumeric():
            if len(parte) > 2:
                peca = parte
                xy = peca[0:4]
                xy = xy[::-1]
                tipo = peca[4:5]
                identificador = peca[5:6]
                id_convertido = ids.get(identificador)
                rotacao = peca[6:]
                if rotacao == '000':
                    rotacao = '2'
                elif rotacao == '090':
                    rotacao = '1'
                elif rotacao == '180':
                    rotacao = '0'
                else:
                    rotacao = '3'

                if tipo == 'r':
                    if id_convertido in retas_elevadas:
                        altura = '1'
                        id_convertido = retas_elevadas.get(id_convertido)
                    else:
                        altura = '0'
                        id_convertido = retas_convertidas.get(id_convertido)
                else:
                    if id_convertido in curvas_elevadas:
                        altura = '1'
                        id_convertido = curvas_elevadas.get(id_convertido)
                    else:
                        altura = '0'
                        id_convertido = curvas_convertidas.get(id_convertido)

                ids_reversos = {v: k for k, v in ids.items()}

                id_convertido = ids_reversos.get(id_convertido)

                arena_final += xy
                arena_final += tipo
                arena_final += id_convertido
                arena_final += rotacao
                arena_final += altura
                arena_final += 'Ç'
                arena_final += ','
            else:
                tipo_resgate = parte
                arena_final += f' {tipo_resgate}, '
        else:
            variavel = parte
            arena_final += variavel
    arena_final += config_adicional_padrao
    return arena_final.strip(',')
