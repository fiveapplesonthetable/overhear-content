# Authoring module for kukhnya-s01e06-scene-18.
ID = 'kukhnya-s01e06-scene-18'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 6
SCENE = 18
TITLE = 'Секретный ингредиент  (The Secret Ingredient)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'louis': 'Луи'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.06'
SOURCE_FILE = 'sources/kukhnya/s01/e06.ru.dual.srt'
INTRO = "In the kitchen at Claude Monet, Barinov has just heard that the inspector turned down the free wine. He isn't giving up. If the man won't drink it, he'll eat it, and he tells Louis, the pastry chef, to put alcohol in everything. It's in Russian first."
OPENER = "Let's go back through the scheme. Barinov is very pleased with himself, and Louis is horrified."
TRANSITION = 'Now the whole scheme again, at full speed.'
OUTRO = 'Keep "napoit" and "nakormit" together: to get someone drunk and to feed someone up. Both have na- on the front, and Barinov makes a slogan of them. See you next time.'
CLOSING = ('barinov', 'Пока!')
STORY = [
    ('barinov', 'Этот инспектор отказался пить наше вино!', 'This inspector refused to drink our wine!', [], ''),
    ('louis', 'Шеф, что же нам теперь делать?', 'Chef, what are we to do now?', [], ''),
    ('barinov', 'Раз не можем напоить, мы его накормим!', 'Since we cannot give him drink, we will feed him!', [(233, 'не можем напоить, мы тебя накормим')], ''),
    ('louis', 'Вы хотите добавить алкоголь в еду?', 'Do you want to add alcohol to food?', [], ''),
    ('barinov', 'Луи, приготовь для него десерт с коньяком!', 'Louis, prepare a dessert with cognac for him!', [(234, 'Луис, тебе десерт с коньяком')], ''),
    ('louis', 'Сколько ложек коньяка добавить в крем?', 'How many spoonfuls of cognac to add to the cream?', [], ''),
    ('barinov', 'Лей от души, коньяка не жалей!', 'Pour from the heart, do not spare cognac!', [], ''),
    ('louis', 'А как поступить с горячими блюдами?', 'And how to deal with hot dishes?', [], ''),
    ('barinov', 'В мясо мы щедро нальём сухое вино.', 'We will generously pour dry wine into the meat.', [], ''),
    ('louis', 'Инспектор точно почувствует вкус крепкого алкоголя.', 'The inspector will definitely taste strong alcohol.', [], ''),
    ('barinov', 'Он ничего не заметит в соусе!', 'He will not notice anything in the sauce!', [], ''),
    ('louis', 'Шеф, это очень дерзкий и опасный план.', 'Chef, this is a very daring and dangerous plan.', [], ''),
    ('barinov', 'Зато наш ресторан будет спасён, работай!', 'At least our restaurant will be saved, work!', [(236, 'Папочка будет готовить')], ''),
]
WALK = [
    (0, None, '\'This inspector refused to drink our wine!\' "Otkazalsya", refused, ends in -sya and takes a plain verb after it: "otkazalsya" pit. "Vino", wine, stays "vino" because it\'s neuter.'),
    (1, None, '\'Chef, what are we to do now?\' "Zhe" adds urgency to "chto", so "chto zhe" is \'what on earth\'. "Nam teper delat", \'to us now to do\', needs no \'should\'.'),
    (2, None, '\'Since we cannot give him drink, we will feed him!\' "Napoit" is to get someone drunk and "nakormit" to feed someone up. "Raz", here \'since\', otherwise means \'once\'.'),
    (3, None, '\'Do you want to add alcohol to food?\' Louis says "Vy khotite", the polite form for the chef. "V edu", into the food, changes "eda" to "edu" because the alcohol goes into it.'),
    (4, None, '\'Louis, prepare a dessert with cognac for him!\' "Prigotov", prepare, tells one person to "prigotovit". "S konyakom", with cognac, adds -om after s.'),
    (5, None, '\'How many spoonfuls of cognac to add to the cream?\' After "skolko", how many, both words change: "lozhka" becomes "lozhek" and "konyak" becomes "konyaka". "Krem", cream, is the pastry kind, not the dairy kind.'),
    (6, None, '\'Pour from the heart, do not spare cognac!\' "Ot dushi", \'from the soul\', means generously. "Ne zhaley", don\'t spare, uses "zhalet", a word that can also mean \'to pity\'.'),
    (7, None, '\'And how to deal with hot dishes?\' "Kak postupit" is \'how to act\' or \'what to do about\'. "S goryachimi blyudami", with hot dishes, has -imi and -ami after s.'),
    (8, None, '\'We will generously pour dry wine into the meat.\' "Sukhoe vino", dry wine, is wine that isn\'t sweet, just as in English. "Nalyom", we\'ll pour, goes back to "nalit", to pour in.'),
    (9, None, '\'The inspector will definitely taste strong alcohol.\' "Pochuvstvuet vkus", will feel the taste, means he\'ll really taste it. "Krepkiy", strong, is the word for strong drinks, coffee and tea.'),
    (10, None, '\'He will not notice anything in the sauce!\' "Nichego ne zametit", \'nothing not notice\', keeps both negatives. "V souse", in the sauce, has -e for the place.'),
    (11, None, '\'Chef, this is a very daring and dangerous plan.\' "Derzkiy", daring, can also mean cheeky or rude. "Opasnyy", dangerous, is from "opasnost", danger, which the inspector used about the floor.'),
    (12, None, '\'At least our restaurant will be saved, work!\' "Zato", \'but on the other hand\', is how Russians find the silver lining. "Rabotay", work, said to one person, ends the conversation.'),
]
