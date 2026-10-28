# Authoring module for kukhnya-s01e05-scene-01.
ID = 'kukhnya-s01e05-scene-01'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 5
SCENE = 1
TITLE = 'Ссора из-за поцелуя  (A Quarrel Over a Kiss)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'kostya': 'Костя', 'max': 'Макс'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.05'
SOURCE_FILE = 'sources/kukhnya/s01/e05.ru.dual.srt'
INTRO = "Morning at Claude Monet begins with high drama behind the bar. Bartender Kostya confronts Max in a fury after finding out Max kissed waitress Nastya during yesterday's shift. Max frantically tries to convince his best friend that the kiss was a sleep-deprived accident and that he has no feelings for Nastya. Let's listen to their argument in Russian first."
OPENER = "Now let's examine Max and Kostya's argument line by line."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = 'That wraps up this scene from Kukhnya. Listen for these everyday Russian expressions when you watch the episode. See you next time!'
CLOSING = ('kostya', 'Пока!')
STORY = [
    ('max', 'Костя, привет. Почему ты сердишься?', 'Kostya, hi. Why are you angry?', [], ''),
    ('kostya', 'Отвали, или я сломаю тебе нос!', 'Back off, or I will break your nose!', [(6, 'Отвали, или я тебе нос сломаю')], ''),
    ('max', 'За что? Что я тебе сделал?', 'What for? What did I do to you?', [(7, 'За что')], ''),
    ('kostya', 'Ты вчера целовался с моей девушкой!', 'Yesterday you kissed my girl!', [(7, 'ты целовался с моей девушкой')], ''),
    ('max', 'Это было совершенно случайное недоразумение.', 'It was a completely accidental misunderstanding.', [(11, 'это вообще недоразумение было')], ''),
    ('kostya', 'Вы целовались прямо в ресторане!', 'You were kissing right in the restaurant!', [], ''),
    ('max', 'Я вчера весь день хотел спать.', 'I wanted to sleep all day yesterday.', [(12, 'Я вчера весь день'), (12, 'спать хотел')], ''),
    ('max', 'Кстати, технически она пока не твоя.', 'By the way, technically she is not yours yet.', [(13, 'Кстати, технически она пока не твоя')], ''),
    ('kostya', 'Для меня это не имеет значения.', 'For me that does not matter.', [], ''),
    ('max', 'Между мной и Настей ничего нет!', 'There is nothing between me and Nastya!', [(15, 'между нами ничего нет')], ''),
    ('kostya', 'Ты предал нашу дружбу, Макс.', 'You betrayed our friendship, Max.', [], ''),
    ('max', 'Я докажу, что она мне безразлична.', 'I will prove that she means nothing to me.', [], ''),
    ('kostya', 'Посмотрим, как ты это докажешь.', 'We will see how you prove it.', [], ''),
]
WALK = [
    (0, None, "'Kostya, hi. Why are you angry?' Max tries to greet his tense friend."),
    (1, None, "'Back off, or I will break your nose!' Kostya aggressively warns his friend to back off."),
    (2, None, "'What for? What did I do to you?' Max questions the sudden hostility, genuinely confused about what he did wrong."),
    (3, None, "'Yesterday you kissed my girl!' Kostya cuts to the chase, furious about the perceived betrayal."),
    (4, None, "'It was a completely accidental misunderstanding.' Max frantically tries to downplay the situation as a total misunderstanding."),
    (5, None, "'You were kissing right in the restaurant!' Kostya emphasizes the public location of their encounter."),
    (6, None, "'I wanted to sleep all day yesterday.' Max offers a weak excuse about being sleep-deprived."),
    (7, None, "'By the way, technically she is not yours yet.' Max makes a technical point that they are not officially a couple yet."),
    (8, None, "'For me that does not matter.' Kostya dismisses the technicality completely."),
    (9, None, "'There is nothing between me and Nastya!' Max insists that his relationship with the waitress is strictly professional."),
    (10, None, "'You betrayed our friendship, Max.' Kostya expresses deep hurt over his friend's actions."),
    (11, None, "'I will prove that she means nothing to me.' Max promises to show how little he cares about her."),
    (12, None, "'We will see how you prove it.' Kostya remains deeply skeptical of this promise."),
]
