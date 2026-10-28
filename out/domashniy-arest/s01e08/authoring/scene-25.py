# Authoring module for domashniy-arest-s01e08-scene-25.
ID = 'domashniy-arest-s01e08-scene-25'
SHOW = 'domashniy-arest'
SEASON = 1
EPISODE = 8
SCENE = 25
TITLE = 'Раненый мэр  (Arkady Hurt)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'arkady': 'Аркадий', 'lyosha': 'Лёша'}
SOURCE_NAME = 'Домашний арест, Сезон 1, Эпизод 8'
SOURCE_FILE = 'sources/domashniy-arest/s01/e08.ru.dual.srt'
INTRO = 'Previously, Ivan failed to convince his family to support him at the upcoming debates. Meanwhile, back in the communal apartment, Arkady and young Lyosha resume their war game, but the physical roughhousing ends with an unexpected injury.'
OPENER = "Let's see how Arkady and Lyosha's game of war turns suddenly painful."
TRANSITION = 'Now listen to the corridor roughhousing once more.'
OUTRO = 'Arkady slowly recovers from his bruised back, reminded of the hazards of playing with energetic boys. See you next time!'
CLOSING = ('arkady', 'Пока!')
STORY = [
    ('lyosha', 'Всё, привал закончен!', 'That is all, the break is over!', [(431, 'Все, привал закончен')], ''),
    ('lyosha', 'Снова начинается война!', 'The war is beginning again!', [(432, 'Снова война')], 'expanded cue 432'),
    ('arkady', 'Хорошо, держи гранату!', 'Alright, take the grenade!', [(435, 'Ладно, держи гранату')], 'replaced Ладно with Хорошо'),
    ('arkady', 'Я злой враг в бункере!', 'I am the evil enemy in the bunker!', [(436, 'Я есть Гитлер'), (437, 'Я сидеть в свой глубокий пукер')], 'cleaned cues 436-437'),
    ('arkady', 'Я сижу и никого не боюсь!', 'I am sitting and fear no one!', [(438, 'и никого не бояться')], 'corrected grammar'),
    ('lyosha', 'Сдавайся, враг! Я стреляю!', 'Surrender, enemy! I am shooting!', [], 'gameplay line'),
    ('arkady', 'Ай, партизан выстрелил мне в спину!', 'Ow, the partisan shot me in the back!', [(439, 'Проклятый партизан'), (440, 'Подло в спину выстрелил')], 'combined cues 439 and 440'),
    ('lyosha', 'Получай ещё раз по спине!', 'Take that on the back again!', [(442, 'Получай')], 'adapted cue 442'),
    ('arkady', 'Тихо, стой! Мне действительно больно!', 'Quiet, stop! It really hurts!', [(443, 'Тихо, не на... Не на больно'), (444, 'Больно, идиот, хватит!')], 'cleaned offensive word'),
    ('arkady', 'Хватит, прекрати сейчас же!', 'Enough, stop right now!', [(444, 'хватит!')], 'expanded cue 444'),
    ('arkady', 'Кажется, я спину повредил.', 'It seems I injured my back.', [(445, 'Кажется, спину сломал')], 'toned down сломал to повредил'),
    ('lyosha', 'Прости, Аркадий, я не хотел.', 'Forgive me, Arkady, I did not mean to.', [], 'apology line'),
    ('arkady', 'Ничего. Помоги мне медленно встать.', 'It is nothing. Help me slowly stand up.', [], 'concluding recovery line'),
]
WALK = [
    (0, None, "'That is all, the break is over!' Lyosha playfully commands the end of their rest."),
    (1, None, "'The war is beginning again!' Playtime isn't over yet — Lyosha announces that the battle is back on."),
    (2, None, "'Alright, take the grenade!' Arkady tosses an imaginary explosive at the boy."),
    (3, None, "'I am the evil enemy in the bunker!' Arkady adopts his villainous role in the game."),
    (4, None, "'I am sitting and fear no one!' Sitting in his imaginary bunker, Arkady boasts that nobody scares him."),
    (5, None, "'Surrender, enemy! I am shooting!' Lyosha charges in yelling for the enemy to give up."),
    (6, None, "'Ow, the partisan shot me in the back!' Arkady pretends to take a hit from behind."),
    (7, None, "'Take that on the back again!' Lyosha gets carried away and strikes Arkady for real."),
    (8, None, "'Quiet, stop! It really hurts!' Arkady drops the game immediately as real pain sets in."),
    (9, None, "'Enough, stop right now!' Playtime is officially over as Arkady winces and begs the boy to stop."),
    (10, None, "'It seems I injured my back.' Clutching his lower back, Arkady realizes that last whack actually pulled something."),
    (11, None, "'Forgive me, Arkady, I did not mean to.' Lyosha feels guilty for hurting his older friend."),
    (12, None, "'It is nothing. Help me slowly stand up.' Arkady reassures the boy despite his aching back."),
]
