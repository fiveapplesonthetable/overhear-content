# Authoring module for kukhnya-s01e05-scene-11.
ID = 'kukhnya-s01e05-scene-11'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 5
SCENE = 11
TITLE = 'План мести  (A Plan of Revenge)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'nastya': 'Настя', 'sasha': 'Саша'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.05'
SOURCE_FILE = 'sources/kukhnya/s01/e05.ru.dual.srt'
INTRO = "In the Claude Monet staff room, Nastya is still in tears over Max, and Sasha, her fellow waitress, has decided crying won't fix anything. She has a plan, and it involves Kostya, the bartender and Max's best friend. Just listen to how it sounds in Russian first."
OPENER = 'Slowly now. Sasha sounds like a general, and Nastya sounds unconvinced.'
TRANSITION = 'Back to the full version.'
OUTRO = 'Saying \'it will get lighter for me\' is the Russian way to say you\'ll feel better. It works just as well for a headache or a bad day as for a broken heart.'
CLOSING = ('nastya', 'Пока!')
STORY = [
    ('nastya', 'Макс поступил со мной очень плохо.', 'Max treated me very badly.', [], ""),
    ('sasha', 'Хватит плакать, Настя, вытри слёзы.', 'Stop crying, Nastya, wipe your tears.', [], ""),
    ('sasha', 'Тебе нужно просто ему отомстить.', 'You just need to get back at him.', [(145, 'Тебе нужно просто ему отомстить')], ""),
    ('nastya', 'Мне станет легче, если отомстить?', 'Will I feel better if I get revenge?', [(146, 'Будет легче')], ""),
    ('sasha', 'Конечно, тебе сразу станет легче.', 'Of course, you will immediately feel better.', [], ""),
    ('nastya', 'Но как я могу наказать его?', 'But how can I punish him?', [(150, 'наказание')], ""),
    ('sasha', 'Начни встречаться с его лучшим другом.', 'Start going out with his best friend.', [(151, 'с его другом')], ""),
    ('nastya', 'С его другом? С барменом Костей?', 'With his friend? With bartender Kostya?', [(152, 'С Костей?')], ""),
    ('sasha', 'Да, именно с Костей!', 'Yes, exactly with Kostya!', [(153, 'Да, с Костей')], ""),
    ('sasha', 'Так Максу будет ещё больнее.', 'That way Max will hurt even more.', [(153, 'Так ему будет еще хуже')], ""),
    ('nastya', 'Думаешь, это действительно хорошая идея?', "Do you think that's really a good idea?", [], ""),
    ('sasha', 'Поверь мне, это самый лучший вариант.', 'Trust me, this is the very best option.', [(157, 'И поверь, это лучший вариант')], ""),
    ('sasha', 'Действуй прямо сейчас, не теряй времени.', 'Act right now, do not lose time.', [(157, 'Действуй давай')], ""),
]
WALK = [
    (0, None, ['\'Max treated me very badly.\' You heard this exact line when Nastya told Vika. ', ('nastya', 'очень'), ('nastya', 'плохо'), ", meaning 'very badly', is the easy part; ", ('nastya', 'поступил'), ('nastya', 'со'), ('nastya', 'мной'), " translates to 'acted with me'."]),
    (1, None, ['\'Stop crying, Nastya, wipe your tears.\' , signifying \'enough\', is followed straight ', ('sasha', 'Хватит'), " away by ", ('sasha', 'плакать'), ", 'to cry'. ", ('sasha', 'вытри'), ", which is used for 'wipe', is a command to one person."]),
    (2, None, ['\'You just need to get back at him.\' The phrase for \'you need to\' is constructed from ', ('sasha', 'Тебе'), ('sasha', 'нужно'), ", meaning 'to you it's needed'. The verb ", ('sasha', 'отомстить'), " expresses taking revenge, and the target goes into the 'to' form: ", ('sasha', 'ему'), "."]),
    (3, None, ['\'Will I feel better if I get revenge?\' Literally \'to me will become lighter\'. The word ', ('nastya', 'легче'), " acts as the comparative of 'light' or 'easy'."]),
    (4, None, ['\'Of course, you will immediately feel better.\' Sasha repeats the shape back with ', ('sasha', 'тебе'), " in place of 'to me'. ", ('sasha', 'сразу'), " stands for 'at once', and you'll hear it constantly."]),
    (5, None, ['\'But how can I punish him?\' The word ', ('nastya', 'могу'), ", indicating 'I can', is one you'll need every day. ", ('nastya', 'наказать'), " corresponds to 'to punish'."]),
    (6, None, ['\'Start going out with his best friend.\' The phrase ', ('sasha', 'встречаться'), ('sasha', 'с'), ", meaning 'to date', is the verb Max used earlier. After ", ('sasha', 'с'), ", the words change to ", ('sasha', 'с'), ('sasha', 'его'), ('sasha', 'лучшим'), ('sasha', 'другом'), ", but ", ('sasha', 'его'), ", meaning 'his', never changes."]),
    (7, None, ['\'With his friend? With bartender Kostya?\' Nastya repeats it in disbelief. Notice how the endings change to ', ('nastya', 'барменом'), ' and ', ('nastya', 'Костей'), ' after the word ', ('nastya', 'С'), '.']),
    (8, None, ['\'Yes, exactly with Kostya!\' The word ', ('sasha', 'именно'), ", acting as 'exactly', points straight at the word after it. Sasha won't let her wriggle out of it."]),
    (9, None, ['\'That way Max will hurt even more.\' The construction ', ('sasha', 'Максу'), ('sasha', 'будет'), ('sasha', 'больнее'), " is used for 'to Max it will be more painful'. Adding ", ('sasha', 'ещё'), " before a comparative word like this adds the meaning 'even'."]),
    (10, None, ['\'Do you think that\'s really a good idea?\' The term ', ('nastya', 'действительно'), " is used for 'really' in the sense of 'actually, in fact'. Starting with ", ('nastya', 'Думаешь'), " on its own creates a doubtful 'you think?' feeling."]),
    (11, None, ['\'Trust me, this is the very best option.\' The phrase ', ('sasha', 'Поверь'), ('sasha', 'мне'), " equates to 'believe to me', with ", ('sasha', 'мне'), " in the 'to' form. The noun ", ('sasha', 'вариант'), " looks like 'variant' but serves as 'option'."]),
    (12, None, ['\'Act right now, do not lose time.\' The combination ', ('sasha', 'не'), ('sasha', 'теряй'), ", representing 'don't lose', is ", ('sasha', 'не'), " plus a command. After it, the word for time takes the form ", ('sasha', 'времени'), ", as it did in Nastya's 'love knows no time'."]),
]
