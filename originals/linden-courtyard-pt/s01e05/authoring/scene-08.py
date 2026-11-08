# Authoring module for linden-courtyard-pt-s01e05-scene-08.
ID = 'linden-courtyard-pt-s01e05-scene-08'
SHOW = 'linden-courtyard-pt'
SEASON = 1
EPISODE = 5
SCENE = 8
TITLE = 'The Red-Stamped Letter  (A carta de carimbo vermelho)'
LEVEL = 'A1 — iniciante'
PAIR = 'en-pt'
LABELS = {'arthur': 'Arthur', 'hannah': 'Hannah', 'tessa': 'Tessa'}
INTRO = 'Depois de abrir o portão para Owen e deixar os irmãos à vontade no pátio, Hannah volta silenciosamente para a recepção, onde Tessa observa sorrindo e Arthur abre o envelope registrado. Vamos ouvir.'
OPENER = 'Vamos passar por cada linha desta cena final do episódio cinco.'
TRANSITION = 'Ouça novamente toda a cena em velocidade natural.'
OUTRO = 'Lá fora debaixo da árvore dois irmãos finalmente se sentam juntos, enquanto lá dentro um aviso de venda comercial ameaça fechar toda a pousada em trinta dias! Episódio cinco concluído; esperamos você no final da temporada, no episódio seis.'
CLOSING = ('arthur', 'Bye for now!')
STORY = [
    ('tessa', 'Hannah, look through the glass. They are standing face to face under the tree!', 'Hannah, olhe pelo vidro. Eles estão parados frente a frente debaixo da árvore!'),
    ('hannah', 'Neither of them walked away! Caleb is pointing at the two chairs right now!', 'Nenhum dos dois foi embora! O Caleb está apontando para as duas cadeiras agora mesmo!'),
    ('arthur', 'Wonderful... let me just glance at this landlord letter while we wait.', 'Maravilha... deixe eu só passar os olhos nesta carta do proprietário enquanto esperamos.'),
    ('tessa', 'Probably a boring notice about painting the street shutters.', 'Provavelmente um aviso sem graça sobre pintar as venezianas da rua.'),
    ('arthur', 'Oh... oh no. Where is my chair? My knees feel weak.', 'Oh... ah, não. Onde está a minha cadeira? Meus joelhos estão bambos.'),
    ('hannah', 'Arthur! Your face went completely white! Sit down, what does the letter say?', 'Arthur! Seu rosto ficou completamente branco! Sente-se, o que diz a carta?'),
    ('arthur', 'Read the top line for me, Hannah. Tell me my glasses are playing tricks again!', 'Leia a primeira linha para mim, Hannah. Diga que meus óculos estão me pregando peças de novo!'),
    ('hannah', "'Notice of Property Transfer: Number Eight Courtyard Building offered for commercial office sale.'", "'Aviso de Transferência de Imóvel: Edifício do Pátio Número Oito colocado à venda para escritórios comerciais.'"),
    ('tessa', 'Commercial office sale?! Turn our guesthouse and kitchen into gray offices?!', 'Venda para escritórios comerciais?! Transformar nossa pousada e cozinha em escritórios cinzentos?!'),
    ('arthur', 'They give us thirty days before new buyers inspect the building!', 'Eles nos dão trinta dias antes que novos compradores vistoriem o prédio!'),
    ('hannah', 'Wait, there is a second folded page clipped to the back of this notice...', 'Esperem, tem uma segunda folha dobrada presa com um clipe atrás deste aviso...'),
    ('arthur', 'Not a word to anyone outside yet! Let the two brothers have their Friday afternoon first!', 'Nem uma palavra a ninguém lá fora ainda! Deixem os dois irmãos aproveitarem a tarde de sexta-feira primeiro!'),
]
WALK = [
    (0, None, ["'Hannah, olhe pelo vidro. Eles estão parados frente a frente debaixo da árvore!' Fácil de guardar,", (None, 'face to face'), "corresponde palavra por palavra ao nosso 'cara a cara'."]),
    (1, None, ["'Nenhum dos dois foi embora! O Caleb está apontando para as duas cadeiras agora mesmo!' Antes de um pronome usamos 'of':", (None, 'Neither of them'), 'nenhum deles, mantendo o verbo na afirmativa.']),
    (2, None, ["'Maravilha... deixe eu só passar os olhos nesta carta do proprietário enquanto esperamos.' O verbo", (None, 'glance at'), 'significa dar uma olhada rápida.']),
    (3, None, ["'Provavelmente um aviso sem graça sobre pintar as venezianas da rua.' Depois da preposição 'about', o verbo entra com '-ing':", (None, 'about painting'), 'sobre pintar.']),
    (4, None, ["'Oh... ah, não. Onde está a minha cadeira? Meus joelhos estão bambos.' Em", (None, 'My knees feel weak'), 'o inglês descreve na hora o susto que faz as pernas fraquejarem.']),
    (5, None, ["'Arthur! Seu rosto ficou completamente branco! Sente-se, o que diz a carta?' Para mudanças súbitas de cor, usa-se o passado de 'go':", (None, 'went completely white'), 'ficou branquinho de susto.']),
    (6, None, ["'Leia a primeira linha para mim, Hannah. Diga que meus óculos estão me pregando peças de novo!' A expressão", (None, 'playing tricks'), "equivale certinho a 'pregando peças'."]),
    (7, None, ["'Aviso de Transferência de Imóvel: Edifício do Pátio Número Oito colocado à venda para escritórios comerciais.' No vocabulário de imóveis,", (None, 'for commercial office sale'), 'indica venda para uso empresarial.']),
    (8, None, ["'Venda para escritórios comerciais?! Transformar nossa pousada e cozinha em escritórios cinzentos?!' Para transformar algo numa coisa totalmente diferente usa-se", (None, 'Turn our guesthouse and kitchen into'), 'transformar em.']),
    (9, None, ["'Eles nos dão trinta dias antes que novos compradores vistoriem o prédio!' Depois de 'before' falando de algo futuro, basta o presente simples:", (None, 'before new buyers inspect'), 'antes que vistoriem.']),
    (10, None, ["'Esperem, tem uma segunda folha dobrada presa com um clipe atrás deste aviso...' A palavra para clipe vira verbo em", (None, 'clipped to the back'), 'presa com clipe na parte de trás.']),
    (11, None, ["'Nem uma palavra a ninguém lá fora ainda! Deixem os dois irmãos aproveitarem a tarde de sexta-feira primeiro!' A frase curta", (None, 'Not a word to anyone'), 'pede segredo absoluto por enquanto.']),
]
