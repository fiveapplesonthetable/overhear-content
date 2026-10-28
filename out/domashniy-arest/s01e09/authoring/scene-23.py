# Authoring module for domashniy-arest-s01e09-scene-23.
ID = 'domashniy-arest-s01e09-scene-23'
SHOW = 'domashniy-arest'
SEASON = 1
EPISODE = 9
SCENE = 23
TITLE = 'Золотой ключик  (The Golden Key)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'arkady': 'Аркадий', 'marina': 'Марина'}
SOURCE_NAME = 'Домашний арест, Сезон 1, Эпизод 9'
SOURCE_FILE = 'sources/domashniy-arest/s01/e09.ru.dual.srt'
INTRO = 'Previously, Marina insisted that honest communication is the foundation of any genuine relationship. Believing her sincerity, Arkady finally discloses where he hid his bribe money, provoking an unexpectedly jealous reaction from Marina.'
OPENER = "Let's see how Arkady reveals the surprising location of his hidden fortune."
TRANSITION = 'Now listen to the revelation of the secret hiding place once more.'
OUTRO = "Marina leaves the meeting with the crucial confession, but finds herself unsettled by Arkady's past. See you next time!"
CLOSING = ('marina', 'Пока!')
STORY = [
    ('marina', 'Если молчите, я сейчас уйду.', 'If you stay silent, I will leave now.', [(701, 'Хорошо, вы не прошли цены, я пошла')], 'adapted cue 701'),
    ('arkady', 'Подождите, я всё вам расскажу.', 'Wait, I will tell you everything.', [(702, 'Ну почему же, я скажу')], 'adapted cue 702'),
    ('arkady', 'Я спрятал деньги в детском садике.', 'I hid the money in a kindergarten.', [(703, 'деньги я спрятал в детском садике «Золотой ключик»')], 'shortened cue 703'),
    ('marina', 'В детском саду? Не может быть!', 'In a kindergarten? That cannot be!', [], 'shocked reaction'),
    ('arkady', 'Там работает одна моя старая знакомая.', 'An old female acquaintance of mine works there.', [(704, 'Одна из воспитательниц – моя любовница')], 'toned down cue 704'),
    ('arkady', 'Она была моей близкой подругой.', 'She was a close female friend of mine.', [(704, 'моя любовница'), (705, 'Бывшая')], 'cleaned cue 704-705'),
    ('arkady', 'Но это было очень давно.', 'But that was very long ago.', [(705, 'Бывшая')], 'expanded cue 705'),
    ('arkady', 'Теперь вы довольны моим ответом?', 'Are you satisfied with my answer now?', [(706, 'Вы довольны?')], 'added Теперь and моим ответом'),
    ('marina', 'А мне это совсем не интересно!', 'And I am not interested in that at all!', [(708, 'мне вообще неинтересно')], 'adapted cue 708'),
    ('marina', 'Я просто спросила из любопытства.', 'I simply asked out of curiosity.', [(707, 'я просто так спросила')], 'adapted cue 707'),
    ('arkady', 'Вы ревнуете меня к прошлому?', 'Are you jealous of my past?', [], 'amused observation'),
    ('marina', 'Ничего подобного, вы мне безразличны!', 'Nothing of the sort, you mean nothing to me!', [], 'defensive denial'),
]
WALK = [
    (0, None, "'If you stay silent, I will leave now.' Marina pretends to walk away to force his hand."),
    (1, None, "'Wait, I will tell you everything.' The command form stops her departure in time."),
    (2, None, "'I hid the money in a kindergarten.' Arkady reveals the bizarre hiding spot."),
    (3, None, "'In a kindergarten? That cannot be!' Marina's exclamation expresses pure disbelief."),
    (4, None, "'An old female acquaintance of mine works there.' Arkady explains his trusted connection."),
    (5, None, "'She was a close female friend of mine.' He clarifies their former intimate bond."),
    (6, None, "'But that was very long ago.' Arkady quickly downplays the relationship to appease Marina."),
    (7, None, "'Are you satisfied with my answer now?' The short adjective checks if she believes him."),
    (8, None, "'And I am not interested in that at all!' Marina huffs and denies any personal interest."),
    (9, None, "'I simply asked out of curiosity.' The location phrase frames her inquiry as casual."),
    (10, None, "'Are you jealous of my past?' Arkady teases her about her obvious emotional reaction."),
    (11, None, "'Nothing of the sort, you mean nothing to me!' Marina furiously denies her rising jealousy."),
]
