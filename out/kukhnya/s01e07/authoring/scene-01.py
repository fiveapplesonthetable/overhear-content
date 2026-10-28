# Authoring module for kukhnya-s01e07-scene-01.
ID = 'kukhnya-s01e07-scene-01'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 7
SCENE = 1
TITLE = 'Жизнь в столице  (Life in the Capital)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'kostya': 'Костя', 'max': 'Макс'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.07'
SOURCE_FILE = 'sources/kukhnya/s01/e07.ru.dual.srt'
INTRO = "This is Kukhnya, which means The Kitchen, a Russian comedy set in Claude Monet, a smart Moscow restaurant where Chef Barinov shouts and the cooks try to keep their jobs. Episode seven opens with Max, a young cook from Voronezh who has been in Moscow for two weeks, chatting with Kostya, the bartender. Max is hiding something about where he lives. You'll hear it in Russian first, and it's fine to miss words."
OPENER = "Now slowly. It's a friendly chat, and the sentences are short enough to follow."
TRANSITION = 'And the whole chat once more.'
OUTRO = "Max says he doesn't pay a single kopeck, and Kostya doesn't believe him, which is how a secret gets started. You can already say how long you've lived somewhere and where you're from. See you next time."
CLOSING = ('max', 'Пока!')
STORY = [
    ('max', 'Я живу в Москве уже две недели.', 'I have been living in Moscow for two weeks already.', [(1, 'Две недели, как я уехал из Воронежа')], ''),
    ('kostya', 'Ты уже привык к жизни в Москве?', 'Have you already gotten used to life in Moscow?', [], ''),
    ('max', 'Я приехал сюда из Воронежа за мечтой.', 'I came here from Voronezh for a dream.', [(1, 'я уехал из Воронежа')], ''),
    ('kostya', 'И теперь ты работаешь в лучшем ресторане.', 'And now you work in the best restaurant.', [(2, 'Я работаю в самом офигенном ресторане Москвы')], ''),
    ('max', 'Ресторан Клод Моне — самый известный в городе.', 'Claude Monet restaurant is the most famous in the city.', [(3, 'Клод Мане')], ''),
    ('kostya', 'Здесь очень строгие правила и дорогое меню.', 'Here there are very strict rules and an expensive menu.', [], ''),
    ('max', 'Но для меня это прекрасный опыт.', 'But for me this is wonderful experience.', [], ''),
    ('kostya', 'А где ты нашёл себе жильё?', 'And where did you find yourself housing?', [], ''),
    ('max', 'Я живу в самом центре города.', 'I live right in the center of the city.', [(3, 'я живу в самом центре Москвы')], ''),
    ('kostya', 'Квартиры в центре стоят огромных денег.', 'Apartments in the center cost huge money.', [], ''),
    ('max', 'А я не плачу ни одной копейки!', 'And I do not pay a single kopeck!', [(3, 'ни копейки за это не'), (4, 'плачу')], ''),
    ('kostya', 'Это звучит очень странно и подозрительно.', 'That sounds very strange and suspicious.', [], ''),
    ('max', 'У меня есть один секретный план.', 'I have one secret plan.', [], ''),
]
WALK = [
    (0, None, "'I have been living in Moscow for two weeks already.' Russian has no 'have been living'. It says 'I live already two weeks', and the plain present covers it. 'Two weeks' uses the feminine 'two', since 'week' is a she-word."),
    (1, None, "'Have you already gotten used to life in Moscow?' 'Get used to' is followed by a small 'to' word, so it's 'used to to life'. 'In Moscow' puts an 'e' on the city."),
    (2, None, "'I came here from Voronezh for a dream.' 'Came' means arriving by some vehicle, such as a train. 'For a dream' uses the Russian 'za', which here is 'in pursuit of'."),
    (3, None, "'And now you work in the best restaurant.' 'The best' is a short word that ends in 'em' here, because it comes after 'in'. 'Now' is 'at this moment'."),
    (4, None, "'Claude Monet restaurant is the most famous in the city.' 'Most' in front of a describing word makes 'the most'. A dash replaces 'is', as Russian leaves it out."),
    (5, None, "'Here there are very strict rules and an expensive menu.' 'Menu' is borrowed and doesn't change. 'Expensive' ends in 'oe', since 'menu' counts as neuter in Russian."),
    (6, None, "'But for me this is a wonderful experience.' 'Experience' is also 'experiment'. 'For me' is two short words."),
    (7, None, "'And where did you find yourself housing?' The extra 'yourself' is a Russian habit that makes it friendlier, like 'for yourself'. 'Housing' is built on 'to live'."),
    (8, None, "'I live right in the center of the city.' 'The very' and 'the most' are the same word, which here means 'right in'. 'Of the city' is shown by the ending."),
    (9, None, "'Apartments in the center cost huge money.' Russian says apartments 'stand' a lot, with the word that also means 'to stand'. 'Huge money' puts the money in the 'of' form."),
    (10, None, "'And I do not pay a single kopeck!' 'Not a single' is a neat chunk, made of 'not even' and 'one'. A kopeck is one hundredth of a rouble."),
    (11, None, "'That sounds very strange and suspicious.' 'Sounds' comes from 'sound'. 'Suspicious' comes from 'suspect'."),
    (12, None, "'I have one secret plan.' Here Russian does use 'there is', for 'I have a particular thing'. 'Secret' looks like English with a different ending."),
]
