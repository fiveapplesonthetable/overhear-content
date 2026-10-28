# Authoring module for kukhnya-s02e03-scene-02.
ID = 'kukhnya-s02e03-scene-02'
SHOW = 'kukhnya'
SEASON = 2
EPISODE = 3
SCENE = 2
TITLE = 'Авария на улице  (Crash on the Street)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'elena': 'Елена'}
SOURCE_NAME = 'Кухня (Kukhnya) S2.03'
SOURCE_FILE = 'sources/kukhnya/s02/e03.ru.dual.srt'
INTRO = "Elena accidentally hits someone with her car. She rushes out to check on the victim and realizes it is her rival, Chef Viktor. Let's listen closely to their exchange in Russian first, and then walk through each line together."
OPENER = "Let's listen to their conversation."
TRANSITION = "Now let's hear the whole thing once more."
OUTRO = "And that's it for this scene. When you watch the episode, listen out for the exchange around crash on the street, and for the words meaning 'living' and 'excuse me'. You'll catch them now. See you next time."
CLOSING = ('elena', 'Пока!')
STORY = [
    ('elena', 'Виктор Петрович, вы живы?', 'Viktor Petrovich, are you alive?', [(8, 'Виктор Петрович, вы живы, Виктор Петрович?')], ''),
    ('barinov', 'А?', 'Huh?', [(9, 'А?')], ''),
    ('elena', 'Ой, вы простите меня.', 'Oh, please forgive me.', [(10, 'Ой.'), (11, 'Вы простите меня, ради бога, я вас просто не заметила.')], ''),
    ('elena', 'Ради бога, простите.', "For God's sake, forgive me.", [(11, 'Вы простите меня, ради бога')], ''),
    ('elena', 'Я вас просто не заметила.', "I just didn't see you.", [(11, 'я вас просто не заметила.')], ''),
    ('barinov', 'Так вы расправляетесь с конкурентами.', 'So this is how you deal with the competition.', [(12, 'Так-то вы расправляетесь с конкурентами.')], ''),
    ('elena', 'Дайте, я вас приподниму.', 'Here, let me help you up.', [(13, 'Дайте, я вас как-то приподниму')], ''),
    ('elena', 'Поедем в больницу.', 'We will go to the hospital.', [(13, 'и в больницу.')], ''),
    ('barinov', 'Мне больно.', 'It hurts.', [], ''),
    ('elena', 'Надо ехать к врачу.', 'We need to go to the doctor.', [], ''),
    ('barinov', 'Ладно, поехали.', "All right, let's go.", [], ''),
    ('elena', 'Осторожно.', 'Careful.', [], ''),
]
WALK = [
    (0, None, "'Viktor Petrovich, are you alive?' Rushing out of her car after the bump, Elena gasps and asks if Viktor is alive."),
    (1, None, "'Huh?' Stunned on the pavement, Barinov can only let out a dazed 'huh?'."),
    (2, None, "'Oh, please forgive me.' Elena apologizes profusely for hitting him."),
    (3, None, "'For God's sake, forgive me.' Shaken by the crash, she begs him for heaven's sake to forgive her."),
    (4, None, "'I just didn't see you.' She explains that she simply did not see him stepping into the street."),
    (5, None, "'So this is how you deal with the competition.' Recognizing the chef from the rival restaurant next door, Viktor jokes that this is how she takes out the competition. Then Elena replies."),
    (6, None, "'Here, let me help you up.' Elena reaches down and offers to help him to his feet."),
    (7, None, "'We will go to the hospital.' She insists on driving him straight to the hospital."),
    (8, None, "'It hurts.' In pain as he tries to stand on his leg, Viktor admits that it hurts. And Elena jumps in."),
    (9, None, "'We need to go to the doctor.' Seeing him limp, Elena says they definitely need to see a doctor."),
    (10, None, "'All right, let's go.' Viktor gives in and agrees to ride with her."),
    (11, None, "'Careful.' Elena tells him to be careful as she helps him into the passenger seat."),
]
