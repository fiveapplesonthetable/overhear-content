# Authoring module for linden-courtyard-pt-s01e02-scene-05.
ID = 'linden-courtyard-pt-s01e02-scene-05'
SHOW = 'linden-courtyard-pt'
SEASON = 1
EPISODE = 2
SCENE = 5
TITLE = 'Juice on the Tie  (Suco na gravata)'
LEVEL = 'A1 — iniciante'
PAIR = 'en-pt'
LABELS = {'arthur': 'Arthur', 'evelyn': 'Evelyn', 'hannah': 'Hannah'}
INTRO = 'O café da manhã corre animado no cantinho iluminado pelo sol. Evelyn senta-se perto da janela enquanto Arthur faz questão de ajudar Hannah a servir as bebidas como anfitrião de hotel cinco estrelas. Ouça primeiro.'
OPENER = 'Vamos repassar cada linha deste café da manhã.'
TRANSITION = 'Agora ouça a cena inteira novamente sem pausas.'
OUTRO = 'Evelyn adorou o café da manhã, mesmo que a gravata do Arthur tenha bebido quase todo o suco de laranja. Logo mais o telefone da recepção trará novidades sobre a mala misteriosa. Até a próxima.'
CLOSING = ('evelyn', 'Take care!')
STORY = [
    ('hannah', 'Good morning again, Miss Evelyn! Would you like coffee or black tea?', 'Bom dia de novo, dona Evelyn! A senhora aceita café ou chá preto?'),
    ('evelyn', 'Black tea without sugar, please, and one slice of warm bread.', 'Chá preto sem açúcar, por favor, e uma fatia de pão quentinho.'),
    ('arthur', "Allow me to pour the fresh orange juice, ma'am!", 'Permita-me servir o suco de laranja fresco, senhora!'),
    ('evelyn', 'Oh, how kind of you, sir. Just half a glass.', 'Ah, que gentileza sua, senhor. Só meio copo.'),
    ('arthur', 'At our guesthouse, five-star service comes naturally... whoops!', 'Na nossa pousada, o serviço cinco estrelas vem naturalmente... opa!'),
    ('hannah', 'Careful, Arthur, the pitcher spout is wide!', 'Cuidado, Arthur, o bico da jarra é largo!'),
    ('arthur', 'Oh dear! Not a drop on the table, thank goodness... all of it is on my tie!', 'Ai, meu Deus! Nem uma gota na mesa, ainda bem... foi tudo na minha gravata!'),
    ('evelyn', 'Do not worry! Cold sparkling water takes orange juice right out.', 'Não se preocupe! Água com gás gelada tira suco de laranja na hora.'),
    ('hannah', 'Here is a clean cloth and cold water, Arthur.', 'Aqui estão um pano limpo e água fria, Arthur.'),
    ('arthur', "Excuse me, ma'am, I shall retreat to my office with dignity!", 'Com licença, senhora, vou me retirar para o meu escritório com dignidade!'),
    ('evelyn', 'Your scrambled eggs are delicious, Hannah. Tell Tessa my compliments!', 'Seus ovos mexidos estão deliciosos, Hannah. Dê meus parabéns à Tessa!'),
    ('hannah', 'I will! Enjoy your morning.', 'Pode deixar! Aproveite sua manhã.'),
]
WALK = [
    (0, None, ["'Bom dia de novo, dona Evelyn! A senhora aceita café ou chá preto?' Para oferecer bebida ou comida com educação, a pergunta ideal é", (None, 'Would you like'), 'gostaria ou aceita?']),
    (1, None, ["'Chá preto sem açúcar, por favor, e uma fatia de pão quentinho.' Como pão é incontável em inglês, pedimos a unidade dizendo", (None, 'one slice of warm bread'), 'uma fatia de pão.']),
    (2, None, ["'Permita-me servir o suco de laranja fresco, senhora!' Num registro bem cortês,", (None, 'Allow me to pour'), 'liga o pedido de permissão ao verbo servir líquidos.']),
    (3, None, ["'Ah, que gentileza sua, senhor. Só meio copo.' Agradecer com", (None, 'how kind of you'), 'soa super elegante, e note a ordem de', (None, 'half a glass'), 'meio copo, com o artigo no meio.']),
    (4, None, ["'Na nossa pousada, o serviço cinco estrelas vem naturalmente... opa!' Quando vira adjetivo antes do nome em", (None, 'five-star service'), 'estrela fica no singular, e', (None, 'whoops'), "é o nosso 'opa!' quando algo escapa."]),
    (5, None, ["'Cuidado, Arthur, o bico da jarra é largo!' Num aviso rápido, uma palavra só resolve tudo:", (None, 'Careful'), 'cuidado!']),
    (6, None, ["'Ai, meu Deus! Nem uma gota na mesa, ainda bem... foi tudo na minha gravata!' O alívio humorístico aparece em", (None, 'thank goodness'), 'ainda bem ou graças a Deus.']),
    (7, None, ["'Não se preocupe! Água com gás gelada tira suco de laranja na hora.' Água gaseificada é chamada de", (None, 'sparkling water'), 'e para remover uma mancha usamos', (None, 'takes orange juice right out'), 'tira na hora.']),
    (8, None, ["'Aqui estão um pano limpo e água fria, Arthur.' Um paninho de limpeza se diz simplesmente", (None, 'a clean cloth'), 'um pano limpo.']),
    (9, None, ["'Com licença, senhora, vou me retirar para o meu escritório com dignidade!' Arthur brinca com uma formalidade solene ao dizer", (None, 'I shall retreat'), 'vou me retirar.']),
    (10, None, ["'Seus ovos mexidos estão deliciosos, Hannah. Dê meus parabéns à Tessa!' Para mandar elogios a quem preparou o prato, usa-se o plural", (None, 'my compliments'), 'meus cumprimentos.']),
    (11, None, ["'Pode deixar! Aproveite sua manhã.' Nosso simpático 'pode deixar!' cabe inteirinho em", (None, 'I will'), 'prometendo transmitir o recado.']),
]
