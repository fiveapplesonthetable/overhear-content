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
    (0, None, '\'You cannot act like this.\' Even though Eleonora cannot act like this, Nagiyev keeps a steady face in front of Eleonora. There is no "you" needed in the Russian here: one short word states the rule for everyone in the room.'),
    (1, None, "'You cannot fire everyone I smile at.' Admitting that Eleonora cannot fire everyone he smiles shows Nagiyev being honest for a change. Russian packs the whole idea of what is allowed or needed into one impersonal word at the front."),
    (2, None, "'What beautiful fingers you have.' Saying that what beautiful fingers Eleonora has is how Nagiyev sets the tone with Eleonora."),
    (3, None, '\'And what are you doing today?\' Here asking what Eleonora doing today is shows Nagiyev looking for the real truth. Even in the middle of the drama, he keeps the polite plural "you" that workplace Russian expects.'),
    (4, None, '\'You are fired.\' Adding that Nagiyev is fired fills in the missing piece for Nagiyev. Notice how she sticks to the formal "you", keeping a professional line between them.'),
    (5, None, "'And your fingers too.' With the work and point in play, Eleonora keeps this short reply brisk and direct."),
    (6, None, '\'Alright then, you fired everyone.\' Around the work and truth, Nagiyev sets a calm, everyday tone with Eleonora. Speaking with the close, informal "you" strips away any polite distance between them.'),
    (7, None, '\'Then who is going to run things today?\' Here wondering who going to run things today is shows Nagiyev looking for the real truth. In Russian, he does not need helper words like "do" or "did"—rising pitch alone turns it into a question.'),
    (8, None, "'Nikita, come here!' Coming here shows Eleonora is done holding back."),
    (9, None, '\'Congratulations, you are the restaurant director.\' Because congratulations Nagiyev is the restaurant director, Eleonora treats the matter as settled. Using the informal "you" shows how direct and unfiltered their kitchen relationship is.'),
    (10, None, "'Thank you, Eleonora Andreyevna.' With the point and work in play, Nikita keeps this short reply brisk and direct."),
    (11, None, "'Nikita Andreyevich, coffee?' With the restaurant and kitchen hanging in the air, Nagiyev puts Eleonora on the spot."),
]
