# Authoring module for linden-courtyard-pt-s01e01-scene-01.
ID = 'linden-courtyard-pt-s01e01-scene-01'
SHOW = 'linden-courtyard-pt'
SEASON = 1
EPISODE = 1
SCENE = 1
TITLE = 'Lift the Handle  (Levante a maçaneta)'
LEVEL = 'A1 — iniciante'
PAIR = 'en-pt'
LABELS = {'hannah': 'Hannah', 'graham': 'Graham'}
INTRO = 'Hannah chega cedo para sua primeira manhã na pousada Linden Courtyard Inn, em Portland. Atrás da recepção, o veterano faz-tudo Graham já está servindo um chá bem forte. Ouça primeiro toda a cena em inglês sem se preocupar em entender cada palavra.'
OPENER = 'Agora vamos repassar a conversa com calma, frase por frase.'
TRANSITION = 'Vamos ouvir toda a cena novamente em velocidade natural.'
OUTRO = 'Hannah já entrou, as oito chaves de latão estão no quadro e sua primeira manhã começou. Não se preocupe se alguma palavra passou rápido; elas vão voltar a aparecer a semana inteira. Até a próxima.'
CLOSING = ('hannah', 'See you soon!')
STORY = [
    ('hannah', 'Good morning! Excuse me, is the door locked?', 'Bom dia! Com licença, a porta está trancada?'),
    ('graham', 'Good morning. No, lift the handle first, then push.', 'Bom dia. Não, primeiro levante a maçaneta e depois empurre.'),
    ('hannah', 'Oh, it opens! Thank you. I am Hannah, the new receptionist.', 'Ah, abriu! Obrigada. Eu sou a Hannah, a nova recepcionista.'),
    ('graham', 'I am Graham. You are ten minutes early.', 'Eu sou o Graham. Você chegou dez minutos adiantada.'),
    ('hannah', 'I always walk fast on my first day. Where is the computer?', 'Eu sempre ando rápido no meu primeiro dia. Onde fica o computador?'),
    ('graham', 'In the drawer. Here we use this big paper book and a pencil.', 'Na gaveta. Aqui nós usamos este grande livro de papel e um lápis.'),
    ('hannah', 'A paper book? Really?', 'Um livro de papel? Sério?'),
    ('graham', 'Paper never loses the room list when it rains.', 'O papel nunca perde a lista de quartos quando chove.'),
    ('hannah', 'Fair enough! And these are the keys?', 'Justo! E estas são as chaves?'),
    ('graham', 'Yes, eight rooms, eight brass keys. Room four is arriving today.', 'Sim, oito quartos, oito chaves de latão. O quarto quatro chega hoje.'),
    ('hannah', 'Great. Tell me everything I need to know.', 'Ótimo. Me conte tudo o que eu preciso saber.'),
    ('graham', 'Rule one: drink hot tea first, then answer the bell.', 'Regra número um: beba chá quente primeiro e depois atenda a campainha.'),
]
WALK = [
    (0, None, ["'Bom dia! Com licença, a porta está trancada?' Em português basta mudar a entonação para perguntar, mas em inglês o verbo vem para a frente em", (None, 'is the door locked'), 'logo depois de chamar a atenção com', (None, 'Excuse me'), 'com educação.']),
    (1, None, ["'Bom dia. Não, primeiro levante a maçaneta e depois empurre.' Para dar instruções simples e diretas, o inglês usa o verbo puro:", (None, 'lift'), 'para levantar e', (None, 'push'), 'que apesar da grafia significa empurrar, nunca puxar!']),
    (2, None, ["'Ah, abriu! Obrigada. Eu sou a Hannah, a nova recepcionista.' Repare em", (None, 'it opens'), 'pois o inglês não deixa o verbo sem sujeito: essa palavrinha neutra representa a porta.']),
    (3, None, ["'Eu sou o Graham. Você chegou dez minutos adiantada.' Para dizer que alguém chegou adiantado, o inglês usa o verbo ser ou estar:", (None, 'You are ten minutes early'), 'dez minutos cedo.']),
    (4, None, ["'Eu sempre ando rápido no meu primeiro dia. Onde fica o computador?' Com dias específicos usamos a preposição de superfície:", (None, 'on my first day'), 'no meu primeiro dia.']),
    (5, None, ["'Na gaveta. Aqui nós usamos este grande livro de papel e um lápis.' Observe a ordem invertida em relação ao português em", (None, 'big paper book'), 'onde tamanho e material vêm antes do substantivo, sem preposição.']),
    (6, None, ["'Um livro de papel? Sério?' Essa reação curtinha,", (None, 'Really'), "funciona exatamente como o nosso 'sério?' ou 'mesmo?' na conversa do dia a dia."]),
    (7, None, ["'O papel nunca perde a lista de quartos quando chove.' Em fenômenos do tempo o inglês também exige sujeito neutro, como você ouve no final em", (None, 'when it rains'), 'quando chove.']),
    (8, None, ["'Justo! E estas são as chaves?' Quando o argumento da outra pessoa faz todo sentido,", (None, 'Fair enough'), "é o jeito mais natural de responder 'justo!' ou 'faz sentido'."]),
    (9, None, ["'Sim, oito quartos, oito chaves de latão. O quarto quatro chega hoje.' Para compromissos já confirmados hoje, o inglês adora usar a forma contínua:", (None, 'is arriving today'), 'chega hoje.']),
    (10, None, ["'Ótimo. Me conte tudo o que eu preciso saber.' Depois de", (None, 'everything'), 'o inglês emenda direto', (None, 'I need to know'), "sem precisar de uma palavra equivalente ao nosso 'que'."]),
    (11, None, ["'Regra número um: beba chá quente primeiro e depois atenda a campainha.' Em inglês o mesmo verbo de responder serve para atender porta, telefone ou sineta:", (None, 'answer the bell'), 'atender a campainha.']),
]
