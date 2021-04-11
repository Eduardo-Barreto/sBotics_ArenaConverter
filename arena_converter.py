from data import *


def antigo_padrao2(arena_antiga):
    arena_antiga = arena_antiga.strip('\n')

    arena_antiga = arena_antiga.split(',')
    arena_final = ''

    for parte in arena_antiga:
        parte = parte.strip()
        if parte[0].isnumeric():
            if len(parte) > 2:
                peca = parte
                x = peca[0:2]
                y = peca[2:4]
                xy = x[::-1] + y[::-1]
                tipo = peca[4:5]
                identificador = peca[5:6]
                if identificador == '(':
                    continue
                id_convertido = ids.get(identificador)
                rotacao = peca[6:]
                if rotacao == '000':
                    rotacao = '0'
                elif rotacao == '090':
                    rotacao = '1'
                elif rotacao == '180':
                    rotacao = '2'
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
            variavel = parte + ','
            arena_final += variavel
    arena_final = arena_final.strip(',')
    arena_final += config_adicional_padrao
    return arena_final


def padrao2_json(arena_antiga):
    arena_antiga = arena_antiga.strip('\n')
    arena_antiga = arena_antiga.split(',')
    arena_final = {}
    tiles = []
    settings = {}
    rescue_zone = {'ramp': 2}
    for parte in arena_antiga:
        parte = parte.strip()
        if parte[0].isnumeric():
            if len(parte) > 2:
                peca = parte
                x = peca[0:2]
                if x.startswith('0'):
                    x = x[1:]
                z = peca[2:4]
                if z.startswith('0'):
                    z = z[1:]
                tipo = peca[4:5]
                if tipo == 'r':
                    tipo = 'straight_line'
                else:
                    tipo = 'curve'
                identificador = peca[5:6]
                if identificador == '(':
                    continue
                id_convertido = ids.get(identificador)
                rotacao = peca[6:7]
                altura = peca[7:8]
                tile = {'id': id_convertido, 'x': x, 'z': z, 'y': altura, 'type': tipo,
                        'rotation': rotacao, 'properties': {'has_checkpoint': False}}
                tiles.append(tile)
            else:
                tipo_resgate = parte
                rescue_zone.update({'ramp': tipo_resgate})
        else:
            config_antiga = parte
            config_antiga = config_antiga.split(': ')
            if config_antiga[0] in configs:
                config_nova = configs.get(config_antiga[0])
            elif config_antiga[0] in configs_resgate:
                config_nova = configs_resgate.get(config_antiga[0])
                if config_nova not in rescue_zone:
                    rescue_zone.update({config_nova: config_antiga[1]})
                continue
            else:
                if config_antiga[0] == 'RobosPerm':
                    robos_permitidos = []
                    for caractere in config_antiga[1]:
                        if caractere == '0':
                            robos_permitidos.append(False)
                        else:
                            robos_permitidos.append(True)
                    settings.update(
                        {'robot_permissions': {
                            'robot_one': robos_permitidos[0],
                            'robot_two': robos_permitidos[1],
                            'robot_three': robos_permitidos[2],
                            'robot_four': robos_permitidos[3],
                            'robot_five': robos_permitidos[4],
                            'custom_robots': robos_permitidos[5]
                        }}
                    )

    settings.update({'rescue_zone': rescue_zone})
    arena_final.update({'tiles': tiles})
    arena_final.update({'settings': settings})
    return str(arena_final).replace('\'', '"').lower()
