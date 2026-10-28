# Authoring module for domashniy-arest-s01e08-scene-07.
ID = 'domashniy-arest-s01e08-scene-07'
SHOW = 'domashniy-arest'
SEASON = 1
EPISODE = 8
SCENE = 7
TITLE = 'Где Самсонов?  (Where Is Samsonov?)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'ilona': 'Илона', 'nina': 'Нина'}
SOURCE_NAME = 'Домашний арест (Domashniy Arest) S1.08'
SOURCE_FILE = 'sources/domashniy-arest/s01/e08.ru.dual.srt'
INTRO = "Welcome back to Domashniy Arest! In the campaign headquarters of mayoral candidate Ivan Samsonov, crisis strikes on the eve of the live televised election debate. Campaign strategist Ilona Leonidovna and Ivan's anxious wife Nina discover that Ivan has vanished without a trace after the devastating smear video accusing his grandfather of wartime treason. Let's listen to the scene in Russian first."
OPENER = "Now let's examine the tense conversation at campaign headquarters line by line. Ilona and Nina discuss Ivan's disappearance and search for ways to save the mayoral campaign."
TRANSITION = "Now let's listen to the conversation at campaign headquarters once more in Russian."
OUTRO = "With the televised debates approaching rapidly, finding Ivan is a matter of political survival. Meanwhile, back in the communal apartment, Arkady is concocting a new scheme to win over Marina; let's see what he plans next. See you next time!"
CLOSING = ('ilona', 'Пока!')
STORY = [
    ('ilona', 'Где Самсонов? Он не берёт трубку.', 'Where is Samsonov? He is not answering his phone.', [], ''),
    ('nina', 'Я не знаю. Он не ночевал дома.', 'I do not know. He did not spend the night at home.', [], ''),
    ('ilona', 'У нас завтра дебаты!', 'We have the debate tomorrow!', [(98, 'У нас завтра дебаты')], ''),
    ('nina', 'Я знаю. Я очень волнуюсь за него.', 'I know. I am very worried about him.', [], ''),
    ('ilona', 'Он совсем не подготовлен.', 'He is completely unprepared.', [(99, 'Он не подготовлен')], ''),
    ('nina', 'Ваня очень переживает из-за слухов.', 'Vanya is very upset because of the rumors.', [], ''),
    ('ilona', 'Слухи про дедушку — это провокация Осипенко.', "The rumors about his grandfather are Osipenko's provocation.", [], ''),
    ('nina', 'Но люди верят этой лжи.', 'But people believe this lie.', [], ''),
    ('ilona', 'Мы должны выиграть эти выборы!', 'We must win this election!', [], ''),
    ('nina', 'Без Вани мы ничего не сделаем.', 'Without Vanya we will do nothing.', [], ''),
    ('ilona', 'Его надо срочно найти!', 'We need to find him urgently!', [(100, 'Его надо срочно найти')], ''),
    ('nina', 'Где мы будем его искать?', 'Where are we going to look for him?', [], ''),
    ('ilona', 'Проверьте все бары и старых друзей.', 'Check all the bars and old friends.', [], ''),
    ('nina', 'Я сейчас же позвоню знакомым.', 'I will call acquaintances right now.', [], ''),
]
WALK = [
    (0, None, "'Where is Samsonov? He is not answering his phone.' Ilona enters the office urgently asking where their candidate has gone."),
    (1, None, "'I do not know. He did not spend the night at home.' Nina looks pale and worried after an anxious sleepless night."),
    (2, None, "'We have the debate tomorrow!' Ilona reminds Nina about the impending live television broadcast."),
    (3, None, "'I know. I am very worried about him.' Nina expresses her deep distress over Ivan's sudden disappearance."),
    (4, None, "'He is completely unprepared.' The political strategist stresses that Ivan has not practiced his debating points."),
    (5, None, "'Vanya is very upset because of the rumors.' Nina explains the emotional toll of the smear campaign on her husband."),
    (6, None, "'The rumors about his grandfather are Osipenko's provocation.' Ilona identifies the dirty political scheme behind the scandal."),
    (7, None, "'But people believe this lie.' Nina laments that public opinion in town is turning against them."),
    (8, None, "'We must win this election!' Ilona tries to rally the room — giving up the race is not an option."),
    (9, None, "'Without Vanya we will do nothing.' Nina states the obvious: without the candidate himself, the campaign is dead in the water."),
    (10, None, "'We need to find him urgently!' Literally, 'him it is necessary urgently to find' — Ilona shifts straight into crisis mode."),
    (11, None, "'Where are we going to look for him?' Nina is at a loss for where to even begin searching next."),
    (12, None, "'Check all the bars and old friends.' Ilona barks out orders to comb every local watering hole and old hangout."),
    (13, None, "'I will call acquaintances right now.' Adding the tiny word 'zhe' right after 'now' means Nina is picking up the phone this very second."),
]
