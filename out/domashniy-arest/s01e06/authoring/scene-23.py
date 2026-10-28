# Authoring module for domashniy-arest-s01e06-scene-23.
ID = 'domashniy-arest-s01e06-scene-23'
SHOW = 'domashniy-arest'
SEASON = 1
EPISODE = 6
SCENE = 23
TITLE = 'Спортивная злость  (Competitive Anger)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'galina': 'Галина', 'ilona': 'Илона', 'nina': 'Нина'}
SOURCE_NAME = 'Домашний арест (Domashniy Arest) S1.06'
SOURCE_FILE = 'sources/domashniy-arest/s01/e06.ru.dual.srt'
INTRO = "Backstage at the ballet studio. Now, while Ilona is waiting backstage at the ballet audition, Nina phones her in a panic because Samson ran off to look for Yulya. Let's listen in Russian first."
OPENER = "Let's go through the scene line by line. Backstage at the ballet hall, Ilona answers a frantic phone call from Nina."
TRANSITION = "Now let's hear the whole scene again, from start to finish."
OUTRO = "So before hurrying off to help Nina find Yulya, Ilona used reverse psychology to turn Galina's stage fright into pure competitive anger right before her audition. See you next time!"
CLOSING = ('ilona', 'Пока!')
STORY = [
    ('nina', 'Не найдёт он никого! Что мне делать?', "He won't find anyone! What should I do?", [(843, 'не найдет он никого'), (845, 'мне делать')], "'он же бестолковый' dropped; 'Да ничего мне делать, а?' -> 'Что мне делать?'"),
    ('ilona', 'Не волнуйся. Можно по телефону узнать, где она.', "Don't worry. We can find out by phone where she is.", [(844, 'Не волнуйся')], "'по социальным сетям пробить геолокацию' (848) -> 'Можно по телефону узнать, где она' (A1)"),
    ('nina', 'Да я в этом ничего не понимаю!', "I don't understand anything about that!", [(849, 'Да я в этом'), (849, 'ничего не')], "'соображаю' -> 'понимаю' (A1)"),
    ('ilona', 'Я сейчас приеду.', "I'll come right over.", [(850, 'Я сейчас приеду')], ''),
    ('galina', 'Я же десять раз сказала! Я видеть его не хочу.', "I've said it ten times! I don't want to see him.", [(851, 'Я же десять раз сказала, я видеть его не хочу')], 'split into two short sentences'),
    ('ilona', 'Когда-нибудь ты захочешь помириться со своим папой.', 'Someday you will want to make up with your dad.', [(854, 'Когда-нибудь ты захочешь помириться со своим папой')], ''),
    ('ilona', 'Но будет уже слишком поздно!', 'But it will already be too late!', [(855, 'но будет уже слишком поздно')], ''),
    ('galina', 'Я сто раз хотела с ним помириться!', 'I wanted to make up with him a hundred times!', [(857, 'Я сто раз'), (857, 'с ним помириться')], "'пыталась' -> 'хотела' (A1)"),
    ('galina', 'Он сразу начинает кричать! Оставьте меня в покое.', 'He immediately starts shouting! Leave me in peace.', [(858, 'Он'), (858, 'сразу начинает'), (859, 'оставьте меня в покое')], "'орать' -> 'кричать' (A1)"),
    ('ilona', 'Хорошо. А знаешь, почему ты так злишься?', 'Fine. And do you know why you are so angry?', [(862, 'А знаешь'), (864, 'ты так злишься')], ''),
    ('ilona', 'Потому что твой папа прав! У тебя нет таланта.', 'Because your dad is right! You have no talent.', [(864, 'потому что твой папа прав')], "'Ну ты реально бездарная' (866) -> 'У тебя нет таланта' (A1)"),
    ('ilona', 'Видела я твой танец. Балерина из тебя никакая!', 'I saw your dance. You are no ballerina at all!', [(867, 'Видела я'), (868, 'из тебя'), (868, 'какая')], "'тренировку' -> 'танец'; garbled 'Валерина из тебя извинения какая' -> 'Балерина из тебя никакая!'"),
    ('ilona', 'Тебя даже в простой театр никто не возьмёт!', 'Nobody will even take you into a simple theatre!', [(870, 'тебя даже'), (871, 'никто не возьмет')], "'под танцовку' -> 'в простой театр' (A1)"),
    ('galina', 'Что?! Да я сейчас всем покажу!', 'What?! Why, I will show everyone right now!', [(863, 'Что')], "Galina's furious reaction as she is called onto the stage in cues 872-874"),
]
WALK = [
    (0, None, "'He won't find anyone! What should I do?' Russian uses double negation here: 'not he will find nobody', and 'what to me to do?' uses the 'to'-form."),
    (1, None, "'Don't worry. We can find out by phone where she is.' Ilona calmly explains that she can check Yulya's location through her phone."),
    (2, None, "'I don't understand anything about that!' Literally, 'in this I nothing not understand' — Russian says you understand 'in' a subject."),
    (3, None, "'I'll come right over.' Hanging up, Ilona turns back to Ignatyev's twenty-year-old daughter Galina, who is waiting nervously in her ballet costume before her big audition."),
    (4, None, "'I've said it ten times! I don't want to see him.' After 'ten', the word for 'times' has a zero ending in the plural 'of' form, equal to the subject-form singular."),
    (5, None, "'Someday you will want to make up with your dad.' The prefix '-nibud' on 'when' means 'someday, at some point', and 'with your own dad' uses the 'with/as' form."),
    (6, None, "'But it will already be too late!' Ilona tries a gentle, sympathetic tone first, thinking of her own past."),
    (7, None, "'I wanted to make up with him a hundred times!' Because Galina is speaking, the past form 'wanted' ends in feminine '-a'."),
    (8, None, "'He immediately starts shouting! Leave me in peace.' Remembering what the ballet teacher said about Galina freezing up with stage fright unless she gets angry, Ilona suddenly changes tactics."),
    (9, None, "'Fine. And do you know why you are so angry?' The '-sya' form at the end means 'you get angry'."),
    (10, 'Потому что твой папа прав!', "'Because your dad is right!' The short masculine describing word 'right' has no ending."),
    (10, 'У тебя нет таланта.', "'You have no talent.' With negative 'there is no', the word 'talent' stands in the 'of' form singular."),
    (11, None, "'I saw your dance. You are no ballerina at all!' Literally, 'a ballerina out of you is none whatsoever', a classic colloquial way to say someone is no good at a profession."),
    (12, None, "'Nobody will even take you into a simple theatre!' Ilona smirks and walks away just as the announcer calls Galina's name for the audition."),
    (13, None, "'What?! Why, I will show everyone right now!' Forgetting all about her stage fright, furious Galina marches out onto the stage to prove Ilona wrong."),
]
