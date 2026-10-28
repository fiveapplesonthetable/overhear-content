# Authoring module for domashniy-arest-s01e07-scene-18.
ID = 'domashniy-arest-s01e07-scene-18'
SHOW = 'domashniy-arest'
SEASON = 1
EPISODE = 7
SCENE = 18
TITLE = 'Зимний пикник на природе  (Winter Picnic in Nature)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'danya': 'Даня', 'klavdia': 'Клавдия Викторовна', 'samson': 'Самсон'}
SOURCE_NAME = 'Домашний арест (Domashniy Arest) S1.07'
SOURCE_FILE = 'sources/domashniy-arest/s01/e07.ru.dual.srt'
INTRO = "In the last scene, acting mayor Pasha Osipenko ordered his bodyguards to ambush Samsonov so he cannot run for mayor. Meanwhile, in the communal kitchen, lawyer Danya is treating the neighbours to hot cheese fondue, giving Samsonov the perfect chance to challenge him to a winter picnic in the forest. Listen to the Russian conversation first, and don't worry about catching every word."
OPENER = "Did you hear how Samsonov goaded Danya into a winter trip to the woods? Let's walk through the scene."
TRANSITION = "Now let's hear the whole kitchen conversation again from start to finish."
OUTRO = 'Just as Sun Tzu advised in his dream, Samsonov has baited polite lawyer Danya into leaving his cosy fondue pot behind and heading out into the snowy forest. See you next time!'
CLOSING = ('samson', 'Пока!')
STORY = [
    ('danya', 'Есть такой английский повар. Я по его передачам научусь готовить.', 'There is this English chef. I will learn to cook from his shows.', [(683, 'Есть такой английский повар'), (684, 'Я по его передачам научусь готовить')], ''),
    ('danya', 'И огурцы тоже можно, можно всё, что хотите! Получаются уникальные вкусы.', 'And cucumbers are fine too, anything you want! You get unique flavours.', [(685, 'огурцы тоже можно'), (686, 'можно все, что хотите'), (687, 'Получаются уникальные вкусы')], "Slavik's question in 685 echoed by Danya"),
    ('danya', 'Ну как, вкусно?', 'Well, is it tasty?', [(688, 'Вкусно')], ''),
    ('samson', 'Ну, честно говоря, не по мне.', 'Well, honestly speaking, it is not for me.', [(689, 'честно говоря, не по мне')], ''),
    ('klavdia', 'Если бы водку макать, другое дело! От сыра в туалете не заснёшь.', 'Now if you could dip vodka in it, that would be another matter! Because you will not fall asleep in the bathroom from cheese.', [(691, 'Если бы водку макать'), (692, 'другое дело')], "cue 693 'на унитазе' -> 'в туалете'"),
    ('samson', 'Клавдия Викторовна, если бы вы моей тёщей были! Тогда я бы терпел.', 'Klavdia Viktorovna, if you were my mother-in-law! Then I would put up with you.', [(697, 'Клавдия Викторовна'), (698, 'если бы вы моей тещей были'), (699, 'я бы терпел')], "ASR 700 'даршочек с кашей ноговым одену' omitted"),
    ('klavdia', 'А Даня на Нине женится! И будем жить дружно и фондю есть.', 'And Danya will marry Nina! And we will live together in harmony and eat fondue.', [(702, 'он на ней женится'), (703, 'И будем жить дружно'), (704, 'Фондю есть')], "Nina's scolding in 705-706 narrated in WALK"),
    ('samson', 'Ладно, всё хорошо. Хорошо сидим!', 'All right, everything is fine. We are having a nice time sitting together!', [(708, 'Все хорошо'), (709, 'Хорошо сидим')], ''),
    ('samson', 'Только нашего русского размаха не хватает. Огонёк горит, а тепла мало.', 'Only it lacks our broad Russian scale. The little flame is burning, but there is hardly any warmth.', [(712, 'размаха'), (712, 'не хватает'), (713, 'огонек горит')], "slur 'по-пиндоски' (711) omitted"),
    ('samson', 'Вот так бы на природе, да? Мы давно на природе не были!', 'Now if we were out in nature, right? We have not been out in nature for a long time!', [(714, 'Вот так бы на природе, да'), (715, 'давно'), (715, 'не были')], ''),
    ('samson', 'Давайте поедем в лес на шашлыки! Даню вон с собой возьмём.', "Let's drive out to the forest for shashlik! We will take Danya here along with us.", [(717, 'Даню вон с собой возьмем')], "slang 'шашлычка намутим' (716) -> 'поедем в лес на шашлыки'"),
    ('danya', 'Ну, странный зимой пикник. Давайте лучше есть фондю.', "Well, a picnic in winter is strange. Let's just eat fondue instead.", [(718, 'Ну, странный зимой пикник'), (719, 'давайте есть фондю')], ''),
    ('klavdia', 'Смотри, дядя Даня, видишь, побелел! Испугался он зимнего леса.', 'Look, Uncle Danya has gone pale, see! He is afraid of the winter forest.', [(720, 'дядя Даня, видишь, побелел')], ''),
    ('danya', 'Нет, почему? Я готов!', 'No, why? I am ready!', [(721, 'почему'), (722, 'Я готов')], ''),
    ('samson', 'Отлично, тогда едем! Через час во дворе, да?', 'Great, then we are going! In an hour in the courtyard, okay?', [(723, 'отлично'), (724, 'Едем'), (730, 'Через час во дворе, да')], ''),
]
WALK = [
    (0, 'Есть такой английский повар.', "At the kitchen table over a bubbling fondue pot, Danya chats cheerfully: 'There is this English chef.'"),
    (0, 'Я по его передачам научусь готовить.', "'I will learn to cook from his shows.' The line opens with 'I' and lands on 'to cook' at the end for emphasis."),
    (1, 'И огурцы тоже можно, можно всё, что хотите!', "When Slavik asks if he can dip cucumbers in the melted cheese, Danya beams: 'Cucumbers are fine too, anything you want!'"),
    (1, 'Получаются уникальные вкусы.', "'You get unique flavours.' Notice the self-action verb form on the verb for 'turn out', which directs the action back onto the subject."),
    (2, None, "Danya turns to Samsonov: 'Well, is it tasty?'"),
    (3, None, "'Well, honestly speaking, it is not for me,' Samsonov replies dryly."),
    (4, 'Если бы водку макать, другое дело!', "Old neighbour Klavdia Viktorovna cackles: 'Now if you could dip vodka in it, that would be another matter!'"),
    (4, 'От сыра в туалете не заснёшь.', "'You won't fall asleep in the bathroom from cheese!' she teases Samsonov."),
    (5, 'Клавдия Викторовна, если бы вы моей тёщей были!', "Samsonov glares at her: 'Klavdia Viktorovna, if you were my mother-in-law!' Notice the conditional particle with the past tense."),
    (5, 'Тогда я бы терпел.', "'Then I would put up with you,' he warns, while Nina scolds the old lady for stirring up trouble."),
    (6, 'А Даня на Нине женится!', "Unbothered, Klavdia Viktorovna adds: 'And Danya will marry Nina!'"),
    (6, 'И будем жить дружно и фондю есть.', "'And we will live together in harmony and eat fondue.' The line opens with 'and' and lands on 'eat' at the end for emphasis."),
    (7, 'Ладно, всё хорошо.', "Samsonov forces a smile to hide his jealousy: 'All right, everything is fine.'"),
    (7, 'Хорошо сидим!', "'We are having a nice time sitting together!' Samson uses the adverb for 'nicely' right alongside the verb meaning 'we are sitting'."),
    (8, 'Только нашего русского размаха не хватает.', "'Only it lacks our broad Russian scale,' he complains, looking at the tiny candle under the pot."),
    (8, 'Огонёк горит, а тепла мало.', "'The little flame is burning, but there is hardly any warmth.' Samson uses the adverb for 'little' right alongside the verb meaning 'is burning'."),
    (9, 'Вот так бы на природе, да?', "'Now if we were out in nature, right?' Samsonov suggests."),
    (9, 'Мы давно на природе не были!', "'We have not been out in nature for a long time!' In spoken Russian, word order is flexible: 'for a long time' comes first to set the focus, followed by 'have been'."),
    (10, 'Давайте поедем в лес на шашлыки!', "'Let's drive out to the forest for shashlik!' he proposes."),
    (10, 'Даню вон с собой возьмём.', "'We will take Danya here along with us.' The key word here means 'we will take', anchored at the close by 'we will take'."),
    (11, 'Ну, странный зимой пикник.', "Danya hesitates: 'Well, a picnic in winter is strange.'"),
    (11, 'Давайте лучше есть фондю.', "'Let's just eat fondue instead.' Notice how 'let's' sets up the clause and leads naturally into 'fondue'."),
    (12, 'Смотри, дядя Даня, видишь, побелел!', "'Look, Uncle Danya has gone pale, see!' Klavdia Viktorovna says to tease him."),
    (12, 'Испугался он зимнего леса.', "'He is afraid of the winter forest.' The key word here means 'got scared of', anchored at the close by 'the forest'."),
    (13, None, "Stung on his pride in front of Nina, Danya straightens up: 'No, why? I am ready!'"),
    (14, 'Отлично, тогда едем!', "'Great, then we are going!' Samsonov says triumphantly."),
    (14, 'Через час во дворе, да?', "'In an hour in the courtyard, okay?' In spoken Russian, word order is flexible: 'an hour' comes first to set the focus, followed by 'the courtyard'."),
]
