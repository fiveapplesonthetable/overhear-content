# Authoring module for kukhnya-s06e05-scene-04.
ID = 'kukhnya-s06e05-scene-04'
SHOW = 'kukhnya'
SEASON = 6
EPISODE = 5
SCENE = 4
TITLE = "Тайный звонок Насти  (Nastya's Secret Call)"
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'mikhail': 'Михаил', 'nastya': 'Настя'}
SOURCE_NAME = 'Кухня (Kukhnya) S6.05'
SOURCE_FILE = 'sources/kukhnya/s06/e05.ru.srt'
INTRO = 'Back in the corridor, Chef Barinov urges Mikhail to give up cards for good, right before Eleonora summons the chef to her office and Nastya takes a mysterious phone call.'
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = 'Overhearing Nastya whisper that she will tell him everything tonight convinces Kostya that his wife is hiding a secret affair. See you next time!'
CLOSING = ('barinov', 'До свидания!')
STORY = [
    ('barinov', 'Миша, может, тебе больше не играть?', 'Misha, maybe you should not play anymore?', [(60, 'Миш, может, тебе больше не играть')], 'adapted'),
    ('barinov', 'Ну пойми, что это не твоё.', 'Just understand that this is not for you.', [(61, 'Ну пойми, что это не твое')], 'adapted'),
    ('mikhail', 'Я очень хорошо умею играть.', 'I know how to play very well.', [(62, 'Я умею играть')], 'adapted'),
    ('mikhail', 'Просто мне сегодня не повезло.', 'I was simply unlucky today.', [(63, 'Просто мне не повезло')], 'adapted'),
    ('barinov', 'Хозяйка отеля к себе зовёт.', 'The hotel owner is calling me to her office.', [(67, 'к себе зовет')], 'adapted'),
    ('mikhail', 'Ей уже обо всём донесли.', 'Someone has already reported everything to her.', [(68, 'А то уже донесли')], 'adapted'),
    ('nastya', 'Алло, да, я могу говорить.', 'Hello, yes, I can talk now.', [(69, 'Алло, да. Да, могу говорить')], 'adapted'),
    ('nastya', 'Нет, Костя сейчас не рядом.', 'No, Kostya is not nearby right now.', [(70, 'Нет, Костя не рядом')], 'adapted'),
    ('nastya', 'Нет, я ещё ничего не сказала.', 'No, I have not said anything yet.', [(71, 'Нет, еще не сказала')], 'adapted'),
    ('nastya', 'Может, скажу ему сегодня вечером.', 'Maybe I will tell him tonight.', [(72, 'может, сегодня вечером')], 'adapted'),
    ('nastya', 'Нет, лучше я скажу сама.', 'No, it is better if I tell him myself.', [(74, 'лучше я сама')], 'adapted'),
    ('nastya', 'Всё, ладно, мне уже пора.', 'Alright, that is all, I have to go.', [(75, 'Все, ладно, мне пора')], 'adapted'),
]
WALK = [
    (0, None, "'Misha, maybe you should not play anymore?' Asking whether maybe Mikhail should not play anymore puts Mikhail right on the defensive."),
    (1, None, '\'Just understand that this is not for you.\' Saying that just understand that this is not for Mikhail is how Barinov sets the tone with Mikhail. Speaking with the close, informal "you" strips away any polite distance between them.'),
    (2, None, "'I know how to play very well.' Adding that he knows how to play very well fills in the missing piece for Barinov."),
    (3, None, "'I was simply unlucky today.' Adding that he was simply unlucky today fills in the missing piece for Barinov."),
    (4, None, "'The hotel owner is calling me to her office.' Saying that the hotel owner is calling him to her office is how Barinov sets the tone with Mikhail."),
    (5, None, "'Someone has already reported everything to her.' Since someone has already reported everything, Mikhail does not waste words on excuses."),
    (6, None, "'Hello, yes, I can talk now.' Mentioning that she can talk now moves the talk in a new direction."),
    (7, None, "'No, Kostya is not nearby right now.' Saying that Kostya is not nearby right now is how Nastya sets the tone with Barinov."),
    (8, None, '\'No, I have not said anything yet.\' Claiming that she has not said anything yet sounds confident, even if Barinov has doubts. Russian stacks "never" or "nothing" together with "not", doubling the refusal for extra weight.'),
    (9, None, "'Maybe I will tell him tonight.' Explaining that maybe she will tell him tonight lays the cards on the table for Barinov."),
    (10, None, "'No, it is better if I tell him myself.' Noting that it is better if she tells him herself keeps Nastya's side of the story simple and clear."),
    (11, None, '\'Alright, that is all, I have to go.\' Claiming that Alright that is all she has to go sounds confident, even if Barinov has doubts. There is no "you" needed in the Russian here: one short word states the rule for everyone in the room.'),
]
