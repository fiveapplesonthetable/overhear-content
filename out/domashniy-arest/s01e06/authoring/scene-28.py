# Authoring module for domashniy-arest-s01e06-scene-28.
ID = 'domashniy-arest-s01e06-scene-28'
SHOW = 'domashniy-arest'
SEASON = 1
EPISODE = 6
SCENE = 28
TITLE = 'По крайней мере, он дочь свою любит  (At Least He Loves His Daughter)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'galina': 'Галина', 'ignatyev': 'Игнатьев', 'ilona': 'Илона'}
SOURCE_NAME = 'Домашний арест (Domashniy Arest) S1.06'
SOURCE_FILE = 'sources/domashniy-arest/s01/e06.ru.dual.srt'
INTRO = "In Ignatyev's office at the meatpacking plant. Meanwhile, having passed the Moscow ballet audition thanks to Ilona's clever provocation, Galina comes to her father's office to make peace and ask him a favour. Let's listen in Russian first."
OPENER = "Let's take the scene line by line. Ignatyev hugs his daughter Galina proudly."
TRANSITION = "Now let's hear the whole scene once more, start to finish."
OUTRO = "So Ilona's backstage psychology pays off twice: Galina wins her place in the Moscow ballet troupe, and Ignatyev agrees to fund Samson's mayoral campaign because Samson fought for his daughter. See you then. See you next time!"
CLOSING = ('ignatyev', 'Пока!')
STORY = [
    ('ignatyev', 'Дочка, а ты вся в меня!', 'Daughter, you take after me completely!', [(1036, 'А ты вся в меня')], ''),
    ('ignatyev', 'Я имею в виду, ты такая же упёртая.', "I mean, you're just as stubborn.", [(1037, 'Я имею в виду, такая же упёртая')], ''),
    ('galina', 'Папа, это всё Илона! Это ей спасибо.', 'Dad, that was all Ilona! Thank her for that.', [(1038, 'Это ей спасибо')], ''),
    ('galina', 'Если бы не она, я бы опять испугалась.', 'If not for her, I would have got scared again.', [(1038, 'Если б не она, я бы')], "'как обычно' -> 'опять испугалась'"),
    ('galina', 'Ты поможешь ей, папа?', 'Will you help her, Dad?', [(1039, 'Поможешь ей')], ''),
    ('ignatyev', 'Ну ладно. Может, Самсонов тоже вором станет.', 'Well, alright. Maybe Samsonov will become a thief too.', [(1040, 'Ну ладно. Может'), (1040, 'тоже'), (1040, 'станет')], "'он... ворюгой' -> 'Самсонов... вором'"),
    ('ignatyev', 'Но, по крайней мере, он дочь свою любит!', 'But at least he loves his daughter!', [(1041, 'по крайней мере, он дочь свою любит')], ''),
    ('ilona', 'Спасибо, Вениамин Игоревич! Вы не пожалеете.', "Thank you, Veniamin Igorevich! You won't regret it.", [], "new: Ilona's response as Ignatyev agrees"),
    ('ignatyev', 'Галя, если бы ты моё дело продолжила!', 'Galya, if only you had continued my business!', [(1042, 'ты мое дело продолжила')], ''),
    ('ignatyev', 'Мы бы с тобой горы свернули! А ты — балет!', 'You and I would have moved mountains! And you chose ballet!', [(1042, 'мы бы с тобой горы свернули'), (1043, 'А ты балет')], ''),
    ('galina', 'Папа, ну не начинай опять!', "Dad, come on, don't start again!", [(1044, 'не начинай')], "'Пап' -> 'Папа'"),
    ('ilona', 'Так, Игнатьев, давайте вы мне сначала деньги переведёте.', 'Right, Ignatyev, first transfer the money to me.', [(1045, 'Так'), (1045, 'давайте вы мне сначала деньги переведете')], "garbled 'Агнатила' -> 'Игнатьев'"),
    ('ilona', 'А потом вы выясняйте отношения!', 'And then sort out your relationship!', [(1046, 'потом'), (1046, 'отношения')], "garbled 'объясняйте' -> 'выясняйте'"),
]
WALK = [
    (0, None, "'Daughter, you take after me completely!' Literally, 'you are all into me' — the same Russian idiom for taking after a parent that we just heard in Marina's room."),
    (1, None, "'I mean, you're just as stubborn.' The three-word phrase at the start literally means 'I have in view', the standard Russian way to say 'I mean'."),
    (2, None, "'Dad, that was all Ilona! Thank her for that.' Notice the 'to me/you' pronoun 'to her' before 'thank you'."),
    (3, None, "'If not for her, I would have got scared again.' By making Galina furious right before she went on stage, Ilona made her forget her stage fright and dance brilliantly. Then Galina asks her father directly."),
    (4, None, "'Will you help her, Dad?' In this moment, Ignatyev still has a bruised face from Samson's punch earlier today, when Samson thought Ignatyev was preying on Yulia. Yet that punch actually impressed him."),
    (5, None, "'Well, alright. Maybe Samsonov will become a thief too.' After 'will become', 'thief' takes the 'with/as' form."),
    (6, None, "'But at least he loves his daughter!' The three-word expression at the start means 'at least', literally 'by the extreme measure'. Ignatyev respects a father who fights for his child."),
    (7, None, "'Thank you, Veniamin Igorevich! You won't regret it.' Then Ignatyev can't resist grumbling to Galina about his beloved meatpacking plant."),
    (8, None, "'Galya, if only you had continued my business!' He still dreams of handing his sausage empire to his daughter."),
    (9, 'Мы бы с тобой горы свернули!', "'You and I would have moved mountains! And you chose ballet!' Literally, 'we would have rolled mountains over'."),
    (10, None, "'Dad, come on, don't start again!' Before father and daughter can quarrel all over again, Ilona steps in."),
    (11, None, "'Right, Ignatyev, first transfer the money to me.' Business first, family arguments second!"),
    (12, None, "'And then sort out your relationship!' Literally, 'clarify relations' — the everyday Russian phrase for hashing out a personal argument."),
]
