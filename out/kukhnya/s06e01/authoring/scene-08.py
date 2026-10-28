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
    (0, None, '\'You prepare the cookies from this recipe.\' Even though Nastya prepares the cookies from this recipe, Barinov keeps a steady face in front of Nastya. Using the informal "you" shows how direct and unfiltered their kitchen relationship is.'),
    (1, None, '\'I beg you, try very hard.\' Explaining that he begs Nastya tries very hard lays the cards on the table for Nastya. Speaking with the close, informal "you" strips away any polite distance between them.'),
    (2, None, "'And why is it so expensive?' Here asking why it so expensive is shows Nikita looking for the real truth."),
    (3, None, "'Six boxes of flower petals.' With the conversation and family in play, Nastya keeps this short reply brisk and direct."),
    (4, None, "'They picked apart every flower.' Around the work and news, Nastya sets a calm, everyday tone with Barinov."),
    (5, None, "'Congratulations on the promotion, Nikita.' Between the work and the news, Nastya gives Barinov a quick, grounded response."),
    (6, None, "'Do not bother, I am going to quit anyway.' Since do not bother he is going to quit anyway, Nikita does not waste words on excuses."),
    (7, None, '\'Why do you want to leave?\' By asking why Barinov wants to leave, Nastya presses Barinov for a straight answer. Speaking with the close, informal "you" strips away any polite distance between them.'),
    (8, None, "'Nothing is working out with Katya.' Nikita reminds Barinov that nothing is working out with Katya before the moment passes."),
    (9, None, '\'Come on, do not even think of it!\' By coming on do not even think of it, Nastya raises the stakes in the room at once. Speaking with the close, informal "you" strips away any polite distance between them.'),
    (10, None, '\'Katya told her mom that she likes you very much.\' Explaining that Katya told her that she likes Barinov very much lays the cards on the table for Barinov. Using the informal "you" shows how direct and unfiltered their kitchen relationship is.'),
    (11, None, "'Are you serious?' Here checking whether Barinov serious shows Nikita looking for the real truth."),
]
