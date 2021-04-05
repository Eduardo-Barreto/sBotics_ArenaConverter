retas_convertidas = {
    '75':   '38',   # Ladrilho de início
    '77':   '37',   # Ladrilho de início com paredes
    '76':   '36',   # Ladrilho de início sem linha
    '78':   '11',   # Ladrilho final
    '80':   '10',   # Ladrilho final com paredes
    '73':   '8',    # Terceira Sala
    '54':   '4',    # Conjunto Bilateral
    '66':   '5',    # Conjunto Unilateral
    '18':   '32',   # 4 Retornos
    '6':    '7',    # Encruzilhada C
    '50':   '6',    # Encruzilhada C com Gap
    '24':   '33',   # Encruzilhada Reta
    '25':   '39',   # Encruzilhada T Reta
    '82':   '35',   # Escadaria
    '0':    '1',    # Linha
    '51':   '40',   # Linha com V
    '56':   '21',   # Meia Lua
    '3':    '2',    # Zigue-Zague
    '5':    '3',    # Zigue-Zague 90°
    '68':   '26',   # Zigue-Zague 90° Unilateral
    '57':   '41',   # Zigue-Zague Suave
    '60':   '42',   # Zigue-Zague Suave Unilateral
    '63':   '43',   # Zigue-Zague Unilateral
    '33':   '14',   # 2 Gaps
    '74':   '12',   # Gangorra
    '1':    '13',   # Gap
    '32':   '17',   # Gap e Redutor
    '35':   '16',   # Gap e Redutor Inclinado
    '4':    '22',   # Obstáculo
    '23':   '31',   # Portal
    '2':    '18',   # Redutor
    '34':   '15',   # Redutor Inclinado
    '22':   '20',   # Redutores
    '36':   '19',   # Redutores Inclinados
    '81':   '34',   # Rotatória
    '37':   '44',   # Zigue-Zague com Redutor
    '21':   '25',   # 3 Paredes
    '20':   '24',   # Parede
    '19':   '23',   # Paredes Laterais
    '8':    '30',   # Rampa
    '9':    '27',   # Rampa com Gap
    '10':   '28',   # Rampa com Redutor
    '11':   '29',   # Rampa com Redutores
}

curvas_convertidas = {
    # Antigo: Novo

    '22':   '0',    # Ladrilho Vazio

    '19':   '3',    # Conjunto simples
    '21':   '2',    # Conjunto Encruzilhadas Simples

    '4':    '5',    # Intersecção C
    '14':   '4',    # Encruzilhada C com Gap


    '2':    '24',   # Encruzilhada Circular
    '7':    '19',   # Encruzilhada com Verde
    '8':    '17',   # Encruzilhada Dupla
    '9':    '16',   # Encruzilhada Dupla Cruzada
    '5':    '27',   # Encruzilhada T
    '6':    '26',   # Encruzilhada T Dupla
    '10':   '18',   # Encruzilhada T Tripla
    '23':   '14',   # Obstáculo
    '27':   '22',   # Rotatória Com Curva 90°
    '26':   '21',   # Rotatória com Degraus
    '28':   '23',   # Rotatória Externa

    '1':    '1',    # Curva 90°
    '3':    '13',   # Curva Complexa
    '15':   '8',    # Curva Degrau
    '17':   '7',    # Curva Degrau Suave
    '24':   '6',    # Curva Diagonal
    '0':    '25',   # Curva Suave
    '30':   '10',   # Dupla de Curvas Degrau
    '29':   '9',    # Dupla de Curvas Degrau Suave
    '31':   '11',   # Dupla de Curvas Diagonal
    '32':   '12',   # Dupla de Curvas Suave
    '25':   '20',   # Rotatória Aberta

    '11':   '15'   # Parede Curvada
}

curvas_elevadas = {
    # Antigo: Elevado Novo
    '12':   '1',
    '13':   '25',
    '16':   '25',
    '18':   '7',
    '20':   '3',
}

retas_elevadas = {
    # Antigo: Elevado Novo
    '12':   '1',
    '13':   '13',
    '14':   '18',
    '15':   '20',
    '16':   '2',
    '17':   '3',
    '26':   '1',    # Linha inferior
    '27':   '1',    # Linha inferior
    '28':   '1',    # Linha inferior
    '29':   '1',    # Linha inferior
    '30':   '1',    # Linha inferior
    '31':   '1',    # Linha inferior
    '38':   '14',   # Linha inferior
    '39':   '14',
    '40':   '15',   # Linha inferior
    '41':   '15',
    '42':   '16',   # Linha inferior
    '43':   '16',
    '44':   '16',   # Linha inferior
    '45':   '17',
    '46':   '19',   # Linha inferior
    '47':   '19',
    '48':   '44',   # Linha inferior
    '49':   '44',
    '52':   '40',
    '53':   '40',   # Linha inferior
    '55':   '4',
    '58':   '41',
    '59':   '41',   # Linha inferior
    '61':   '42',   # Linha inferior
    '62':   '42',   # Linha inferior
    '64':   '43',
    '65':   '43',   # Linha inferior
    '67':   '5',
    '69':   '26',
    '70':   '26'   # Linha inferior
}

ids = {
    '0': '0',  '1': '1',  '2': '2',  '3': '3',
    '4': '4',  '5': '5',  '6': '6',  '7': '7',
    '8': '8',  '9': '9',  'a': '10',  'b': '11',
    'c': '12',  'd': '13',  'e': '14',  'f': '15',
    'g': '16',  'h': '17',  'i': '18',  'j': '19',
    'k': '20',  'l': '21',  'm': '22',  'n': '23',
    'o': '24',  'p': '25',  'q': '26',  'r': '27',
    's': '28',  't': '29',  'u': '30',  'v': '31',
    'w': '32',  'x': '33',  'y': '34',  'z': '35',
    'A': '36',  'B': '37',  'C': '38',  'D': '39',
    'E': '40',  'F': '41',  'G': '42',  'H': '43',
    'I': '44',  'J': '45',  'K': '46',  'L': '47',
    'M': '48',  'N': '49',  'O': '50',  'P': '51',
    'Q': '52',  'R': '53',  'S': '54',  'T': '55',
    'U': '56',  'V': '57',  'W': '58',  'X': '59',
    'Y': '60',  'Z': '61',  '+': '62',  '/': '63',
    '=': '64',  '<': '65',  '>': '66',  '{': '67',
    '}':  '68',  '[':  '69',  ']':  '70',  '(':  '71',
    ')':  '72',  '?':  '73',  '&':  '74',  '$':  '75',
    '^':  '76',  '-':  '77',  '_':  '78',  '@':  '79',
    'Á':  '80',  'É':  '81',  'Í':  '82',  'Ó':  '83'
}

config_adicional_padrao = ', SaidaSala: 0, TRescueKit: true, RescueKit: false'

# Não utilizado ainda
linha_inferior = [
    '26', '27', '28', '29', '30', '31',
    '38', '40', '42', '44', '46', '48',
    '53', '59', '61', '62', '65', '70'
]
