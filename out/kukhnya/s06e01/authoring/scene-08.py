# Authoring module for kukhnya-s06e01-scene-08.
ID = 'kukhnya-s06e01-scene-08'
SHOW = 'kukhnya'
SEASON = 6
EPISODE = 1
SCENE = 8
TITLE = 'Хорошая новость для Никиты  (Good News for Nikita)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'nastya': 'Настя', 'nikita': 'Никита'}
SOURCE_NAME = 'Кухня (Kukhnya) S6.01'
SOURCE_FILE = 'sources/kukhnya/s06/e01.ru.srt'
INTRO = 'After Barinov begs Louis to bake the family wedding cookies properly, Nastya congratulates newly promoted director Nikita and stops him from quitting by revealing what Katya just told her mother.'
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = "Encouraged by Nastya's revelation, Nikita decides to stay and prove himself as the new restaurant director. See you next time!"
CLOSING = ('nastya', 'Хорошего дня!')
STORY = [
    ('barinov', 'Ты готовь печенье по этому рецепту.', 'You prepare the cookies from this recipe.', [(129, 'Ты готовь печенье по этому рецепту')], 'exact'),
    ('barinov', 'Я тебя прошу, очень постарайся.', 'I beg you, try very hard.', [(130, 'Я тебя прошу, очень постарайся')], 'exact'),
    ('nikita', 'А почему так дорого?', 'And why is it so expensive?', [(135, 'так дорого')], 'adapted'),
    ('nastya', 'Шесть коробок с лепестками.', 'Six boxes of flower petals.', [(136, 'Шесть коробок с лепестками')], 'adapted'),
    ('nastya', 'Каждый цветок разбирали.', 'They picked apart every flower.', [(139, 'Каждый цветок')], 'adapted'),
    ('nastya', 'Поздравляю с повышением, Никита.', 'Congratulations on the promotion, Nikita.', [(142, 'Поздравляю с повышением')], 'adapted'),
    ('nikita', 'Не стоит, я все равно уволюсь.', 'Do not bother, I am going to quit anyway.', [(143, 'я все равно уволюсь')], 'adapted'),
    ('nastya', 'Почему ты хочешь уйти?', 'Why do you want to leave?', [(144, 'Почему?')], 'adapted'),
    ('nikita', 'С Катей ничего не получается.', 'Nothing is working out with Katya.', [(145, 'С Катей ничего не получается')], 'exact'),
    ('nastya', 'Да ты что, не вздумай!', 'Come on, do not even think of it!', [(146, 'Да ты что, не вздумай')], 'exact'),
    ('nastya', 'Катя говорила маме, что ты ей очень нравишься.', 'Katya told her mom that she likes you very much.', [(146, 'Катя сегодня говорила маме'), (147, 'что ты ей очень нравишься')], 'adapted'),
    ('nikita', 'Ты серьезно?', 'Are you serious?', [(148, 'Ты серьезно?')], 'exact'),
]
WALK = [
    (0, None, "'You prepare the cookies from this recipe.' Barinov weighs in evenly beside Nikita, steering the talk right where he wants it."),
    (1, None, "'I beg you, try very hard.' Barinov reacts steadily toward Nikita, to clear the air between them once and for all."),
    (2, None, '\'And why is it so expensive?\' Nikita speaks up firmly at once and centers the remark on "dorogo" ("expensive") without any extra fuss.'),
    (3, None, "'Six boxes of flower petals.' Pointing to the petals at once, spoken Russian compresses the whole thought into just 4 words, skipping the extra helper words English needs."),
    (4, None, "'They picked apart every flower.' Addressing the flower beside Nikita, Nastya makes it clear to Nikita that she means every word."),
    (5, None, '\'Congratulations on the promotion, Nikita.\' Nastya chimes in earnestly with Nikita and chooses "pozdravlyayu" ("congratulations", from the root "pozdravlyat") so Nikita hears the exact meaning.'),
    (6, None, '\'Do not bother, I am going to quit anyway.\' Following up promptly to Nastya, the "-sya" ending on "uvolyus" ("will quit, resign") marks an action that unfolds mutually or turns back on the speaker.'),
    (7, None, "'Why do you want to leave?' Nastya tests evenly if there is more going on behind the scenes."),
    (8, None, '\'Nothing is working out with Katya.\' Nikita speaks calmly in front of Nastya and centers the thought on "poluchayetsya" ("works out", from "poluchatsya") without wasting a word.'),
    (9, None, "'Come on, do not even think of it!' Nastya speaks decisively with a shrug, refusing to let the moment slip past."),
    (10, None, "'Katya told her mom that she likes you very much.' Nastya answers candidly with a sigh, watching Nikita's face to see how the news lands."),
    (11, None, '\'Are you serious?\' Nikita proceeds quietly in front of Nastya and centers the thought on "seryezno" ("seriously", from "seryozno") without wasting a word.'),
]
