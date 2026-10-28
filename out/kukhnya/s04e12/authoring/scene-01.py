ID = 'kukhnya-s04e12-scene-01'
SHOW = 'kukhnya'
SEASON = 4
EPISODE = 12
SCENE = 1
TITLE = "Свадебный банкет  (The Wedding Banquet)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = 'ru-en'
VOICES = {"narrator": "sky", "sasha": "anja", "vika": "angelina"}
LABELS = {"sasha": "Саша", "vika": "Вика"}
SOURCE_NAME = 'Кухня (Kukhnya) S4.12'
SOURCE_FILE = 'sources/kukhnya/s04/e12.ru.srt'

INTRO = "At the host podium in Claude Monet, Max's ex-girlfriend Sasha cheerfully greets Vika and asks to book a Thursday wedding banquet for thirty guests, triggering an immediate lie from Vika."

STORY = [
    ('sasha', 'Вика, привет, как твои дела?', 'Vika, hi, how are you doing?', [(1, 'Вика, привет')], 'adapted for A1 clarity'),
    ('sasha', 'А я решила отпраздновать здесь свадьбу.', 'And I decided to celebrate my wedding here.', [(2, 'А я решила отпраздновать здесь свадьбу')], ''),
    ('sasha', 'Это ведь здорово, правда?', "That is great, isn't it?", [(3, 'Здорово, правда')], 'adapted for A1 clarity'),
    ('vika', 'Ты хочешь праздновать свадьбу здесь?', 'You want to celebrate your wedding here?', [(4, 'Свадьбу? Здесь')], 'adapted for A1 clarity'),
    ('sasha', 'Ну да, мы с Мишей женимся.', 'Well yes, Misha and I are getting married.', [(5, 'Ну да. Мы с Мишей')], 'adapted for A1 clarity'),
    ('sasha', 'Хотим отпраздновать в узком кругу.', 'We want to celebrate in a close circle.', [(6, 'Хотим отпраздновать в узком кругу')], ''),
    ('sasha', 'Банкет примерно человек на тридцать.', 'A banquet for approximately thirty people.', [(7, 'Банкет приблизительно человек на')], 'adapted for A1 clarity'),
    ('sasha', 'Посмотри, пожалуйста, у вас четверг свободен?', 'Check, please, is Thursday free at your place?', [(8, 'Посмотри, пожалуйста, у вас четверг свободен')], ''),
    ('vika', 'Сейчас посмотрю в нашем журнале.', 'I will look in our logbook right now.', [(8, 'у вас четверг свободен')], 'adapted for A1 clarity'),
    ('vika', 'К сожалению, на этой неделе всё занято.', 'Unfortunately, everything is booked this week.', [(9, 'К сожалению, на этой неделе у нас все занято')], 'adapted for A1 clarity'),
    ('vika', 'Так что извините меня, пожалуйста.', 'So excuse me, please.', [(10, 'Так что извините')], 'adapted for A1 clarity'),
    ('vika', 'Ничем не можем вам помочь.', 'We cannot help you with anything.', [(10, 'ничем я помочь не можем')], 'adapted for A1 clarity'),
]

OPENER = "Let's go through each line of Sasha's request and Vika's polite refusal."

WALK = [
    (0, None, "'Vika, hi, how are you doing?' Sasha greets Max's wife with breezy friendliness."),
    (1, None, "'And I decided to celebrate my wedding here.' Here Sasha anchors the thought on 'decided' and finishes on 'wedding', keeping the spoken rhythm brisk and natural."),
    (2, None, "'That is great, isn't it?' Adding 'truth?' at the end of a statement asks 'right?' or 'isn't it?'."),
    (3, None, "'You want to celebrate your wedding here?' In spoken Russian, the words stay in their normal statement order and Vika's rising voice at the end turns the line into a question."),
    (4, None, "'Well yes, Misha and I are getting married.' Russian says 'we with Misha' to mean 'Misha and I'."),
    (5, None, "'We want to celebrate in a close circle.' Here Sasha anchors the thought on 'want' and finishes on 'circle, ring, buoy', keeping the spoken rhythm brisk and natural."),
    (6, None, "'A banquet for approximately thirty people.' Putting the noun 'people' before 'for thirty' expresses an approximate headcount in Russian."),
    (7, None, "'Check, please, is Thursday free at your place?' The masculine short-form adjective 'free/available' agrees with 'Thursday'."),
    (8, None, "'I will look in our logbook right now.' Vika pretends to study the reservation book while making up her mind."),
    (9, None, "'Unfortunately, everything is booked this week.' The opener 'to regret' means 'unfortunately', and neuter 'all is occupied' shuts the door."),
    (10, None, "'So excuse me, please.' Vika switches to cold, formal plural 'excuse me'."),
    (11, None, "'We cannot help you with anything.' Putting the short word for 'not' right in front of the action word is all Russian needs to make a sentence negative, with no extra helper words like 'do' or 'did'."),
]

TRANSITION = 'Now listen to the whole opening conversation again at natural speed.'
OUTRO = "Notice how Russian says 'in a close circle' with the special locative ending '-u' on 'v uzkom krugu'. Until next time!"
CLOSING = ("sasha", "Всего хорошего!")
