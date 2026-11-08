# Authoring module for linden-courtyard-pt-s01e03-scene-01.
ID = 'linden-courtyard-pt-s01e03-scene-01'
SHOW = 'linden-courtyard-pt'
SEASON = 1
EPISODE = 3
SCENE = 1
TITLE = 'Thirty-Five Minutes  (Trinta e cinco minutos)'
LEVEL = 'A1 — iniciante'
PAIR = 'en-pt'
LABELS = {'arthur': 'Arthur', 'hannah': 'Hannah', 'graham': 'Graham'}
INTRO = 'A chuva bate nas janelas da recepção na pousada Linden Courtyard Inn, em Portland. Com um segundo hóspede para o quarto sete chegando em trinta e cinco minutos, Arthur, Hannah e Graham correm em direção à escada. Ouça primeiro toda a cena em inglês.'
OPENER = 'Agora vamos repassar a conversa com calma, frase por frase.'
TRANSITION = 'Vamos ouvir toda a cena novamente em velocidade natural.'
OUTRO = 'Trinta e cinco minutos no relógio e quatro caixas pelo caminho. Não tem problema se alguma palavra passou rápido; você vai ouvi-las de novo lá no terceiro andar. Até a próxima.'
CLOSING = ('hannah', 'See you soon!')
STORY = [
    ('arthur', 'Thirty-five minutes! He will write a terrible one star review!', 'Trinta e cinco minutos! Ele vai escrever uma avaliação terrível de uma estrela!'),
    ('hannah', 'Take a deep breath, Arthur. Nobody has written anything yet.', 'Respire fundo, Arthur. Ninguém escreveu nada ainda.'),
    ('graham', 'Here is the small silver key for the third floor attic door.', 'Aqui está a pequena chave prateada da porta do sótão do terceiro andar.'),
    ('arthur', 'Does the attic even have a proper bed?', 'O sótão tem pelo menos uma cama de verdade?'),
    ('graham', 'Yes, a good wooden bed, a clean desk, and the best view in the house.', 'Sim, uma boa cama de madeira, uma escrivaninha limpa e a melhor vista da casa.'),
    ('hannah', 'Then why do we never rent it to guests?', 'Então por que nós nunca alugamos esse quarto para os hóspedes?'),
    ('graham', 'Because the stairs are narrow and Arthur keeps old lamp boxes there.', 'Porque a escada é estreita e o Arthur guarda caixas velhas de luminárias lá.'),
    ('arthur', 'Only three small boxes! Maybe four!', 'Só três caixas pequenas! Talvez quatro!'),
    ('hannah', 'We can move four boxes in five minutes. Let us go look right now!', 'Podemos tirar quatro caixas em cinco minutos. Vamos lá olhar agora mesmo!'),
    ('graham', 'Up the stairs, turn left at the landing, last door at the top.', 'Subindo a escada, vire à esquerda no patamar, última porta lá no alto.'),
    ('arthur', 'I will bring clean white sheets from the linen closet!', 'Eu vou trazer lençóis brancos limpos do armário de roupa de cama!'),
    ('hannah', 'Come on, race you to the third floor!', 'Vamos, aposto corrida até o terceiro andar!'),
]
WALK = [
    (0, None, ["'Trinta e cinco minutos! Ele vai escrever uma avaliação terrível de uma estrela!' Para falar do futuro em inglês basta colocar o auxiliar antes do verbo:", (None, 'will write'), 'vai escrever.']),
    (1, None, ["'Respire fundo, Arthur. Ninguém escreveu nada ainda.' Guarde a expressão pronta", (None, 'Take a deep breath'), 'que pede literalmente para alguém puxar um fôlego fundo e se acalmar.']),
    (2, None, ["'Aqui está a pequena chave prateada da porta do sótão do terceiro andar.' Repare como os detalhes vêm todos antes da palavra principal em", (None, 'third floor attic door'), 'porta do sótão do terceiro andar.']),
    (3, None, ["'O sótão tem pelo menos uma cama de verdade?' A palavrinha", (None, 'even'), "na pergunta reforça a dúvida, funcionando como 'ao menos' ou 'por acaso'."]),
    (4, None, ["'Sim, uma boa cama de madeira, uma escrivaninha limpa e a melhor vista da casa.' Com superlativos ligados a um lugar, o inglês prefere", (None, 'best view in the house'), "usando 'em' em vez de 'de'."]),
    (5, None, ["'Então por que nós nunca alugamos esse quarto para os hóspedes?' Veja a ordem da pergunta com advérbio de frequência em", (None, 'why do we never rent'), "mantendo 'never' colado antes do verbo."]),
    (6, None, ["'Porque a escada é estreita e o Arthur guarda caixas velhas de luminárias lá.' Em inglês uma escada interna costuma ser tratada no plural:", (None, 'the stairs are narrow'), 'por causa dos degraus.']),
    (7, None, ["'Só três caixas pequenas! Talvez quatro!' Curta e muito prática,", (None, 'Maybe'), "resolve qualquer 'talvez' ou 'quem sabe' na fala cotidiana."]),
    (8, None, ["'Podemos tirar quatro caixas em cinco minutos. Vamos lá olhar agora mesmo!' No inglês falado dos Estados Unidos é super natural juntar dois verbos assim:", (None, 'go look'), 'ir olhar.']),
    (9, None, ["'Subindo a escada, vire à esquerda no patamar, última porta lá no alto.' Para dar direções rápidas dentro de um prédio,", (None, 'turn left at the landing'), 'indica a curva e o ponto exato.']),
    (10, None, ["'Eu vou trazer lençóis brancos limpos do armário de roupa de cama!' Quando você se oferece na hora para ajudar,", (None, 'I will bring'), 'soa prestativo e imediato.']),
    (11, None, ["'Vamos, aposto corrida até o terceiro andar!' O convite brincalhão", (None, 'race you'), 'dispensa o sujeito e desafia a outra pessoa na hora.']),
]
