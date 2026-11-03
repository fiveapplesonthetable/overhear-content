# Authoring module for kukhnya-s01e08-scene-12.
ID = 'kukhnya-s01e08-scene-12'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 8
SCENE = 12
TITLE = 'Воспоминания о Провансе  (Memories of Provence)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'elena': 'Елена', 'louis': 'Луи'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.08'
SOURCE_FILE = 'sources/kukhnya/s01/e08.ru.dual.srt'
INTRO = "Still running Barinov's kitchen at Claude Monet, Elena goes over to Louis, the French pastry chef, who does not want her anywhere near his desserts. She finds a way to win him over. It's in Russian first."
OPENER = 'Slowly now. Louis starts out rude, and Elena wins him over with talk of home.'
TRANSITION = 'Now hear it all again, from the cold start to the warm finish.'
OUTRO = "Elena's method with Louis is simple: notice an accent, guess where it comes from, and talk warmly about home, starting with 'you have such a familiar accent'. See you next time."
CLOSING = ('louis', 'Пока!')
STORY = [
    ('elena', 'Луи, чем вы сейчас занимаетесь на десертах?', 'Louis, what are you doing on the desserts right now?', [], ''),
    ('louis', 'Какое вам вообще дело до моих десертов?', 'What business is it of yours regarding my desserts?', [], ''),
    ('elena', 'У вас такой тёплый и знакомый акцент.', 'You have such a warm and familiar accent.', [(131, 'Какой знакомый акцент')], ''),
    ('louis', 'Да, я приехал сюда из самой Франции.', 'Yes, I came here from France itself.', [], ''),
    ('elena', 'Это же Прованс, я абсолютно права?', 'It is Provence, am I absolutely right?', [(132, 'Прованс? Я права')], ''),
    ('louis', 'Да, мадам, вы очень тонко угадали!', 'Yes, madame, you guessed very subtly!', [(133, 'Да')], ''),
    ('elena', 'Я просто обожаю прекрасный Сен-Поль-де-Ванс!', 'I simply adore wonderful Saint-Paul-de-Vence!', [(133, 'Я обожаю Прованс'), (134, 'Особенно я люблю Сан-Поль-де-Ванс')], ''),
    ('louis', 'Невероятно, вся моя семья живёт именно там!', 'Incredible, my whole family lives right there!', [(135, 'Моя семья там живет')], ''),
    ('elena', 'А какие десерты подают в «Золотой голубке»!', "And what desserts they serve at La Colombe d'Or!", [(136, 'А какие десерты подают золотой голубке')], ''),
    ('louis', 'О, мадам, это моё самое любимое место!', 'Oh, madame, that is my most favorite place!', [(137, 'О, мадам')], ''),
    ('elena', 'Там великолепный вид и совершенно волшебная атмосфера.', 'There is a magnificent view and completely magical atmosphere.', [(136, 'Какой там вид')], ''),
    ('louis', 'Спасибо, я словно ненадолго вернулся домой!', 'Thank you, I felt as if I briefly returned home!', [(138, 'Я как будто ненадолго вернулся домой')], ''),
]
WALK = [
    (0, None, ["'Louis, what are you doing on the desserts right now?' Elena starts her question by using ", ('elena', 'занимаетесь'), ' to ask what Louis is currently busy doing in the kitchen.']),
    (1, None, ["'What business is it of yours regarding my desserts?' Louis responds dismissively with the word ", ('louis', 'дело'), ' to mean business or concern, asking why she cares.']),
    (2, None, ["'You have such a warm and familiar accent.' She tries to soften him up with ", ('elena', 'знакомый'), ', pointing out that his way of speaking sounds familiar.']),
    (3, None, ["'Yes, I came here from France itself.' He proudly emphasizes his origin by adding ", ('louis', 'самой'), ' before mentioning his home country, meaning the very place itself.']),
    (4, None, ["'It is Provence, am I absolutely right?' Asking if her guess is completely correct, she includes ", ('elena', 'абсолютно'), ' in her question to him.']),
    (5, None, ["'Yes, madame, you guessed very subtly!' The pastry chef is impressed and says ", ('louis', 'тонко'), ' to show that she figured it out with great subtlety.']),
    (6, None, ["'I simply adore wonderful Saint-Paul-de-Vence!' Expressing her deep affection for the town, Elena chooses ", ('elena', 'обожаю'), ' rather than a simpler word for love.']),
    (7, None, ["'Incredible, my whole family lives right there!' Finding this coincidence very hard to believe, Louis exclaims ", ('louis', 'Невероятно'), ' at the start of his sentence.']),
    (8, None, ["'And what desserts they serve at La Colombe d'Or!' When talking about the food they serve at the restaurant, she picks ", ('elena', 'подают'), ' to describe what is brought to the table.']),
    (9, None, ["'Oh, madame, that is my most favorite place!' He is completely won over now and calls it his ", ('louis', 'любимое'), ' location to visit.']),
    (10, None, ["'There is a magnificent view and completely magical atmosphere.' Describing the vibe of the place as magical, she says ", ('elena', 'волшебная'), ' to capture its special feeling.']),
    (11, None, ["'Thank you, I felt as if I briefly returned home!' Grateful for the chat, he mentions feeling like he returned home ", ('louis', 'ненадолго'), ', meaning for a short while.']),
]
