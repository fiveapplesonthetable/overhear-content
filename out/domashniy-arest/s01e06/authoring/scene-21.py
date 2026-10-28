# Authoring module for domashniy-arest-s01e06-scene-21.
ID = 'domashniy-arest-s01e06-scene-21'
SHOW = 'domashniy-arest'
SEASON = 1
EPISODE = 6
SCENE = 21
TITLE = 'У нас просто сгущёнка взорвалась!  (Our Condensed Milk Just Exploded!)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'arkady': 'Аркадий', 'samson': 'Самсон', 'slavik': 'Славик'}
SOURCE_NAME = 'Домашний арест (Domashniy Arest) S1.06'
SOURCE_FILE = 'sources/domashniy-arest/s01/e06.ru.dual.srt'
INTRO = "In the communal kitchen and out in the snowy courtyard right after that. While Yulya runs out of the building in tears, Arkady is in the kitchen with a broom tied to a mop, trying to knock the trash bag off the tree branch outside Klavdia Viktorovna's window to earn his five thousand roubles. Let's listen in Russian first."
OPENER = "Let's go through the scene line by line. First, Arkady calls ten-year-old Slavik into the kitchen."
TRANSITION = "Now let's hear the whole scene once more, from start to finish."
OUTRO = "So Marina's exploding condensed milk has sent Arkady flying out the window into a snowbank, while Samson has just learned that Yulya has a secret older admirer. Well done following all that chaos in Russian. See you next time!"
CLOSING = ('arkady', 'Пока!')
STORY = [
    ('arkady', 'Алло! Иди сюда! Дело есть!', 'Hello! Come over here! I have a job for you!', [(773, 'Алло! Иди сюда'), (773, 'Дело есть')], ''),
    ('arkady', 'Видишь, висит? — Да, он уже месяц там висит.', "See that hanging there? — Yes, it's been hanging there for a month.", [(774, 'Видишь, висит'), (775, 'Да, он уже месяц там висит')], ''),
    ('arkady', 'Его надо снять! Залезаешь на окно и шваброй сбиваешь его.', 'It needs to come down! You climb onto the window and knock it down with the mop.', [(776, 'его надо снять'), (777, 'залезаешь на окно и'), (777, 'шваброй'), (777, 'сбиваешь его')], "'вот этой... с веником' dropped to keep sentence <= 8 words"),
    ('arkady', 'А я тебя страхую. Понял? — Да, понял!', "And I'll spot you. Got it? — Yes, got it!", [(778, 'А я тебя страхую. Понял'), (779, 'Да, понял')], ''),
    ('arkady', 'Бери швабру, вперёд! Давай, давай!', 'Grab the mop, go! Come on, come on!', [(780, 'бери швабру, вперед! Давай! Давай')], ''),
    ('arkady', 'Что вы, Клавдия Викторовна! Ладно, я сам полезу.', "Oh stop it, Klavdia Viktorovna! Fine, I'll climb up myself.", [(783, 'Что вы'), (784, 'Ладно, я сам полезу')], "Klavdia Viktorovna's scolding in 781-782 narrated; ASR 'Владимир Викторович' (787) restored to 'Клавдия Викторовна'"),
    ('arkady', 'Только держи меня! — А как держать? — Нежно!', 'Just hold me! — How do I hold you? — Gently!', [(784, 'Только держи меня'), (785, 'А как держать'), (786, 'Нежно')], ''),
    ('arkady', 'Смотри, держи меня за ногу. Вот так! Крепче держи!', 'Look, hold me by the leg. Like that! Hold tighter!', [(789, 'смотри'), (789, 'держи меня за ногу. Вот так'), (791, 'Крепче держи')], ''),
    ('slavik', 'Ой! У нас просто сгущёнка взорвалась!', 'Oh! Our condensed milk just exploded!', [(795, 'у нас просто сгущенка взорвалась')], "Marina's apology in 795 voiced by startled Slavik at the stove explosion"),
    ('samson', 'Сейчас пойду, найду её! — Ты что, Аркаша?', "I'll go find her right now! — What are you doing, Arkasha?", [(797, 'Сейчас пойду, найду ее'), (802, 'Ты что, Аркаша')], ''),
    ('arkady', 'Ничего! Твой сын — убийца!', 'Nothing! Your son is a murderer!', [(803, 'Ничего. Твой сын убийца')], ''),
    ('samson', 'Капустина! Привет. Юльку видела?', 'Kapustina! Hi. Have you seen Yulka?', [(805, 'Капустина'), (806, 'Привет'), (806, 'видела')], "ASR 'Юрку' restored to 'Юльку'"),
    ('samson', 'Пробежала вся в слезах? А куда она могла пойти?', 'She ran past all in tears? And where could she have gone?', [(807, 'Пробежала'), (807, 'вся'), (809, 'куда она могла пойти')], "Samson echoes Kapustina's answer from cue 807 ('вся слеза' -> 'вся в слезах')"),
    ('samson', 'К жениху своему? Чего? Стоять, кому сказал! Иди сюда!', "To her boyfriend's? What? Stop right there, I said! Come here!", [(810, 'своему'), (811, 'Чего'), (813, 'стоять'), (813, 'Стоять, кому сказал! Иди сюда')], "slang/ASR 'К хахоти своему' cleaned to 'К жениху своему'"),
]
WALK = [
    (0, None, "'Hello! Come over here! I have a job for you!' Literally, 'there is a matter'. Arkady points out the open kitchen window at the tree branch."),
    (1, None, "'See that hanging there? — Yes, it's been hanging there for a month.' Notice how Russian uses the present tense with 'already a month' for an action that started in the past and is still going on."),
    (2, None, "'It needs to come down! You climb onto the window and knock it down with the mop.' He uses the vivid present tense to give step-by-step instructions."),
    (3, None, "'And I'll spot you. Got it? — Yes, got it!' The verb for 'to spot' or 'insure' means holding someone so they don't fall."),
    (4, None, "'Grab the mop, go! Come on, come on!' Just as Slavik steps up, Klavdia Viktorovna walks in and scolds them, warning that the boy will fall and get hurt."),
    (5, None, "'Oh stop it, Klavdia Viktorovna! Fine, I'll climb up myself.' Shamed by the old lady, Arkady climbs onto the windowsill himself."),
    (6, None, "'Just hold me! — How do I hold you? — Gently!' Arkady's sarcastic reply is the adverb 'tenderly' or 'gently'."),
    (7, None, "'Look, hold me by the leg. Like that! Hold tighter!' After verbs of holding or grabbing, Russian uses the preposition 'for' plus the direct-object form: 'by the leg'."),
    (8, None, "'Oh! Our condensed milk just exploded!' Behind them on the stove, Marina's forgotten tin of condensed milk blows up with a thunderous bang. Startled Slavik lets go of Arkady's ankle, and Arkady tumbles headfirst out the first-floor window into a snowbank!"),
    (9, None, "'I'll go find her right now! — What are you doing, Arkasha?' Running out into the courtyard to look for Yulya, Samson pauses in surprise as he sees Arkady lying in the snow."),
    (10, None, "'Nothing! Your son is a murderer!' Groaning in the snowdrift, Arkady blames Slavik for letting go of his leg."),
    (11, None, "'Kapustina! Hi. Have you seen Yulka?' Leaving Arkady to the prison-service guard, Samson spots Yulya's classmate by the gate."),
    (12, None, "'She ran past all in tears? And where could she have gone?' When Kapustina says Yulya ran past crying after their fight, Samson asks where she went."),
    (13, None, "'To her boyfriend's? What? Stop right there, I said! Come here!' The moment Kapustina mentions Yulya's rich older 'boyfriend', Samson grabs her coat sleeve to find out where he lives."),
]
