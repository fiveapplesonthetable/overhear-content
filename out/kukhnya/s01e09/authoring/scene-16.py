# Authoring module for kukhnya-s01e09-scene-16.
ID = 'kukhnya-s01e09-scene-16'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 9
SCENE = 16
TITLE = 'Торт для банкета  (The Banquet Cake)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'louis': 'Луи'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.09'
SOURCE_FILE = 'sources/kukhnya/s01/e09.ru.dual.srt'
INTRO = "The banquet cake is almost ready in the pastry section, and Louis is proud of it. Barinov comes by to check. Then he spots something in the cream that shouldn't be there. Hear it first, then we'll pick it apart."
OPENER = "We'll go slowly this time."
TRANSITION = "This time you'll hear more."
OUTRO = "Louis will fix it, and he promises the cake will be perfect. What the guests don't know won't hurt them. Carry on listening, and see you soon."
CLOSING = ('louis', 'Пока!')
STORY = [
    ('louis', 'Шеф, я почти закончил этот торт.', 'Chef, I have almost finished this cake.', [], ''),
    ('barinov', 'Покажи мне его, Луи.', 'Show it to me, Louis.', [], ''),
    ('louis', 'Я думаю, торт скоро можно подавать.', 'I think the cake can be served soon.', [(309, 'Я думаю, торт через пять минут уже можно подавать.')], ''),
    ('barinov', 'Подожди, это ещё что такое?', 'Wait, what on earth is this?', [(310, 'Это еще что такое?')], ''),
    ('louis', 'Ой, это же железная струбцина!', 'Oh, this is an iron clamp!', [(311, 'Это струб.')], ''),
    ('barinov', 'Откуда она взялась в креме?', 'Where did it come from in the cream?', [], ''),
    ('barinov', 'Это же праздничный торт для гостей!', 'This is a celebration cake for the guests!', [], ''),
    ('louis', 'Наверное, маленькая девочка играла здесь.', 'Probably the little girl was playing here.', [], ''),
    ('barinov', 'Алиса трогала твой торт?', 'Did Alisa touch your cake?', [], ''),
    ('louis', 'Шеф, спокойно, не нужно кричать.', 'Chef, calm down, no need to shout.', [(312, 'Спокойно.')], ''),
    ('louis', 'Я сейчас быстро всё исправлю.', 'I will quickly fix everything right now.', [(313, 'Я все исправлю.')], ''),
    ('barinov', 'Сделай красиво, чтобы гости ничего не заметили.', 'Make it pretty so the guests notice nothing.', [], ''),
    ('louis', 'Обещаю, торт будет идеальным.', 'I promise, the cake will be perfect.', [], ''),
]
WALK = [
    (0, None, '\'Chef, I have almost finished this cake.\' "Zakonchil", "finished", ends in the man\'s -l, and "pochti" is "almost". It\'s a modest, tired sentence from a pastry chef who has been working all day.'),
    (1, None, '\'Show it to me, Louis.\' "Pokazhi" is the same short command the chef used about Alisa\'s face. "Pokazhi mne ego" is "show me it", with no "please". Barinov wants to look first.'),
    (2, None, '\'I think the cake can be served soon.\' "Mozhno", "it\'s possible" or "allowed", is the opposite of "nelzya" from the chocolate talk. "Podavat" is "to serve" a dish. Louis says it with caution.'),
    (3, None, '\'Wait, what on earth is this?\' The Russian is "eto eshchyo chto takoe", "this still what such", and "eshchyo" adds the "on earth". "Podozhdi" is "wait", said to one person. Barinov has seen it, and it can\'t be good.'),
    (4, None, '\'Oh, this is an iron clamp!\' "Zheleznaya", "iron", grows from "zhelezo", the metal, and ends in -aya to match "strubtsina", "clamp". A tool in a banquet cake is a disaster.'),
    (5, None, '\'Where did it come from in the cream?\' "Otkuda" is the third "where", "from where", after "gde" and "kuda". "Vzyalas" literally says "took itself", the Russian way to ask how something turned up.'),
    (6, None, '\'This is a celebration cake for the guests!\' "Prazdnichny", "festive", grows from "prazdnik", "holiday". "Dlya gostey" is "for the guests". Barinov is outraged, because a tool in the cake would ruin the whole evening.'),
    (7, None, '\'Probably the little girl was playing here.\' "Navernoe" is "probably". "Igrala", "was playing", has the girl\'s -la. Louis names the culprit without saying her name, but he means Alisa.'),
    (8, None, '\'Did Alisa touch your cake?\' "Trogala" is "touched", with a girl\'s -la. There is no question word, only the voice rising at the end. Barinov\'s anger is already building.'),
    (9, None, '\'Chef, calm down, no need to shout.\' "Spokoyno", "calmly", works alone as "calm down". "Ne nuzhno krichat" is "not needed to shout", the "nuzhno" pattern again. Louis tries to soothe.'),
    (10, None, '\'I will quickly fix everything right now.\' "Ispravlyu", "I will fix", grows from "pravy", "right", so it means "make right". "Vsyo" is "everything". Louis knows how to rescue a cake.'),
    (11, None, '\'Make it pretty so the guests notice nothing.\' After "chtoby", so that, the verb goes into the past: "zametili", though nothing has happened yet. "Nichego ne", nothing not, is the double negative Russian insists on.'),
    (12, None, '\'I promise, the cake will be perfect.\' "Obeshchayu" is "I promise". "Idealnym" is the word "ideal" with a Russian ending, the one that comes after "budet", "will be". Louis keeps his word.'),
]
