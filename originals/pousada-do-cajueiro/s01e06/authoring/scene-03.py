ID = 'pousada-do-cajueiro-s01e06-scene-03'
SHOW, SEASON, EPISODE, SCENE = 'pousada-do-cajueiro', 1, 6, 3
TITLE = 'Trinta dias no papel  (Thirty Days on Paper)'
LEVEL, PAIR = 'A1 — beginner', 'pt-en'
LABELS = {'otavio': 'Otávio', 'jorge': 'Jorge', 'camila': 'Camila'}

INTRO = ('Back behind the front desk, Otavio sits slumped beside the wooden key board while Jorge and Camila lean '
 'over the counter speaking quietly. Listen first.')
OPENER = "Let's replay their huddle behind the desk line by line."
TRANSITION = "Now let's listen to the whole desk conversation again."
OUTRO = ('Camila remembered they have an expert on historic Recife courtyard buildings sitting ten metres away! Next '
 'time, Bianca serves the lemon cake and Tiago senses trouble inside. See you next time.')
CLOSING = ('jorge', 'Até logo!')

STORY = [
    ('otavio', 'Quinze anos lustrando chaves de latão e arrumando gravatas... acabados em trinta dias!', 'Fifteen years polishing brass keys and straightening ties... finished in thirty days!'),
    ('jorge', 'Pare de fechar a pousada antes de ler o documento inteiro, chefe.', 'Stop closing the guesthouse before reading the whole document, boss.'),
    ('camila', 'Isso mesmo! Mais cedo eu vi uma segunda página presa atrás da carta.', "That's right! Earlier I saw a second page clipped behind the letter."),
    ('otavio', 'Parágrafos de advogado me dão dor de cabeça até com dois óculos!', 'Lawyer paragraphs give me a headache even with two pairs of glasses!'),
    ('jorge', 'Esta casa aguentou oitenta anos de chuva e uma válvula quebrada ontem.', 'This house endured eighty years of rain and a broken valve yesterday.'),
    ('camila', 'Esperem, quem está sentado a dez metros daqui no nosso pátio agora?', 'Wait, who is sitting ten metres from here in our courtyard right now?'),
    ('otavio', 'Dois irmãos comendo bolo de limão?', 'Two brothers eating lemon cake?'),
    ('camila', 'Um arquiteto que trabalha com prédios históricos de pátio pelo Recife inteiro!', 'An architect who works with historic courtyard buildings across all of Recife!'),
    ('jorge', 'Bem pensado, Camila. O Rafael lê leis da prefeitura toda semana.', 'Well thought, Camila. Rafael reads city-hall laws every week.'),
    ('otavio', 'Ah, eu jamais incomodaria um hóspede pagante com os nossos problemas!', 'Oh, I would never bother a paying guest with our troubles!'),
    ('camila', 'Depois de guardarmos a mala azul dele a semana toda? Ele vai querer ajudar!', 'After we kept his blue suitcase all week? He will want to help!'),
    ('jorge', 'Olhem, a Bianca está levando o bolo para a mesa deles agora mesmo.', 'Wait—Bianca is taking the cake out to their table right now.'),
]

WALK = [
    (1, None, ["'Stop closing the guesthouse before reading the whole document, boss.' Blunt ", (None, 'Pare de fechar'), " in Portuguese puts 'of' right after 'stop' before the next action."]),
    (2, None, ["'That's right! Earlier I saw a second page clipped behind the letter.' Useful time pointer ", (None, 'Mais cedo'), " literally 'more early', means 'earlier today'."]),
    (3, None, ["'Lawyer paragraphs give me a headache even with two pairs of glasses!' Everyday ", (None, 'dor de cabeça'), " literally says 'pain of head' for both a real headache and a bureaucratic hassle."]),
    (4, None, ["'This house endured eighty years of rain and a broken valve yesterday.' Tough ", (None, 'aguentou'), " means 'endured', 'held up against', or 'put up with'."]),
    (8, None, ["'Well thought, Camila. Rafael reads city-hall laws every week.' Crisp praise ", (None, 'Bem pensado,'), " means 'good thinking!' or 'smart move!', and ", (None, 'prefeitura'), ' is City Hall.']),
    (9, None, ["'Oh, I would never bother a paying guest with our troubles!' Stronger than everyday 'never', ", (None, 'jamais'), " means 'never ever!'."]),
    (10, None, ["'After we kept his blue suitcase all week? He will want to help!' Putting together ", (None, 'vai querer ajudar!'), " is a handy three-word chain that means 'is going to want to help!'."]),
    (11, None, ["'Wait—Bianca is taking the cake out to their table right now.' To say someone is taking something away from the speaker, Portuguese uses ", (None, 'está levando'), " literally 'is taking'."]),
]
