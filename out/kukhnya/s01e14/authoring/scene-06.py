# Authoring module for kukhnya-s01e14-scene-06.
ID = 'kukhnya-s01e14-scene-06'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 14
SCENE = 6
TITLE = "Нервы су-шефа  (The Sous-Chef's Nerves)"
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'lyova': 'Лёва', 'senya': 'Сеня'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.14'
SOURCE_FILE = 'sources/kukhnya/s01/e14.ru.dual.srt'
INTRO = "With the chef in no state to work, the sous-chef Lyova is told he's in charge. He is terrified, and his friend Senya tries to build up his courage. Hear it in Russian first."
OPENER = 'Slowly, and watch Lyova find his voice.'
TRANSITION = 'Now the pep talk from the top.'
OUTRO = "Lyova is ready, or at least he is ready to try. Notice how 'I can't' turns into 'I can' by the end of the pep talk. Speak soon."
CLOSING = ('senya', 'Пока!')
STORY = [
    ('lyova', 'Я не смогу управлять всей кухней!', 'I cannot manage the whole kitchen!', [(65, 'Я не смогу.')], ''),
    ('senya', 'У тебя обязательно всё отлично получится!', 'You will definitely do absolutely great!', [(68, 'У тебя все получится.')], ''),
    ('lyova', 'Я никогда раньше не заменял шефа.', 'I have never replaced the chef before.', [], ''),
    ('senya', 'Ведь ты наш су-шеф, то есть супер-шеф!', 'Because you are our sous-chef, that is super-chef!', [(69, 'Ведь ты же су-шеф, а это значит супер-шеф.')], ''),
    ('lyova', 'Но шеф всегда так сильно кричит.', 'But the chef always shouts so loudly.', [], ''),
    ('senya', 'А ты просто кричи на всех громче.', 'And you simply shout at everyone louder.', [], ''),
    ('lyova', 'Я совсем не умею страшно кричать.', 'I completely do not know how to shout terribly.', [], ''),
    ('senya', 'Давай, попробуй громко накричать на меня.', 'Come on, try to shout loudly at me.', [], ''),
    ('lyova', 'Сеня, немедленно иди резать эти овощи!', 'Senya, go cut these vegetables immediately!', [], ''),
    ('senya', 'Очень слабо, Лёва, нужно больше злости!', 'Very weak, Lyova, we need more anger!', [], ''),
    ('lyova', 'Хорошо, сейчас я соберусь с силами.', 'All right, now I will gather my strength.', [], ''),
    ('senya', 'Ты наш самый лучший главный повар сегодня!', 'You are our absolute best head chef today!', [], ''),
    ('lyova', 'Да, я смогу, я точно смогу!', 'Yes, I can do it, I definitely can!', [(70, 'Да, я смогу.'), (71, 'Я точно смогу.')], ''),
    ('senya', 'Вот теперь я вижу настоящего шефа!', 'Now I see a real chef!', [], ''),
]
WALK = [
    (0, None, ["'I cannot manage the whole kitchen!' Let's inspect the words: ", ('lyova', 'управлять'), " takes the 'with' form, so 'the whole kitchen' becomes ", ('lyova', 'всей'), ('lyova', 'кухней'), ", ending in 'ey'. ", ('lyova', 'не'), ('lyova', 'смогу'), ' is a future, meaning I will not be able to.']),
    (1, None, ["'You will definitely do absolutely great!' Now let's analyze this part: ", ('senya', 'обязательно'), " is the adverb from obligatory, and in speech it is a firm 'definitely'. ", ('senya', 'получится'), " is 'it will work out', so 'you will manage'."]),
    (2, None, ["'I have never replaced the chef before.' In Russian, the negatives ", ('lyova', 'никогда'), ' and ', ('lyova', 'не'), ' are both kept. ', ('lyova', 'заменял'), " is the man's past form, since it is Lyova."]),
    (3, None, ["'Because you are our sous-chef, that is super-chef!' We can focus on this line: ", ('senya', 'Ведь'), " is 'after all', used for reminding someone of the obvious. ", ('senya', 'то'), ('senya', 'есть'), " means 'that is', and Russians use it just like English 'i.e.'."]),
    (4, None, ["'But the chef always shouts so loudly.' Russian says 'shouts so strongly', ", ('lyova', 'так'), ('lyova', 'сильно'), ('lyova', 'кричит'), '; ', ('lyova', 'сильно'), ' is the all-purpose intensifier for noise and pain alike.']),
    (5, None, ["'And you simply shout at everyone louder.' Now let's analyze this part: ", ('senya', 'громко'), ' is loud, and ', ('senya', 'громче'), ' is louder; its opposite works the same way. You shout ', ('senya', 'на'), ('senya', 'всех'), ', onto everyone.']),
    (6, None, ["'I completely do not know how to shout terribly.' We can focus on this part: ", ('lyova', 'не'), ('lyova', 'умею'), " is 'I do not know how', about a skill, not about being allowed. ", ('lyova', 'страшно'), " is from fear, so 'frighteningly'."]),
    (7, None, ["'Come on, try to shout loudly at me.' Now we can look at the words: ", ('senya', 'Давай'), ", meaning 'give', is the everyday 'come on'. ", ('senya', 'накричать'), ('senya', 'на'), ('senya', 'меня'), ' has ', ('senya', 'на'), " twice: once as the prefix, for one complete telling-off, and once as 'at'."]),
    (8, None, ["'Senya, go cut these vegetables immediately!' We can analyze the speech: ", ('lyova', 'иди'), ('lyova', 'резать'), " is 'go cut', two verbs side by side, the second in its basic form. ", ('lyova', 'эти'), ('lyova', 'овощи'), " is 'these vegetables', plural all the way."]),
    (9, None, ["'Very weak, Lyova, we need more anger!' Let's examine the speech: ", ('senya', 'слабо'), " alone is a verdict, 'weak!'. After ", ('senya', 'больше'), ", more, the noun takes its 'of' form, so anger becomes ", ('senya', 'злости'), '.']),
    (10, None, ["'All right, now I will gather my strength.' We will inspect the words: ", ('lyova', 'соберусь'), ('lyova', 'с'), ('lyova', 'силами'), " reads 'I will gather myself with strengths', the set phrase for pulling yourself together. The final 's' on ", ('lyova', 'соберусь'), " is the 'myself'."]),
    (11, None, ["'You are our absolute best head chef today!' We will examine the phrase: ", ('senya', 'самый'), ('senya', 'лучший'), " is 'the very best', with ", ('senya', 'самый'), ' doubling up on an already top word. ', ('senya', 'главный'), ('senya', 'повар'), " word-for-word means 'main cook'."]),
    (12, None, ["'Yes, I can do it, I definitely can!' Let us examine the sentence: ", ('lyova', 'смогу'), ' keeps that same verb from his first line, now without the negative. ', ('lyova', 'точно'), " means 'exactly', and here 'for sure'."]),
    (13, None, ["'Now I see a real chef!' Now let's examine the phrase: ", ('senya', 'вижу'), " is 'I see'. The chef is the one being seen, so 'real chef' becomes ", ('senya', 'настоящего'), ('senya', 'шефа'), ", with 'ego' and 'a' endings for a man."]),
]
