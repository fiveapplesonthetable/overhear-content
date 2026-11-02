# Authoring module for kukhnya-s01e08-scene-07.
ID = 'kukhnya-s01e08-scene-07'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 8
SCENE = 7
TITLE = 'Проверка на прочность  (Testing the Crew)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'elena': 'Елена'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.08'
SOURCE_FILE = 'sources/kukhnya/s01/e08.ru.dual.srt'
INTRO = "Elena is in the middle of her shift at Barinov's restaurant, Claude Monet. The orders are piling up, she thinks his cooks are too slow, and Barinov decides it is a good moment to leave her in charge. It's in Russian first."
OPENER = 'Slowly now. Elena pushes, Barinov defends his cooks, and then he walks out.'
TRANSITION = "Here's the argument once more, without stopping."
OUTRO = "Barinov's posmotrim, 'we'll see', is a whole reply on its own, and his longer posmotrim, kto ostanetsya pobeditelem, is a good line to end a bet on. You've also heard vy otlichno spravites, 'you'll manage excellently', a polite thing to say to anyone. See you next time."
CLOSING = ('barinov', 'До встречи!')
STORY = [
    ('elena', 'Повторяю для всех, заказ уже ждёт!', 'I repeat for everyone, the order is already waiting!', [(93, 'я повторю. Всем понятно')], ''),
    ('barinov', 'Елена, они прекрасно вас услышали.', 'Elena, they heard you perfectly well.', [(94, 'Всем понятно')], ''),
    ('elena', 'Почему тогда никто не работает?', 'Why then is nobody working?', [(94, 'Всем понятно')], ''),
    ('barinov', 'На моей кухне всегда строгий порядок.', 'In my kitchen there is always strict order.', [(95, 'вы справитесь')], ''),
    ('elena', 'Вы работаете слишком медленно для ресторана.', 'You work too slowly for a restaurant.', [(95, 'вы справитесь')], ''),
    ('barinov', 'Каждому хорошему блюду нужно своё время.', 'Every good dish needs its own time.', [(95, 'вы справитесь')], ''),
    ('elena', 'Гости не любят долго ждать еду.', 'Guests do not like to wait long for food.', [(95, 'вы справитесь')], ''),
    ('barinov', 'Наши гости ценят высокий вкус.', 'Our guests appreciate high taste.', [(95, 'вы справитесь')], ''),
    ('elena', 'Я сама покажу, как надо работать!', 'I will show myself how one must work!', [(95, 'вы справитесь')], ''),
    ('barinov', 'Отлично, я пойду спокойно отдохну.', 'Great, I will go calmly rest.', [(96, 'Я пойду прогуляюсь пока')], ''),
    ('elena', 'Вы бросаете свою кухню на меня?', 'Are you abandoning your kitchen to me?', [(96, 'Я пойду прогуляюсь пока')], ''),
    ('barinov', 'Я уверен, что вы отлично справитесь.', 'I am sure that you will manage excellently.', [(95, 'Ну, я думаю, вы справитесь')], ''),
    ('elena', 'Возвращайтесь скорее, иначе я заберу ресторан!', 'Return soon, otherwise I will take the restaurant!', [(97, 'Так, работаем, работаем, работаем')], ''),
    ('barinov', 'Посмотрим, кто здесь останется победителем!', "We'll see who stays the winner here!", [(97, 'Так, работаем')], ''),
]
WALK = [
    (0, None, ["'I repeat for everyone, the order is already waiting!' When nobody reacted the first time, ", ('elena', 'Повторяю'), ' is what you say to them.']),
    (1, None, ["'Elena, they heard you perfectly well.' Using this specific word for hearing, ", ('barinov', 'услышали'), ' means they actually did get the message.']),
    (2, None, ["'Why then is nobody working?' Russian keeps both negative parts, so ", ('elena', 'никто'), ' pairs with a not working action.']),
    (3, None, ["'In my kitchen there is always strict order.' People often use this exact word ", ('barinov', 'строгий'), ' when talking about schools, armies and kitchens.']),
    (4, None, ["'You work too slowly for a restaurant.' Just like in English, this word ", ('elena', 'слишком'), ' sits right in front of the describing word.']),
    (5, None, ["'Every good dish needs its own time.' This little pointing word right here ", ('barinov', 'своё'), ' looks back at the dish as the owner of the time.']),
    (6, None, ["'Guests do not like to wait long for food.' English waits for meals, but here ", ('elena', 'ждать'), ' applies directly to the food itself without a connecting word.']),
    (7, None, ["'Our guests appreciate high taste.' The core part of this word ", ('barinov', 'ценят'), ' is exactly the same as the word for a price tag.']),
    (8, None, ["'I will show myself how one must work!' Speaking as a woman, she uses ", ('elena', 'сама'), ' to mean that she will do the job with her own hands.']),
    (9, None, ["'Great, I will go calmly rest.' In everyday casual speech, actions like ", ('barinov', 'отдохну'), ' can sit right next to going somewhere without an and between them.']),
    (10, None, ["'Are you abandoning your kitchen to me?' Literally meaning to throw something away, ", ('elena', 'бросаете'), ' also talks about abandoning someone or dumping a job on them.']),
    (11, None, ["'I am sure that you will manage excellently.' A man talking about himself says ", ('barinov', 'уверен'), ' to show that he is very sure of things.']),
    (12, None, ["'Return soon, otherwise I will take the restaurant!' Bringing in a fun little threat, ", ('elena', 'иначе'), ' shows what will happen next if he does not come back.']),
    (13, None, ["'We'll see who stays the winner here!' Time will tell is what this ", ('barinov', 'Посмотрим'), ' basically means in this situation.']),
]
