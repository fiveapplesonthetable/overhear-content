# Authoring module for domashniy-arest-s01e07-scene-30.
ID = 'domashniy-arest-s01e07-scene-30'
SHOW = 'domashniy-arest'
SEASON = 1
EPISODE = 7
SCENE = 30
TITLE = "Мастерство не купишь  (You Can't Buy Skill)"
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'danya': 'Даня', 'nina': 'Нина', 'samson': 'Самсон'}
SOURCE_NAME = 'Домашний арест (Domashniy Arest) S1.07'
SOURCE_FILE = 'sources/domashniy-arest/s01/e07.ru.dual.srt'
INTRO = "Out in the snowy woods, the second batch of shashlik is ready. After Yulya and Nina pose for photos with lawyer Danya, a jealous Samsonov spots Danya's camping axe and decides to show off his airborne combat skills. Let's listen in Russian first."
OPENER = "Let's go through the scene line by line. As the second batch of skewers comes off the grill, Yulya asks Danya for an Instagram selfie and Danya calls everyone over."
TRANSITION = "Now let's hear the whole scene again, from start to finish."
OUTRO = "So Samsonov's attempt to show off his airborne combat skills ended with the camping axe falling straight onto Danya's hand, sending the whole party racing to the hospital. See you next time!"
CLOSING = ('samson', 'Пока!')
STORY = [
    ('danya', 'Вторая партия готова! Идём, сфотографируемся все вместе!', "The second batch is ready! Come on, let's take a photo all together!", [(1141, 'Вторая партия готова'), (1145, 'Идем, сфотографируемся')], ''),
    ('nina', 'Самсон, пойдём! Улыбаемся! Сыр, сыр!', 'Samson, come on! Smile! Cheese, cheese!', [(1151, 'Улыбаемся'), (1152, 'Самсон, пойдем'), (1157, 'Сыр, сыр')], ''),
    ('nina', 'Иван, встань подальше, вон там за соснами.', 'Ivan, stand further back, over there behind the pines.', [(1158, 'Иван'), (1158, 'соснами')], "ASR 'Иван, отдавай соснами' restored"),
    ('samson', 'Даня, это твоя точилка? И твой топор?', 'Danya, is this your sharpener? And your axe?', [(1159, 'это твоя точилка'), (1160, 'топор')], ''),
    ('danya', 'Да, мой топор. Ух ты! Как ты это сделал?', 'Yes, my axe. Wow! How did you do that?', [(1160, 'топор'), (1162, 'Ух ты')], 'Danya amazed as Samsonov hurls the axe into a pine tree'),
    ('samson', 'Вот так, Даня! Метр пятьдесят от земли!', 'Just like that, Danya! A meter fifty off the ground!', [(1164, 'Вот так'), (1165, 'Метр пятьдесят от земли')], ''),
    ('samson', 'Купить можно всё что угодно!', 'You can buy anything at all!', [(1167, 'Купить можно все, что угодно')], ''),
    ('samson', 'А мастерство не купишь, понял?', "But you can't buy skill, got it?", [(1168, 'А мастерство не купишь, понял')], ''),
    ('samson', 'Нам вообще запрещено это показывать. Но вы же свои!', "We're strictly forbidden to show this. But you're family!", [(1171, 'Нам вообще запрещено это показывать'), (1172, 'Но вы же свои')], ''),
    ('samson', 'А ещё есть ближний бой! Смотри, как я умею!', "And there's also close combat! Watch what I can do!", [(1175, 'ближний бой')], ''),
    ('nina', 'Тише, Ваня, осторожно! Зачем ты бьёшь дерево ногой?', 'Easy, Vanya, be careful! Why are you kicking the tree with your foot?', [(1178, 'Тише')], ''),
    ('samson', 'Да нормально, не бойся! Можешь так, Даня, или нет?', "It's fine, don't be afraid! Can you do that, Danya, or not?", [(1179, 'Да нормально'), (1180, 'нет')], "'не боись' -> 'не бойся'"),
    ('danya', 'Нет, так не могу. Ты выше меня ударил.', "No, I can't do that. You kicked higher than me.", [(1181, 'Нет'), (1184, 'Ты выше')], ''),
    ('samson', 'А я сейчас ещё выше ударю! Смотрите все!', "And right now I'll kick even higher! Watch, everyone!", [(1184, 'выше')], ''),
    ('danya', 'Ай, моя рука! Топор упал мне на руку!', 'Ow, my hand! The axe fell onto my hand!', [], 'new line voicing the visual accident between cues 1185 and 1186'),
    ('nina', 'Самсонов, ты с ума сошёл?! Быстро в больницу!', 'Samsonov, have you lost your mind?! Quickly to the hospital!', [(1186, 'Самсонов, ты')], "'дебил' -> 'с ума сошёл'"),
]
WALK = [
    (0, None, "'The second batch is ready! Come on, let's take a photo all together!' The self-action verb form verb means 'let us be photographed together'."),
    (1, None, "'Samson, come on! Smile! Cheese, cheese!' Nina waves Samsonov into the frame for the family photo."),
    (2, None, "'Ivan, stand further back, over there behind the pines.' After 'behind', the noun 'pines' takes the 'with'-form plural."),
    (3, None, "'Danya, is this your sharpener? And your axe?' Feeling sidelined, Samsonov spots Danya's blade sharpener and camping axe on the table."),
    (4, None, "'Yes, my axe. Wow! How did you do that?' Without warning, Samsonov spins and hurls the axe straight into a pine trunk, leaving Danya amazed."),
    (5, None, "'Just like that, Danya! A meter fifty off the ground!' Beaming with pride for the first time all day, Samsonov points to the height of the stuck blade."),
    (6, None, "'You can buy anything at all!' The pronoun phrase means 'whatever you please, anything at all'."),
    (7, None, "'But you can't buy skill, got it?' Russian uses the generalized second-person singular for 'one cannot buy'."),
    (8, None, "'We're strictly forbidden to show this. But you're family!' When Slavik asks why his dad never showed them this before, Samsonov claims it is a military secret."),
    (9, None, "'And there's also close combat! Watch what I can do!' Carried away by his children's applause, Samsonov launches into a demonstration of high kicks."),
    (10, None, "'Easy, Vanya, be careful! Why are you kicking the tree with your foot?' Nina watches nervously as Samsonov kicks the pine trunk where the axe is embedded."),
    (11, None, "'It's fine, don't be afraid! Can you do that, Danya, or not?' Samsonov challenges Danya to match his high kick."),
    (12, None, "'No, I can't do that. You kicked higher than me.' Danya tries a modest kick, rests his hand on the tree trunk to brace himself, and admits Samsonov kicked higher."),
    (13, None, "'And right now I'll kick even higher! Watch, everyone!' Samsonov winds up and slams his boot into the trunk — shaking the stuck axe loose right onto Danya's hand."),
    (14, None, "'Ow, my hand! The axe fell onto my hand!' Danya cries out as the falling axe slices his finger against the bark."),
    (15, None, "'Samsonov, have you lost your mind?! Quickly to the hospital!' Nina rushes to Danya's side in horror as they scramble for the car."),
]
