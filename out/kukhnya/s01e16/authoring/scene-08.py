# Authoring module for kukhnya-s01e16-scene-08.
ID = 'kukhnya-s01e16-scene-08'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 16
SCENE = 8
TITLE = 'Чей паштет лучше  (Whose Pâté is Better)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'kostya': 'Костя', 'max': 'Макс'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.16'
SOURCE_FILE = 'sources/kukhnya/s01/e16.ru.dual.srt'
INTRO = "Over in the bar, Kostya has gossip: the inspectors have turned up next door. Max doesn't care. All he can think about is his bet with the chef, so he makes his friend say, honestly, whose pâté is better. Listen for how long Kostya stalls before he answers."
OPENER = 'Now the honest verdict, line by line.'
TRANSITION = 'And the bar conversation once more, at full speed.'
OUTRO = "Kostya gives the honest answer and Max takes it on the chin. Notice that Kostya sends him off with 'udachi', a wish for luck: it's a good word to keep for yourself. See you next time!"
CLOSING = ('kostya', 'Ну, удачи!')
STORY = [
    ('kostya', 'Макс, ты слышал про проверку?', 'Max, did you hear about the inspection?', [(58, 'А ты слышал про проверку ФМС в другом ресторане?')], ''),
    ('max', 'Нет, не слышал.', "No, I didn't.", [(59, 'Ё-моё, нет.')], ''),
    ('kostya', 'В соседнем ресторане сейчас проверка.', 'There is an inspection at the restaurant next door right now.', [(58, 'в другом ресторане?')], ''),
    ('max', 'Мне сейчас не до этого.', 'I have no time for that right now.', [], ''),
    ('kostya', 'Там проверяют всех поваров.', 'They are checking all the cooks over there.', [], ''),
    ('max', 'Скажи честно, чей паштет лучше, мой или шефа?', "Tell me honestly, whose pâté is better, mine or the chef's?", [(59, 'Чей паштет лучше, мой или шефа?')], ''),
    ('kostya', 'А ты не обидишься?', "And you won't be offended?", [], ''),
    ('max', 'Нет, говори правду.', 'No, tell the truth.', [], ''),
    ('kostya', 'А ты шефу не скажешь?', "And you won't tell the chef?", [(60, 'А ты шефу не скажешь?')], ''),
    ('max', 'Нет, не скажу.', "No, I won't.", [(60, 'Нет.')], ''),
    ('kostya', 'У шефа лучше.', "The chef's is better.", [(61, 'У шефа лучше.')], ''),
    ('max', 'Ничего, я найду его секретный ингредиент!', "Never mind, I'll find his secret ingredient!", [], ''),
]
WALK = [
    (0, None, "'Max, did you hear about the inspection?' 'Pro', 'about', is the casual partner of the more formal 'o'. After 'pro', 'proverka' becomes 'proverku'."),
    (1, None, "'No, I didn't.' Russian answers with the verb itself, 'ne slyshal', literally 'not heard'. There is no short 'I didn't' to lean on."),
    (2, None, "'There is an inspection at the restaurant next door right now.' In Russian, 'v sosednem restorane', 'in the neighboring restaurant', changes both words to say where."),
    (3, None, "'I have no time for that right now.' 'Mne ne do etogo' is literally 'to me not up to this', the everyday way to say you're too busy to care."),
    (4, None, "'They are checking all the cooks over there.' Russian drops 'they' and lets the verb carry it: 'proveryayut', 'they check'. 'Vsekh povarov' means 'all the cooks' as the ones being checked."),
    (5, None, "'Tell me honestly, whose pâté is better, mine or the chef's?' 'Chey' means 'whose', and it matches the word after it: 'chey pashtet', but 'chya kniga', 'whose book'."),
    (6, None, "'And you won't be offended?' 'Obidishsya' means 'you'll take offense'. The '-sya' on the end shows the hurt happens to you."),
    (7, None, "'No, tell the truth.' 'Govori', 'speak' or 'tell', is the 'ty' command, and 'pravda' becomes 'pravdu' because it's the thing told. The newspaper 'Pravda' is the same word."),
    (8, None, "'And you won't tell the chef?' 'Shefu', 'to the chef', is 'shef' with '-u' added for the person you tell something to."),
    (9, None, "'No, I won't.' Russian repeats the verb: 'ne skazhu', literally 'I won't say'. It's the natural short answer to 'ty ne skazhesh?'"),
    (10, None, "'The chef's is better.' Kostya keeps it to three words. 'U shefa' is literally 'at the chef', so 'u shefa luchshe' means 'at the chef's place it's better'."),
    (11, None, "'Never mind, I'll find his secret ingredient!' 'Nichego' literally means 'nothing', but at the start of a reply it means 'never mind' or 'no matter'."),
]
