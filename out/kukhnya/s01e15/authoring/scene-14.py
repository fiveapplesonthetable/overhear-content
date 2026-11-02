# Authoring module for kukhnya-s01e15-scene-14.
ID = 'kukhnya-s01e15-scene-14'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 15
SCENE = 14
TITLE = 'Извинения  (Apologies)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'lyova': 'Лёва'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.15'
SOURCE_FILE = 'sources/kukhnya/s01/e15.ru.dual.srt'
INTRO = 'Lyova has come home and found Barinov asleep in his bed. He starts apologising, in a long, heartfelt speech. Listen to it in Russian first.'
OPENER = 'Back through the apology, slowly.'
TRANSITION = 'Here is the apology again, whole.'
OUTRO = "Lyova has said everything he wanted to say. Barinov's answer comes in the next scene. Until then."
CLOSING = ('lyova', 'Пока!')
STORY = [
    ('barinov', 'Лёва, закрой дверь, я уже сплю.', 'Lyova, close the door, I am already sleeping.', [(318, 'Лева, закрой дверь, я сплю уже.')], ''),
    ('lyova', 'Ой, Виктор Петрович, вы дома.', 'Oh, Viktor Petrovich, you are home.', [], ''),
    ('lyova', 'Слава богу.', 'Thank god.', [], ''),
    ('lyova', 'Я так боялся, что вы уйдёте.', 'I was so afraid that you would leave.', [], ''),
    ('lyova', 'Я был очень неправ.', 'I was very wrong.', [], ''),
    ('lyova', 'Я не должен был вас выгонять.', 'I should not have kicked you out.', [], ''),
    ('lyova', 'Мы знакомы тысячи лет.', 'We have known each other for thousands of years.', [], ''),
    ('lyova', 'Всякое может случиться.', 'Anything can happen.', [], ''),
    ('lyova', 'Надо просто попросить прощения.', 'We just need to ask for forgiveness.', [], ''),
    ('lyova', 'Надо забыть эту дурацкую историю.', 'We need to forget this stupid story.', [], ''),
    ('lyova', 'Я прошу у вас прощения.', 'I ask for your forgiveness.', [], ''),
    ('lyova', 'Виктор Петрович, вы меня слышите?', 'Viktor Petrovich, do you hear me?', [], ''),
]
WALK = [
    (0, None, ["'Lyova, close the door, I am already sleeping.' Let us focus on the sentence: ", ('barinov', 'закрой'), ' is the order to close. The noun ', ('barinov', 'дверь'), ' is feminine and has no ending, so it stays the same.']),
    (1, None, ["'Oh, Viktor Petrovich, you are home.' Let us look at the dialogue: ", ('lyova', 'дома'), " means 'at home', while to say you are going homewards you would use a different form. English uses 'home' for both."]),
    (2, None, ["'Thank god.' We will consider the sentence: ", ('lyova', 'Слава'), ('lyova', 'богу'), " means 'glory to God', and it is used just as we say 'thank heavens'. It is a standard phrase."]),
    (3, None, ["'I was so afraid that you would leave.' After 'afraid that', Russian keeps the future and uses ", ('lyova', 'уйдёте'), ", meaning 'that you will leave'. English shifts it to 'would'."]),
    (4, None, ["'I was very wrong.' The term ", ('lyova', 'неправ'), " means 'wrong', built by adding a negative prefix to the word meaning 'right'. Lyova is a man, so it has no ending; a woman would add an 'a'."]),
    (5, None, ["'I should not have kicked you out.' The expression ", ('lyova', 'не'), ('lyova', 'должен'), ('lyova', 'был'), " means 'was not obliged', giving 'should not have'. The verb ", ('lyova', 'выгонять'), " means 'to drive out'."]),
    (6, None, ["'We have known each other for thousands of years.' The term ", ('lyova', 'знакомы'), " means 'acquainted'. After ", ('lyova', 'тысячи'), ", 'thousands', the noun for 'years' takes the special form ", ('lyova', 'лет'), '.']),
    (7, None, ["'Anything can happen.' Let's analyze the speech: ", ('lyova', 'Всякое'), " means 'all sorts', so 'all sorts can happen'. Notice ", ('lyova', 'может'), ('lyova', 'случиться'), " means 'can happen'."]),
    (8, None, ["'We just need to ask for forgiveness.' Let's break down the phrase: ", ('lyova', 'попросить'), ('lyova', 'прощения'), " means 'ask for forgiveness'. After 'ask for', the noun ", ('lyova', 'прощения'), ' takes a specific ending. Notice ', ('lyova', 'Надо'), ('lyova', 'просто'), " means 'we just need to'."]),
    (9, None, ["'We need to forget this stupid story.' The word ", ('lyova', 'дурацкую'), " comes from a root meaning fool, and is the everyday term for 'stupid' or 'silly'. The word ", ('lyova', 'историю'), ' means a story, but also an incident or a business.']),
    (10, None, ["'I ask for your forgiveness.' Let's focus on the words: ", ('lyova', 'прошу'), ('lyova', 'у'), ('lyova', 'вас'), ('lyova', 'прощения'), " says 'I ask of you forgiveness'. It is the full, formal way to apologise."]),
    (11, None, ["'Viktor Petrovich, do you hear me?' Now let's focus on the dialogue: ", ('lyova', 'слышите'), ' comes from the verb to hear. The verb to listen is one letter different, and easy to mix up.']),
]
