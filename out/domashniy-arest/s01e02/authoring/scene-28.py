# Authoring module for domashniy-arest-s01e02-scene-28.
ID = 'domashniy-arest-s01e02-scene-28'
SHOW = 'domashniy-arest'
SEASON = 1
EPISODE = 2
SCENE = 28
TITLE = 'Пир из холодильника  (A Feast from the Fridge)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'arkady': 'Аркадий', 'lyosha': 'Лёша', 'yulia': 'Юля'}
SOURCE_NAME = 'Домашний арест (Domashniy Arest) S1.02'
SOURCE_FILE = 'sources/domashniy-arest/s01/e02.ru.dual.srt'
INTRO = "Back in the communal flat, Arkady is very pleased with himself: last time, he phoned the governor with a number-faking app, pretending to be the powerful Tretyakov from Moscow, and ordered him to let the mayor go. Now, starving, he goes looking for food with the children, and finds the old neighbour's locked fridge. Let's listen in Russian first."
OPENER = "Let's go back through it slowly. The trick call is over, and Arkady can hardly believe how cheap his freedom was."
TRANSITION = "Now let's hear the whole feast again, from the beginning."
OUTRO = "And that's the scene: a broken lock, a stolen feast, and a boy who has just eaten the one thing he was told never to touch. We'll soon find out what the caviar does. See you next time!"
CLOSING = ('arkady', 'Пока!')
STORY = [
    ('arkady', 'Не могу поверить! Я всё сделал за пятьсот рублей.', "I can't believe it! I did it all for five hundred roubles.", [(992, 'Не могу поверить'), (993, 'все сделал')], "'за 500 рублей' written out in words; the million-dollar comparison (992) is left out"),
    ('yulia', 'Значит, вас скоро отпустят?', "So they'll let you go soon?", [], 'new: the children know about the trick call (scene 27) and Arkady expects to be freed (cue 1011)'),
    ('arkady', 'Скоро. А пока я есть хочу, слона бы съел!', "Soon. But for now I'm hungry, I could eat an elephant!", [(995, 'слона бы съел')], "'Скоро. А пока' new; жрать -> есть (plain word)"),
    ('yulia', 'Да вон, курица.', "There's chicken, over there.", [(998, 'Да вон')], 'the garbled «мам, курицу свою» simplified to «курица»'),
    ('arkady', 'Курица? Нет. А чей это холодильник?', 'Chicken? No. And whose fridge is this?', [(999, 'Курицу'), (1002, 'чей холодильник')], "case changed (курицу -> курица); 'Нет.' new; 'это' added"),
    ('yulia', 'Это Клавдии Викторовны.', "That's Klavdia Viktorovna's.", [(1003, 'Это Клавдии Викторовны')], 'speaker unclear in the source, given to Yulia'),
    ('arkady', 'А почему там замок?', 'And why is there a lock on it?', [(1004, 'замок')], '«А чё, замок висит?» -> «А почему там замок?» (plain words)'),
    ('yulia', 'Она там взятки для врачей хранит.', 'She keeps bribes for the doctors in there.', [(1005, 'Она там взятки для врачей хранит')], 'speaker unclear in the source, given to Yulia'),
    ('arkady', 'Взятки? Очень интересно.', 'Bribes? Very interesting.', [(1006, 'Взятки')], "'Очень интересно.' new (Arkady then breaks the lock, told by the narrator)"),
    ('lyosha', 'Вы что? Нас же мама убьёт!', 'What are you doing? Mum will kill us!', [(1009, 'Нас же мама убьёт')], '«вы чё» (1008) -> «Вы что?»; speaker unclear in the source, given to Lyosha'),
    ('arkady', 'Так, успокойтесь все. Сейчас за мной приедут.', "Right, everyone calm down. They're coming for me any minute.", [(1010, 'успокойтесь все'), (1011, 'Сейчас за мной приедут')], ''),
    ('yulia', 'А так можно?', 'Is that allowed?', [(1017, 'А так можно')], 'speaker unclear in the source, given to Yulia'),
    ('arkady', 'Можно. А ты чего сидишь? Давай, ешь.', 'It is. And why are you just sitting there? Come on, eat.', [(1024, 'а ты чего сидишь'), (1024, 'Давай, ешь')], "'Можно.' new; «как неродной» left out"),
    ('lyosha', 'Мама говорила, что у меня на икру аллергия.', "Mum said I'm allergic to caviar.", [(1025, 'Мама говорила, что у меня на икру аллергия')], ''),
    ('arkady', 'Мама так говорит, чтобы ты икру не просил. У неё денег нет.', "Mum says that so you won't ask for caviar. She has no money.", [(1026, 'Мама так говорит'), (1027, 'У неё денег нет')], '«чтоб ты у неё икру не просила» -> «чтобы ты икру не просил» (full form, masculine for the boy); «Вы ж нищие» left out'),
    ('lyosha', 'Ладно. Ой, вкусно!', "All right. Oh, it's tasty!", [(1029, 'Вкусно')], "'Ладно. Ой' new; Arkady's question «Вкусно?» and the boy's «Ага» (1029-1030) become the boy's exclamation"),
    ('arkady', 'Вот видишь? И никакой аллергии.', 'There, you see? And no allergy at all.', [(1031, 'И никакой аллергии')], "'Вот видишь?' new"),
]
WALK = [
    (0, 'Не могу поверить!', "'I can't believe it!' Literally, 'I can't to believe': the word for 'can' is followed by a basic action word, just like in English. Then he explains why."),
    (0, 'Я всё сделал за пятьсот рублей.', "'I did it all for five hundred roubles.' The little word in front of the price means 'for', in the sense of 'in exchange for'. Five hundred roubles is what the faking app cost, and it came out of little Lyosha's piggy bank. Samson's teenage daughter Yulia has a question."),
    (1, None, "'So they'll let you go soon?' The first word means 'so' or 'that means', a handy way to draw a conclusion. Arkady is sure of it, but his stomach comes first."),
    (2, 'Скоро.', "'Soon.' A one-word answer. Then a famous way of saying you are very hungry."),
    (2, 'А пока я есть хочу, слона бы съел!', "'But for now I'm hungry, I could eat an elephant!' Russians eat an elephant where English speakers eat a horse. The word for 'to eat' here looks exactly like the word for 'there is'. Yulia points at something."),
    (3, None, "'There's chicken, over there.' The word in the middle points at something a little way off, like 'over there'. Arkady has bigger ideas than chicken."),
    (4, 'А чей это холодильник?', "'And whose fridge is this?' The question word means 'whose', and it changes its ending to match the thing owned. A fridge is masculine, so it stays in this short form."),
    (5, None, "'That's Klavdia Viktorovna's.' The old neighbour's name takes the ending that means 'of': literally, 'that is of Klavdia Viktorovna'. Arkady notices something on the door."),
    (6, None, "'And why is there a lock on it?' Literally, 'and why is there a lock there?' There's no 'is' or 'are' at all: in the present, Russian simply leaves out 'is'. The answer is a good one."),
    (7, None, "'She keeps bribes for the doctors in there.' The old lady hides little gifts for her doctors, which the children call bribes. The action word, 'keeps', comes last, which sounds very natural in speech. That word catches Arkady's ear."),
    (8, None, "'Bribes? Very interesting.' He knows a thing or two about bribes, of course. And with that, he breaks the lock and opens the fridge. Lyosha is horrified."),
    (9, None, "'What are you doing? Mum will kill us!' The first question, literally 'you what?', is how people react to something outrageous. 'Us' comes first in the second sentence, for emphasis. Arkady waves it away."),
    (10, 'Так, успокойтесь все.', "'Right, everyone calm down.' That's a command for several people, and the ending also makes it polite. Then his reason."),
    (10, 'Сейчас за мной приедут.', "'They're coming for me any minute.' There's no 'they' in it: the plural form on its own means 'people', 'they'. The word at the start is usually 'now', but here it means 'very soon'. He promises to send them delicacies they've never tasted. Yulia is still a little doubtful."),
    (11, None, "'Is that allowed?' The last word means 'it is allowed' or 'you may'. So Arkady simply repeats it."),
    (12, 'Можно.', "'It is.' Out come crab and caviar, though Arkady sniffs that these hardly count as crabs. Then he turns to Lyosha, who isn't touching anything."),
    (12, 'А ты чего сидишь? Давай, ешь.', "'And why are you just sitting there? Come on, eat.' In everyday speech, 'what' often stands in for 'why'. The word for 'come on' is really a command from the action word 'to give'. Lyosha has a good reason not to eat."),
    (13, None, "'Mum said I'm allergic to caviar.' Word for word, 'at me there is an allergy to caviar'. That's how Russian says someone has something. Remember this line. Arkady doesn't believe a word of it."),
    (14, 'Мама так говорит, чтобы ты икру не просил.', "'Mum says that so you won't ask for caviar.' The word in the middle means 'so that', and the action word after it goes into the past form, even though it's about the future. Then the cruel part."),
    (14, 'У неё денег нет.', "'She has no money.' Literally, 'at her there is no money'. After 'no', money takes the ending that means 'of'. So Lyosha gives in and tries it."),
    (15, None, "'All right. Oh, it's tasty!' The last word on its own means 'it tastes good', and you'll hear it at every Russian table. Arkady is triumphant."),
    (16, None, "'There, you see? And no allergy at all.' The word before allergy means 'no ... at all', and it makes the denial stronger. Meanwhile, on a building site, Samson is phoning Nina: his boss has given him a trip to Crimea, with a heated seawater pool, and she should go and buy a swimsuit."),
]
