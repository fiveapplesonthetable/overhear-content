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
    (0, None, '\'You prepare the cookies from this recipe.\' Barinov takes a serious tempo as the scene unfolds, building the phrase around "gotov" ("prepare") and "pechenye" ("cookies, pastry") for a crisp, natural delivery.'),
    (1, None, '\'I beg you, try very hard.\' Barinov chooses a resolute manner in front of Nikita, building the phrase around "proshu" ("beg, ask") and "ochen" ("very much") for a crisp, natural delivery.'),
    (2, None, '\'And why is it so expensive?\' Nikita prompts bluntly without a pause, leaning on "pochemu" ("why") before closing the thought with "dorogo" ("expensive").'),
    (3, None, '\'Six boxes of flower petals.\' Nastya establishes an easygoing course during the exchange, leaning on "korobok" ("boxes") before closing the thought with "lepestkami" ("petals").'),
    (4, None, '\'They picked apart every flower.\' Nastya takes a measured course across the room, building the phrase around "kazhdyy" ("every") and "tsvetok" ("flower") for a crisp, natural delivery.'),
    (5, None, '\'Congratulations on the promotion, Nikita.\' Nastya offers a clear view straight away, linking "pozdravlyayu" ("congratulations"), "povysheniyem" ("to promotion"), and "nikita" ("Nikita") in one brisk exchange.'),
    (6, None, '\'Do not bother, I am going to quit anyway.\' Nikita sustains a wry attitude as they talk, building the phrase around "stoit" ("is parked") and "ravno" ("the same") for a crisp, natural delivery.'),
    (7, None, '\'Why do you want to leave?\' Nastya queries directly as the talk turns, leaning on "pochemu" ("why") before closing the thought with "khochesh" ("do you want").'),
    (8, None, '\'Nothing is working out with Katya.\' Nikita conveys a wry footing at this moment, pairing "poluchayetsya" ("works out") with "katey" ("Katya") so the "-sya" ending carries the action.'),
    (9, None, '\'Come on, do not even think of it!\' Nastya shows a playful tempo in the room, using "vzdumay" (from "vzdumat", "don\'t even think") alongside "da" ("yes") to shape the meaning.'),
    (10, None, '\'Katya told her mom that she likes you very much.\' Nastya sets a warm rhythm right away, using "govorila" (from "govorit", "said") alongside "mame" ("mother, mum") to shape the meaning.'),
    (11, None, '\'Are you serious?\' Nikita quizzes quietly in the scene, linking "seryezno" ("seriously") directly with "ty" ("you"), since Russian drops "is" and "are" in the present.'),
]
