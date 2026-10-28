# Authoring module for domashniy-arest-s01e08-scene-23.
ID = 'domashniy-arest-s01e08-scene-23'
SHOW = 'domashniy-arest'
SEASON = 1
EPISODE = 8
SCENE = 23
TITLE = 'Военная игра  (War Games)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'arkady': 'Аркадий', 'lyosha': 'Лёша'}
SOURCE_NAME = 'Домашний арест, Сезон 1, Эпизод 8'
SOURCE_FILE = 'sources/domashniy-arest/s01/e08.ru.dual.srt'
INTRO = 'Previously, elderly neighbor Klavdia Viktorovna alarmed everyone in the communal kitchen with her grim river stories. Meanwhile, out in the corridor, Arkady and young Lyosha continue bonding by playing an imaginative game of war with toy weapons.'
OPENER = "Let's follow the playful corridor battle between Arkady and young Lyosha."
TRANSITION = 'Now listen to the playful battle in the hallway once more.'
OUTRO = 'Arkady and Lyosha finish their game in high spirits, growing closer despite the chaotic apartment. See you next time!'
CLOSING = ('arkady', 'Пока!')
STORY = [
    ('arkady', 'Я считаю до пяти!', 'I am counting to five!', [(359, 'Считаю до пяти')], 'added Я'),
    ('arkady', 'Один, два, три, четыре, пять!', 'One, two, three, four, five!', [(360, 'Айн, цвайн, дайн, фир, фир, фир')], 'rendered in Russian numbers'),
    ('arkady', 'Где эти русские партизаны?', 'Where are those Russian partisans?', [(362, 'Где эти русские партизаны?')], ''),
    ('arkady', 'Я никого здесь не вижу.', 'I do not see anyone here.', [(363, 'Я никого не видеть')], 'corrected grammar'),
    ('lyosha', 'Я здесь, прямо за дверью!', 'I am here, right behind the door!', [], 'transitional dialogue line'),
    ('lyosha', 'Сдавайся, враг окружён!', 'Surrender, the enemy is surrounded!', [], 'gameplay dialogue line'),
    ('arkady', 'Никогда я не сдамся!', 'Never will I surrender!', [], 'gameplay response'),
    ('arkady', 'Я открываю ответный огонь!', 'I am opening return fire!', [(359, 'открываю ответный огонь')], 'added Я'),
    ('lyosha', 'Ты ранен в руку!', 'You are wounded in the arm!', [], 'gameplay line'),
    ('arkady', 'Ой, я тяжело ранен!', 'Oh, I am heavily wounded!', [(364, 'прострелил')], 'adapted dramatically'),
    ('arkady', 'Но у меня ещё есть силы.', 'But I still have strength left.', [(370, 'силы у меня еще есть')], 'adapted cue 370'),
    ('lyosha', 'Отличная игра, Аркадий!', 'Great game, Arkady!', [(368, 'Отлично!')], 'added Отличная игра, Аркадий!'),
    ('arkady', 'Спасибо, Лёша. Мы отличная команда.', 'Thank you, Lyosha. We are a great team.', [(367, 'Привет!')], 'concluding line'),
]
WALK = [
    (0, None, "'I am counting to five!' Arkady starts the playful countdown in the corridor."),
    (1, None, "'One, two, three, four, five!' The Russian cardinal numbers build tension in their game."),
    (2, None, "'Where are those Russian partisans?' The demonstrative pronoun modifies the plural noun."),
    (3, None, "'I do not see anyone here.' The negative pronoun takes the 'of' form with negation."),
    (4, None, "'I am here, right behind the door!' The preposition 'za' with This phrase indicates location."),
    (5, None, "'Surrender, the enemy is surrounded!' The command form command demands full capitulation."),
    (6, None, "'Never will I surrender!' The negative adverb emphasizes Arkady's defiant refusal."),
    (7, None, "'I am opening return fire!' The present tense verb describes his playful counterattack."),
    (8, None, "'You are wounded in the arm!' This phrase indicates the hit."),
    (9, None, "'Oh, I am heavily wounded!' Arkady melodramatically plays along with the boy."),
    (10, None, "'But I still have strength left.' The plural 'of' form follows the existence construction."),
    (11, None, "'Great game, Arkady!' Lyosha happily praises their imaginative battle in the corridor."),
    (12, None, "'Thank you, Lyosha. We are a great team.' Arkady strengthens his bond with Marina's son."),
]
