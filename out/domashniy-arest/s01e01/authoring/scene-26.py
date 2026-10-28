# domashniy-arest/s01e01/scene-26.py
ID = "domashniy-arest-s01e01-scene-26"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 1
SCENE = 26
TITLE = "Паша по телевизору  (Pasha on TV)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
SOURCE_NAME = "Домашний арест (Domashniy Arest) S1.01"
SOURCE_FILE = "sources/domashniy-arest/s01/e01.ru.dual.srt"
VOICES = {"narrator": "sky", "samson": "anja", "anya": "alisa"}
LABELS = {"samson": "Самсон", "anya": "Аркадий"}
INTRO = "That evening, in the shared kitchen of the communal flat. Last time, Arkady scrubbed the flooded bathroom, Samson took the credit, and Nina refused to say a word to her husband. Now the two men sit with a bottle of very bad vodka, and on television Pasha, Arkady's old deputy, makes a big announcement. Let's listen in Russian first."
STORY = [
    ("samson", "Я знаю наш город как никто.", "I know our town like nobody else.", [(991, 'знаю'), (991, 'как никто')], "'знаю его как никто' -> 'знаю наш город как никто'"),
    ("samson", "Поэтому я решил стать мэром.", "That's why I've decided to become mayor.", [(994, 'Поэтому я решил')], "'выдвинуть свою кандидатуру на пост главы города' -> 'стать мэром'"),
    ("samson", "Смотри, как он говорит!", "Look how he talks!", [(995, 'смотри, как')], "'гладко чешет' (slang: talks smoothly) -> 'говорит'"),
    ("anya", "Это он у меня научился.", "He learned that from me.", [(996, 'Меня научился')], "'Это он у' added (standard grammar)"),
    ("samson", "Мы построим кластер. Это тысячи рабочих мест.", "We will build the cluster. That means thousands of jobs.", [(999, 'кластер'), (1001, 'тысячи рабочих мест')], "two long lines of the speech cut down"),
    ("anya", "Паша, эти выборы ты не выиграешь.", "Pasha, you won't win this election.", [(1003, 'эти выборы')], "clean version of cue 1003 (a rude 'like hell you'll win'); 'Пашенька' -> 'Паша'"),
    ("samson", "Да ладно!", "Oh, come on!", [], "new: Samson's usual reaction (characters.md)"),
    ("anya", "Очень плохая водка.", "Very bad vodka.", [(1004, 'Очень плохая водка')], ""),
    ("samson", "Ничего, ничего.", "Never mind, never mind.", [(1005, 'Ничего, ничего')], ""),
    ("anya", "Как говорит наш губернатор, выход всегда есть.", "As our governor says, there's always a way out.", [(1006, 'Как говорит наш губернатор, выход всегда есть')], ""),
    ("samson", "Ну-ну.", "Yeah, sure.", [], "new: Samson doesn't buy it (cue 1009 'Ну ладно, ты прямо')"),
    ("samson", "Хочешь, честно скажу?", "Do you want me to tell you honestly?", [(1013, 'хочешь')], "'по чесноку' (slang) -> 'честно'"),
    ("anya", "Скажи.", "Tell me.", [], "new"),
    ("samson", "Мне всё равно. Что ты, что он.", "It's all the same to me. You or him.", [(1015, 'Что ты, что он')], "'по мне один хрен' (cue 1014, crude) -> 'Мне всё равно'"),
    ("anya", "Почему?", "Why?", [], "new"),
    ("samson", "Вы все воры.", "You're all thieves.", [(1016, 'все воры')], "'мы' -> 'вы' (he means the officials); 'уроды' dropped"),
    ("anya", "Ну, спасибо.", "Well, thanks.", [], "new: Arkady's dry answer"),
    ("samson", "И знаешь, что самое главное? Всем всё равно.", "And you know the main thing? Nobody cares.", [(1025, 'что самое главное')], "'Знаете' -> 'знаешь'; 'Никому' -> 'Всем всё равно'"),
]
OPENER = "Let's go through it bit by bit. Pasha is on the screen, smiling, and he starts with himself."
WALK = [
    (0, None, "'I know our town like nobody else.' The verb 'know' comes right after 'I', and the last two words mean 'like no one'. Then comes the news."),
    (1, None, "'That's why I've decided to become mayor.' He has just helped to put Arkady under arrest, and now he wants his job. Samson is impressed by the style."),
    (2, None, "'Look how he talks!' The first word is a casual command, 'look'. Arkady is not impressed at all."),
    (3, None, "'He learned that from me.' The phrase in the middle, literally 'at me', is how you say who you learned something from. Pasha moves on to his big project."),
    (4, None, "'We will build the cluster. That means thousands of jobs.' The cluster is the industrial project Arkady blocked, and the reason Pasha set him up. Arkady talks back to the television."),
    (5, None, "'Pasha, you won't win this election.' The verb here has a future meaning, even though it looks like a present form. That is how completed actions work in Russian. Samson just laughs."),
    (6, None, "'Oh, come on!' Two short words for disbelief. Arkady takes a sip and makes a face."),
    (7, None, "'Very bad vodka.' Spoken like an expert. Samson is not bothered."),
    (8, None, "'Never mind, never mind.' The word literally means 'nothing', and it's how you say 'it's fine, never mind'. Arkady tries to sound hopeful."),
    (9, None, "'As our governor says, there's always a way out.' He tells Samson the governor once burned a pile of money before a police search, and stayed free. Samson is not convinced."),
    (10, None, "'Yeah, sure.' Said slowly, it means 'I don't believe a word of it'. Then he gets serious."),
    (11, None, "'Do you want me to tell you honestly?' The first word is the verb 'want', and the last one, 'I'll tell', is in the future. Arkady lets him go on."),
    (12, None, "'Tell me.' One word, a command from the same verb. And Samson is very direct."),
    (13, None, "'It's all the same to me. You or him.' The first sentence starts with 'to me': in Russian the person who feels something often comes first, in this form. The second literally says 'what you, what him'. Arkady asks why."),
    (14, None, "'Why?' And the answer is short."),
    (15, None, "'You're all thieves.' He uses the plural 'you', for all the officials together. Arkady takes it calmly."),
    (16, None, "'Well, thanks.' Not real thanks, of course. Samson finishes his thought."),
    (17, None, "'And you know the main thing? Nobody cares.' The last sentence literally says 'to everyone, it's all the same', the same phrase he used a moment ago. On that cheerful note, Arkady goes very quiet."),
]
TRANSITION = "Let's hear the whole conversation again."
OUTRO = "And that's this scene. When you watch, listen for Pasha's big promise on television, and for the moment Samson says it's all the same to him; you'll recognise them now. Until next time!"
CLOSING = ("anya", "До свидания!")
