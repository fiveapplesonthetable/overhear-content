# Authoring module for kukhnya-s01e19-scene-02.
ID = 'kukhnya-s01e19-scene-02'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 19
SCENE = 2
TITLE = 'Новые имена  (New names)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'artyom': 'Артём', 'barinov': 'Шеф', 'fedya': 'Федя'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.19'
SOURCE_FILE = 'sources/kukhnya/s01/e19.ru.dual.srt'
INTRO = "Meanwhile at Claude Monet, Barinov misses Senya and Fedya, the two cooks who were fired, and he won't learn the new cooks' names. Listen to it in Russian first, and just catch what you can."
OPENER = "Now, line by line, the chef's naming game."
TRANSITION = 'Here it is once more, with the new names flying.'
OUTRO = 'Barinov handed out two new names in under a minute, and you kept up with the swaps. See you next time!'
CLOSING = ('barinov', 'Пока!')
STORY = [
    ('barinov', 'Сеня, соус готов?', 'Senya, is the sauce ready?', [(16, 'Сеня, соус готов?')], ''),
    ('artyom', 'А я не Сеня.', 'I am not Senya.', [(17, 'А я не Сеня, я Артем.')], ''),
    ('artyom', 'Я Артем.', 'I am Artyom.', [(17, 'А я не Сеня, я Артем.')], ''),
    ('barinov', 'Сеню уволили.', 'Senya got fired.', [(18, 'Сеню же уволили. А мне плевать, кто ты.')], ''),
    ('barinov', 'Мне плевать, кто ты.', 'I do not care who you are.', [(18, 'Сеню же уволили. А мне плевать, кто ты.')], ''),
    ('barinov', 'Сегодня ты Сеня.', 'Today you are Senya.', [(19, 'Сегодня ты Сеня.')], ''),
    ('barinov', 'Федя бы это быстро сделал.', 'Fedya would have done it fast.', [(21, 'Федя бы это за 10 секунд сделал.')], ''),
    ('fedya', 'Я тоже Федя, шеф.', 'I am Fedya too, Chef.', [(22, 'Я, кстати, тоже Федя, шеф.')], ''),
    ('barinov', 'Нет, ты не Федя.', 'No, you are not Fedya.', [(23, 'Нет, ты не Федя.')], ''),
    ('barinov', 'Имя Федя заслужить надо.', 'You have to earn the name Fedya.', [(24, 'Имя Федя заслужить надо.')], ''),
    ('barinov', 'Теперь ты Артем.', 'Now you are Artyom.', [(25, 'Теперь ты Артем.')], ''),
    ('fedya', 'Да, шеф.', 'Yes, Chef.', [(26, 'Да, шеф.')], ''),
]
WALK = [
    (0, None, "'Senya, is the sauce ready?' \"Gotov\", 'ready', has no ending because \"sous\", 'sauce', is a masculine word; a ready pizza would be \"gotova\". \"Sous\" itself comes from French."),
    (1, None, "'But I'm not Senya.' A at the start is a soft 'but', used when you correct someone. Ya ne Senya is simply 'I not Senya', with no word for 'am'."),
    (2, None, "'I'm Artyom.' Ya and a name is the simplest way to introduce yourself. You could say it at any door: ya Maks."),
    (3, None, "'Senya got fired.' The name turns into \"Senyu\" because he's the one being fired. \"Uvolili\", 'they fired', has no 'they': the -li ending alone points at whoever did it."),
    (4, None, "'I don't care who you are.' \"Mne plevat'\" is literally 'to me, to spit', a rude way to say 'I don't care'. \"Kto ty\", 'who you are', is just 'who you', with no verb at all."),
    (5, None, "'Today you're Senya.' \"Segodnya\", 'today', is spelled with a \"g\" but said with a \"v\", 'sevodnya'. The chef hands out the name like a job for the day."),
    (6, None, "'Fedya would have done it fast.' \"By\" after the name turns \"sdelal\", 'did', into 'would have done'. \"Sdelal\" is \"s-\" plus \"delal\", and the \"s-\" marks the job as finished."),
    (7, None, "'I'm Fedya too, Chef.' This cook's real name happens to be Fedya. \"Tozhe\", 'too', sits right before what it adds to: \"tozhe\" Fedya, 'also Fedya'."),
    (8, None, "'No, you're not Fedya.' Ne goes straight in front of the thing denied, here the name. It's the same pattern as ya ne Senya a moment ago."),
    (9, None, "'You have to earn the name Fedya.' \"Zasluzhit' nado\", 'to earn is needed', is how Russian says 'you have to earn'. \"Imya\", 'name', is one of a few odd words ending in -mya; \"vremya\", 'time', is another."),
    (10, None, "'Now you're Artyom.' \"Teper'\" means 'now' as in 'from now on', a change from before. So this cook gets the other one's name."),
    (11, None, "'Yes, Chef.' \"Da, shef\" is all a cook ever needs to say back. \"Shef\" is French chef, borrowed whole."),
]
