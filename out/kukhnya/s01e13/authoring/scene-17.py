# Authoring module for kukhnya-s01e13-scene-17.
ID = 'kukhnya-s01e13-scene-17'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 13
SCENE = 17
TITLE = 'Неловкая встреча  (An Awkward Encounter)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'nastya': 'Настя', 'vika': 'Вика'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.13'
SOURCE_FILE = 'sources/kukhnya/s01/e13.ru.dual.srt'
INTRO = "Vika is trying to slip out of Max's flat unnoticed, but Nastya is standing in the hallway. Here is how that goes, in Russian."
OPENER = 'The awkward conversation again, slowly.'
TRANSITION = 'Here is the hallway meeting from the top.'
OUTRO = "Nastya promises to keep quiet, with the same triple 'no' Kostya used at the bar. Bye for now."
CLOSING = ('vika', 'Пока!')
STORY = [
    ('nastya', 'Здравствуйте, Виктория Сергеевна.', 'Hello, Victoria Sergeyevna.', [(240, 'Здрасте, Виктория Сергеевна')], ''),
    ('vika', 'Доброе утро, Настя.', 'Good morning, Nastya.', [(240, 'Привет, Настя')], ''),
    ('nastya', 'Проходите, я уже всё закончила.', 'Come in, I am already done.', [(241, 'Проходите, я уже закончила')], ''),
    ('vika', 'Спасибо, я просто ухожу на работу.', 'Thank you, I am just leaving for work.', [], ''),
    ('nastya', 'Извините, я сегодня немного опоздаю.', 'Excuse me, I will be a little late today.', [(242, 'извините, пожалуйста, я, наверное, сегодня немножко задержусь')], ''),
    ('vika', 'Да, я всё прекрасно понимаю.', 'Yes, I understand everything perfectly.', [(243, 'Да-да, я понимаю')], ''),
    ('vika', 'Я сегодня тоже задержусь немного.', 'I will also be delayed a bit today.', [(243, 'Я, наверное, тоже')], ''),
    ('nastya', 'Вы провели здесь всю ночь?', 'Did you spend the whole night here?', [], ''),
    ('nastya', 'Вы теперь встречаетесь с Максимом?', 'Are you seeing Maxim now?', [(244, 'а вы с Максимом?')], ''),
    ('vika', 'Настя, не задавай глупых вопросов.', 'Nastya, do not ask silly questions.', [(245, 'Настя')], ''),
    ('nastya', 'Всё, я молчу и всё поняла.', 'That is all, I am silent and understood everything.', [(245, 'Все-все, я поняла')], ''),
    ('vika', 'В ресторане об этом никто не знает.', 'No one at the restaurant knows about this.', [], ''),
    ('nastya', 'Я никому ничего не скажу, обещаю.', 'I will not tell anyone anything, I promise.', [], ''),
]
WALK = [
    (0, None, "'Hello, Victoria Sergeyevna.' 'Zdravstvuyte' is the polite, long hello. Nastya uses name plus father's name, as she would for her boss."),
    (1, None, "'Good morning, Nastya.' Vika answers with just the first name, while Nastya used the full name. 'Dobroe' ends in 'oe' to match 'utro', which is neuter."),
    (2, None, "'Come in, I am already done.' 'Prokhodite' means 'go through', so it works for letting someone pass. 'Zakonchila' means 'finished', with an 'a' for a woman."),
    (3, None, "'Thank you, I am just leaving for work.' 'Ukhozhu' is 'I am going away', with the 'u' that means 'away'. 'Na rabotu' is 'to work', and 'rabota' becomes 'rabotu' for the direction."),
    (4, None, "'Excuse me, I will be a little late today.' 'Opozdayu' is 'I will be late'. 'Izvinite' is the polite 'excuse me', and 'nemnogo' means 'a little'."),
    (5, None, "'Yes, I understand everything perfectly.' 'Prekrasno' means 'beautifully', but here it just says 'perfectly well'. 'Ponimayu' is 'I understand'."),
    (6, None, "'I will also be delayed a bit today.' 'Zaderzhus' is literally 'I will hold myself back', and the 's' on the end is a short 'sya'. 'Tozhe' is 'also'."),
    (7, None, "'Did you spend the whole night here?' 'Proveli' is 'spent', for time. 'Vsyu noch' is 'the whole night', where 'noch' picks up a 'yu' ending."),
    (8, None, "'Are you seeing Maxim now?' Word for word, 'are you meeting each other', and that's how Russians ask whether two people are a couple. 'Maksim' is the full form of Max."),
    (9, None, "'Nastya, do not ask silly questions.' Russian says 'give a question' for 'ask a question', 'zadavat vopros'. 'Ne zadavay' is 'don't ask', and 'glupykh' means 'of silly'."),
    (10, None, "'That is all, I am silent and understood everything.' 'Vsyo' at the start is 'that's it'. 'Molchu' is 'I'm silent', and 'ponyala' is 'I understood', in a woman's form."),
    (11, None, "'No one at the restaurant knows about this.' 'Nobody' and 'not' sit next to each other in the sentence. Russian wants both, so 'nikto ne znaet' is 'nobody doesn't know'."),
    (12, None, "'I will not tell anyone anything, I promise.' 'Nikomu nichego ne' has three negatives in a row. 'Skazhu', I will say, and 'obeshchayu', I promise, each do the job of several English words."),
]
