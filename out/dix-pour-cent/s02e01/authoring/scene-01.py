# Authoring module for dix-pour-cent-s02e01-scene-01.
ID = 'dix-pour-cent-s02e01-scene-01'
SHOW = 'dix-pour-cent'
SEASON = 2
EPISODE = 1
SCENE = 1
TITLE = 'Interview télévisée de Virginie et Ramzy  (TV Interview of Virginie and Ramzy)'
LEVEL = 'A1 — débutant'
PAIR = 'fr-en'
LABELS = {'journaliste': 'Le journaliste', 'ramzy': 'Ramzy', 'virginie': 'Virginie'}
SOURCE_NAME = 'Dix pour cent (Call My Agent!) S02E01'
SOURCE_FILE = 'sources/dix-pour-cent/s02/e01.fr.dual.srt'
INTRO = "Season 2 of Dix pour cent opens with ASK in financial crisis: the agency desperately needs a new majority shareholder before its rivals swallow it up, while Gabriel's client Virginie Efira and her ex-boyfriend Ramzy Bedia are trapped together on a desert-island shoot. We begin in Mathias's office as he checks in with Noémie. Listen to the whole conversation in French first — don't worry about catching every word."
OPENER = "Let's examine how the couple answers questions during their television interview."
TRANSITION = "Now let's listen to the whole interview again at natural speed."
OUTRO = 'Virginie and Ramzy seem completely united on screen, but fame and intense schedules put heavy pressure on their relationship. See you next time!'
CLOSING = ('virginie', 'Bonne journée!')
STORY = [
    ('journaliste', 'Vous vivez ensemble depuis de nombreuses années.', 'You have lived together for many years.', [(2, 'vous vivez ensemble depuis de nombreuses années')], ''),
    ('journaliste', "Et c'est votre premier film ensemble!", 'And this is your first film together!', [(5, "c'est votre premier film ensemble.")], ''),
    ('journaliste', "Qu'est-ce qui vous a décidés à faire ce film?", 'What made you decide to make this film?', [(6, "Qu'est-ce qui vous a décidés à faire ce film ?")], ''),
    ('virginie', 'Avec nos plannings, on ne se voit jamais.', 'With our schedules, we never see each other.', [(8, 'avec nos plannings'), (8, 'on ne se voit jamais.')], ''),
    ('journaliste', 'Recevoir le même cachet était important pour vous?', 'Was receiving the same fee important to you?', [(11, 'recevoir le même cachet était important pour vous')], ''),
    ('ramzy', 'Pour moi, oui!', 'For me, yes!', [(12, 'Pour moi, oui !')], ''),
    ('virginie', "L'égalité des salaires est importante dans tous les métiers.", 'Equal pay is important in every profession.', [(13, "L'égalité des salaires est importante dans tous les métiers.")], ''),
    ('ramzy', 'Deux cachets égaux, sur le même compte.', 'Two equal fees, into the same account.', [(15, 'Deux cachets égaux, sur le même compte.')], ''),
    ('virginie', 'Tout le monde est content, même notre agent.', 'Everyone is happy, even our agent.', [(16, 'Tout le monde est content, même notre agent.')], ''),
    ('journaliste', 'Vous avez le même agent?', 'Do you have the same agent?', [(18, 'Vous avez le même agent ?')], ''),
    ('ramzy', 'On partage tout. Absolument tout.', 'We share everything. Absolutely everything.', [(19, 'On partage tout.'), (20, 'Absolument tout.')], ''),
    ('journaliste', 'Bonne chance pour le film! Vous êtes angoissés?', 'Good luck with the film! Are you anxious?', [(21, 'Bonne chance pour le film'), (22, 'Vous êtes angoissés ?')], ''),
    ('ramzy', 'Jamais, je suis un pro.', 'Never, I am a pro.', [(23, 'Jamais, je suis un pro.')], ''),
    ('virginie', 'Ça va aller. Merci beaucoup.', 'It will be fine. Thank you very much.', [(25, 'Ça va aller.'), (26, 'Merci beaucoup.')], ''),
]
WALK = [
    (0, None, "'You have lived together for many years.' The radio host notes that Virginie and Ramzy have been a couple for many years."),
    (1, None, "'And this is your first film together!' The journalist points out enthusiastically that this is their first movie together."),
    (2, None, "'What made you decide to make this film?' The interviewer asks what convinced the two of them to make this film together."),
    (3, None, "'With our schedules, we never see each other.' Virginie jokes that with their busy schedules, filming together is the only way they see each other."),
    (4, None, "'Was receiving the same fee important to you?' The journalist asks whether getting paid the exact same fee mattered to them."),
    (5, None, "'For me, yes!' Ramzy chimes in emphatically that equal pay mattered to him."),
    (6, None, "'Equal pay is important in every profession.' Virginie states proudly that equal pay is vital in every profession."),
    (7, None, "'Two equal fees, into the same account.' Ramzy jokes that both equal fees go straight into the same joint bank account."),
    (8, None, "'Everyone is happy, even our agent.' Virginie adds with a smile that everyone is happy, including their agent Mathias."),
    (9, None, "'Do you have the same agent?' The journalist checks a surprising professional arrangement."),
    (10, None, "'We share everything. Absolutely everything.' Ramzy boasts that they share everything, repeating the word for emphasis."),
    (11, None, "'Good luck with the film! Are you anxious?' The journalist offers polite good wishes before asking if they feel anxious."),
    (12, None, "'Never, I am a pro.' Ramzy boasts that he is never anxious because he is a pro."),
    (13, None, "'It will be fine. Thank you very much.' Virginie ends with gratitude."),
]
