# Authoring module for dix-pour-cent-s01e02-scene-05.
ID = 'dix-pour-cent-s01e02-scene-05'
SHOW = 'dix-pour-cent'
SEASON = 1
EPISODE = 2
SCENE = 5
TITLE = 'Le châle vert  (The Green Shawl)'
LEVEL = 'A1 — débutant'
PAIR = 'fr-en'
LABELS = {'andrea': 'Andréa', 'camille': 'Camille'}
SOURCE_NAME = 'Dix pour cent (Call My Agent!) S01E02'
SOURCE_FILE = 'sources/dix-pour-cent/s01/e02.fr.dual.srt'
INTRO = "But at the office she's all business again, with twenty-four hours to win back Françoise Fabian. Then an old client of Andréa's, an actress called Rebecca Vialle whom nobody has hired for years, turns up without an appointment. Camille tries to help her, and finds out she has made a mistake of her own. First the scene in French; you don't need every word."
OPENER = "Let's go through it. Camille starts by talking to the actress waiting at her desk, very politely."
TRANSITION = "Now let's listen to the entire dialogue once more."
OUTRO = "Poor Camille: a kind heart for Rebecca, and a green shawl for Françoise. If you followed the polite 'you' between the two women, you're doing really well. See you next time!"
CLOSING = ('andrea', 'Bonne soirée!')
STORY = [
    ('camille', 'Je vais voir si elle peut vous recevoir.', 'I', [(200, 'Je vais voir si elle peut vous recevoir')], ''),
    ('camille', 'Andréa! Une de vos actrices est là, Rebecca Vialle.', 'Andréa! One of your actresses is here, Rebecca Vialle.', [(203, 'Andréa'), (204, 'Une de vos actrices est là, Rebecca Vialle')], ''),
    ('camille', 'Vous pouvez la voir?', 'Can you see her?', [(204, 'Vous pouvez la voir ?')], ''),
    ('andrea', 'Elle est là?', 'She', [(205, 'Elle est là ?')], ''),
    ('camille', 'Dans le couloir.', 'In the corridor.', [(205, 'Dans le couloir')], ''),
    ('andrea', "Est-ce que Rebecca Vialle est dans mon agenda aujourd'hui?", 'Is Rebecca Vialle in my diary today?', [(206, "Est-ce que Rebecca Vialle est dans mon agenda aujourd'hui ?")], ''),
    ('camille', "Mais c'est quand même une cliente.", 'But she', [(207, "Mais c'est quand même une cliente")], ''),
    ('andrea', "Elle n'a pas travaillé depuis deux ans.", 'She hasn', [(208, "Elle n'a pas travaillé depuis deux ans")], ''),
    ('camille', "Si on ne l'aide pas, elle ne trouvera pas de travail.", 'If we don', [(209, "Si on ne l'aide pas, elle ne trouvera pas de travail")], ''),
    ('camille', 'Elle a commencé à pleurer.', 'She', [(210, 'Elle a commencé à pleurer')], ''),
    ('andrea', 'Les actrices peuvent pleurer quand elles veulent.', 'Actresses can cry whenever they want.', [(211, 'Les actrices peuvent pleurer quand elles veulent')], ''),
    ('andrea', 'Vous avez eu le châle pour Françoise Fabian?', 'Did you get the shawl for Françoise Fabian?', [(212, 'Vous avez eu le châle'), (212, 'pour Françoise Fabian ?')], ''),
    ('camille', "Oui, c'est envoyé. Voici la facture.", 'Yes, it', [(213, "Oui, c'est envoyé. Voici la facture")], ''),
    ('andrea', 'Vous avez eu du vert?', 'You got green?', [(214, 'Vous avez eu du vert ?')], ''),
    ('camille', 'Oui, un très beau vert.', 'Yes, a very nice green.', [(214, 'Oui, un très beau vert')], ''),
    ('andrea', "On n'offre pas du vert à une actrice. Ça porte malheur.", 'You don', [(215, "On n'offre pas du vert à une actrice. Ça porte malheur")], ''),
    ('camille', 'Oh non!', 'Oh no!', [], ''),
]
WALK = [
    (0, None, "'I'll see if she can see you.' The first part is the near future: 'I'm going to see'. The polite 'you' at the end is for the actress, a stranger. Then Camille calls out to her boss."),
    (1, None, "'Andréa! One of your actresses is here, Rebecca Vialle.' Notice that Camille uses the polite 'you' with Andréa, and Andréa uses it back. That's our first point today: in this scene, both women stay formal. Then the question."),
    (2, None, "'Can you see her?' The little word for 'her' comes before the verb, not after it, as it always does in French. Andréa looks up."),
    (3, None, "'She's here?' No question word at all, just a rising voice. Camille answers in three words."),
    (4, None, "'In the corridor.' A useful word for any office. Andréa answers with a very pointed question."),
    (5, None, "'Is Rebecca Vialle in my diary today?' The two little words at the start simply turn a sentence into a yes-or-no question. Of course the answer is no. Camille stands up for the actress."),
    (6, None, "'But she's still a client.' The middle words mean 'all the same' or 'still'. Camille has a good heart. Andréa is less sentimental."),
    (7, None, "'She hasn't worked for two years.' Here's our second point, the negative with a past verb: the two little 'not' words go around the helper verb 'has', not around 'worked'. She adds that the actress is just a name on her list. Camille insists."),
    (8, None, "'If we don't help her, she won't find work.' Two negatives in one sentence, and the second one is in the future. Then Camille plays her last card."),
    (9, None, "'She's started crying.' Literally 'she has begun to cry'. Surely that will move Andréa?"),
    (10, None, "'Actresses can cry whenever they want.' Not at all. Andréa has seen too many tears in her job. And she changes the subject to something that worries her more."),
    (11, None, "'Did you get the shawl for Françoise Fabian?' It was a soft cashmere shawl, a present to win back the star. Camille is proud of herself."),
    (12, None, "'Yes, it's been sent. Here's the bill.' The last word is the invoice, the paper that shows what it cost. Then Andréa notices something."),
    (13, None, "'You got green?' Literally 'you had some green?'. Her voice already tells us something is wrong. Camille doesn't see it coming."),
    (14, None, "'Yes, a very nice green.' The word for 'nice' here is the one for beautiful, in its masculine form, because the colour word is masculine. And then the bad news."),
    (15, None, "'You don't give green to an actress. It brings bad luck.' In French theatre, green is said to bring bad luck on stage, an old superstition. The little word at the start means 'one' or 'people in general'. Camille realises what she's done."),
    (16, None, "'Oh no!' In the show she says something much ruder. Whatever the words, the shawl is already on its way to Françoise."),
]
