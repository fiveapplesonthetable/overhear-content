# Authoring module for domashniy-arest-s01e10-scene-41.
ID = 'domashniy-arest-s01e10-scene-41'
SHOW = 'domashniy-arest'
SEASON = 1
EPISODE = 10
SCENE = 41
TITLE = 'Разбор полётов  (Debriefing)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'chief': 'Михаил Михайлович', 'lavrov': 'Лавров', 'lyova': 'Лёва'}
SOURCE_NAME = 'Домашний арест (Domashniy Arest) S1.10'
SOURCE_FILE = 'sources/domashniy-arest/s01/e10.ru.dual.srt'
INTRO = "Following the chaotic rescue of agent Sokolov, senior security official Uncle Misha storms in to demand answers from Major Lavrov and his surveillance crew. Sensing disaster for his colleagues, Sokolov steps forward to confess his own reckless mistake. Let's listen to the confrontation in Russian first; don't worry if you don't catch every word right away."
OPENER = "Now let's walk through the tense military debriefing line by line."
TRANSITION = "Now let's listen to the entire dialogue once again from start to finish."
OUTRO = 'Uncle Misha reprimands Lavrov and Sokolov for their sloppy handling of the hostage situation, demanding a full formal report from the undercover operative. See you next time!'
CLOSING = ('chief', 'Пока!')
STORY = [
    ('chief', 'Что здесь произошло? Отвечайте немедленно!', 'What happened here? Answer immediately!', [(1194, 'Это что такое?'), (1195, 'я вас спрашиваю?')], ''),
    ('lavrov', 'Всё нормально, дорогой дядя Миша.', 'Everything is fine, dear Uncle Misha.', [(1198, 'все нормально'), (1199, 'дядь Миша')], ''),
    ('lavrov', 'Наш агент был в бронежилете.', 'Our agent was wearing body armor.', [(1196, 'Он же в бронике')], ''),
    ('chief', 'Почему вы отпустили его одного?', 'Why did you let him go alone?', [(1200, 'Вы почему его одного'), (1201, 'отпустили?')], ''),
    ('chief', 'Вы просто сидели в своём фургоне!', 'You were just sitting in your van!', [(1201, 'Сидели там в своем'), (1202, 'фургончики')], ''),
    ('chief', 'Я сейчас доложу об этом генералу!', 'I will report about this to the general now!', [(1203, 'Я проинформирую генерал')], ''),
    ('lyova', 'Дядя Миша, я сам во всём виноват.', 'Uncle Misha, I am to blame for everything myself.', [(1203, 'Дядь Миш'), (1204, 'я сам виноват')], ''),
    ('lyova', 'Я должен был сразу позвонить им.', 'I should have called them right away.', [(1204, 'Я должен был'), (1205, 'им позвонить')], ''),
    ('lyova', 'Но я не стал звонить.', "But I didn't call.", [(1205, 'но не стал')], ''),
    ('lyova', 'Я сильно недооценил реальную опасность.', 'I severely underestimated the real danger.', [(1206, 'Недооценив в опасность')], ''),
    ('lyova', 'Я совершил очень глупый поступок.', 'I committed a very foolish act.', [(1207, 'Совершил необдуманный поступок')], ''),
    ('chief', 'Ты поступил крайне легкомысленно, Соколов.', 'You acted extremely recklessly, Sokolov.', [], ''),
    ('lyova', 'Я обещаю, такое больше не повторится.', 'I promise this will not happen again.', [(1194, 'такое')], ''),
]
WALK = [
    (0, None, "'What happened here? Answer immediately!' Storming onto the scene after the botched stakeout, the senior boss demands answers."),
    (1, None, "'Everything is fine, dear Uncle Misha.' Calling his superior \"Uncle Misha\", Lavrov tries to smooth things over using family ties."),
    (2, None, "'Our agent was wearing body armor.' Pointing out the bulletproof vest is a weak excuse for letting Sokolov get kidnapped."),
    (3, None, "'Why did you let him go alone?' The boss goes straight to the real blunder: leaving one man out on the street with zero backup."),
    (4, None, "'You were just sitting in your van!' While their partner was being hauled away by crooks, Tolya was relaxing inside the truck."),
    (5, None, "'I will report about this to the general now!' Bringing the general into it means Lavrov's career is on the line."),
    (6, None, "'Uncle Misha, I am to blame for everything myself.' Remembering their heartfelt talk in the van, Lyova steps up to take the fall for his partner."),
    (7, None, "'I should have called them right away.' He claims he broke protocol by rushing in without calling the van first."),
    (8, None, "'But I didn't call.' Saying \"ne stal\" means \"I decided not to\" or \"I didn't bother to\", taking the blame squarely on himself."),
    (9, None, "'I severely underestimated the real danger.' Sounding like an official report, Sokolov recites his own fault to shield Tolya."),
    (10, None, "'I committed a very foolish act.' For all his clumsiness in the field, Lyova proves he is a loyal friend."),
    (11, None, "'You acted extremely recklessly, Sokolov.' Buying the confession, the boss turns his anger onto the junior operative instead."),
    (12, None, "'I promise this will not happen again.' With a crisp promise to do better, he saves his mentor's badge."),
]
