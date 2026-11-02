# Authoring module for kukhnya-s01e14-scene-10.
ID = 'kukhnya-s01e14-scene-10'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 14
SCENE = 10
TITLE = 'Заказ для гостей  (Order for the Guests)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'guest': 'Гость', 'kostya': 'Костя'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.14'
SOURCE_FILE = 'sources/kukhnya/s01/e14.ru.dual.srt'
INTRO = 'Kostya carries the plates over to the VIP table in the dining room. The guests are delighted with what they see. Russian first.'
OPENER = 'Once more, at a slower pace.'
TRANSITION = 'The table scene once more, from the top.'
OUTRO = "The guests are pleased, and Kostya goes off to fetch more wine. Both sides say the polite you and your all the way through, as you would at a good restaurant. Bye for now."
CLOSING = ('kostya', 'Пока!')
STORY = [
    ('kostya', 'Господа, вот ваши редкие французские блюда.', 'Gentlemen, here are your rare French dishes.', [(170, 'Господа, филиминьон по-фламански и лангусты а-ля Франце.')], ''),
    ('guest', 'Ого, как красиво лежит горячее мясо!', 'Wow, how beautifully the hot meat lies!', [], ''),
    ('kostya', 'Наш повар старался приготовить настоящий шедевр.', 'Our cook tried to prepare a real masterpiece.', [], ''),
    ('guest', 'Рыба тоже выглядит невероятно аппетитно и вкусно.', 'The fish also looks incredibly appetizing and tasty.', [], ''),
    ('kostya', 'Мы всегда используем только самые лучшие продукты.', 'We always use only the best products.', [], ''),
    ('guest', 'Передайте шеф-повару нашу искреннюю благодарность.', 'Pass on our sincere gratitude to the head chef.', [], ''),
    ('kostya', 'Обязательно скажу ему эти приятные слова.', 'I will certainly tell him these pleasant words.', [], ''),
    ('guest', 'Мы хотим заказать ещё бутылку вина.', 'We want to order another bottle of wine.', [], ''),
    ('kostya', 'Я сейчас быстро принесу ваше вино.', 'I will quickly bring your wine right now.', [], ''),
    ('guest', 'Спасибо за вашу прекрасную работу здесь.', 'Thank you for your wonderful work here.', [], ''),
    ('kostya', 'Приятного аппетита и хорошего вечера вам!', 'Bon appétit and have a good evening!', [], ''),
    ('guest', 'Спасибо, мы обязательно вернёмся сюда снова.', 'Thank you, we will definitely return here again.', [], ''),
    ('kostya', 'Мы всегда очень рады видеть вас!', 'We are always very glad to see you!', [], ''),
]
WALK = [
    (0, None, ["'Gentlemen, here are your rare French dishes.' Let's look at this line: ", ('kostya', 'Господа'), ' is the plural of sir, the formal way to address a table. ', ('kostya', 'ваши'), ', your, is plural to match ', ('kostya', 'блюда'), ', dishes.']),
    (1, None, ["'Wow, how beautifully the hot meat lies!' Let's focus on the phrase: ", ('guest', 'Ого'), " is a cheerful 'wow'. Russians say food ", ('guest', 'лежит'), ', lies, on a plate. ', ('guest', 'мясо'), ", meat, is neuter, so 'hot' is ", ('guest', 'горячее'), '.']),
    (2, None, ["'Our cook tried to prepare a real masterpiece.' Let's focus on the sentence: ", ('kostya', 'старался'), " is the man's form of the verb Sasha used about her cake. ", ('kostya', 'шедевр'), ' is borrowed from French.']),
    (3, None, ["'The fish also looks incredibly appetizing and tasty.' Let's look at the dialogue: ", ('guest', 'выглядит'), ' reuses the same for the feminine ', ('guest', 'Рыба'), ' as for a masculine steak: Russian verbs only change for he and she in the past.']),
    (4, None, ["'We always use only the best products.' We can break down the words: ", ('kostya', 'продукты'), ' in Russian means food ingredients, groceries, not products in general. ', ('kostya', 'используем'), " says 'we use', adding the 'we' ending."]),
    (5, None, ["'Pass on our sincere gratitude to the head chef.' We will break down the dialogue: ", ('guest', 'Передайте'), ", pass on, has the polite plural ending. The person it goes to takes the 'to' form, so head chef becomes ", ('guest', 'шеф'), '-', ('guest', 'повару'), '.']),
    (6, None, ["'I will certainly tell him these pleasant words.' We can consider this part: ", ('kostya', 'приятные'), ', pleasant, is the very word in the expression for bon appétit from the kitchen, here in its plural form. ', ('kostya', 'ему'), " is 'to him'."]),
    (7, None, ["'We want to order another bottle of wine.' We will consider the sentence: ", ('guest', 'ещё'), ('guest', 'бутылку'), " is 'one more bottle'. Wine becomes ", ('guest', 'вина'), " for 'of wine', and bottle becomes ", ('guest', 'бутылку'), ' as the thing ordered.']),
    (8, None, ["'I will quickly bring your wine right now.' We can focus on the words: ", ('kostya', 'принесу'), " is 'I will bring', with a prefix for towards here; in the kitchen Kostya said he would carry away. ", ('kostya', 'ваше'), ' is neuter, for ', ('kostya', 'вино'), '.']),
    (9, None, ["'Thank you for your wonderful work here.' Let's inspect the dialogue: ", ('guest', 'Спасибо'), ('guest', 'за'), " is 'thanks for', and what follows takes the same form as a thing seen: work becomes ", ('guest', 'вашу'), ('guest', 'прекрасную'), ('guest', 'работу'), '.']),
    (10, None, ["'Bon appétit and have a good evening!' Wishes take the 'of' form, as if 'I wish' were said: ", ('kostya', 'хорошего'), ('kostya', 'вечера'), ', of a good evening. ', ('kostya', 'вам'), " is 'to you'."]),
    (11, None, ["'Thank you, we will definitely return here again.' Let's focus on this part: ", ('guest', 'вернёмся'), " is 'we will come back'; without the reflexive ending, the verb means to give something back. ", ('guest', 'сюда'), " is 'here' as a destination."]),
    (12, None, ["'We are always very glad to see you!' Glad has a plural, ", ('kostya', 'рады'), ", since the speaker is 'we'. ", ('kostya', 'видеть'), ('kostya', 'вас'), " is 'to see you', using the polite ", ('kostya', 'вас'), '.']),
]
