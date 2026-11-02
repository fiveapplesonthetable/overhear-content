# Authoring module for domashniy-arest-s01e01-scene-03.
ID = 'domashniy-arest-s01e01-scene-03'
SHOW = 'domashniy-arest'
SEASON = 1
EPISODE = 1
SCENE = 3
TITLE = 'Второй срок  (A Second Term)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'arkady': 'Аркадий', 'reporter': 'Журналистка'}
SOURCE_NAME = 'Домашний арест (Domashniy Arest) S1.01'
SOURCE_FILE = 'sources/domashniy-arest/s01/e01.ru.dual.srt'
INTRO = "Now we jump forward more than thirty years, to today. Last time, little Arkady was humiliated by Vanya and swore that one day Vanya would beg his forgiveness. Now Arkady is grown up and the mayor of Sineozersk, and he is on a stage in front of the town hall, giving a speech and answering reporters. Let's listen in Russian first."
OPENER = "Let's go through it line by line. The crowd is clapping as Arkady steps up to the microphone, and he thanks them twice."
TRANSITION = "Here's his speech once more, all the way through."
OUTRO = "So that's Arkady in public: the boy from the communal flat, now a smooth politician who dodges hard questions. Watch for those reporters' questions when you see the episode. See you next time!"
CLOSING = ('arkady', 'До свидания!')
STORY = [
    ('arkady', 'Спасибо, спасибо! Как вы все знаете, я родился и вырос в Синеозерске.', 'Thank you, thank you! As you all know, I was born and grew up in Sineozersk.', [(109, 'Спасибо, спасибо'), (110, 'Как вы все знаете, я родился и вырос в')], "'в нашем Синей Озерске' -> 'в Синеозерске' (standard name of the town)"),
    ('arkady', 'Детство у меня было трудное. Я вырос в коммуналке.', 'My childhood was hard. I grew up in a communal flat.', [(111, 'Детство у меня было трудное'), (112, 'Я вырос в коммуналке')], ''),
    ('arkady', 'Я знаю проблемы простых людей.', 'I know the problems of ordinary people.', [(112, 'проблемы простых людей')], "'видел ... изнутри' (saw from the inside) -> 'знаю' (know)"),
    ('arkady', 'Я уже четыре года работаю мэром.', "I've been working as mayor for four years now.", [(113, 'четыре года'), (113, 'мэром')], "'За четыре года моей работы мэром' rephrased"),
    ('arkady', 'Мы сделали много, но надо сделать ещё больше.', "We've done a lot, but we need to do even more.", [(113, 'сделать еще больше')], "'было сделано немало, но предстоит' simplified"),
    ('arkady', 'Я очень люблю наш город. Поэтому я иду на второй срок.', "I love our town very much. That's why I'm running for a second term.", [(114, 'наш город'), (115, 'Поэтому я'), (115, 'на второй срок')], "'хочу, чтобы наш город ... процветал' -> 'люблю наш город'; 'выдвигаю свою кандидатуру' -> 'иду'"),
    ('arkady', 'Спасибо за доверие!', 'Thank you for your trust!', [(116, 'Спасибо за доверие')], ''),
    ('reporter', 'Аркадий Борисович, кто ваши конкуренты?', 'Arkady Borisovich, who are your rivals?', [(117, 'Аркадий Борисович, кто ваши'), (117, 'конкуренты')], "'основные' (main) dropped"),
    ('arkady', 'Мне некогда об этом думать. Слишком много дел.', "I have no time to think about that. There's too much to do.", [(118, 'Мне некогда об этом думать'), (118, 'Слишком много дел')], ''),
    ('reporter', 'Скажите, когда будет ваша программа?', 'Tell us, when will your programme be out?', [(119, 'Скажите, когда')], "'вы озвучите' (you will announce) -> 'будет'"),
    ('arkady', 'На днях, на сайте.', 'Any day now, on the website.', [(120, 'На днях, на сайте')], "'администрации' dropped"),
    ('reporter', 'А вас поддерживает губернатор?', 'And does the governor support you?', [(121, 'поддерживает губернатор')], "'вашу кандидатуру' -> 'вас'"),
    ('arkady', 'Самое главное — это народ.', 'The most important thing is the people.', [(122, 'Самое главное')], "'чтобы меня поддерживал народ' simplified; he still dodges the question"),
    ('reporter', 'Спасибо, Аркадий Борисович!', 'Thank you, Arkady Borisovich!', [], 'the reporter closes the interview'),
]
WALK = [
    (0, 'Спасибо, спасибо!', [
        "'Thank you, thank you!' Repeating the term meaning 'thank you', ",
        ('arkady', "спасибо"),
        ", twice warms up the crowd before he starts his speech."
    ]),
    (0, 'Как вы все знаете, я родился и вырос в Синеозерске.', [
        "'As you all know, I was born and grew up in Sineozersk.' ",
        ('arkady', "Родился"),
        " ('was born') and ",
        ('arkady', "вырос"),
        " ('grew up') are the past action words for a man. Now comes the sad part of his story."
    ]),
    (1, 'Детство у меня было трудное.', [
        "'My childhood was hard.' Literally, 'childhood at me was hard' — ",
        ('arkady', "у меня"),
        " works just like saying what you have. Then a detail we saw for ourselves."
    ]),
    (1, 'Я вырос в коммуналке.', [
        "'I grew up in a communal flat.' the translation for a shared Soviet flat, ",
        ('arkady', "коммуналке"),
        ", is everyday shorthand where several families share one kitchen and toilet. So he makes a claim."
    ]),
    (2, None, [
        "'I know the problems of ordinary people.' ",
        ('arkady', "Простых людей"),
        " literally translates to 'of simple people', a politician's favourite phrase. Then he talks about his job."
    ]),
    (3, None, [
        "'I've been working as mayor for four years now.' Russian uses the present action word ",
        ('arkady', "работаю"),
        " ('I work') where English says 'I've been working', and ",
        ('arkady', "мэром"),
        " is built from the Russian for mayor with a little ending."
    ]),
    (4, None, [
        "'We've done a lot, but we need to do even more.' which translates to 'we need to', ",
        ('arkady', "надо"),
        ", is the very same everyday word little Vanya used back in the bathroom. Then the big news."
    ]),
    (5, 'Я очень люблю наш город.', [
        "'I love our town very much.' In Russian, the term meaning 'very much', ",
        ('arkady', "очень"),
        ", sits right before ",
        ('arkady', "люблю"),
        ", as if saying 'I very love our town'. So he makes his announcement."
    ]),
    (5, 'Поэтому я иду на второй срок.', [
        "'That's why I'm running for a second term.' Literally, 'I'm going onto a second term' — ",
        ('arkady', "иду на второй срок"),
        " — how Russian talks about standing again. He finishes politely."
    ]),
    (6, None, [
        "'Thank you for your trust!' ",
        ('arkady', "Спасибо за"),
        " is the go-to pattern whenever you thank someone for something, here the Russian for 'trust', ",
        ('arkady', "доверие"),
        ". Then the questions start."
    ]),
    (7, None, [
        "'Arkady Borisovich, who are your rivals?' Addressing him by first name plus his father's name, ",
        ('reporter', "Борисович"),
        ", translates to 'son of Boris' and is standard polite Russian. Arkady brushes it off."
    ]),
    (8, 'Мне некогда об этом думать.', [
        "'I have no time to think about that.' ",
        ('arkady', "Мне некогда"),
        " literally translates to 'to me there is no time' packed into just two words. He gives a reason."
    ]),
    (8, 'Слишком много дел.', [
        "'There's too much to do.' the term meaning 'excessively', ",
        ('arkady', "слишком"),
        ", adds the sense of 'too' before ",
        ('arkady', "много дел"),
        " ('many matters'). Another question."
    ]),
    (9, None, [
        "'Tell us, when will your programme be out?' ",
        ('reporter', "Скажите"),
        " is the polite 'tell us!' built from a polite ending on the action word, and ",
        ('reporter', "программа"),
        " translates to his election manifesto."
    ]),
    (10, None, [
        "'Any day now, on the website.' ",
        ('arkady', "На днях"),
        " literally translates to 'on the days', a handy chunk for 'in the next few days'. Then comes the awkward question."
    ]),
    (11, None, [
        "'And does the governor support you?' ",
        ('reporter', "Губернатор"),
        " translates to the one who runs the whole region, and putting ",
        ('reporter', "вас"),
        " ('you') up front spotlights Arkady before the action word ",
        ('reporter', "поддерживает"),
        " ('supports'). Watch how he answers."
    ]),
    (12, None, [
        "'The most important thing is the people.' ",
        ('arkady', "Самое главное"),
        " ('the main thing') linked by a spoken pause to ",
        ('arkady', "народ"),
        ", the term for 'the people', dodges answering yes or no. The reporter gives up."
    ]),
    (13, None, [
        "'Thank you, Arkady Borisovich!' Once again the polite pairing of first name and father's name closes the exchange."
    ]),
]
