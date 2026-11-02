# Authoring module for kukhnya-s01e06-scene-15.
ID = 'kukhnya-s01e06-scene-15'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 6
SCENE = 15
TITLE = 'Писатель Виктор Пелевин  (The Writer Viktor Pelevin)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'kostya': 'Костя', 'max': 'Макс'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.06'
SOURCE_FILE = 'sources/kukhnya/s01/e06.ru.dual.srt'
INTRO = "Back at Claude Monet, Max has a plan to get Rodion a table: book it in the name of Viktor Pelevin, a famous writer whom nobody ever sees. Kostya thinks it's madness. It's in Russian first."
OPENER = "Let's go through the phone call and the argument after it. Max is sure of himself, and Kostya isn't."
TRANSITION = "Here's the booking and the argument in one go."
OUTRO = 'You can now book a table in Russian: "zabronirovat stolik", for whom, and the name. And if you need to worry out loud, a "esli" and "vdrug" both mean \'what if\'. See you next time.'
CLOSING = ('max', 'Пока!')
STORY = [
    ('max', 'Алло, ресторан, я хочу забронировать столик.', 'Hello, restaurant, I want to reserve a table.', [(201, 'Ресторан Клод Мане, я слушаю вас')], ''),
    ('kostya', 'Макс, для кого именно ты заказываешь стол?', 'Max, for whom exactly are you booking a table?', [(204, 'Макс, какой Пелевин?')], ''),
    ('max', 'Для известного русского писателя Виктора Пелевина.', 'For the famous Russian writer Viktor Pelevin.', [(202, 'для писателя Виктора Пелевина')], ''),
    ('kostya', 'Ты с ума сошёл, какой ещё Пелевин?', 'Are you out of your mind, what Pelevin?', [(204, 'Макс, какой Пелевин?')], ''),
    ('max', 'Администратор очень обрадовалась такому важному гостю.', 'The administrator was very thrilled with such an important guest.', [(203, 'Какая честь. Ждем вас')], ''),
    ('kostya', 'А если Виктория знает его в лицо?', 'And what if Victoria knows what he looks like?', [(205, 'Вдруг она знает, как он выглядит')], ''),
    ('max', 'Пелевин — загадочный писатель, никто его не видел.', 'Pelevin is a mysterious writer, nobody has seen him.', [(206, 'Ты знаешь, как выглядит Виктор Пелевин?')], ''),
    ('kostya', 'Вдруг в ресторане есть его преданные читатели?', 'What if there are his devoted readers in the restaurant?', [(205, 'как он выглядит, а?')], ''),
    ('max', 'Они видели только его имя на обложке.', 'They only saw his name on the cover.', [(206, 'Да ладно тебе')], ''),
    ('kostya', 'Как Родион сможет убедительно изобразить гения?', 'How will Rodion be able to convincingly portray a genius?', [(207, 'А я знаю')], ''),
    ('max', 'Он просто наденет тёмные очки.', 'He will simply put on dark glasses.', [(208, 'Вот так')], ''),
    ('kostya', 'Надеюсь, эта безумная авантюра сработает сегодня.', 'I hope this crazy gamble will work today.', [(208, 'Вот так')], ''),
]
WALK = [
    (0, None, ["'Hello, restaurant, I want to reserve a table.' To sound like a serious customer, Max uses ", ('max', 'забронировать'), ' for booking the table.']),
    (1, None, ["'Max, for whom exactly are you booking a table?' Kostya wants to know the exact details, asking for whom ", ('kostya', 'именно'), ' the reservation is made.']),
    (2, None, ["'For the famous Russian writer Viktor Pelevin.' When describing the writer, the word ", ('max', 'известного'), ' highlights that he is very famous.']),
    (3, None, ["'Are you out of your mind, what Pelevin?' Expressing complete disbelief, Kostya uses the word ", ('kostya', 'сошёл'), ' as part of a common phrase for going crazy.']),
    (4, None, ["'The administrator was very thrilled with such an important guest.' The administrator was clearly very happy, so Max mentions she ", ('max', 'обрадовалась'), ' to hear about the VIP guest.']),
    (5, None, ["'And what if Victoria knows what he looks like?' Worrying about recognition, Kostya wonders if she knows his ", ('kostya', 'лицо'), ' from seeing him in person before.']),
    (6, None, ["'Pelevin is a mysterious writer, nobody has seen him.' Since nobody has ever seen the author, he is considered quite ", ('max', 'загадочный'), ' and mysterious.']),
    (7, None, ["'What if there are his devoted readers in the restaurant?' There might be some very loyal and ", ('kostya', 'преданные'), ' readers sitting in the dining room right now.']),
    (8, None, ["'They only saw his name on the cover.' People only know his name from seeing it printed on the ", ('max', 'обложке'), ' of his books.']),
    (9, None, ["'How will Rodion be able to convincingly portray a genius?' It will be very hard for Rodion to ", ('kostya', 'убедительно'), ' pretend to be someone so smart.']),
    (10, None, ["'He will simply put on dark glasses.' The simple plan is that the fake author just ", ('max', 'наденет'), ' dark glasses to hide his identity.']),
    (11, None, ["'I hope this crazy gamble will work today.' This whole crazy plan is just a risky ", ('kostya', 'авантюра'), ' that they hope will succeed today.']),
]
