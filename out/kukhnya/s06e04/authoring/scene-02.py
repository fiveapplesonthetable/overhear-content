# Authoring module for kukhnya-s06e04-scene-02.
ID = 'kukhnya-s06e04-scene-02'
SHOW = 'kukhnya'
SEASON = 6
EPISODE = 4
SCENE = 2
TITLE = 'Старый друг из Парижа  (An Old Friend from Paris)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'eleonora': 'Элеонора', 'guest': 'Гость', 'katya': 'Катя'}
SOURCE_NAME = 'Кухня (Kukhnya) S6.04'
SOURCE_FILE = 'sources/kukhnya/s06/e04.ru.srt'
INTRO = 'At the reception desk, Katya is surprised by her old French classmate Olivier from the Paris culinary academy—and when Barinov and Eleonora hear the words Paris and culinary academy, they jump to conclusions.'
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = 'Hearing that Olivier is a French chef on a mysterious business trip, Barinov and Eleonora exchange a knowing look. See you next time!'
CLOSING = ('eleonora', 'Всего хорошего!')
STORY = [
    ('guest', 'Мне показалось, что вы мне подмигнули.', 'It seemed to me that you winked at me.', [(14, 'мне показалось, что вы мне подмигнули')], 'exact'),
    ('katya', 'Нет, вам показалось.', 'No, you imagined it.', [(15, 'Нет, вам показалось')], 'exact'),
    ('katya', 'Столько лет прошло, а ты все пользуешься этим!', 'So many years have passed, and you still use that line!', [(17, 'Столько лет прошло, а ты все пользуешься этим')], 'adapted'),
    ('guest', 'Катя, сколько мы не виделись?', 'Katya, how long has it been since we saw each other?', [(18, 'Катя, сколько мы не виделись?')], 'exact'),
    ('katya', 'Мы не виделись с тех пор, как меня отчислили.', 'We have not seen each other since they expelled me.', [(20, 'с тех пор, как меня отчислили')], 'adapted'),
    ('katya', 'А ты что здесь делаешь?', 'And what are you doing here?', [(21, 'А ты что здесь делаешь?')], 'exact'),
    ('guest', 'Это небольшой бизнес, а ты как?', 'It is a small business trip, and how about you?', [(21, 'Это небольшой бизнес'), (22, 'А ты как?')], 'adapted'),
    ('katya', 'Я отлично работаю здесь в ресторане.', 'I am doing great working here in the restaurant.', [(22, 'Я отлично работаю здесь в ресторане')], 'exact'),
    ('guest', 'Ты помнишь нашего старого профессора?', 'Do you remember our old professor?', [(24, 'Ты помнишь профессора')], 'adapted'),
    ('guest', 'Когда он заснул на занятии, я проучился на месяц больше, чем ты.', 'When he fell asleep in class, I studied a month longer than you.', [(25, 'заснул на занятии'), (27, 'я проучился на месяц больше, чем ты')], 'adapted'),
    ('eleonora', 'А кто это такой, Катя?', 'And who is that, Katya?', [(34, 'А кто это?')], 'adapted'),
    ('katya', 'Это Оливье, мы с ним учились в Париже в кулинарной академии.', 'That is Olivier, he and I studied together in Paris at the culinary academy.', [(34, 'Это Оливье'), (35, 'Мы с ним учились в Париже, в кулинарной академии')], 'adapted'),
]
WALK = [
    (0, None, "'It seemed to me that you winked at me.' The guest responds candidly without any doubt, so Katya knows he is not just making small talk."),
    (1, None, "'No, you imagined it.' Katya responds evenly in this moment, letting the remark speak for itself."),
    (2, None, '\'So many years have passed, and you still use that line!\' Katya jumps in smoothly in the exchange and brings in "polzuyeshsya" ("use", from "polzovatsya") as the key Russian word here.'),
    (3, None, '\'Katya, how long has it been since we saw each other?\' Cutting in dryly during the talk, the "-sya" ending on "videlis" ("have seen each other") marks an action that unfolds mutually or turns back on the speaker.'),
    (4, None, "'We have not seen each other since they expelled me.' Katya steps in warmly in this moment, before the guest can change the subject."),
    (5, None, '\'And what are you doing here?\' Katya fires back firmly during the talk and brings in "delayesh" ("are you doing", from "delat") as the key Russian word here.'),
    (6, None, '\'It is a small business trip, and how about you?\' Underscoring how small things are before Katya, the guest links the Russian words directly in the present with no word for "am", "is", or "are" needed.'),
    (7, None, "'I am doing great working here in the restaurant.' Katya opens up plainly hearing the guest, letting the remark speak for itself."),
    (8, None, '\'Do you remember our old professor?\' Touching on the professor in front of Katya, the guest brings in "professora" ("professor", from "professor") as the key Russian word here.'),
    (9, None, "'When he fell asleep in class, I studied a month longer than you.' The guest cuts in candidly in their talk, before Eleonora can change the subject."),
    (10, None, "'And who is that, Katya?' Eleonora checks straight out what Katya is actually getting at here."),
    (11, None, '\'That is Olivier, he and I studied together in Paris at the culinary academy.\' Explaining how culinary things are in this beat, Katya uses "kulinarnoy" ("culinary", from "kulinarnyy") to make the point stick.'),
]
