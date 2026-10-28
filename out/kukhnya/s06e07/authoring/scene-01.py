# Authoring module for kukhnya-s06e07-scene-01.
ID = 'kukhnya-s06e07-scene-01'
SHOW = 'kukhnya'
SEASON = 6
EPISODE = 7
SCENE = 1
TITLE = 'Звонок на громкой связи  (The Call on Speakerphone)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'elena': 'Елена', 'lyova': 'Лёва'}
SOURCE_NAME = 'Кухня (Kukhnya) S6.07'
SOURCE_FILE = 'sources/kukhnya/s06/e07.ru.srt'
INTRO = 'Welcome to episode seven of Kukhnya season six. Chef Barinov sneaks out of work early by telling Lyova he is sick, only for Lyova to call while Elena is listening on speakerphone.'
OPENER = "Now let's go back through their conversation line by line and unpack the Russian phrasing."
TRANSITION = "Alright, let's hear the entire conversation one more time from start to finish."
OUTRO = 'Refusing to believe that Victor lied to his own sous-chef, Elena insists on booking him a full medical examination the very next day. Until next time!'
CLOSING = ('barinov', 'Хорошего дня!')
STORY = [
    ('elena', 'Любимый мужчина готовит мне вкусный ужин.', 'My beloved man is cooking me a delicious dinner.', [(1, 'любимый мужчина готовит тебе ужин')], 'adapted'),
    ('barinov', 'Тем более я гениальный шеф-повар.', 'Especially since I am a brilliant head chef.', [(2, 'он гениальный повар')], 'adapted'),
    ('elena', 'Смотри, твой су-шеф сейчас звонит.', 'Look, your sous-chef is calling right now.', [(6, 'твой су-шеф звонит')], 'adapted'),
    ('barinov', 'Поставь телефон на громкую связь.', 'Put the phone on speakerphone.', [(8, 'поставь на громкую')], 'adapted'),
    ('barinov', 'Да, Лёва, что там случилось?', 'Yes, Lyova, what happened over there?', [(9, 'Да, Лёва, что случилось')], 'adapted'),
    ('lyova', 'Завтра можете вообще на работу не приходить.', 'Tomorrow you do not have to come to work at all.', [(10, 'а завтра можете вообще не приходить')], 'adapted'),
    ('lyova', 'Вы лучше спокойно дома отдохните.', 'You had better rest quietly at home.', [(11, 'Вы лучше отдохните')], 'adapted'),
    ('barinov', 'Лёва, какую ерунду ты сейчас говоришь?', 'Lyova, what nonsense are you talking right now?', [(12, 'что за ерунду ты говоришь')], 'adapted'),
    ('lyova', 'Я знаю, что вам нельзя работать.', 'I know that you must not work.', [(13, 'Я прекрасно знаю, что вам вообще нельзя работать')], 'adapted'),
    ('barinov', 'Это я соврал, чтобы уйти пораньше.', 'I made that up so I could leave early.', [(18, 'Это я Лёве соврал, чтобы уйти пораньше с работы')], 'adapted'),
    ('elena', 'Ты обязательно пройдёшь полное обследование.', 'You will definitely undergo a full medical checkup.', [(22, 'пока ты не пройдешь полное обследование')], 'adapted'),
    ('elena', 'У меня подруга работает в поликлинике.', 'My friend works as chief doctor at the clinic.', [(23, 'главврач в поликлинике')], 'adapted'),
]
WALK = [
    (0, None, "'My beloved man is cooking me a delicious dinner.' Explaining that her beloved man is cooking her a delicious dinner lays the cards on the table for Barinov."),
    (1, None, "'Especially since I am a brilliant head chef.' Barinov mentions that especially since he is a brilliant head so Elena sees what is at stake."),
    (2, None, '\'Look, your sous-chef is calling right now.\' Claiming that Barinov\'s is calling right now sounds confident, even if Barinov has doubts. Speaking with the close, informal "you" strips away any polite distance between them.'),
    (3, None, "'Put the phone on speakerphone.' Here putting the phone on speakerphone sets up the next turn in their exchange."),
    (4, None, '\'Yes, Lyova, what happened over there?\' With the point and dinner hanging in the air, Barinov puts Elena on the spot. In Russian, he does not need helper words like "do" or "did"—rising pitch alone turns it into a question.'),
    (5, None, "'Tomorrow you do not have to come to work at all.' Realizing that tomorrow Barinov does not have to come to work at all changes how Lyova handles the situation."),
    (6, None, "'You had better rest quietly at home.' Noting that Barinov had better rest quietly at home keeps Lyova's side of the story simple and clear."),
    (7, None, '\'Lyova, what nonsense are you talking right now?\' Questioning whether what nonsense are Elena talking right now is how Barinov tests Elena\'s story. Using the informal "you" shows how direct and unfiltered their kitchen relationship is.'),
    (8, None, '\'I know that you must not work.\' Knowing that Barinov must not work moves the conversation forward without extra drama. There is no "you" needed in the Russian here: one short word states the rule for everyone in the room.'),
    (9, None, "'I made that up so I could leave early.' Saying that he made that up so he could leave early is how Barinov sets the tone with Elena."),
    (10, None, '\'You will definitely undergo a full medical checkup.\' Once Barinov will definitely undergo a full medical checkup, Elena can finally tell Barinov what she means. Speaking with the close, informal "you" strips away any polite distance between them.'),
    (11, None, '\'My friend works as chief doctor at the clinic.\' Adding that her friend works as chief doctor at the clinic fills in the missing piece for Barinov. In Russian you say "by me" or "with us" rather than "I have", so the situation sits right with the person.'),
]
