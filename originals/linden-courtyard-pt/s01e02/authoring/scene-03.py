# Authoring module for linden-courtyard-pt-s01e02-scene-03.
ID = 'linden-courtyard-pt-s01e02-scene-03'
SHOW = 'linden-courtyard-pt'
SEASON = 1
EPISODE = 2
SCENE = 3
TITLE = 'Counting the Change  (Contando o troco)'
LEVEL = 'A1 — iniciante'
PAIR = 'en-pt'
LABELS = {'hannah': 'Hannah', 'arthur': 'Arthur', 'tessa': 'Tessa'}
INTRO = 'Nove minutos depois, Hannah entra esbaforida pelo portão do pátio carregando duas sacolas de pano cheias de compras para Tessa e Arthur. Ouça a cena primeiro.'
OPENER = 'Agora vamos examinar cada frase com calma.'
TRANSITION = 'Vamos ouvir novamente a cena inteira sem paradas.'
OUTRO = 'Um tablete de manteiga com sal quase virou crise com a geleia, até Tessa transformá-lo no toque especial dos ovos mexidos. Até a próxima.'
CLOSING = ('tessa', 'Bye for now!')
STORY = [
    ('hannah', 'Nine minutes! Here are the milk, the eggs, and the apples!', 'Nove minutos! Aqui estão o leite, os ovos e as maçãs!'),
    ('tessa', 'You are a hero, Hannah! Give me the milk first for the coffee machine.', 'Você é uma heroína, Hannah! Me dê o leite primeiro para a máquina de café.'),
    ('arthur', 'Impressive speed! Did the shopkeeper give you a receipt?', 'Velocidade impressionante! O dono da loja te deu o recibo?'),
    ('hannah', 'Right here! Everything cost thirty-eight, so here is twelve in change.', 'Bem aqui! Tudo custou trinta e oito, então aqui estão doze de troco.'),
    ('arthur', 'Ten, eleven, twelve. Exact to the last coin, thank you!', 'Dez, onze, doze. Exato até a última moeda, obrigado!'),
    ('tessa', 'Wait a second, Hannah... which pack of butter did you grab?', 'Espere um segundo, Hannah... qual pacote de manteiga você pegou?'),
    ('hannah', 'The gold wrapper on the top shelf. Why?', 'O da embalagem dourada na prateleira de cima. Por quê?'),
    ('tessa', 'That is extra salty sea butter! My sweet jam rolls need plain butter!', 'Essa é manteiga marinha extrassalgada! Meus pãezinhos doces de geleia precisam de manteiga sem sal!'),
    ('hannah', 'Oh no! All the wrappers looked the same when I was running!', 'Ah não! Todas as embalagens pareciam iguais enquanto eu estava correndo!'),
    ('arthur', 'Can we serve salty butter with sweet strawberry jam?', 'Podemos servir manteiga salgada com geleia doce de morango?'),
    ('tessa', 'Wait, salty butter is terrible for jam, but amazing for scrambled eggs!', 'Espere, manteiga salgada é péssima para geleia, mas incrível para ovos mexidos!'),
    ('hannah', 'Phew! Quick thinking saves breakfast again.', 'Ufa! Raciocínio rápido salva o café da manhã de novo.'),
]
WALK = [
    (0, None, ["'Nove minutos! Aqui estão o leite, os ovos e as maçãs!' Como ela entrega vários itens de uma vez, a apresentação vai para o plural:", (None, 'Here are'), 'aqui estão.']),
    (1, None, ["'Você é uma heroína, Hannah! Me dê o leite primeiro para a máquina de café.' No inglês moderno,", (None, 'a hero'), 'é usado no dia a dia tanto para homens quanto para mulheres.']),
    (2, None, ["'Velocidade impressionante! O dono da loja te deu o recibo?' Repare na ordem sem preposição em", (None, 'give you a receipt'), 'em que a pessoa que recebe vem logo depois do verbo.']),
    (3, None, ["'Bem aqui! Tudo custou trinta e oito, então aqui estão doze de troco.' O verbo", (None, 'cost'), 'não muda nada no passado, e troco devolvido na compra se diz', (None, 'in change'), 'de troco.']),
    (4, None, ["'Dez, onze, doze. Exato até a última moeda, obrigado!' Para elogiar uma conta certinha nos centavos, use", (None, 'to the last coin'), 'até a última moeda.']),
    (5, None, ["'Espere um segundo, Hannah... qual pacote de manteiga você pegou?' Quando a escolha é entre embalagens diferentes na prateleira, a pergunta usa", (None, 'which pack'), 'qual pacote.']),
    (6, None, ["'O da embalagem dourada na prateleira de cima. Por quê?' Em superfícies e prateleiras usamos sempre a preposição de contato:", (None, 'on the top shelf'), 'na prateleira superior.']),
    (7, None, ["'Essa é manteiga marinha extrassalgada! Meus pãezinhos doces de geleia precisam de manteiga sem sal!' Em culinária, um ingrediente puro e sem tempero extra é chamado de", (None, 'plain butter'), 'manteiga comum sem sal.']),
    (8, None, ["'Ah não! Todas as embalagens pareciam iguais enquanto eu estava correndo!' Para dizer que tudo parecia igual, o artigo definido é obrigatório em", (None, 'looked the same'), 'pareciam a mesma coisa.']),
    (9, None, ["'Podemos servir manteiga salgada com geleia doce de morango?' Com verbos modais, perguntar é só inverter a ordem em", (None, 'Can we serve'), 'podemos servir?']),
    (10, None, ["'Espere, manteiga salgada é péssima para geleia, mas incrível para ovos mexidos!' O clássico prato matinal de", (None, 'scrambled eggs'), 'vem do verbo misturar e mexer na frigideira.']),
    (11, None, ["'Ufa! Raciocínio rápido salva o café da manhã de novo.' O suspiro de alívio se escreve", (None, 'Phew'), 'e', (None, 'Quick thinking'), "traduz perfeitamente 'raciocínio rápido'."]),
]
