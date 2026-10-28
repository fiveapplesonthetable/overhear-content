# Authoring module for domashniy-arest-s01e12-scene-04.
ID = 'domashniy-arest-s01e12-scene-04'
SHOW = 'domashniy-arest'
SEASON = 1
EPISODE = 12
SCENE = 4
TITLE = 'Утечка из кабинета  (Leak from the Office)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'pasha': 'Паша', 'vika': 'Вика'}
SOURCE_NAME = 'Домашний арест (Domashniy Arest) S1.12'
SOURCE_FILE = 'sources/domashniy-arest/s01/e12.ru.dual.srt'
INTRO = "Local television broadcasts shocking leaked footage recorded by a hidden camera inside the mayor's office. Pavel panics upon realizing that he installed the secret camera himself a year ago to catch office thieves. Seeing that the political campaign is ruined and the public is laughing at them, Vika packs her bags to abandon him. Let's listen to their panicked argument in Russian first."
OPENER = "Now let's examine Pavel and Vika's office dispute line by line."
TRANSITION = "Now let's listen to Pavel and Vika's quarrel again without interruption."
OUTRO = 'Vika leaves Pavel to deal with the public relations disaster by himself. See you next time!'
CLOSING = ('vika', 'Пока!')
STORY = [
    ('pasha', 'В новостях снова говорят про выборы.', 'The news is talking about the elections again.', [(74, 'Выборная эпопея в Синеозерске продолжается')], 'adapted'),
    ('pasha', 'Кто-то опубликовал секретное видео в интернете!', 'Someone published a secret video on the internet!', [(75, 'Опубликованные сегодня кадры с камер наблюдения')], 'adapted'),
    ('vika', 'Это же кадры из твоего кабинета!', 'These are clips from your office!', [(75, 'в кабинете мэра')], 'adapted'),
    ('pasha', 'Я совсем забыл про скрытую камеру.', 'I completely forgot about the hidden camera.', [(80, 'Я забыл совсем, что у меня там камера')], 'adapted'),
    ('vika', 'Зачем ты вообще её туда поставил?', 'Why did you put it there in the first place?', [(81, 'Ее год назад поставил')], 'adapted'),
    ('pasha', 'Я хотел поймать воров на работе.', 'I wanted to catch thieves at work.', [(81, 'чтобы узнать, кто мне какая ворует')], 'adapted'),
    ('vika', 'Теперь над нами смеётся весь город!', 'Now the whole city is laughing at us!', [(77, 'повеселили пользователей интернета')], 'adapted'),
    ('pasha', 'Нам нужно срочно что-то придумать.', 'We need to come up with something urgently.', [(83, 'Надо что-то делать')], 'adapted'),
    ('vika', 'Здесь больше нечего ловить, Паша.', 'There is nothing left to gain here, Pasha.', [(88, 'Больше здесь ловить нечего')], ''),
    ('pasha', 'Вика, куда ты сейчас собираешься?', 'Vika, where are you going right now?', [(87, 'А ты куда собралась-то')], ''),
    ('vika', 'Я собираю свои вещи и ухожу.', 'I am packing my things and leaving.', [(89, 'Уйди')], 'adapted'),
    ('pasha', 'Пожалуйста, не бросай меня одного!', "Please don't abandon me alone!", [], 'new'),
    ('vika', 'Твоя политическая карьера уже закончилась.', 'Your political career is already over.', [], 'new'),
]
WALK = [
    (0, None, '\'The news is talking about the elections again.\' Russian just says "in the news they talk", without naming an anchor, as Pasha stares at the TV screen.'),
    (1, None, "'Someone published a secret video on the internet!' His campaign was already shaky, and now an anonymous upload is about to sink it completely."),
    (2, None, "'These are clips from your office!' Vika recognizes the furniture on the screen right away—the camera angle is inside the mayor's own room."),
    (3, None, "'I completely forgot about the hidden camera.' What a confession: nobody bugged the acting mayor, he bugged himself and forgot to turn it off."),
    (4, None, '\'Why did you put it there in the first place?\' Her voice is pure disbelief. The word "voobshche" adds that extra "at all / in the first place" edge.'),
    (5, None, "'I wanted to catch thieves at work.' Paranoid about petty office theft, Pasha ended up broadcasting his own schemes to the public."),
    (6, None, "'Now the whole city is laughing at us!' For an ambitious campaign manager like Vika, being a laughingstock in Sineozersk is unforgivable."),
    (7, None, "'We need to come up with something urgently.' Still clinging to hope, Pavel thinks a clever spin can fix a viral scandal."),
    (8, None, '\'There is nothing left to gain here, Pasha.\' Literally she says "there is nothing left to catch here"—a Russian fishing idiom for a dead-end situation.'),
    (9, None, "'Vika, where are you going right now?' Watching her reach for her suitcase, Pasha realizes his strategist is abandoning ship."),
    (10, None, "'I am packing my things and leaving.' Cold, practical, and unsentimental, Vika cuts her losses the second the polls are dead."),
    (11, None, "'Please don't abandon me alone!' All the bluster of the acting mayor vanishes as he begs her not to leave him to face the fallout."),
    (12, None, "'Your political career is already over.' She delivers the verdict like a doctor calling the time of death."),
]
