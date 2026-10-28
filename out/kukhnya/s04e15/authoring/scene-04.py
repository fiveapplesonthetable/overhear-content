ID = 'kukhnya-s04e15-scene-04'
SHOW = 'kukhnya'
SEASON = 4
EPISODE = 15
SCENE = 4
TITLE = "Билет на свидание  (Ticket for a Date)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = 'ru-en'
VOICES = {"narrator": "sky", "katya": "angelina", "denis": "anja"}
LABELS = {"katya": "Катя", "denis": "Денис"}
SOURCE_NAME = 'Кухня (Kukhnya) S4.15'
SOURCE_FILE = 'sources/kukhnya/s04/e15.ru.srt'

INTRO = "At Claude Monet, Denis tries to catch Katya's eye while Senya and Fedya grumble about carrying heavy boxes. Katya pulls Denis aside and declares that last night was a fluke and he has zero chance with her—so Denis writes his number on a fifty-ruble note and hands it to Nastya, betting that fate will return the bill to Katya."

STORY = [
    ('katya', 'Мне вообще нельзя такие тяжести таскать!', 'I must not haul such heavy loads at all!', [(47, 'веселей! Да мне вообще')], 'adapted'),
    ('katya', 'У меня от ящиков пальцы станут грубыми.', 'My fingers will become rough from the crates.', [(48, 'У меня пальцы загрубеют,')], 'adapted'),
    ('denis', 'Девушка, мы случайно утром вместе не просыпались?', 'Miss, did we not happen to wake up together this morning?', [(52, 'Мы случайно вместе не')], 'adapted'),
    ('katya', 'Денис, послушай меня внимательно, уймись!', 'Denis, listen to me carefully, calm down!', [(55, 'Послушай, хватит. У тебя')], 'adapted'),
    ('katya', 'У тебя со мной нет никаких шансов.', 'You have no chances with me at all.', [(55, 'Послушай, хватит. У тебя')], 'adapted'),
    ('katya', 'То, что было вчера, — просто случайность!', 'What happened yesterday was just a fluke!', [(56, 'У тебя нет даже')], 'adapted'),
    ('denis', 'Случайность, а может быть, это наша судьба?', 'A fluke, or maybe it is our destiny?', [(57, 'Случайность? А может, это')], 'adapted'),
    ('katya', 'Значит, ты у нас в судьбу веришь?', 'So, you believe in fate then?', [(58, 'Ты на судьбу веришь,')], 'adapted'),
    ('denis', 'Смотри, это билет на свидание со мной.', 'Look, this is a ticket for a date with me.', [(60, 'Это твой билет на')], 'adapted'),
    ('denis', 'Если судьба захочет, эта купюра к тебе вернётся!', 'If fate wants it, this bill will return to you!', [(62, 'то этот полтинник обязательно')], 'adapted'),
    ('denis', 'Настя, возьми, пожалуйста, разменяй эти деньги.', 'Nastya, take this, please, and change this money.', [(59, 'Настя, можно?')], 'adapted'),
    ('katya', 'Какая интересная у вас сегодня игра!', 'What an interesting game you two have today!', [(64, 'Прикольная у вас игра.')], 'adapted'),
]

OPENER = "Let's examine how Denis turns Katya's rejection into a clever bet on fate."

WALK = [
    (0, None, "'I must not haul such heavy loads at all!' Senya pairs 'at all, even' with 'to drag around, to lug' directly, since spoken Russian skips English filler words like 'the', 'a', and 'is'."),
    (1, None, "'My fingers will become rough from the crates.' Russians say 'by me' or 'with us' where English says 'I have' or 'we have', without needing a separate word for 'have'."),
    (2, None, "'Miss, did we not happen to wake up together this morning?' Putting the short word for 'not' right in front of the action word is all Russian needs to make a sentence negative, with no extra helper words like 'do' or 'did'."),
    (3, None, "'Denis, listen to me carefully, calm down!' Katya pulls him aside with two direct singular imperatives."),
    (4, None, "'You have no chances with me at all.' Russians say 'by me' or 'with us' where English says 'I have' or 'we have', without needing a separate word for 'have'."),
    (5, None, "'What happened yesterday was just a fluke!' Notice how Russian puts 'yesterday' and 'accident' together in a short, direct phrase where word endings show how the ideas connect."),
    (6, None, "'A fluke, or maybe it is our destiny?' Denis counters with the feminine noun for fate or destiny."),
    (7, None, "'So, you believe in fate then?' Russians say 'by me' or 'with us' where English says 'I have' or 'we have', without needing a separate word for 'have'."),
    (8, None, "'Look, this is a ticket for a date with me.' Denis writes his number on a fifty-ruble bill and shows it to her."),
    (9, None, "'If fate wants it, this bill will return to you!' Notice how Russian puts 'fate, destiny, fortune' and 'will return' together in a short, direct phrase where word endings show how the ideas connect."),
    (10, None, "'Nastya, take this, please, and change this money.' Denis hands the marked bill to Nastya so it enters the restaurant cash register."),
    (11, None, "'What an interesting game you two have today!' Nastya smiles as she carries the fifty-ruble note back to the bar."),
]

TRANSITION = "Now let's hear the complete fifty-ruble bet scene again without interruption."
OUTRO = "Amused by Denis's romantic game, Nastya puts the fifty-ruble bill into circulation at the bar. Next, Chef Barinov seeks advice from Lyova about Eva. See you next time!"
CLOSING = ("denis", "До встречи!")
