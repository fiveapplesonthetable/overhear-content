ID = "kukhnya-s04e06-scene-08"
SHOW = "kukhnya"
SEASON = 4
EPISODE = 6
SCENE = 8
TITLE = "Бутылка за пять тысяч  (The Five-Thousand-Dollar Bottle)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "kostya": "anja", "vika": "angelina"}
LABELS = {"anya": "Макс", "kostya": "Костя", "vika": "Вика"}
SOURCE_NAME = "Кухня (Kukhnya) S4.06"
SOURCE_FILE = "sources/kukhnya/s04/e06.ru.srt"
SOURCE_NOTE = "Cues 99-118. At the bar, Kostya searches frantically for a rare bottle of wine that Dmitry Nagiyev entrusted to him, and is horrified when Max admits he drank it with Vika."

INTRO = "Out at the bar counter, Kostya is frantically searching the shelves for a special bottle of wine. Max casually mentions that he borrowed it for his romantic dinner with Vika, only for Kostya to reveal that the bottle belongs to Dmitry Nagiyev and costs five thousand dollars!"

STORY = [
    ("anya", "Костя, привет, что ты тут потерял?", "Kostya, hi, what did you lose here?", [(99, "Костян, здорово."), (100, "Что потерял?")], "adapted"),
    ("kostya", "Я одну дорогую бутылку не могу найти.", "I cannot find one expensive bottle.", [(100, "бутылку одну не могу найти.")], "adapted"),
    ("anya", "Я вчера вечером одолжил её у тебя.", "I borrowed it from you last night.", [(102, "Я вчера у тебя ее одолжил")], "adapted"),
    ("anya", "Взял домой для нашего романтического ужина.", "I took it home for our romantic dinner.", [(102, "для романтического ужина.")], "adapted"),
    ("kostya", "Макс, какого ещё романтического ужина?", "Max, what romantic dinner on earth?", [(103, "Макс, какого нафиг ужина?")], "adapted"),
    ("anya", "Не волнуйся, я тебе возмещу всю стоимость.", "Do not worry, I will reimburse you the full cost.", [(104, "Я тебе все возмещу по себестоимости.")], "adapted"),
    ("anya", "Сколько она стоит, одну или две тысячи?", "How much does it cost, one or two thousand?", [(105, "Сколько стоит? Тысячу, две?")], "adapted"),
    ("kostya", "Эту бутылку вчера оставил сам Дмитрий Владимирович!", "Dmitry Vladimirovich himself left this bottle yesterday!", [(106, "вчера на корпорации подогнали"), (107, "Пускай у тебя полежит на завтра.")], "adapted"),
    ("kostya", "Ты знаешь, сколько стоит эта редкая бутылка?", "Do you know how much this rare bottle costs?", [(109, "Знаешь, сколько стоит?")], "adapted"),
    ("kostya", "Она стоит ровно пять тысяч долларов!", "It costs exactly five thousand dollars!", [(110, "Пять тысяч долларов.")], "adapted"),
    ("anya", "Ничего себе, а я только с Викой помирился!", "Whoa, and I just made up with Vika!", [(114, "Офигеть."), (115, "А я ведь только с Викой помирился.")], "adapted"),
    ("kostya", "Неплохое примирение за пять тысяч долларов!", "Not a bad reconciliation for five thousand dollars!", [(116, "Неплохое такое примирение за пять тысяч баков.")], "adapted"),
    ("vika", "Костя, привет, сделай мне, пожалуйста, кофе.", "Kostya, hi, please make me a coffee.", [(118, "Привет. Сделай мне, пожалуйста, кофе.")], "adapted"),
]

OPENER = "Let's break down Max and Kostya's shock over the five-thousand-dollar wine line by line."

WALK = [
    (0, None, "'Kostya, hi, what did you lose here?' Max greets his friend with a past-tense perfective question."),
    (1, None, "'I cannot find one expensive bottle.' Feminine accusative endings mark the missing bottle."),
    (2, None, "'I borrowed it from you last night.' Perfective past verb 'borrowed' takes 'at/from you' in the genitive."),
    (3, None, "'I took it home for our romantic dinner.' Preposition 'for' governs the genitive singular phrase."),
    (4, None, "'Max, what romantic dinner on earth?' Kostya echoes the genitive phrase in sheer disbelief."),
    (5, None, "'Do not worry, I will reimburse you the full cost.' First-person perfective future verb promises financial reimbursement."),
    (6, None, "'How much does it cost, one or two thousand?' Max assumes it is an ordinary restaurant bottle."),
    (7, None, "'Dmitry Vladimirovich himself left this bottle yesterday!' Emphatic pronoun highlights the celebrity owner's name."),
    (8, None, "'Do you know how much this rare bottle costs?' Indirect question clause retains the verb 'costs'."),
    (9, None, "'It costs exactly five thousand dollars!' Both 'thousand' and 'dollars' stand in the genitive plural after 'five'."),
    (10, None, "'Whoa, and I just made up with Vika!' Reflexive perfective past verb means reconciling after a quarrel."),
    (11, None, "'Not a bad reconciliation for five thousand dollars!' Kostya remarks dryly on the price of Max's romance."),
    (12, None, "'Kostya, hi, please make me a coffee.' Vika walks up to the bar just as Max tries to process the disaster."),
]

TRANSITION = "Now let's listen to the bar conversation about the expensive bottle again."
OUTRO = "Stunned by the five-thousand-dollar price tag, Max decides he has to tell Vika the truth about what they drank last night. See you in the next scene."
CLOSING = ("kostya", "Она стоит ровно пять тысяч долларов!")
CLOSING_TRANS = "It costs exactly five thousand dollars!"
