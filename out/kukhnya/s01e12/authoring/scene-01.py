# Authoring module for kukhnya-s01e12-scene-01.
ID = 'kukhnya-s01e12-scene-01'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 12
SCENE = 1
TITLE = 'Время перемен  (Time for Changes)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'kostya': 'Костя', 'max': 'Макс'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.12'
SOURCE_FILE = 'sources/kukhnya/s01/e12.ru.dual.srt'
INTRO = "This is Kukhnya, a comedy set in the kitchen of Claude Monet, a smart restaurant in Moscow. In this episode, young cook Max is in the changing room before his shift, telling his friend Kostya the bartender that he is done waiting for life to happen to him. He has a plan, and it involves Vika, the restaurant's art director. You'll hear it in Russian first, and you don't need to catch every word."
OPENER = "Now the slow version, starting with Max's big speech."
TRANSITION = 'And now the whole thing once more, from the top.'
OUTRO = "So Max has his speech, his goal and a surprise in his pocket. Kostya's last bit of advice, don't ruin it, turns out to be the hard part. Until next time."
CLOSING = ('max', 'Пока!')
STORY = [
    ('max', 'В жизни каждого человека нужны изменения.', "Changes are needed in every person's life.", [(1, 'Рано или поздно в жизни каждого человека наступают перемены.')], ''),
    ('kostya', 'Ты абсолютно прав, Макс.', 'You are absolutely right, Max.', [], ''),
    ('max', 'Я хочу изменить свою судьбу сегодня.', 'I want to change my destiny today.', [], ''),
    ('kostya', 'Надо действовать смело и не бояться.', 'One must act boldly and not be afraid.', [], ''),
    ('max', 'Моя цель — стать лучшим поваром.', 'My goal is to become the best cook.', [], ''),
    ('kostya', 'Это очень хорошая мечта для тебя.', 'This is a very good dream for you.', [], ''),
    ('max', 'Я сделаю важный шаг прямо сейчас.', 'I will make an important step right now.', [], ''),
    ('kostya', 'Какой сюрприз ты приготовил для нас?', 'What surprise have you prepared for us?', [], ''),
    ('max', 'Этот сюрприз ждёт только Вику.', 'This surprise is waiting only for Vika.', [], ''),
    ('kostya', 'Удачи тебе, мой смелый друг.', 'Good luck to you, my brave friend.', [], ''),
    ('max', 'Спасибо, Костя, я пойду к ней.', 'Thank you, Kostya, I will go to her.', [], ''),
    ('kostya', 'Главное — ничего не испортить сегодня.', 'The main thing is not to ruin anything today.', [], ''),
    ('max', 'Не волнуйся, всё будет просто отлично.', 'Do not worry, everything will be simply great.', [], ''),
]
WALK = [
    (0, None, ["'Changes are needed in every person's life.' There's no 'is' in it. Notice how ", ('max', 'нужны'), ' sits next to ', ('max', 'изменения'), " and that's the whole sentence. Russian drops 'is' in the present all the time."]),
    (1, None, ["'You are absolutely right, Max.' Notice how ", ('kostya', 'прав'), " ends in a bare consonant because Max is a man. If a woman were being agreed with, it would get an 'a' on the end. The name at the end is like calling someone over."]),
    (2, None, ["'I want to change my destiny today.' After 'I want', the next action just follows in its basic form, so 'I want to change' is two words, like English. Notice how ", ('max', 'свою'), ('max', 'судьбу'), " means 'my own destiny'. Russian uses a special word for 'one's own' when the owner is the one doing the action, and ", ('max', 'судьбу'), " ends in an 'u' sound as the thing being changed."]),
    (3, None, ["'One must act boldly and not be afraid.' Notice how ", ('kostya', 'Надо'), " means 'it's necessary' and it works for anybody, a bit like 'one must'. The expression for 'boldly' is built from 'bold' with its ending swapped, and Kostya uses 'bold' itself later when he wishes Max luck."]),
    (4, None, ["'My goal is to become the best cook.' A dash stands where the missing 'is' would be. After ", ('max', 'стать'), ", both words take the 'as' ending: ", ('max', 'лучшим'), ('max', 'поваром'), ", so you hear an 'm' at the end of each."]),
    (5, None, ["'This is a very good dream for you.' 'Dream' is a feminine word, so 'good' takes the feminine ending to match. Notice how 'for you' is ", ('kostya', 'для'), ('kostya', 'тебя'), ". After 'for', the term for 'you' changes its shape."]),
    (6, None, ["'I will make an important step right now.' 'Right now' is ", ('max', 'прямо'), ('max', 'сейчас'), ', straight now. Notice how ', ('max', 'сделаю'), " is a future with no extra 'will' word: the verb's own ending does it."]),
    (7, None, ["'What surprise have you prepared for us?' 'Surprise' is the English word, borrowed whole. Notice how ", ('kostya', 'приготовил'), " takes an 'l' sound since the 'you' here is Max. Asking a woman, Kostya would add an 'a'."]),
    (8, None, ["'This surprise is waiting only for Vika.' There's no word for 'for' after ", ('max', 'ждёт'), '. The person waited for just changes ending, so Vika becomes ', ('max', 'Вику'), ". It has the same 'u' ending as 'destiny' earlier."]),
    (9, None, ["'Good luck to you, my brave friend.' It's a fixed phrase, and the first word is 'luck' in a special shape. Notice how ", ('kostya', 'смелый'), " is the adjective behind Kostya's earlier 'boldly'."]),
    (10, None, ["'Thank you, Kostya, I will go to her.' Observe how 'to her' is two words, ", ('max', 'к'), ('max', 'ней'), ". After a little word like 'to', 'her' changes shape. The term ", ('max', 'Спасибо'), ' carries an everyday thank you.']),
    (11, None, ["'The main thing is not to ruin anything today.' It has two 'no' words in it, ", ('kostya', 'ничего'), ' and ', ('kostya', 'не'), ", and Russian wants both. The first word means 'the main thing', like a headline for the rest of the sentence."]),
    (12, None, ["'Do not worry, everything will be simply great.' Pay attention to how ", ('max', 'Не'), ('max', 'волнуйся'), " is really 'don't worry yourself', and the suffix at the end is that 'yourself'. 'Will be' is spoken out loud because Russian drops 'to be' only in the present."]),
]
