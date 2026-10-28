ID = "kukhnya-s02e03-scene-19"
SHOW = "kukhnya"
SEASON = 2
EPISODE = 3
SCENE = 19
TITLE = 'Быстрая реакция  (Quick Reaction)'
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "sasha": "anja", "vika": "angelina"}
LABELS = {"anya": "Макс", "sasha": "Саша", "vika": "Вика"}
SOURCE_NAME = "Кухня (Kukhnya) S2.03"
SOURCE_FILE = "sources/kukhnya/s02/e03.ru.dual.srt"
SOURCE_NOTE = "Scene 19"

INTRO = 'Max thanks his colleague Sasha for saving him from an awkward situation. Meanwhile, Vika approaches Max, treating him sarcastically like a difficult customer who overstayed his welcome.'

STORY = [
    ('anya', 'Саша, спасибо.',
     'Sasha, thanks.',
     [(287, 'Саша, спасибо')], 'adapted'),
    ('anya', 'Выручила, быстро соображаешь.',
     'You saved me. That was quick thinking.',
     [(288, 'Выручила, быстро соображаешь')], 'adapted'),
    ('sasha', 'Да ладно, все нормально.',
     'Oh, do not mention it.',
     [(289, 'Да ладно, все нормально')], 'adapted'),
    ('anya', 'Я твой должник навсегда.',
     'I am your debtor forever.',
     [], 'new'),
    ('sasha', 'Будешь должен мне услугу.',
     'You will owe me a favor.',
     [], 'new'),
    ('anya', 'А, кстати, та девушка ничего мне не передавала?',
     'By the way, did that girl leave a message for me?',
     [(290, 'та девушка ничего мне не передавала')], 'adapted'),
    ('sasha', 'Понятия не имею. Я даже не видела, как она свалила.',
     'No idea. I did not even see her leave.',
     [(291, 'Понятия не имею, я даже не видела, как она свалила')], 'adapted'),
    ('anya', 'Ладно, пойду работать дальше.',
     'Alright, I will go back to work.',
     [], 'new'),
    ('vika', 'Простите, может быть, вы хотели попросить счет?',
     'Excuse me, would you like the check?',
     [(292, 'может быть, вы хотели попросить счет')], 'adapted'),
    ('anya', 'Нет, спасибо, я еще посижу.',
     'No, thanks. I will stay a little longer.',
     [(293, 'Нет, спасибо, я еще посижу')], 'adapted'),
    ('anya', 'Хочу лично поблагодарить повара.',
     'I would like to thank the chef personally.',
     [(294, 'Хочу лично поблагодарить повара')], 'adapted'),
    ('vika', 'Понятно.',
     'I see.',
     [(295, 'Понятно')], 'adapted'),
]

OPENER = "Let us break down this interaction."

WALK = [
    (1, None,
     "'You saved me. That was quick thinking.' Listen for the word meaning 'to help out' right alongside 'quickly' in this line."),
    (5, None,
     "'By the way, did that girl leave a message for me?' There is no question word here — in Russian, rising intonation on 'pass on' is enough to make it a question. Sasha answers straight away."),
    (6, None,
     "'No idea. I did not even see her leave.' You'll hear 'concept' all the time in the show, here connected with 'take off'."),
    (8, None,
     "'Excuse me, would you like the check?' Notice the word order: 'excuse me' comes first, and 'bill' finishes the sentence."),
    (10, None,
     "'I would like to thank the chef personally.' A compact expression built around 'want' and 'cook'."),
]

TRANSITION = "Now let us listen to the conversation again without interruption."
OUTRO = "Max plays along with Vika's joke, pretending to be a highly satisfied guest at the restaurant."
CLOSING = ('vika', 'Понятно.')
