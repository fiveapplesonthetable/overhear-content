# Authoring module for linden-courtyard-pt-s01e01-scene-08.
ID = 'linden-courtyard-pt-s01e01-scene-08'
SHOW = 'linden-courtyard-pt'
SEASON = 1
EPISODE = 1
SCENE = 8
TITLE = 'Left on the Step  (Deixada no degrau)'
LEVEL = 'A1 — iniciante'
PAIR = 'en-pt'
LABELS = {'hannah': 'Hannah', 'graham': 'Graham'}
INTRO = 'Já são quase nove da noite, e as lanternas do pátio brilham suavemente enquanto Hannah encerra seu primeiro dia com Graham. De repente, o sino do portão toca uma vez na noite silenciosa. Ouça primeiro.'
OPENER = 'Vamos repassar juntos cada fala deste final de episódio.'
TRANSITION = 'Agora ouça a cena completa mais uma vez.'
OUTRO = 'A mala da dona Evelyn voltou, mas o desconhecido sumiu na noite pedindo que guardem a mala dele até sexta-feira. Fim do episódio um — esperamos você no episódio dois!'
CLOSING = ('graham', 'Have a good night!')
STORY = [
    ('hannah', 'Did you hear that, Graham? Someone just rang the gate bell!', 'Você ouviu isso, Graham? Alguém acabou de tocar o sino do portão!'),
    ('graham', "At nine o'clock? Stay here, let us open the door together.", 'Às nove em ponto? Fique aqui, vamos abrir a porta juntos.'),
    ('hannah', 'Hello? Good evening! Nobody is standing in the courtyard!', 'Alô? Boa noite! Não tem ninguém parado no pátio!'),
    ('graham', 'Wait. Look down on the stone step.', 'Espere. Olhe para baixo, no degrau de pedra.'),
    ('hannah', "Another dark blue suitcase! Is this Miss Evelyn's bag?", 'Outra mala azul-escura! Esta é a mala da dona Evelyn?'),
    ('graham', 'Check the zipper... yes, her initials are right here!', 'Confira o zíper... sim, as iniciais dela estão bem aqui!'),
    ('hannah', 'Why did the person run away without taking his own suitcase back?', 'Por que a pessoa saiu correndo sem levar a própria mala de volta?'),
    ('graham', 'Look, there is a folded white envelope taped to the handle.', 'Olhe, tem um envelope branco dobrado colado com fita na alça.'),
    ('hannah', "Let me read it: 'Sorry for the mistake. Please keep my blue bag until Friday.'", 'Deixe-me ler: "Desculpe pelo engano. Por favor, guardem minha mala azul até sexta-feira."'),
    ('graham', 'Until Friday? No name, no signature!', 'Até sexta-feira? Sem nome, sem assinatura!'),
    ('hannah', 'Why leave your own shoes and wooden train with strangers until Friday?', 'Por que deixar seus próprios sapatos e um trem de madeira com estranhos até sexta-feira?'),
    ('graham', 'Welcome to the Linden Courtyard Inn, Hannah. Your second day will not be boring.', 'Bem-vinda à Linden Courtyard Inn, Hannah. Seu segundo dia não vai ser entediante.'),
]
WALK = [
    (0, None, ["'Você ouviu isso, Graham? Alguém acabou de tocar o sino do portão!' Veja como a pergunta no passado começa limpa com", (None, 'Did you hear that'), 'deixando o verbo ouvir sem alteração.']),
    (1, None, ["'Às nove em ponto? Fique aqui, vamos abrir a porta juntos.' Para horas redondas no relógio usamos", (None, "nine o'clock"), "exatamente como 'nove em ponto'."]),
    (2, None, ["'Alô? Boa noite! Não tem ninguém parado no pátio!' Lembre desta diferença essencial: ao chegar ou atender alguém à noite dizemos", (None, 'Good evening'), 'enquanto a despedida na hora de dormir é outra.']),
    (3, None, ["'Espere. Olhe para baixo, no degrau de pedra.' Juntar o verbo olhar com a direção em", (None, 'Look down'), 'orienta o olhar na mesma hora para o chão.']),
    (4, None, ["'Outra mala azul-escura! Esta é a mala da dona Evelyn?' Para dizer 'mais uma' no singular, o inglês junta artigo e adjetivo numa palavra só:", (None, 'Another'), 'outra mala.']),
    (5, None, ["'Confira o zíper... sim, as iniciais dela estão bem aqui!' Em inglês o possessivo concorda com quem possui, não com a coisa possuída; por isso 'as iniciais dela' fica", (None, 'her initials'), 'sem marca de plural no possessivo.']),
    (6, None, ["'Por que a pessoa saiu correndo sem levar a própria mala de volta?' Depois de preposições como 'sem', o verbo ganha terminação contínua em", (None, 'without taking'), 'sem levar.']),
    (7, None, ["'Olhe, tem um envelope branco dobrado colado com fita na alça.' Da palavra para fita adesiva surge direto o adjetivo verbal", (None, 'taped'), 'preso com fita.']),
    (8, None, ['\'Deixe-me ler: "Desculpe pelo engano. Por favor, guardem minha mala azul até sexta-feira."\' Para pedir desculpas por um motivo específico, ligamos tudo com', (None, 'Sorry for the mistake'), 'desculpe pelo erro.']),
    (9, None, ["'Até sexta-feira? Sem nome, sem assinatura!' Dias da semana como", (None, 'Friday'), 'são sempre escritos com letra maiúscula em inglês, precedidos aqui por', (None, 'until'), 'até.']),
    (10, None, ["'Por que deixar seus próprios sapatos e um trem de madeira com estranhos até sexta-feira?' A palavra", (None, 'strangers'), 'significa pessoas desconhecidas, e não estrangeiros de outro país.']),
    (11, None, ["'Bem-vinda à Linden Courtyard Inn, Hannah. Seu segundo dia não vai ser entediante.' Na previsão negativa do futuro,", (None, 'will not be boring'), 'mostra que a rotina ali nunca dá tédio.']),
]
