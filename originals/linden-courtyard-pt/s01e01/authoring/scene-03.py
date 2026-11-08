# Authoring module for linden-courtyard-pt-s01e01-scene-03.
ID = 'linden-courtyard-pt-s01e01-scene-03'
SHOW = 'linden-courtyard-pt'
SEASON = 1
EPISODE = 1
SCENE = 3
TITLE = 'Where Are My Glasses?  (Onde estão meus óculos?)'
LEVEL = 'A1 — iniciante'
PAIR = 'en-pt'
LABELS = {'arthur': 'Arthur', 'hannah': 'Hannah', 'graham': 'Graham'}
INTRO = 'Antes da chegada da primeira hóspede, o dono da pousada, Arthur, entra apressado vindo do pátio, todo afobado. Hannah e Graham observam enquanto ele revira os bolsos em pânico. Ouça a cena inteira primeiro.'
OPENER = 'Vamos conferir os detalhes passo a passo.'
TRANSITION = 'Agora ouça novamente toda a cena sem pausas.'
OUTRO = 'Arthur achou os óculos na própria testa bem na hora em que o táxi encostou lá fora. Relaxe e deixe o ritmo das frases entrar no ouvido; até a próxima cena.'
CLOSING = ('arthur', 'Bye for now!')
STORY = [
    ('arthur', 'Good morning, everyone! Welcome, Hannah. Is everything ready?', 'Bom dia, pessoal! Bem-vinda, Hannah. Está tudo pronto?'),
    ('hannah', 'Good morning! Yes, the desk is clean and the keys are ready.', 'Bom dia! Sim, o balcão está limpo e as chaves estão prontas.'),
    ('arthur', "Today's guest in room four is staying all week. Everything must be perfect!", 'A hóspede de hoje no quarto quatro vai ficar a semana toda. Tudo precisa estar perfeito!'),
    ('graham', 'Relax, Arthur. The room is clean and the towels are fresh.', 'Calma, Arthur. O quarto está limpo e as toalhas estão fresquinhas.'),
    ('arthur', 'I need to read the reservation book, but I cannot find my glasses!', 'Preciso ler o livro de reservas, mas não consigo achar meus óculos!'),
    ('hannah', 'Are they in your coat pocket?', 'Eles estão no bolso do seu casaco?'),
    ('arthur', 'No, only my pen and three old receipts!', 'Não, só minha caneta e três recibos velhos!'),
    ('graham', 'Look in the mirror behind the desk, boss.', 'Olhe no espelho atrás do balcão, chefe.'),
    ('arthur', 'Why would my glasses be in the... oh! They are on my head!', 'Por que meus óculos estariam no... ah! Estão na minha cabeça!'),
    ('hannah', 'Right there on your forehead, safe and sound.', 'Bem aí na sua testa, sãos e salvos.'),
    ('arthur', 'Do not tell anyone! Now, smile brightly when the bell rings.', 'Não conte para ninguém! Agora abra um belo sorriso quando a campainha tocar.'),
    ('graham', 'Here comes a taxi at the gate right now.', 'Lá vem um táxi no portão agora mesmo.'),
]
WALK = [
    (0, None, ["'Bom dia, pessoal! Bem-vinda, Hannah. Está tudo pronto?' Ao cumprimentar uma sala inteira,", (None, 'everyone'), "vale por 'pessoal' ou 'todos', e", (None, 'Is everything ready'), 'fica sempre no singular.']),
    (1, None, ["'Bom dia! Sim, o balcão está limpo e as chaves estão prontas.' Os adjetivos em inglês não mudam nem em gênero nem em número: repare que", (None, 'ready'), 'serve tanto para singular quanto para plural.']),
    (2, None, ["'A hóspede de hoje no quarto quatro vai ficar a semana toda. Tudo precisa estar perfeito!' Até palavras de tempo aceitam apóstrofo e esse de posse, como em", (None, "Today's guest"), 'a hóspede de hoje.']),
    (3, None, ["'Calma, Arthur. O quarto está limpo e as toalhas estão fresquinhas.' Um simples", (None, 'Relax'), "no começo da frase funciona igual ao nosso 'calma' ou 'fique tranquilo'."]),
    (4, None, ["'Preciso ler o livro de reservas, mas não consigo achar meus óculos!' Quando procuramos algo sem sucesso na hora, o inglês costuma dizer", (None, 'cannot find'), 'não consigo encontrar.']),
    (5, None, ["'Eles estão no bolso do seu casaco?' Como óculos é plural em inglês, a pergunta retoma o objeto com", (None, 'Are they'), 'antes de mencionar', (None, 'coat pocket'), 'o bolso do casaco.']),
    (6, None, ["'Não, só minha caneta e três recibos velhos!' Repare na pronúncia de", (None, 'receipts'), "em que a letra 'p' escrita no meio da palavra fica completamente muda."]),
    (7, None, ["'Olhe no espelho atrás do balcão, chefe.' Em inglês a gente olha 'dentro' do espelho,", (None, 'in the mirror'), 'e', (None, 'behind the desk'), 'marca a posição logo atrás.']),
    (8, None, ["'Por que meus óculos estariam no... ah! Estão na minha cabeça!' O auxiliar condicional em", (None, 'Why would'), "dá exatamente aquele tom de 'por que cargas d'água estariam lá?'."]),
    (9, None, ["'Bem aí na sua testa, sãos e salvos.' A expressão consagrada", (None, 'safe and sound'), "equivale ao nosso 'são e salvo', usada até de brincadeira para objetos."]),
    (10, None, ["'Não conte para ninguém! Agora abra um belo sorriso quando a campainha tocar.' Em ordens negativas começamos com", (None, 'Do not tell anyone'), 'sem repetir negativa no final.']),
    (11, None, ["'Lá vem um táxi no portão agora mesmo.' Para apontar alguém ou algo chegando,", (None, 'Here comes'), "traz o verbo antes do táxi, igual ao nosso 'lá vem'."]),
]
