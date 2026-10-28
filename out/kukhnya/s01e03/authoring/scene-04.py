# Authoring module for kukhnya-s01e03-scene-04.
ID = 'kukhnya-s01e03-scene-04'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 3
SCENE = 4
TITLE = 'Опасный разговор  (A Dangerous Conversation)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'max': 'Макс', 'vadim': 'Вадим'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.03'
SOURCE_FILE = 'sources/kukhnya/s01/e03.ru.dual.srt'
INTRO = "A rough-looking man stops Max outside Claude Monet. His name is Vadim, he is a prosecutor, and he wants to know who Vika is seeing these days. Max is not enjoying this. Here's the conversation in Russian first."
OPENER = "Let's go through the threat."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = 'Max promises that Vika is seeing nobody, and Vadim does not look convinced. Take away "ni s kem ne", the double negative with a word wedged in the middle.'
CLOSING = ('max', 'До встречи!')
STORY = [
    ('vadim', 'Слышь, малой, есть разговор.', 'Listen, kid, I want to talk.', [(132, 'разговор есть')], ''),
    ('max', 'Что вам нужно?', 'What do you need?', [], ''),
    ('vadim', 'Тут у вас работает Вика.', 'Vika works here with you.', [(133, 'Тут у вас работает Вика')], ''),
    ('vadim', 'Виктория Сергеевна.', 'Viktoria Sergeyevna.', [(133, 'Виктория Сергеевна')], ''),
    ('vadim', 'С кем она тут встречается?', 'Who is she seeing here?', [(134, 'с кем она у вас тут встречается')], ''),
    ('vadim', 'Ну, почему молчим?', 'Well, why are we silent?', [], ''),
    ('max', 'Почему я должен отвечать?', 'Why should I answer?', [(136, 'я тебе должен отвечать')], ''),
    ('vadim', 'Не хочешь отвечать здесь?', "Don't want to answer here?", [(137, 'Не хочешь отвечать здесь')], ''),
    ('vadim', 'Ответишь у меня в прокуратуре.', "You'll answer in my prosecutor's office.", [(138, 'у меня в прокуратуре')], ''),
    ('vadim', 'Ты меня понял?', 'Did you understand me?', [(139, 'Понял')], ''),
    ('max', 'Понял, всё понял.', 'Understood, understood everything.', [(140, 'Понял, понял')], ''),
    ('max', 'Она ни с кем не встречается.', 'She is not seeing anyone.', [(141, 'она здесь ни с кем не встречается')], ''),
    ('vadim', 'Ну, смотри у меня.', 'Well, you watch yourself.', [(142, 'Ну, смотри')], ''),
    ('max', 'Надо срочно предупредить всех.', 'Must urgently warn everyone.', [(160, 'Надо предупредить')], ''),
]
WALK = [
    (0, None, '\'Listen, kid, I want to talk.\' "Slysh\'" is street speech, clipped from "slyshish\'", do you hear. "Maloy", kid, is really "malyy", small, and "yest\' razgovor" is "there is a conversation".'),
    (1, None, '\'What do you need?\' "Chto vam nuzhno?" is "what to you needed?". Max uses "vam", the polite "you", with a stranger.'),
    (2, None, '\'Vika works here with you.\' "U vas" is "at you", meaning "at your place". "Tut" is an everyday "here", and "rabotayet" is "works".'),
    (3, None, '\'Viktoria Sergeyevna.\' A first name plus the father\'s name, "Sergeyevna", daughter of Sergey, is the formal way to name an adult.'),
    (4, None, '\'Who is she seeing here?\' "Vstrechat\'sya s", to meet with, is the normal way to say you\'re dating someone. "S kem" is "with whom", from "kto", who.'),
    (5, None, '\'Well, why are we silent?\' "Molchim" is "we are silent", from "molchat\'". Vadim says "we" when he means "you", the scolding "we" used on children.'),
    (6, None, '\'Why should I answer?\' "Dolzhen", should, has a man\'s ending. "Otvechat\'", to answer, sits next to the noun "otvet", an answer.'),
    (7, None, '\'Don\'t want to answer here?\' Vadim has called Max "ty" from his first word, and "khochesh\'" is the "ty" form of "want". "Zdes\'" is "here".'),
    (8, None, '\'You\'ll answer in my prosecutor\'s office.\' "Otvetish\'" is the finished verb, so it means "you will answer". "U menya v prokurature" is "at me in the prosecutor\'s office".'),
    (9, None, '\'Did you understand me?\' "Ty menya ponyal?" is "you me understood?". "Ponyal" ends in -l because Max is a man.'),
    (10, None, '\'Understood, understood everything.\' "Ponyal, vsyo ponyal" repeats the same word and adds "vsyo", everything.'),
    (11, None, '\'She is not seeing anyone.\' The pieces of "nikem", nobody, come apart around "s", with: "ni s kem". Then "ne" follows, so the double negative has a preposition inside it.'),
    (12, None, '\'Well, you watch yourself.\' "Smotri u menya" is "look, at me", meaning "careful, or you\'ll answer to me". "Smotri" is the "ty" command of "smotret\'", to look.'),
    (13, None, '\'Must urgently warn everyone.\' "Nado" is a one-word "must". "Predupredit\'" is "to warn", and "vse", everyone, becomes "vsekh" as the object.'),
]
