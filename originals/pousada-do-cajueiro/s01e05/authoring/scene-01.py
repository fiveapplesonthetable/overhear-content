ID = 'pousada-do-cajueiro-s01e05-scene-01'
SHOW, SEASON, EPISODE, SCENE = 'pousada-do-cajueiro', 1, 5, 1
TITLE = 'A verdade no pátio  (Truth in the Courtyard)'
LEVEL, PAIR = 'A1 — beginner', 'pt-en'
LABELS = {'helena': 'Helena', 'rafael': 'Rafael', 'camila': 'Camila'}

INTRO = 'Lá fora, sob a árvore do pátio na Pousada do Cajueiro no Recife, Rafael senta-se com Camila e Helena para explicar o mistério de segunda-feira desde o início. Ouça primeiro a cena inteira.'
OPENER = "Let's walk through Rafael's confession one line at a time."
TRANSITION = "Now let's listen to the whole courtyard conversation again."
OUTRO = ('All the puzzle pieces from Monday and Tuesday finally fit together! Next time, Rafael explains why he has '
 'not spoken to his older brother Tiago in three years. See you next time.')
CLOSING = ('camila', 'Até logo!')

STORY = [
    ('helena', 'Deixe eu olhar bem para você, Rafael! Cresceu mais que o piano!', 'Let me look properly at you, Rafael! You grew taller than the piano!'),
    ('rafael', 'Nem acredito que a senhora está hospedada na mesma pousada, Dona Helena.', 'I cannot believe you are staying at the exact same guesthouse, Madam Helena.'),
    ('camila', 'Espere, então você pegou o mesmo ônibus na segunda-feira e levou a mala dela?', 'Wait—so you rode the same train on Monday and took her suitcase?'),
    ('rafael', 'Por puro acidente! Na casa do meu primo eu abri a mala e vi partituras e uma fita vermelha.', "By pure accident! At my cousin's house I opened the bag and saw sheet music and a red ribbon."),
    ('helena', 'Por que você deixou a minha mala no degrau à noite e saiu correndo?', 'Why did you leave my suitcase on the step at night and run off?'),
    ('rafael', 'Porque na segunda à noite, chegando aqui, vi meu irmão mais velho descendo esta rua!', 'Because on Monday night, arriving here, I saw my older brother walking down this street!'),
    ('camila', 'O seu irmão mais velho mora aqui no Recife?', 'Does your older brother live here in Recife?'),
    ('rafael', 'Sim. Fiquei nervoso, toquei o sino e prendi o bilhete de sexta-feira na alça.', 'Yes. I panicked, rang the bell, and attached the Friday note to the handle.'),
    ('helena', 'Espere, e na quarta à noite você fez reserva aqui com o seu nome verdadeiro?', 'Wait, and on Wednesday night you booked here under your real name?'),
    ('rafael', 'Eu precisava de um lugar calmo aqui perto antes de sexta, e sinceramente fiquei com vergonha de pedir a mala!', 'I needed a quiet place nearby before Friday, and honestly felt too shy to ask for my bag!'),
    ('camila', 'Mesmo depois de você ligar na terça sobre o pacote branco!', 'Even after you called us on Tuesday about the white parcel!'),
    ('rafael', 'Tudo dentro daquele papel branco pertence ao meu irmão Tiago, não a mim.', 'Everything inside that white paper belongs to my brother Tiago, not to me.'),
]

WALK = [
    (1, None, ["'I cannot believe you are staying at the exact same guesthouse, Madam Helena.' Exclaiming ", (None, 'Nem acredito'), " literally says 'I don't even believe', a natural way to express amazement, and ", (None, 'hospedada'), " means 'staying as a guest'."]),
    (3, None, ["'By pure accident! At my cousin's house I opened the bag and saw sheet music and a red ribbon.' Clear ", (None, 'Por puro acidente!'), " means 'by pure accident!'."]),
    (4, None, ["'Why did you leave my suitcase on the step at night and run off?' Pairing ", (None, 'saiu correndo?'), " literally says 'exited running' for 'ran away'."]),
    (7, None, ["'Yes. I panicked, rang the bell, and attached the Friday note to the handle.' Everyday ", (None, 'Fiquei nervoso,'), " uses 'became nervous' where English might say 'I panicked'."]),
    (8, None, ["'Wait, and on Wednesday night you booked here under your real name?' Hotel bookings use ", (None, 'fez reserva'), " literally 'made a reservation'."]),
    (9, None, ["'I needed a quiet place nearby before Friday, and honestly felt too shy to ask for my bag!' To admit shyness, ", (None, 'fiquei com vergonha'), " is literally 'stayed with shame', commonly used for 'felt too shy'."]),
    (11, None, ["'Everything inside that white paper belongs to my brother Tiago, not to me.' Notice ", (None, 'a mim.'), " at the end—after a word like 'to' or 'for', 'I' changes to its object form meaning 'me'."]),
    (0, None, ["'Let me look properly at you, Rafael! You grew taller than the piano!' Warm ", (None, 'Cresceu'), " means 'you grew up!'."]),
]
