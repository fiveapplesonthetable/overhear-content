# Authoring module for kukhnya-s01e01-scene-14.
ID = 'kukhnya-s01e01-scene-14'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 1
SCENE = 14
TITLE = 'Разговор с хозяином  (Talk with the Owner)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'max': 'Макс', 'nagiyev': 'Нагиев'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.01'
SOURCE_FILE = 'sources/kukhnya/s01/e01.ru.dual.srt'
INTRO = 'Max finds the owner of Claude Monet, Dmitry Nagiyev, and reminds him that a year ago he promised Max a job. Nagiyev is in a hurry, and does not seem to remember at all. Here is their conversation in Russian first.'
OPENER = 'Now their lines, slowly.'
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = 'Nagiyev sends Max to the kitchen, which is exactly where the trouble starts. You can now say "do you remember me" and "I\'m in a hurry" in Russian.'
CLOSING = ('max', 'Пока!')
STORY = [
    ('max', 'Дмитрий Владимирович, добрый день, вы помните меня?', 'Dmitry Vladimirovich, good afternoon, do you remember me?', [(107, 'Дмитрий Владимирович здравствуйте'), (109, 'Помните меня')], ''),
    ('nagiyev', 'Конечно же, я вас совсем не помню.', 'Of course, I do not remember you at all.', [(110, 'Конечно же я не помню')], ''),
    ('max', 'Мы познакомились с вами ровно год назад.', 'We met with you exactly one year ago.', [(108, 'Мы с вами встречались год назад')], ''),
    ('nagiyev', 'У меня сегодня очень много важных дел.', 'I have very many important matters today.', [(111, 'нашли время')], ''),
    ('max', 'Вы обещали взять меня на эту работу.', 'You promised to hire me for this job.', [(117, 'Он меня взял')], ''),
    ('nagiyev', 'Молодой человек, я очень сильно спешу.', 'Young man, I am in a very big hurry.', [(112, 'хорошего вечера')], ''),
    ('max', 'Я отличный повар и закончил кулинарный колледж.', 'I am an excellent cook and finished culinary college.', [(119, 'человек на кухне')], ''),
    ('nagiyev', 'Хорошо, тогда идите прямо на нашу кухню.', 'All right, then go straight to our kitchen.', [(117, 'Сказал идти на кухню')], ''),
    ('nagiyev', 'Шеф-повар решит, подходите ли вы ресторану.', 'The head chef will decide whether you suit the restaurant.', [(119, 'Хозяин ресторана это не самый главный человек на кухне')], ''),
    ('max', 'Хозяин ресторана отправил меня прямо к шефу.', 'The owner of the restaurant sent me straight to the chef.', [(117, 'Сказал идти на кухню')], ''),
    ('max', 'Главное теперь — понравиться строгому шеф-повару.', 'The main thing now is to please the strict head chef.', [(120, 'Главное чтобы я шефу понравился')], ''),
    ('nagiyev', 'Посмотрим, умеете ли вы вкусно готовить.', 'We shall see whether you know how to cook deliciously.', [(120, 'шефу понравился')], ''),
]
WALK = [
    (0, None, '\'Dmitry Vladimirovich, good afternoon, do you remember me?\' Max uses the full name and father\'s name again. "Pomnite" is "do you remember", formal, and "menya" is "me" as the object.'),
    (1, None, '\'Of course, I do not remember you at all.\' "Konechno zhe" is "of course", with "zhe" leaning on it for emphasis. Then comes "sovsem ne pomnyu", "I don\'t remember at all", so the polite start makes the brush-off sound even ruder.'),
    (2, None, '\'We met with you exactly one year ago.\' "Poznakomilis\'" is "we got acquainted", from "znakomyy", familiar. "God nazad" is "a year back", and "nazad" means "ago" after a time.'),
    (3, None, '\'I have very many important matters today.\' "U menya" is the "I have" pattern. "Del" is the plural of "delo", matter, after "mnogo", many. It\'s the same "dela" Max used when he left Vika.'),
    (4, None, '\'You promised to hire me for this job.\' "Obeshchali" ends in "-li" even for one person, because "vy" is polite. "Vzyat\' na rabotu" is "to take onto work", which means "to hire".'),
    (5, None, '\'Young man, I am in a very big hurry.\' "Speshu" is "I\'m hurrying", all in one word. "Sil\'no", literally "strongly", is another way Russians say "very", and it goes with feelings and hurry rather than with describing words.'),
    (6, None, '\'I am an excellent cook and finished culinary college.\' "Zakonchil", "finished", has "konets", the end, inside it. "Kulinarnyy kolledzh" sounds almost like English: "culinary college".'),
    (7, None, '\'All right, then go straight to our kitchen.\' "Idite" is the formal command "go". "Na nashu kukhnyu" ends in -u because he\'s going there; to be there it would be "na nashey kukhne".'),
    (8, None, '\'The head chef will decide whether you suit the restaurant.\' "Li" means "whether", and it comes right after the key word: "podkhodite li", "do you suit". "Reshit" is "will decide".'),
    (9, None, '\'The owner of the restaurant sent me straight to the chef.\' "Otpravil" is "sent". "K shefu" is "to the chef": after "k", meaning "to a person", "shef" picks up an -u.'),
    (10, None, '\'The main thing now is to please the strict head chef.\' "Ponravit\'sya" is the same root as "mne nravitsya", "I like". It means "to please". "Strogomu" has the ending "-omu" that means "to".'),
    (11, None, '\'We shall see whether you know how to cook deliciously.\' "Posmotrim" is "we shall see", one word. "Umeyete" is "you know how to", for skills. "Vkusno" comes from "vkus", taste.'),
]
