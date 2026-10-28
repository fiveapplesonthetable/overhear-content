# Authoring module for kukhnya-s06e01-scene-05.
ID = 'kukhnya-s06e01-scene-05'
SHOW = 'kukhnya'
SEASON = 6
EPISODE = 1
SCENE = 5
TITLE = 'Новый директор ресторана  (The New Restaurant Director)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'eleonora': 'Элеонора', 'nagiyev': 'Нагиев', 'nikita': 'Никита'}
SOURCE_NAME = 'Кухня (Kukhnya) S6.01'
SOURCE_FILE = 'sources/kukhnya/s06/e01.ru.srt'
INTRO = "As Dmitry Nagiyev protests that his bride cannot fire everyone he smiles at, he compliments the female pianist's fingers—prompting Eleonora to fire her too and appoint waiter Nikita as the new restaurant director."
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = 'In a matter of seconds, Nikita goes from waiter to restaurant director, while the wedding still lacks a pianist. Until next time!'
CLOSING = ('eleonora', 'До встречи!')
STORY = [
    ('nagiyev', 'Нельзя так делать.', 'You cannot act like this.', [(65, 'Нельзя так')], 'adapted'),
    ('nagiyev', 'Нельзя увольнять всех, кому я улыбаюсь.', 'You cannot fire everyone I smile at.', [(66, 'Нельзя увольнять всех, кому я улыбаюсь')], 'exact'),
    ('nagiyev', 'Какие красивые у вас пальцы.', 'What beautiful fingers you have.', [(69, 'Какие красивые у вас пальцы')], 'exact'),
    ('nagiyev', 'А что вы делаете сегодня?', 'And what are you doing today?', [(70, 'А что вы сегодня')], 'adapted'),
    ('eleonora', 'Вы уволены.', 'You are fired.', [(71, 'Вы уволены')], 'exact'),
    ('eleonora', 'И ваши пальцы тоже.', 'And your fingers too.', [(72, 'И ваши пальцы тоже')], 'exact'),
    ('nagiyev', 'Ну ладно, ты уволила всех.', 'Alright then, you fired everyone.', [(73, 'Ну ладно, ты уволила')], 'adapted'),
    ('nagiyev', 'А кто работать будет сегодня?', 'Then who is going to run things today?', [(77, 'Кто рулить-то будет')], 'adapted'),
    ('eleonora', 'Никита, иди сюда!', 'Nikita, come here!', [(78, 'Никита!')], 'adapted'),
    ('eleonora', 'Поздравляю, ты директор ресторана.', 'Congratulations, you are the restaurant director.', [(80, 'Поздравляю. С этой минуты ты директор ресторана')], 'adapted'),
    ('nikita', 'Спасибо, Элеонора Андреевна.', 'Thank you, Eleonora Andreyevna.', [(80, 'Поздравляю')], 'adapted'),
    ('nagiyev', 'Никита Андреевич, кофе?', 'Nikita Andreyevich, coffee?', [(81, 'Никита Андреевич, кофе?')], 'exact'),
]
WALK = [
    (0, None, '\'You cannot act like this.\' Leaning in plainly with Eleonora, Nagiyev leans on "nelzya" ("it is not allowed, one must not"), which carries the whole predicate in Russian without needing "it is".'),
    (1, None, "'You cannot fire everyone I smile at.' Nagiyev chimes in boldly in their talk, without trying to dress up how he really feels."),
    (2, None, '\'What beautiful fingers you have.\' Talking about the fingers with Eleonora, Nagiyev chooses "krasivyye" ("beautiful", from the root "krasivyy") so Eleonora hears the exact meaning.'),
    (3, None, '\'And what are you doing today?\' Reacting evenly in front of Eleonora, Nagiyev puts the question word "chto" right at the start so Eleonora hears the focus immediately.'),
    (4, None, "'You are fired.' Eleonora answers quietly toward Nagiyev, grounding the moment in plain reality."),
    (5, None, '\'And your fingers too.\' Addressing the fingers during the talk, Eleonora reaches for the Russian word "paltsy" ("fingers", built from "palets") right at the center of the line.'),
    (6, None, "'Alright then, you fired everyone.' Nagiyev replies plainly across the room, so Eleonora knows he is not just making small talk."),
    (7, None, "'Then who is going to run things today?' Nagiyev challenges curiously where this conversation is heading next."),
    (8, None, "'Nikita, come here!' Pressing on earnestly right here, spoken Russian compresses the whole thought into just 3 words, skipping the extra helper words English needs."),
    (9, None, "'Congratulations, you are the restaurant director.' Reacting readily to Nikita, spoken Russian compresses the whole thought into just 4 words, skipping the extra helper words English needs."),
    (10, None, '\'Thank you, Eleonora Andreyevna.\' Nikita smoothly chooses this word of thanks at the start of the beat using "spasibo" ("thank you") — the everyday word for "thank you", which grew out of the old blessing "spasi Bog" ("God save you").'),
    (11, None, '\'Nikita Andreyevich, coffee?\' Mentioning the coffee to Nikita, Nagiyev centers the remark on "andreyevich" ("andreyevich") without any extra fuss.'),
]
