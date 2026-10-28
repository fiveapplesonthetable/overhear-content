# Authoring module for kukhnya-s01e12-scene-07.
ID = 'kukhnya-s01e12-scene-07'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 12
SCENE = 7
TITLE = "На кухне шефа  (In the Chef's Kitchen)"
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'barinov': 'Шеф', 'senya': 'Сеня'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.12'
SOURCE_FILE = 'sources/kukhnya/s01/e12.ru.dual.srt'
INTRO = "During the busy afternoon prep shift at Claude Monet, Chef Viktor Barinov storms through the kitchen, furious about mess and delays. Catching his cooks hesitating at their stations, Barinov aggressively reprimands Senya and demands strict kitchen discipline. Let's listen to their fast-paced kitchen exchange in Russian."
OPENER = "Let's explore how Chef Barinov demands discipline and reprimands his cooks for kitchen slowdowns."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = "Now you know how to give urgent kitchen commands, address mess at workstations, and ask for quiet in Russian. Listen for these intense workplace phrases in the upcoming scene. Next time you watch the episode, listen for the Russian expressions for 'dish' and 'fast' — you will catch every word right away. See you next time!"
CLOSING = ('barinov', 'Пока!')
STORY = [
    ('barinov', 'Сеня, почему ты стоишь без дела?', 'Senya, why are you standing doing nothing?', [], ''),
    ('senya', 'Я жду нужные специи для мяса.', 'I am waiting for the needed spices for the meat.', [], ''),
    ('barinov', 'Ты ждёшь, пока гном насыпет корицу?', 'Are you waiting until a gnome sprinkles cinnamon?', [(64, 'насыпет корицу')], ''),
    ('senya', 'Шеф, я всё делаю быстро.', 'Chef, I do everything quickly.', [(65, 'Ну, шеф')], ''),
    ('barinov', 'Тогда работай быстрее и не стой.', 'Then work faster and do not stand around.', [(66, 'Сам ты')], ''),
    ('barinov', 'И всегда убирай за собой стол.', 'And always clean up your table.', [(67, 'убирай за собой')], ''),
    ('senya', 'Шеф, говорите немного тише, пожалуйста.', 'Chef, please speak a bit quieter.', [(68, 'потише бы')], ''),
    ('barinov', 'Не надо учить меня дисциплине!', 'Do not teach me discipline!', [(69, 'Учи меня еще')], ''),
    ('senya', 'Мы просто очень стараемся для вас.', 'We are simply trying very hard for you.', [], ''),
    ('barinov', 'На моей кухне должен быть идеальный порядок.', 'There must be perfect order in my kitchen.', [], ''),
    ('senya', 'Мы сейчас же всё уберём, шеф.', 'We will clean everything up right now, chef.', [], ''),
    ('barinov', 'Спокойнее, я проверю каждое блюдо лично.', 'Calm down, I will check every dish personally.', [(71, 'Покойнее')], ''),
]
WALK = [
    (0, None, "'Are you waiting until a gnome sprinkles cinnamon?' Barinov yells at a cook for being slow. He asks if a magic gnome is going to do the work."),
    (1, None, "'And always clean up your table.' Barinov reminds the cook to clean his workspace."),
    (2, None, "'Chef, please speak a bit quieter.' Senya politely asks his boss to lower his voice."),
    (3, None, "'There must be perfect order in my kitchen.' Barinov demands absolute order in his kitchen and will not quiet down."),
]
