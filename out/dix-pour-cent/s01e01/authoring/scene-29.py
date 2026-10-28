# Authoring module for dix-pour-cent-s01e01-scene-29.
ID = 'dix-pour-cent-s01e01-scene-29'
SHOW = 'dix-pour-cent'
SEASON = 1
EPISODE = 1
SCENE = 29
TITLE = 'Arlette et Jean Gabin  (Arlette and Jean Gabin)'
LEVEL = 'A1 — débutant'
PAIR = 'fr-en'
LABELS = {'arlette': 'Arlette', 'camille': 'Camille'}
SOURCE_NAME = 'Dix pour cent (Call My Agent!) S01E01'
SOURCE_FILE = 'sources/dix-pour-cent/s01/e01.fr.dual.srt'
INTRO = "Walking past an open door, Camille spots a little white dog with a contract in its mouth, in the office of Arlette, the oldest agent in Paris. We'll play the scene in French first. Don't worry if some of it slips past you. Let's listen to the scene in French first."
OPENER = "Let's walk through it. Camille rushes in and tries to rescue the paper from the dog's teeth."
TRANSITION = "Now let's listen to the entire dialogue once more."
OUTRO = "That was a lovely little meeting: one woman uses the casual 'you', the other the polite one, and you can now hear the difference. See you next time!"
CLOSING = ('arlette', 'Au revoir, ma petite!')
STORY = [
    ('camille', 'Non! Lâche le contrat!', 'No! Let go of the contract!', [(759, 'Non'), (760, 'Lâche le contrat')], ''),
    ('arlette', "Qu'est-ce que tu fais?", 'What are you doing?', [(761, "Qu'est-ce que tu fais")], ''),
    ('camille', 'Regarde, voilà ta maîtresse.', 'Look, here', [(762, 'Regarde, voilà ta maîtresse')], ''),
    ('camille', 'Je passais par là. Il jouait avec un contrat.', 'I was walking by. He was playing with a contract.', [(763, 'Je passais par là'), (764, 'il jouait avec un contrat')], ''),
    ('arlette', "J'en doute. Jean Gabin déteste les contrats.", 'I doubt it. Jean Gabin hates contracts.', [(765, "J'en doute. Jean Gabin déteste les contrats")], ''),
    ('arlette', "Il n'a jamais joué avec un contrat.", 'He has never played with a contract.', [(766, "il n'a jamais joué avec")], ''),
    ('arlette', "C'est Andréa qui t'envoie?", 'Did Andréa send you?', [(767, "Andréa t'a envoyé")], ''),
    ('camille', 'Non, pas du tout.', 'No, not at all.', [(767, 'Non, pas du tout')], ''),
    ('camille', 'Vous êtes Arlette Azémar?', 'Are you Arlette Azémar?', [(768, 'Vous êtes Arlette Azémar')], ''),
    ('arlette', 'Oui. Et toi?', 'Yes. And you?', [], ''),
    ('camille', "Moi, c'est Camille. Je pars aujourd'hui.", "I'm Camille. I'm leaving today.", [], ''),
    ('camille', 'On dit que vous êtes la plus grande imprésario de Paris.', 'People say you', [(769, 'la plus grande imprésario de Paris')], ''),
    ('arlette', 'Pas besoin de me flatter!', 'No need to flatter me!', [(770, 'Pas besoin de')], ''),
    ('camille', 'Vous avez dit imprésario.', 'You said impresario.', [(771, 'Vous avez dit')], ''),
    ('arlette', "C'est plus classe qu'agent.", 'It', [(771, "C'est plus classe qu")], ''),
    ('arlette', 'Allez, viens, Jean Gabin!', 'Come on, Jean Gabin!', [], ''),
]
WALK = [
    (0, None, "'No! Let go of the contract!' She's talking to a dog, so she uses the casual 'you' command. You'd never use the polite form with an animal. Then a voice behind her."),
    (1, None, "'What are you doing?' The opening chunk is a fixed way to start a 'what' question; just learn it as one block. Arlette uses the casual 'you' with Camille, a young stranger. Older people sometimes do that."),
    (2, None, "'Look, here's your owner.' Camille combines 'look' with 'owner' in a natural French turn of phrase."),
    (3, 'Je passais par là.', "'I was walking by.' Literally 'I was passing through there'. The ending of the verb tells you it was going on in the background, an ongoing past action."),
    (3, 'Il jouait avec un contrat.', "'He was playing with a contract.' Same background past tense, same ending sound. Arlette is not convinced."),
    (4, None, "'I doubt it. Jean Gabin hates contracts.' The dog is named after a famous French film star of the old days, which tells you a lot about Arlette."),
    (5, None, "'He has never played with a contract.' Here the negative pattern changes: instead of plain 'not', the second little word means 'never'. Then Arlette gets suspicious."),
    (6, None, "'Did Andréa send you?' Literally 'is it Andréa who sends you?'. Arlette thinks Camille might be spying for another agent."),
    (7, None, "'No, not at all.' A quick, firm denial. And now Camille realises who she's talking to."),
    (8, None, "'Are you Arlette Azémar?' Camille uses the polite or plural 'you' here with 'Azémar'. Then Arlette responds."),
    (9, None, "'Yes. And you?' And this time it's the casual 'you' again, the stressed form you use on its own."),
    (10, "Moi, c'est Camille.", "'I'm Camille.' Literally 'me, it's Camille'. It's the easiest, most natural way to introduce yourself."),
    (10, "Je pars aujourd'hui.", "'I'm leaving today.' She says it simply, without explaining that she's just been fired. Then she pays Arlette a compliment."),
    (11, None, "'People say you're the greatest impresario in Paris.' 'The greatest' is built with 'the most big'. The first little word means 'people' or 'one', a very common way to say 'they say'. Arlette waves it off."),
    (12, None, "'No need to flatter me!' Literally 'no need to'. It's short and dry, but secretly she enjoys it. Camille noticed one word."),
    (13, None, "'You said impresario.' The polite 'you' again, and the verb in the past with 'have' plus 'said'. Arlette explains her choice."),
    (14, None, "'It's classier than agent.' The word for 'more' plus an adjective gives you a comparison, and the little word after it means 'than'. Then she calls her dog."),
    (15, None, "'Come on, Jean Gabin!' The first word literally means 'go', but here it's just 'come on'. Then a casual command to the dog: 'come'. And now the whole scene again, without stopping. Let's listen to the whole scene once more without interruption."),
]
