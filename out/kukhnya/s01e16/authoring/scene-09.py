# Authoring module for kukhnya-s01e16-scene-09.
ID = 'kukhnya-s01e16-scene-09'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 16
SCENE = 9
TITLE = 'Проверка у конкурентов  (Inspection at the Rivals)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'elena': 'Елена', 'inspector': 'Инспектор'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.16'
SOURCE_FILE = 'sources/kukhnya/s01/e16.ru.dual.srt'
INTRO = "At Arcobaleno, the migration inspector has finished with Elena Pavlovna's kitchen and found nothing wrong. He wants to go somewhere else with his team, and Elena knows exactly where to send him. Listen for the name of the restaurant she suggests."
OPENER = "Now Elena's quiet revenge, one line at a time."
TRANSITION = "And the whole thing once more, from the inspector's praise to the chef's panic."
OUTRO = "The revenge is about to land on Claude Monet's own doorstep, and Barinov is the first to see it coming. As you watch, keep an ear out for 'vot' and 'von': they look alike but mean very different things. See you next time!"
CLOSING = ('barinov', 'Всё, пока!')
STORY = [
    ('inspector', 'У вас всё в порядке.', 'Everything is in order with you.', [(62, 'Ну что же, уважаемая Елена Павловна, мне кажется, что ваш ресторан будет...'), (63, 'весьма успешным.')], ''),
    ('elena', 'Мы всё делаем правильно.', 'We do everything right.', [], ''),
    ('elena', 'Большое спасибо вам.', 'Thank you very much.', [(64, 'Спасибо.')], ''),
    ('inspector', 'Вы меня очень удивили.', 'You really surprised me.', [(66, 'Признаюсь, вы меня очень сильно удивили.')], ''),
    ('inspector', 'Ни одного повара без документов.', 'Not a single cook without documents.', [(67, 'Ни одного нелегального работника на кухне.')], ''),
    ('elena', 'Я привыкла работать по закону.', 'I got used to working by the law.', [(68, 'Дело в том, что я очень долго работала за границей и привыкла,'), (69, 'чтобы все было по закону.')], ''),
    ('inspector', 'Мне было очень приятно познакомиться.', 'It was very nice to meet you.', [(72, 'Мне было чрезвычайно приятно с вами познакомиться.')], ''),
    ('inspector', 'Может, пойдём ещё куда-нибудь?', 'Maybe we can go somewhere else?', [(74, 'Может, мы еще куда-нибудь прогуляемся?')], ''),
    ('elena', 'Рядом есть Клод Моне.', 'Claude Monet is right nearby.', [(75, 'В этом же здании есть ресторан.'), (76, 'Клод Мане.')], ''),
    ('inspector', 'Отлично, люблю французскую кухню.', 'Excellent, I love French cuisine.', [(77, 'Отлично. Я обожаю французскую кухню.')], ''),
    ('barinov', 'Внимание! К нам идёт проверка!', 'Attention! An inspection is coming to us!', [(83, 'Внимание!'), (79, 'К нам идет проверка ФМС.')], ''),
    ('barinov', 'Все без документов, вон!', 'Everyone without documents, get out!', [(84, 'Все нелегалы немедленно вон из ресторана.')], ''),
]
WALK = [
    (0, None, "'Everything is in order with you.' 'U vas' is literally 'at you', and 'vsyo v poryadke' means 'all is in order'. It's the happy ending to any inspection."),
    (1, None, "'We do everything right.' 'Pravilno' means 'correctly' and comes from 'pravilo', 'a rule'. 'Delaem' is the 'we' ending: 'my delaem'."),
    (2, None, "'Thank you very much.' 'Spasibo' is a noun in Russian, so 'big' has to agree with it: 'bolshoe spasibo', literally 'a big thanks'."),
    (3, None, "'You really surprised me.' 'Udivili' comes from 'divo', an old word for 'wonder'. The '-li' ending is the polite 'vy' past, even for one person."),
    (4, None, "'Not a single cook without documents.' 'Ni odnogo' means 'not even one'. 'Bez', 'without', changes 'dokumenty' to 'dokumentov'."),
    (5, None, "'I got used to working by the law.' 'Privykla', 'I got used to', ends in '-la' because Elena is a woman; a man would say 'privyk'. 'Po zakonu' means 'by the law'."),
    (6, None, "'It was very nice to meet you.' Russian says 'mne bylo priyatno', literally 'to me it was pleasant'. 'Poznakomitsya' grows out of 'znakomy', 'acquainted'."),
    (7, None, "'Maybe we can go somewhere else?' 'Kuda-nibud' means 'somewhere', in the sense of any place at all. '-nibud' makes 'who', 'what' and 'where' vague: 'kto-nibud', 'anyone'."),
    (8, None, "'Claude Monet is right nearby.' 'Ryadom' means 'nearby' or 'next door', and 'est' means 'there is'. In the subtitles the name is spelled 'Klod Mane', with an a, the way it sounds."),
    (9, None, "'Excellent, I love French cuisine.' 'Kukhnya' means both 'kitchen' and 'cuisine', and it is the name of this show. 'Frantsuzskuyu' ends in '-uyu' because the cuisine is what he loves."),
    (10, None, "'Attention! An inspection is coming to us!' 'Vnimanie' is the word for 'attention' on loudspeakers and in announcements. Russian says the inspection 'idyot', 'walks', toward them."),
    (11, None, "'Everyone without documents, out!' 'Von' means 'out!' or 'get out!', a one-word shove. Don't mix it up with 'vot', 'here it is'."),
]
