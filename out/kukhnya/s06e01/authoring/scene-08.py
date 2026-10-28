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
    (0, None, '\'You prepare the cookies from this recipe.\' Barinov uses this sharp detail in earnest: "pechenye" means "cookies, pastry", and it carries the main weight of what Barinov is saying.'),
    (1, None, "'I beg you, try very hard.' Barinov responds candidly before Nikita, grounding the moment in plain reality."),
    (2, None, '\'And why is it so expensive?\' Nikita uses this clear term at once: "dorogo" means "expensive", and it carries the main weight of what Nikita is saying.'),
    (3, None, "'Six boxes of flower petals.' Nastya delivers the comeback calmly now: spoken Russian trims this down to just 4 words, dropping the extra helper words that English has to spell out."),
    (4, None, "'They picked apart every flower.' Nastya speaks candidly toward Barinov, testing Barinov's reaction in the middle of the exchange."),
    (5, None, '\'Congratulations on the promotion, Nikita.\' Nastya frames one direct piece in earnest: "pozdravlyayu" means "congratulations" (from "pozdravlyat"), giving the line its exact edge.'),
    (6, None, '\'Do not bother, I am going to quit anyway.\' Nikita shares the reply for Barinov: the "-sya" ending on "uvolyus" ("will quit, resign") turns the action inward or makes it happen between people naturally.'),
    (7, None, "'Why do you want to leave?' Nastya tests evenly if there is more going on behind the scenes."),
    (8, None, '\'Nothing is working out with Katya.\' Nikita leans on one memorable element in reply: "poluchayetsya" means "works out" (from "poluchatsya"), giving the line its exact edge.'),
    (9, None, '\'Come on, do not even think of it!\' Nastya picks this telling touch with Nikita: "vzdumay" means "don\'t even think" (from "vzdumat"), giving the line its exact edge.'),
    (10, None, "'Katya told her mom that she likes you very much.' Nastya answers candidly to settle things, bringing things back to earth after the buildup."),
    (11, None, '\'Are you serious?\' Nikita centers this clear choice in reply: "seryezno" means "seriously" (from "seryozno"), giving the line its exact edge.'),
]
