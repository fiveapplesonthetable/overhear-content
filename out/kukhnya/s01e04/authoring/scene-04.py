# Authoring module for kukhnya-s01e04-scene-04.
ID = 'kukhnya-s01e04-scene-04'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 4
SCENE = 4
TITLE = 'Сладкий сон  (A Sweet Dream)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'max': 'Макс'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.04'
SOURCE_FILE = 'sources/kukhnya/s01/e04.ru.dual.srt'
INTRO = "Max has fallen asleep in the dining room and is having a lovely dream about the chef. When Barinov shakes him awake, Max is still half in the dream and says things he really shouldn't. Here's the Russian first."

OPENER = "Now let's see what Max says in his sleep."

TRANSITION = "Now let's listen to the whole conversation again from start to finish."

OUTRO = "Calling the boss by a pet name is not the way to keep a job. If you take one thing away, remember the Russian term for 'it's not allowed'."


CLOSING = ('max', 'До встречи!')
STORY = [
    ('max', 'Ты молодец, Витька.', 'Good job, Vitka.', [(30, 'Ты молодец, Витька')], ''),
    ('max', 'Витюшенька, мой огузок.', 'Vityushenka, my Oguzok.', [(31, 'Витюшенька'), (31, 'Мой Агузак')], ''),
    ('barinov', 'Ты что, совсем с ума сошёл?', 'Have you completely lost your mind?', [(32, 'Ты что, совсем')], ''),
    ('barinov', 'Ты что здесь спишь?', 'Why are you sleeping here?', [(33, 'Ты что здесь')], ''),
    ('max', 'Шеф, простите меня, пожалуйста.', 'Chef, please forgive me.', [(33, 'Шеф, я')], ''),
    ('max', 'Я прилёг на пять минут.', 'I lay down for five minutes.', [(34, 'прилег на пять минут заснуть')], ''),
    ('barinov', 'На кухне спать нельзя!', 'You cannot sleep in the kitchen!', [], ''),
    ('max', 'Я всю ночь не мог уснуть.', 'I could not sleep all night.', [(35, 'Всю ночь не мог')], ''),
    ('barinov', 'Почему ты ночью не спал?', "Why didn't you sleep at night?", [], ''),
    ('max', 'Наверное, это акклиматизация.', 'Probably it is acclimatization.', [(35, 'акклиматизация, наверное')], ''),
    ('barinov', 'Какая ещё акклиматизация?', 'What acclimatization?', [], ''),
    ('max', 'Я ещё не привык к Москве.', 'I am not used to Moscow yet.', [], ''),
    ('barinov', 'Быстро вставай и мой посуду!', 'Quickly get up and wash dishes!', [], ''),
    ('max', 'Уже встаю, шеф.', 'Already getting up, Chef.', [], ''),
]
WALK = [(0,
  None,
  ["'Good job, Vitka.' The phrase ",
   ('max', 'Ты молодец,'),
   " translates to 'you're a fine fellow', the everyday praise. ",
   ('max', 'Витька.'),
   " is an overfamiliar short form of the name Viktor, and Max uses the familiar 'you' with his boss in his sleep."]),
 (1,
  None,
  ["'Vityushenka, my Oguzok.' The Russian term for this doting pet form of Viktor is ",
   ('max', 'Витюшенька,'),
   " built from extra syllables for tenderness. Max then flips the chef's nickname for him back onto the chef by calling him ",
   ('max', 'мой огузок.')]),
 (2,
  None,
  ["'Have you completely lost your mind?' The phrase ",
   ('barinov', 'с ума сошёл?'),
   " literally translates to 'came down off the mind'. Starting with ",
   ('barinov', 'Ты что,'),
   " translates to 'what's wrong with you?'."]),
 (3,
  None,
  ["'Why are you sleeping here?' Here, ",
   ('barinov', 'Ты что,'),
   " does the job of 'why', as in everyday speech. The term for 'you sleep' is ",
   ('barinov', 'спишь?')]),
 (4,
  None,
  ["'Chef, please forgive me.' Awake, Max switches to the polite 'you'. The Russian term for 'forgive' is ",
   ('max', 'простите'),
   ' built from the polite extra letters at the end.']),
 (5,
  None,
  ["'I lay down for five minutes.' The added part turns the translation for 'lay down' into ",
   ('max', 'прилёг'),
   " which literally translates to 'lay down for a bit'. And ",
   ('max', 'на пять минут.'),
   " translates to 'for five minutes'."]),
 (6,
  None,
  ["'You cannot sleep in the kitchen!' The expression for 'it's not allowed' is ",
   ('barinov', 'нельзя!'),
   ' It needs no person doing the action. The action word ',
   ('barinov', 'спать'),
   " translates to the plain 'to sleep'."]),
 (7,
  None,
  ["'I could not sleep all night.' The phrase for 'all night' is ",
   ('max', 'всю ночь'),
   " which needs no extra little word for 'during'. The phrase ",
   ('max', 'не мог уснуть.'),
   " translates to 'could not fall asleep', built from the man's past form of 'can'."]),
 (8,
  None,
  ["'Why didn't you sleep at night?' The translation for 'at night' is ",
   ('barinov', 'ночью'),
   " built from 'night' with an extra sound at the end. Other times of day work the same way, taking a similar extra sound to mean 'in the morning' "
   "or 'in the evening'."]),
 (9,
  None,
  ["'Probably it is acclimatization.' Max gives the same long borrowed word as before for 'acclimatization', ",
   ('max', 'акклиматизация.'),
   " And the word for 'probably' is ",
   ('max', 'Наверное,')]),
 (10,
  None,
  ["'What acclimatization?' The phrase ",
   ('barinov', 'Какая ещё'),
   " repeats the word back with an edge, which translates to 'what acclimatization, exactly?'."]),
 (11,
  None,
  ["'I am not used to Moscow yet.' The phrase that translates to 'got used to' is ",
   ('max', 'привык к'),
   ' and the little word linking to the city changes its spelling, making it ',
   ('max', 'к Москве.'),
   " The phrase that translates to 'not yet' is ",
   ('max', 'ещё не')]),
 (12,
  None,
  ["'Quickly get up and wash dishes!' The Russian expression for telling someone to 'wash' here is ",
   ('barinov', 'мой'),
   " and it is spelled the same as the translation for 'my'. The term for 'dishes' is ",
   ('barinov', 'посуду!'),
   ' which translates to one singular thing in Russian.']),
 (13,
  None,
  ["'Already getting up, Chef.' The phrase ",
   ('max', 'Уже встаю,'),
   " translates to 'already I get up'. The plain action word stands in for 'I am getting up'."])]
