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
    (0, None, '\'You cannot act like this.\' Nagiyev makes this update right away: the single Russian word "nelzya" ("it is not allowed, one must not") sets up the whole statement without needing a separate word for "it is".'),
    (1, None, "'You cannot fire everyone I smile at.' Nagiyev pushes back boldly hearing Nikita, making his position completely clear."),
    (2, None, '\'What beautiful fingers you have.\' Nagiyev spotlights one colorful term on cue: "krasivyye" means "beautiful" (from "krasivyy"), giving the line its exact edge.'),
    (3, None, '\'And what are you doing today?\' Nagiyev sends this answer at once: putting the question word "chto" right at the front of the line lets Nikita hear the point of the question on the very first beat.'),
    (4, None, "'You are fired.' Eleonora holds firm quietly with a nod, shifting the whole mood of the room in a single beat."),
    (5, None, '\'And your fingers too.\' Eleonora grounds one concrete piece at once: "paltsy" means "fingers" (from "palets"), giving the line its exact edge.'),
    (6, None, '\'Alright then, you fired everyone.\' Nagiyev frames the comeback with warmth: tacking on "ladno" ("okay, fine, deal") softens the edge and checks that Eleonora is on board.'),
    (7, None, "'Then who is going to run things today?' Nagiyev challenges curiously about what Nikita just brought up."),
    (8, None, "'Nikita, come here!' Eleonora offers the reply briskly now: spoken Russian trims this down to just 3 words, dropping the extra helper words that English has to spell out."),
    (9, None, "'Congratulations, you are the restaurant director.' Eleonora gives this statement beside Nikita: spoken Russian trims this down to just 4 words, dropping the extra helper words that English has to spell out."),
    (10, None, "'Thank you, Eleonora Andreyevna.' Nikita replies honestly toward Eleonora, before Eleonora can change the subject."),
    (11, None, '\'Nikita Andreyevich, coffee?\' Nagiyev stresses one sharp expression on cue: "andreyevich" means "andreyevich", and it carries the main weight of what Nagiyev is saying.'),
]
