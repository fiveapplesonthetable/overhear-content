# Authoring module for linden-courtyard-pt-s01e06-scene-07.
ID = 'linden-courtyard-pt-s01e06-scene-07'
SHOW = 'linden-courtyard-pt'
SEASON = 1
EPISODE = 6
SCENE = 7
TITLE = 'Under the Golden Lanterns  (Debaixo das lanternas douradas)'
LEVEL = 'A1 — iniciante'
PAIR = 'en-pt'
LABELS = {'hannah': 'Hannah', 'evelyn': 'Evelyn', 'owen': 'Owen'}
INTRO = 'O entardecer ameno desce sobre Portland, e fios de lanternas douradas de papel brilham acima da árvore do pátio. Hannah, a senhorita Evelyn e Owen tomam chá e lembram histórias de música. Ouça primeiro.'
OPENER = 'Agora vamos repassar cada fala desta noite especial.'
TRANSITION = 'Vamos escutar toda a cena novamente sem pausas.'
OUTRO = 'Lanternas douradas no alto, velhos amigos reunidos e o café do pátio pronto para abrir amanhã às oito! Resta apenas uma cena na primeira temporada, e Graham acabou de achar algo curioso no porão. Até já.'
CLOSING = ('evelyn', 'Good night!')
STORY = [
    ('evelyn', 'Look up at those golden lanterns against the evening sky. How peaceful!', 'Olhem lá para cima para aquelas lanternas douradas contra o céu do fim de tarde. Que paz!'),
    ('owen', 'To think on Monday morning Caleb picked up the wrong blue bag on Platform Two.', 'E pensar que na segunda de manhã o Caleb pegou a mala azul errada na Plataforma Dois.'),
    ('hannah', 'If he had picked up the right bag, none of us would be standing here tonight!', 'Se ele tivesse pegado a mala certa, nenhum de nós estaria aqui hoje à noite!'),
    ('evelyn', 'My teacup survived, two brothers made peace, and Hannah found a new home.', 'Minha xícara sobreviveu, dois irmãos fizeram as pazes e a Hannah encontrou um novo lar.'),
    ('owen', 'Miss Evelyn, Caleb and I booked a quiet dinner nearby. Will you join us tomorrow?', 'Senhorita Evelyn, o Caleb e eu reservamos um jantar tranquilo aqui perto. A senhora se junta a nós amanhã?'),
    ('evelyn', 'Gladly, Owen, as long as nobody talks about selling old pianos!', 'Com todo prazer, Owen, desde que ninguém fale em vender pianos antigos!'),
    ('hannah', 'And tomorrow morning at eight, your first courtyard coffees are on the house!', 'E amanhã cedo às oito, os primeiros cafés de vocês no pátio são por conta da casa!'),
    ('owen', "We will bring half of City Hall to Tessa's tables next week, I promise.", 'Na semana que vem traremos metade da Prefeitura para as mesas da Tessa, eu prometo.'),
    ('evelyn', 'Listen, even the buzzer from room four has been quiet all evening!', 'Escutem, até a campainha do quarto quatro ficou quieta a noite inteira!'),
    ('hannah', 'Do not tempt it, Miss Evelyn! I am almost fond of those two rings now.', 'Não provoque, senhorita Evelyn! Eu já estou quase afeiçoada àqueles dois toques agora.'),
    ('owen', 'Here is to the Linden Courtyard Inn, the loudest quiet place in Portland!', 'Um brinde à pousada Linden Courtyard Inn, o lugar silencioso mais animado de Portland!'),
    ('hannah', 'To good neighbors, warm bread, and open gates!', 'Aos bons vizinhos, ao pão quentinho e aos portões abertos!'),
]
WALK = [
    (0, None, ["'Olhem lá para cima para aquelas lanternas douradas contra o céu do fim de tarde. Que paz!' A preposição", (None, 'against the evening sky'), 'mostra o brilho destacando-se contra o fundo escuro do céu.']),
    (1, None, ["'E pensar que na segunda de manhã o Caleb pegou a mala azul errada na Plataforma Dois.' Começar com", (None, 'To think'), "equivale ao nosso 'e pensar que...', enquanto", (None, 'picked up'), 'é pegar do chão.']),
    (2, None, ["'Se ele tivesse pegado a mala certa, nenhum de nós estaria aqui hoje à noite!' Para imaginar um presente diferente, usamos", (None, 'none of us would be standing'), 'nenhum de nós estaria aqui.']),
    (3, None, ["'Minha xícara sobreviveu, dois irmãos fizeram as pazes e a Hannah encontrou um novo lar.' Fazer as pazes em inglês fica no singular e sem artigo:", (None, 'made peace'), 'fizeram as pazes.']),
    (4, None, ["'Senhorita Evelyn, o Caleb e eu reservamos um jantar tranquilo aqui perto. A senhora se junta a nós amanhã?' Para convidar alguém para jantar ou sair junto, use", (None, 'Will you join us'), 'você vem conosco?']),
    (5, None, ["'Com todo prazer, Owen, desde que ninguém fale em vender pianos antigos!' A locução", (None, 'as long as'), "traduz perfeitamente 'desde que' ou 'contanto que'."]),
    (6, None, ["'E amanhã cedo às oito, os primeiros cafés de vocês no pátio são por conta da casa!' Expressão clássica de restaurantes e cafés:", (None, 'on the house'), 'cortesia da casa.']),
    (7, None, ["'Na semana que vem traremos metade da Prefeitura para as mesas da Tessa, eu prometo.' Fechar a frase com", (None, 'I promise'), 'dá firmeza simpática à promessa.']),
    (8, None, ["'Escutem, até a campainha do quarto quatro ficou quieta a noite inteira!' O tempo perfeito", (None, 'has been quiet'), 'cobre toda a noite até agora.']),
    (9, None, ["'Não provoque, senhorita Evelyn! Eu já estou quase afeiçoada àqueles dois toques agora.' Ter carinho por algo ou alguém é sempre", (None, 'fond of'), 'apegada a.']),
    (10, None, ["'Um brinde à pousada Linden Courtyard Inn, o lugar silencioso mais animado de Portland!' Ao erguer uma xícara ou taça para brindar, diga", (None, 'Here is to'), 'um brinde a!']),
    (11, None, ["'Aos bons vizinhos, ao pão quentinho e aos portões abertos!' Para completar o brinde basta começar direto com 'to':", (None, 'To good neighbors'), 'aos bons vizinhos!']),
]
