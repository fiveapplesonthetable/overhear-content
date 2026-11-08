ID = 'pousada-do-cajueiro-s01e05-scene-02'
SHOW, SEASON, EPISODE, SCENE = 'pousada-do-cajueiro', 1, 5, 2
TITLE = 'Três anos de silêncio  (Three Years of Silence)'
LEVEL, PAIR = 'A1 — beginner', 'pt-en'
LABELS = {'jorge': 'Jorge', 'rafael': 'Rafael', 'camila': 'Camila'}

INTRO = ('Inside at the front desk, Jorge brings the dark-blue suitcase out of the closet for Rafael and Camila. It '
 'is Friday morning now, three hours before noon. Listen first.')
OPENER = "Let's listen again to the story behind the two brothers line by line."
TRANSITION = "Now let's hear the whole scene again from start to finish."
OUTRO = ('Instead of watching from across the street, Rafael has three hours to gather the courage to greet Tiago '
 'right here in the courtyard. See you next time.')
CLOSING = ('jorge', 'Até mais!')

STORY = [
    ('jorge', 'Então o misterioso homem de sexta estava dormindo no meu sótão o tempo todo.', 'So the mysterious Friday man was sleeping in my attic the whole time.'),
    ('rafael', 'Desculpe o trabalho, Jorge. Obrigado por guardar esta mala a semana inteira.', 'Sorry for the trouble, Jorge. Thank you for keeping this bag the whole week.'),
    ('camila', 'Por que você não entregou o trenzinho de madeira na porta da casa do Tiago?', "Why did you not hand the wooden train over at Tiago's front door?"),
    ('rafael', 'Três anos atrás, depois que nosso avô morreu, eu e o Tiago brigamos feio por causa da casa.', 'Three years ago, after our grandfather died, Tiago and I argued badly over the house.'),
    ('jorge', 'Casas de família e lembranças antigas... essas brigas machucam fundo.', 'Family houses and old memories... those fights hurt deep.'),
    ('rafael', 'Nós não nos falamos desde aquele dia. Na semana passada, mandei um cartão-postal curto para ele.', 'We have not spoken since that day. Last week I sent him one short postcard.'),
    ('camila', 'Pedindo para ele encontrar você aqui na sexta ao meio-dia?', 'Asking him to meet you here on Friday at noon?'),
    ('rafael', "Na verdade, só escrevi: 'Uma lembrança do vovô espera na Pousada do Cajueiro sexta ao meio-dia.'", "Actually, I only wrote: 'A keepsake from Grandpa awaits at the Cashew Tree Guesthouse Friday at noon.'"),
    ('jorge', 'Ah! Você teve medo de assinar o nome e o irmão teimoso ficar em casa!', 'Aha! You were afraid of signing your name and your stubborn brother staying home!'),
    ('rafael', 'O senhor conhece bem irmãos mais velhos, Jorge.', 'You know older brothers well, Jorge.'),
    ('camila', 'Espere, você ia deixar o balconista entregar a mala a ele e olhar do outro lado da rua?!', 'Wait—you were planning to let the clerk hand him the bag and watch from across the street?!'),
    ('rafael', 'Esse era o meu plano medroso de segunda-feira... antes de conhecer vocês.', 'That was my fearful Monday plan... before meeting all of you.'),
]

WALK = [
    (0, None, ["'So the mysterious Friday man was sleeping in my attic the whole time.' Handy time chunk ", (None, 'o tempo todo.'), " means 'all along' or 'the whole time'."]),
    (1, None, ["'Sorry for the trouble, Jorge. Thank you for keeping this bag the whole week.' Polite ", (None, 'Desculpe o trabalho,'), ' apologizes for putting someone to extra work.']),
    (3, None, ["'Three years ago, after our grandfather died, Tiago and I argued badly over the house.' Vivid ", (None, 'brigamos feio'), " literally says 'we fought ugly' for having a bitter falling-out."]),
    (4, None, ["'Family houses and old memories... those fights hurt deep.' Notice ", (None, 'lembranças'), ' meaning cherished memories—and in line eight it also means a physical keepsake!']),
    (5, None, ["'We have not spoken since that day. Last week I sent him one short postcard.' Time marker ", (None, 'desde'), " means 'since', paired with present-tense 'we do not speak to each other'."]),
    (7, None, ["'Actually, I only wrote: A keepsake from Grandpa awaits at the Cashew Tree Guesthouse Friday at noon.' Affectionate ", (None, 'do vovô'), " means 'from Grandpa', contrasting with formal 'grandfather' earlier."]),
    (8, None, ["'Aha! You were afraid of signing your name and your stubborn brother staying home!' Expressive ", (None, 'teimoso'), " means 'stubborn' or 'headstrong'."]),
    (10, None, ["'Wait—you were planning to let the clerk hand him the bag and watch from across the street?!' Saying ", (None, 'você ia deixar'), " literally 'you were going to leave', talks about an old plan that changed."]),
]
