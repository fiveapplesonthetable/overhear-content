# Authoring module for linden-courtyard-pt-s01e06-scene-05.
ID = 'linden-courtyard-pt-s01e06-scene-05'
SHOW = 'linden-courtyard-pt'
SEASON = 1
EPISODE = 6
SCENE = 5
TITLE = 'Page Two, Clause Fourteen  (Página dois, cláusula quatorze)'
LEVEL = 'A1 — iniciante'
PAIR = 'en-pt'
LABELS = {'arthur': 'Arthur', 'caleb': 'Caleb', 'hannah': 'Hannah'}
INTRO = 'Na recepção, Arthur entrega o aviso de duas páginas a Caleb enquanto Hannah prende a respiração ao lado do livro de reservas. Caleb vira imediatamente para a segunda folha. Ouça primeiro.'
OPENER = 'Vamos repassar cada linha desta reviravolta.'
TRANSITION = 'Agora ouça toda a cena novamente do começo ao fim.'
OUTRO = 'A página dois mudou tudo: abrir as quatro mesas do café da manhã para os moradores do bairro protege a pousada por mais dez anos! Na próxima cena, Arthur tem dois grandes anúncios para fazer.'
CLOSING = ('hannah', 'Take care!')
STORY = [
    ('arthur', "Look at page one, Caleb: 'commercial office conversion next month.' We are finished!", "Olhe a página um, Caleb: 'conversão em escritórios comerciais no mês que vem'. Estamos acabados!"),
    ('caleb', 'Wait a moment, sir. Did you read page two clipped underneath?', 'Espere um instante, senhor. O senhor leu a página dois presa por baixo?'),
    ('arthur', 'Only small gray numbers! My heart stopped at page one!', 'Só letrinhas cinzentas! Meu coração parou na página um!'),
    ('hannah', 'Look where Caleb is pointing with his pencil, Arthur!', 'Olhe onde o Caleb está apontando com o lápis, Arthur!'),
    ('caleb', 'Clause fourteen of the Portland Old Quarter Act, and my brother here just nodded!', 'Cláusula quatorze da Lei do Centro Antigo de Portland, e meu irmão aqui acabou de concordar!'),
    ('arthur', 'In plain words, please! What does Clause fourteen say?', 'Em português claro, por favor! O que diz a cláusula quatorze?'),
    ('caleb', 'No courtyard building over eighty years old may become private offices if the first floor serves neighbors daily.', 'Nenhum prédio com pátio de mais de oitenta anos pode virar escritórios privados se o térreo atender os vizinhos diariamente.'),
    ('hannah', "'Serves neighbors daily'... like a public morning cafe?!", "'Atender os vizinhos diariamente'... tipo um café matinal aberto ao público?!"),
    ('caleb', 'Exactly! Right now your four tables only serve overnight hotel guests.', 'Exatamente! Hoje suas quatro mesas só atendem hóspedes que dormem no hotel.'),
    ('arthur', 'Wait, if we open our courtyard gate every morning for neighborhood coffee and bread...', 'Espere, se abrirmos o portão do nosso pátio toda manhã para café e pão do bairro...'),
    ('caleb', 'Then your guesthouse lease is protected for another ten years by city law!', 'Então o contrato de aluguel da sua pousada fica protegido por mais dez anos pela lei municipal!'),
    ('hannah', 'Arthur! Your glasses just fell off your nose for a happy reason!', 'Arthur! Seus óculos acabaram de escorregar do nariz por um motivo feliz!'),
]
WALK = [
    (0, None, ["'Olhe a página um, Caleb: conversão em escritórios comerciais no mês que vem. Estamos acabados!' Em momentos de desespero cômico,", (None, 'We are finished'), "significa 'estamos perdidos ou acabados'."]),
    (1, None, ["'Espere um instante, senhor. O senhor leu a página dois presa por baixo?' Com páginas numeradas não vai artigo:", (None, 'read page two'), 'leu a página dois.']),
    (2, None, ["'Só letrinhas cinzentas! Meu coração parou na página um!' O exagero divertido", (None, 'My heart stopped'), 'mostra o susto de Arthur logo na primeira folha.']),
    (3, None, ["'Olhe onde o Caleb está apontando com o lápis, Arthur!' Dentro da frase, 'where' mantém a ordem direta:", (None, 'where Caleb is pointing'), 'onde Caleb está apontando.']),
    (4, None, ["'Cláusula quatorze da Lei do Centro Antigo de Portland, e meu irmão aqui acabou de concordar!' O verbo", (None, 'just nodded'), "diz numa palavra só 'concordar balançando a cabeça'."]),
    (5, None, ["'Em português claro, por favor! O que diz a cláusula quatorze?' Quando aparece linguagem jurídica difícil, peça simplicidade dizendo", (None, 'In plain words'), 'em palavras simples.']),
    (6, None, ["'Nenhum prédio com pátio de mais de oitenta anos pode virar escritórios privados se o térreo atender os vizinhos diariamente.' Em leis e regras formais,", (None, 'may become'), 'indica permissão legal.']),
    (7, None, ["'Atender os vizinhos diariamente... tipo um café matinal aberto ao público?!' Para dar exemplos rápidos, 'like' funciona igual a 'como' ou 'tipo':", (None, 'like a public morning cafe'), 'como um café público.']),
    (8, None, ["'Exatamente! Hoje suas quatro mesas só atendem hóspedes que dormem no hotel!' Como adjetivo antes do nome,", (None, 'overnight hotel guests'), 'indica hóspedes que pernoitam.']),
    (9, None, ["'Espere, se abrirmos o portão do nosso pátio toda manhã para café e pão do bairro...' Onde o português usa futuro do subjuntivo, o inglês usa presente simples:", (None, 'if we open'), 'se abrirmos.']),
    (10, None, ["'Então o contrato de aluguel da sua pousada fica protegido por mais dez anos pela lei municipal!' Mesmo com 'dez anos' no plural, usa-se 'another' pensando no período inteiro:", (None, 'another ten years'), 'mais dez anos.']),
    (11, None, ["'Arthur! Seus óculos acabaram de escorregar do nariz por um motivo feliz!' A combinação", (None, 'fell off your nose'), 'mostra algo que se solta e cai de onde estava apoiado.']),
]
