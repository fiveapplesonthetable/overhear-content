# Authoring module for kukhnya-s01e16-scene-08.
ID = 'kukhnya-s01e16-scene-08'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 16
SCENE = 8
TITLE = 'Чей паштет лучше  (Whose Pâté is Better)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'kostya': 'Костя', 'max': 'Макс'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.16'
SOURCE_FILE = 'sources/kukhnya/s01/e16.ru.dual.srt'
INTRO = "Over in the bar, Kostya has gossip: the inspectors have turned up next door. Max doesn't care. All he can think about is his bet with the chef, so he makes his friend say, honestly, whose pâté is better. Listen to it in Russian first."
OPENER = "We'll go through it again, this time with the meaning."
TRANSITION = "Let's hear the whole thing again, start to finish."
OUTRO = "Kostya gives the honest answer and Max takes it on the chin. Notice that Kostya sends him off with a wish for luck: it's a good phrase to keep for yourself. See you next time!"
CLOSING = ('kostya', 'Пока!')
STORY = [
    ('kostya', 'Макс, ты слышал важные новости сегодня?', 'Max, did you hear important news today?', [(58, 'А ты слышал про проверку ФМС в другом ресторане?')], ''),
    ('max', 'Какие ещё новости могут волновать меня?', 'What other news could worry me?', [], ''),
    ('kostya', 'В соседнем ресторане сейчас идёт большая проверка.', 'A huge inspection is going on in the neighboring restaurant right now.', [(58, 'в другом ресторане?')], ''),
    ('max', 'Мне сейчас совсем не до чужих проверок.', 'Right now I do not care at all about outside inspections.', [], ''),
    ('kostya', 'Там проверяют всех поваров.', 'They are checking all the cooks over there.', [], ''),
    ('max', 'Ответь честно, чей паштет сейчас лучше?', 'Answer honestly, whose pâté is better right now?', [(59, 'Чей паштет лучше, мой или шефа?')], ''),
    ('kostya', 'Ты обещаешь не обижаться на меня?', 'Do you promise not to be offended with me?', [], ''),
    ('max', 'Я хочу услышать только чистую правду.', 'I want to hear only the pure truth.', [], ''),
    ('kostya', 'И ты точно не скажешь шефу?', 'And you definitely will not tell the chef?', [(60, 'А ты шефу не скажешь?')], ''),
    ('max', 'Нет, я просто хочу знать результат.', 'No, I simply want to know the result.', [(60, 'Нет.')], ''),
    ('kostya', 'У шефа этот паштет намного лучше.', 'The chef makes this pâté much better.', [(61, 'У шефа лучше.')], ''),
    ('max', 'Я обязательно найду его секретный ингредиент!', 'I will definitely find his secret ingredient!', [], ''),
    ('kostya', 'Желаю тебе большой удачи в этом!', 'I wish you great luck in that!', [], ''),
]
WALK = [
    (0, None, "'Max, did you hear important news today?' 'News' is always plural in Russian, so 'important' is plural too. The 'l' on 'did you hear' marks Kostya as the one asking a man."),
    (1, None, "'What other news could worry me?' The first words are 'what else', and the Russian for 'can' is in the plural to go with 'news'. Max sounds distracted and a little annoyed."),
    (2, None, "'A big inspection is going on in the neighboring restaurant right now.' Russian says the inspection 'goes' where English says 'is going on'. 'In the neighboring restaurant' has an 'e' ending on both words."),
    (3, None, "'Right now I don't care about someone else's inspections.' The little group 'to me, not up to' means 'I'm not in the mood for'. Russian's 'someone else's' comes from the Russian for 'foreign'."),
    (4, None, "'They are checking all the cooks over there.' Nobody is named, so Russian just uses the 'they' ending on Russian's 'check'. We do the same in English when we say 'they're checking everyone'."),
    (5, None, "'Answer honestly, whose pâté is better right now?' 'Whose' has to match 'pâté', so it has the masculine form. 'Honestly' carries 'o' like the other words for 'how'."),
    (6, None, "'Do you promise not to be offended by me?' The Russian for 'be offended' ends in 'sya', the 'oneself' bit, as it is something that happens to you. Russians say 'offended on' someone."),
    (7, None, "'I want to hear only the pure truth.' Russian's 'I want' is irregular, so it's worth learning as it is. 'Pure truth' finishes with 'uyu', since the truth is the thing being asked for."),
    (8, None, "'And you definitely won't tell the chef?' The Russian for 'to the chef' has a 'u' on the end, where the chef is the one it goes to. 'Definitely' is the same word as 'exactly'."),
    (9, None, "'No, I just want to know the result.' The small word for 'just' also means 'simply', and it softens what could sound blunt. Russian's 'result' is a borrowing, easy to recognise."),
    (10, None, "'The chef's pâté is much better.' Kostya has to say it, and he does it in the plainest words he can. 'At the chef' is Russian's way of saying 'the chef's', and 'better' is the short one."),
    (11, None, "'I will definitely find his secret ingredient!' The Russian for 'definitely' means 'without fail'. 'His' is the same as Russian's 'him', pronounced 'yevo'."),
    (12, None, "'I wish you great luck in that!' The Russian for 'luck' takes an 'i' ending because 'wish' calls for the 'of' form. It's a ready-made phrase you can use for anything."),
]
