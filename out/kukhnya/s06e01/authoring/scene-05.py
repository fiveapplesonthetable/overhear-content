ID = 'kukhnya-s06e01-scene-05'
SHOW = 'kukhnya'
SEASON = 6
EPISODE = 1
SCENE = 5
TITLE = "Новый директор ресторана  (The New Restaurant Director)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = 'ru-en'
VOICES = {"narrator": "sky", "nagiyev": "angelina", "nikita": "anja"}
LABELS = {"nagiyev": "Нагиев", "nikita": "Никита"}
SOURCE_NAME = 'Кухня (Kukhnya) S6.01'
SOURCE_FILE = 'sources/kukhnya/s06/e01.ru.srt'

INTRO = "As Dmitry Nagiyev protests that his bride cannot fire everyone he smiles at, he compliments the female pianist's fingers—prompting Eleonora to fire her too and appoint waiter Nikita as the new restaurant director."

STORY = [
    ('nagiyev', 'Нельзя так делать.', 'You cannot act like this.', [(65, 'Нельзя так')], 'adapted'),
    ('nagiyev', 'Нельзя увольнять всех, кому я улыбаюсь.', 'You cannot fire everyone I smile at.', [(66, 'Нельзя увольнять всех, кому я улыбаюсь')], 'exact'),
    ('nagiyev', 'Какие красивые у вас пальцы.', 'What beautiful fingers you have.', [(69, 'Какие красивые у вас пальцы')], 'exact'),
    ('nagiyev', 'А что вы делаете сегодня?', 'And what are you doing today?', [(70, 'А что вы сегодня')], 'adapted'),
    ('nagiyev', 'Вы уволены.', 'You are fired.', [(71, 'Вы уволены')], 'exact'),
    ('nagiyev', 'И ваши пальцы тоже.', 'And your fingers too.', [(72, 'И ваши пальцы тоже')], 'exact'),
    ('nagiyev', 'Ну ладно, ты уволила всех.', 'Alright then, you fired everyone.', [(73, 'Ну ладно, ты уволила')], 'adapted'),
    ('nagiyev', 'А кто работать будет сегодня?', 'Then who is going to run things today?', [(77, 'Кто рулить-то будет')], 'adapted'),
    ('nagiyev', 'Никита, иди сюда!', 'Nikita, come here!', [(78, 'Никита!')], 'adapted'),
    ('nagiyev', 'Поздравляю, ты директор ресторана.', 'Congratulations, you are the restaurant director.', [(80, 'Поздравляю. С этой минуты ты директор ресторана')], 'adapted'),
    ('nikita', 'Спасибо, Элеонора Андреевна.', 'Thank you, Eleonora Andreyevna.', [(80, 'Поздравляю')], 'adapted'),
    ('nagiyev', 'Никита Андреевич, кофе?', 'Nikita Andreyevich, coffee?', [(81, 'Никита Андреевич, кофе?')], 'exact'),
]

OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."

WALK = [
    (0, None, "'You cannot act like this.' Spoken Russian keeps this brisk, leaning on 'one must not' and finishing on 'to do'."),
    (1, None, "'You cannot fire everyone I smile at.' Here Nagiyev anchors the thought on 'one must not' and finishes on 'smile', keeping the spoken rhythm brisk and natural."),
    (2, None, "'What beautiful fingers you have.' The meaning hinges on 'what' working together with 'fingers' in spoken Russian."),
    (3, None, "'And what are you doing today?' Dmitry Nagiyev chooses the respectful plural 'you' alongside 'tonight' to keep a polite distance."),
    (4, None, "'You are fired.' Spoken Russian keeps this brisk, leaning on 'you' and finishing on 'to fire'."),
    (5, None, "'And your fingers too.' Eleonora anchors the line on 'and', while 'also' completes the thought."),
    (6, None, "'Alright then, you fired everyone.' The meaning hinges on 'come on' working together with 'everyone' in spoken Russian."),
    (7, None, "'Then who is going to run things today?' Notice how Russian expresses 'and' and 'tonight' with crisp inflection rather than helper words. Eleonora answers right away."),
    (8, None, "'Nikita, come here!' Here the Russian phrasing highlights 'Nikita' before landing on 'here'."),
    (9, None, "'Congratulations, you are the restaurant director.' The meaning hinges on 'congratulations' working together with 'restaurant' in spoken Russian."),
    (10, None, "'Thank you, Eleonora Andreyevna.' Here the Russian phrasing highlights 'thank you' before landing on 'Eleonora'. Dmitry Nagiyev answers right away."),
    (11, None, "'Nikita Andreyevich, coffee?' Dmitry Nagiyev brings out the contrast between 'Nikita' and 'coffee' in a few short words."),
]

TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = 'In a matter of seconds, Nikita goes from waiter to restaurant director, while the wedding still lacks a pianist. Until next time!'
CLOSING = ("nagiyev", "До встречи!")
