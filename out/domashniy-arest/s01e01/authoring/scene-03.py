# domashniy-arest/s01e01/scene-03.py
ID = "domashniy-arest-s01e01-scene-03"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 1
SCENE = 3
TITLE = "Второй срок  (A Second Term)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
SOURCE_NAME = "Домашний арест (Domashniy Arest) S1.01"
SOURCE_FILE = "sources/domashniy-arest/s01/e01.ru.dual.srt"
VOICES = {"narrator": "sky", "anya": "alisa", "reporter": "angelina"}
LABELS = {"anya": "Аркадий", "reporter": "Журналистка"}
INTRO = "Now we jump forward more than thirty years, to today. Last time, little Arkady was humiliated by Vanya and swore that one day Vanya would beg his forgiveness. Now Arkady is grown up and the mayor of Sineozersk, and he is on a stage in front of the town hall, giving a speech and answering reporters. Let's listen in Russian first."
STORY = [
    ("anya", "Спасибо, спасибо! Как вы все знаете, я родился и вырос в Синеозерске.", "Thank you, thank you! As you all know, I was born and grew up in Sineozersk.", [(109, 'Спасибо, спасибо'), (110, 'Как вы все знаете, я родился и вырос в')], "'в нашем Синей Озерске' -> 'в Синеозерске' (standard name of the town)"),
    ("anya", "Детство у меня было трудное. Я вырос в коммуналке.", "My childhood was hard. I grew up in a communal flat.", [(111, 'Детство у меня было трудное'), (112, 'Я вырос в коммуналке')], ""),
    ("anya", "Я знаю проблемы простых людей.", "I know the problems of ordinary people.", [(112, 'проблемы простых людей')], "'видел ... изнутри' (saw from the inside) -> 'знаю' (know)"),
    ("anya", "Я уже четыре года работаю мэром.", "I've been working as mayor for four years now.", [(113, 'четыре года'), (113, 'мэром')], "'За четыре года моей работы мэром' rephrased"),
    ("anya", "Мы сделали много, но надо сделать ещё больше.", "We've done a lot, but we need to do even more.", [(113, 'сделать еще больше')], "'было сделано немало, но предстоит' simplified"),
    ("anya", "Я очень люблю наш город. Поэтому я иду на второй срок.", "I love our town very much. That's why I'm running for a second term.", [(114, 'наш город'), (115, 'Поэтому я'), (115, 'на второй срок')], "'хочу, чтобы наш город ... процветал' -> 'люблю наш город'; 'выдвигаю свою кандидатуру' -> 'иду'"),
    ("anya", "Спасибо за доверие!", "Thank you for your trust!", [(116, 'Спасибо за доверие')], ""),
    ("reporter", "Аркадий Борисович, кто ваши конкуренты?", "Arkady Borisovich, who are your rivals?", [(117, 'Аркадий Борисович, кто ваши'), (117, 'конкуренты')], "'основные' (main) dropped"),
    ("anya", "Мне некогда об этом думать. Слишком много дел.", "I have no time to think about that. There's too much to do.", [(118, 'Мне некогда об этом думать'), (118, 'Слишком много дел')], ""),
    ("reporter", "Скажите, когда будет ваша программа?", "Tell us, when will your programme be out?", [(119, 'Скажите, когда')], "'вы озвучите' (you will announce) -> 'будет'"),
    ("anya", "На днях, на сайте.", "Any day now, on the website.", [(120, 'На днях, на сайте')], "'администрации' dropped"),
    ("reporter", "А вас поддерживает губернатор?", "And does the governor support you?", [(121, 'поддерживает губернатор')], "'вашу кандидатуру' -> 'вас'"),
    ("anya", "Самое главное — это народ.", "The most important thing is the people.", [(122, 'Самое главное')], "'чтобы меня поддерживал народ' simplified; he still dodges the question"),
    ("reporter", "Спасибо, Аркадий Борисович!", "Thank you, Arkady Borisovich!", [], "the reporter closes the interview"),
]
OPENER = "Let's go through it line by line. The crowd is clapping as Arkady steps up to the microphone, and he thanks them twice."
WALK = [
    (0, 'Спасибо, спасибо!', "'Thank you, thank you!' Then he reminds everyone where he comes from."),
    (0, 'Как вы все знаете, я родился и вырос в Синеозерске.', "'As you all know, I was born and grew up in Sineozersk.' Two verbs in the past: 'was born' and 'grew up'. They end in a plain consonant because Arkady is a man. Now the sad part of the story."),
    (1, 'Детство у меня было трудное.', "'My childhood was hard.' Literally, 'childhood at me was hard'. It's the same 'at me' you use to say what you have. Then a detail we saw for ourselves."),
    (1, 'Я вырос в коммуналке.', "'I grew up in a communal flat.' A communal flat is one flat shared by several families, with one kitchen and one toilet, just like the one in the last scene. So he makes a claim."),
    (2, None, "'I know the problems of ordinary people.' A politician's favourite line. Then he talks about his job."),
    (3, None, "'I've been working as mayor for four years now.' Russian uses the present tense here, 'I work', where English says 'I've been working'. And after the verb 'to work as', the job takes a special ending. Then a classic promise."),
    (4, None, "'We've done a lot, but we need to do even more.' The word for 'need' is the same one little Vanya used about the toilet. Then the big news."),
    (5, 'Я очень люблю наш город.', "'I love our town very much.' The word for 'very' comes before the verb, as in 'I very love'. And so he makes his announcement."),
    (5, 'Поэтому я иду на второй срок.', "'That's why I'm running for a second term.' Literally, 'I'm going for a second term', the everyday way to say a politician stands again. He finishes politely."),
    (6, None, "'Thank you for your trust!' The word for 'for' here is the one you use when you thank someone for something. Then the questions start."),
    (7, None, "'Arkady Borisovich, who are your rivals?' Notice the reporter uses his first name and his father's name, the respectful way to address someone in Russian. Arkady brushes it off."),
    (8, 'Мне некогда об этом думать.', "'I have no time to think about that.' Literally, 'to me there's no time to think about it'. He gives a reason."),
    (8, 'Слишком много дел.', "'There's too much to do.' Literally, 'too many things to do'. Another question."),
    (9, None, "'Tell us, when will your programme be out?' The first word is the polite command for 'tell'. His programme means his plans for the town."),
    (10, None, "'Any day now, on the website.' The first two words mean 'in the next few days'. Then the awkward question."),
    (11, None, "'And does the governor support you?' The governor runs the whole region and is Arkady's political boss. Watch how he answers."),
    (12, None, "'The most important thing is the people.' A nice answer, and it doesn't say yes or no. The reporter gives up."),
    (13, None, "'Thank you, Arkady Borisovich!' Again the polite name and patronymic."),
]
TRANSITION = "Here's his speech once more, all the way through."
OUTRO = "So that's Arkady in public: the boy from the communal flat, now a smooth politician who dodges hard questions. Watch for those reporters' questions when you see the episode. See you next time!"
CLOSING = ("anya", "До свидания!")
