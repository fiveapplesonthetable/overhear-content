# Authoring module for kukhnya-s01e08-scene-17.
ID = 'kukhnya-s01e08-scene-17'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 8
SCENE = 17
TITLE = 'Преданный Аркашка  (Loyal Arkasha)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'lyova': 'Лёва'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.08'
SOURCE_FILE = 'sources/kukhnya/s01/e08.ru.dual.srt'
INTRO = "At Claude Monet, Barinov has shut himself in his dark office, sure that his cooks have betrayed him for Elena. He talks to the only one he trusts, his goldfish Arkasha, until Lyova, one of his cooks, comes to find him. It's in Russian first."
OPENER = 'Slowly now. Barinov is dramatic, and Lyova tries to bring him back.'
TRANSITION = 'And the whole sad scene again, without the pauses.'
OUTRO = "Barinov's ya nikuda ne poydu, 'I'm not going anywhere', is easy to say and very firm. And skuchat bez, literally 'to be bored without', is how Russians say they miss someone. See you next time."
CLOSING = ('barinov', 'Пока')
STORY = [
    ('barinov', 'Один ты остался у меня, милый Аркашка.', 'You are all I have left, dear Arkasha.', [(213, 'Один ты у меня остался, Аркашка')], ''),
    ('lyova', 'Шеф, почему вы сидите здесь в темноте?', 'Chef, why are you sitting here in the dark?', [(213, 'Аркашка')], ''),
    ('barinov', 'Моя рыбка — единственный верный организм на свете.', 'My fish is the only loyal organism in the world.', [(214, 'Единственный преданный мне живой')], ''),
    ('lyova', 'Но вся наша кухня очень скучает без вас!', 'But our entire kitchen misses you very much!', [(212, 'предатели')], ''),
    ('barinov', 'Все повара на кухне — настоящие предатели.', 'All the cooks in the kitchen are true traitors.', [(212, 'предатели')], ''),
    ('lyova', 'Они просто испугались нового строгого порядка.', 'They just got scared of the new strict order.', [(216, 'Бузеров')], ''),
    ('barinov', 'Они с удовольствием бросили своего старого шефа.', 'They gladly abandoned their old chef.', [(214, 'преданный мне')], ''),
    ('lyova', 'Мы все искренне любим только вас, шеф.', 'We all sincerely love only you, chef.', [(214, 'живой человек')], ''),
    ('barinov', 'Только Аркашка слушает меня внимательно и молчит.', 'Only Arkasha listens to me attentively and keeps quiet.', [(215, 'организм')], ''),
    ('lyova', 'Пойдёмте на кухню, пока суп не остыл.', "Let's go to the kitchen before the soup gets cold.", [(216, 'Бузеров')], ''),
    ('barinov', 'Я никуда не пойду из этого кабинета.', 'I will not go anywhere out of this office.', [(213, 'Один ты у меня остался')], ''),
    ('lyova', 'Тогда я принесу вам горячего чаю сюда.', 'Then I will bring you some hot tea here.', [(213, 'Аркашка')], ''),
]
WALK = [
    (0, None, ["'You are all I have left, dear Arkasha.' In this sad sentence, the word ", ('barinov', 'Один'), ' simply means alone or one.']),
    (1, None, ["'Chef, why are you sitting here in the dark?' When asking about the lack of light, he uses ", ('lyova', 'темноте'), ' for the dark.']),
    (2, None, ["'My fish is the only loyal organism in the world.' To highlight his isolation, he calls the fish the ", ('barinov', 'единственный'), ' or only friend.']),
    (3, None, ["'But our entire kitchen misses you very much!' The expression for missing someone heavily relies on ", ('lyova', 'скучает'), ' which describes feeling bored without them.']),
    (4, None, ["'All the cooks in the kitchen are true traitors.' He feels deeply hurt and labels his team as ", ('barinov', 'предатели'), ' meaning traitors.']),
    (5, None, ["'They just got scared of the new strict order.' Trying to defend the team, the cook explains they ", ('lyova', 'испугались'), ' or got scared.']),
    (6, None, ["'They gladly abandoned their old chef.' Adding bitterness, the head cook claims they left with ", ('barinov', 'удовольствием'), ' indicating pleasure.']),
    (7, None, ["'We all sincerely love only you, chef.' Speaking from the heart, the loyal cook says they ", ('lyova', 'искренне'), ' or sincerely care.']),
    (8, None, ["'Only Arkasha listens to me attentively and keeps quiet.' Praising the fish, he points out it listens very ", ('barinov', 'внимательно'), ' meaning attentively.']),
    (9, None, ["'Let's go to the kitchen before the soup gets cold.' Urging his boss to move, he worries the food has ", ('lyova', 'остыл'), ' or cooled down.']),
    (10, None, ["'I will not go anywhere out of this office.' Refusing to leave the room, the boss firmly says ", ('barinov', 'никуда'), ' for nowhere.']),
    (11, None, ["'Then I will bring you some hot tea here.' Offering comfort instead of leaving, the cook suggests ", ('lyova', 'горячего'), ' for something hot.']),
]
