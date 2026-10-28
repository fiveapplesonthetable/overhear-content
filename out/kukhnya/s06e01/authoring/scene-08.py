ID = 'kukhnya-s06e01-scene-08'
SHOW = 'kukhnya'
SEASON = 6
EPISODE = 1
SCENE = 8
TITLE = "Хорошая новость для Никиты  (Good News for Nikita)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = 'ru-en'
VOICES = {"narrator": "sky", "nastya": "angelina", "nikita": "anja"}
LABELS = {"nastya": "Настя", "nikita": "Никита"}
SOURCE_NAME = 'Кухня (Kukhnya) S6.01'
SOURCE_FILE = 'sources/kukhnya/s06/e01.ru.srt'

INTRO = 'After Barinov begs Louis to bake the family wedding cookies properly, Nastya congratulates newly promoted director Nikita and stops him from quitting by revealing what Katya just told her mother.'

STORY = [
    ('nikita', 'Ты готовь печенье по этому рецепту.', 'You prepare the cookies from this recipe.', [(129, 'Ты готовь печенье по этому рецепту')], 'exact'),
    ('nikita', 'Я тебя прошу, очень постарайся.', 'I beg you, try very hard.', [(130, 'Я тебя прошу, очень постарайся')], 'exact'),
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

OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."

WALK = [
    (0, None, "'You prepare the cookies from this recipe.' Chef Barinov pairs 'prepare' with 'recipe' directly, since spoken Russian skips English filler words like 'the', 'a', and 'is'."),
    (1, None, "'I beg you, try very hard.' Chef Barinov addresses the listener with the informal singular 'you' alongside 'try'. Nikita answers right away."),
    (2, None, "'And why is it so expensive?' Nikita anchors the line on 'and', while 'expensive' completes the thought."),
    (3, None, "'Six boxes of flower petals.' Here the Russian phrasing highlights 'six' before landing on 'petals'."),
    (4, None, "'They picked apart every flower.' Notice how Russian expresses 'every' and 'to take apart' with crisp inflection rather than helper words."),
    (5, None, "'Congratulations on the promotion, Nikita.' Nastya anchors the line on 'congratulations', while 'Nikita' completes the thought."),
    (6, None, "'Do not bother, I am going to quit anyway.' Nikita brings out the contrast between 'not' and 'is standing' in a few short words."),
    (7, None, "'Why do you want to leave?' Nastya raises the pitch on 'to leave' to turn the phrase into a direct spoken question. Nikita answers right away."),
    (8, None, "'Nothing is working out with Katya.' Nikita brings out the contrast between 'with' and 'nothing' in a few short words."),
    (9, None, "'Come on, do not even think of it!' Notice how Russian expresses 'yes' and 'even think of it' with crisp inflection rather than helper words."),
    (10, None, "'Katya told her mom that she likes you very much.' Here the Russian phrasing highlights 'Katya' before landing on 'appeal to'. Nikita answers right away."),
    (11, None, "'Are you serious?' Nikita raises the pitch on 'seriously' to turn the phrase into a direct spoken question."),
]

TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = "Encouraged by Nastya's revelation, Nikita decides to stay and prove himself as the new restaurant director. See you next time!"
CLOSING = ("nastya", "Хорошего дня!")
