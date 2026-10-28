# Authoring module for domashniy-arest-s01e02-scene-29.
ID = 'domashniy-arest-s01e02-scene-29'
SHOW = 'domashniy-arest'
SEASON = 1
EPISODE = 2
SCENE = 29
TITLE = 'Аллергия  (The Allergy)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'arkady': 'Аркадий', 'lyosha': 'Лёша', 'marina': 'Марина'}
SOURCE_NAME = 'Домашний арест (Domashniy Arest) S1.02'
SOURCE_FILE = 'sources/domashniy-arest/s01/e02.ru.dual.srt'
INTRO = "We're still in the communal kitchen, among the stolen crab and caviar: last time, Arkady broke the lock on the old neighbour's fridge, fed the children her delicacies. Told little Lyosha that his allergy to caviar was just his mother's way of saving money. Now, sure he'll soon be free, Arkady promises the children everything. Let's listen in Russian first."
OPENER = "Let's go through it slowly. Arkady is in a generous mood, and very pleased with himself."
TRANSITION = 'Now the whole scene once more, from the start.'
OUTRO = "And that's the scene: a frightening allergy, an angry mother, and a mayor who still thinks he's about to be free. See you next time!"
CLOSING = ('marina', 'Пока!')
STORY = [
    ('arkady', 'Держитесь меня, и всё у вас будет хорошо. Потому что я кто?', 'Stick with me, and everything will be fine for you. Because who am I?', [(1052, 'и всё у вас будет хорошо'), (1053, 'Потому что я кто')], '«Вы меня, ребятки, держитесь» -> «Держитесь меня» (address word dropped, normal word order)'),
    ('lyosha', 'Взяточник!', 'A bribe-taker!', [], 'the cue is garbled («В яточник!», 1054); speaker unclear, given to Lyosha'),
    ('arkady', 'Во-первых, суда ещё не было.', "First of all, there hasn't been a trial yet.", [(1056, 'Во-первых, суда ещё не было')], ''),
    ('lyosha', 'А во-вторых?', 'And second?', [], "new: the boy prompts the 'second' point (1057)"),
    ('arkady', 'А во-вторых, я тебе могу игрушку купить, а твоя мама нет.', "And second, I can buy you a toy, and your mum can't.", [(1057, 'А во-вторых'), (1059, 'Я тебе могу игрушку купить, а твоя мама нет')], ''),
    ('lyosha', 'Почему?', 'Why?', [(1060, 'Почему')], ''),
    ('arkady', 'Потому что она простая. Её все обманывают.', "Because she's naive. Everybody cheats her.", [(1061, 'потому что она')], '«лохушка» (sucker) -> «простая»; «Она овца, и все её стригут» (1063) -> «Её все обманывают»'),
    ('lyosha', 'Мама хорошая!', 'My mum is good!', [(1065, 'Мама хорошая')], ''),
    ('arkady', 'Хорошая, никто же не говорит. Эй, ты что?', "She is good, nobody's saying she isn't. Hey, what's wrong?", [(1066, 'никто же не говорит')], "'Хорошая' replaces «Да отличная мама твоя»; «Ты чё, пацан?» (1068) -> «Эй, ты что?»"),
    ('marina', 'Лёша, что случилось? Дыши, сынок, дыши!', 'Lyosha, what happened? Breathe, son, breathe!', [(1079, 'Лёша, что случилось'), (1080, 'дыши, сынок, дыши')], ''),
    ('arkady', 'Мы только икру ели!', 'We were only eating caviar!', [], 'new: tells Marina what happened (the allergy attack follows the caviar, scene 28)'),
    ('marina', 'Вам же ребёнок сказал, что у него аллергия.', 'The child told you he has an allergy.', [(1087, 'Вам же ребенок сказал, что у него аллергия')], ''),
    ('arkady', 'Я думал, вы ему врёте, потому что икра дорогая.', 'I thought you were lying to him because caviar is expensive.', [(1088, 'Я думал, вы ему врете, потому что икра дорогая')], ''),
    ('marina', 'Я своему ребёнку никогда не вру.', 'I never lie to my child.', [(1089, 'Я своему ребенку никогда не вру')], ''),
    ('lyosha', 'Мама, я ему копилку отдал за приставку.', 'Mum, I gave him my piggy bank for a games console.', [(1096, 'Я ему копилку отдал за')], "'Мама' added as address; ПСП -> приставка (the plain word for a games console)"),
    ('arkady', 'В чём дело? Куплю я ему приставку.', "What's the problem? I'll buy him the console.", [(1098, 'В чём дело? Куплю я ему')], '«это ПСП» -> «приставку»'),
    ('marina', 'Нам не нужна ваша приставка! Ещё раз подойдёте к ребёнку, пожалеете!', "We don't need your console! Come near my child again and you'll be sorry!", [(1101, 'Нам не нужно ваше'), (1107, 'ребенку')], '«ваше ПСП» -> «ваша приставка» (agreement follows the noun); the threat (1107-1109) is retold cleanly, ты -> вы'),
    ('arkady', 'Я ухожу. Ваш сын будет бедным и честным.', "I'm leaving. Your son will be poor and honest.", [(1116, 'будет бедным и честным')], '«Я покидаю вас» (1115) -> «Я ухожу»; the garbled «безопасности» dropped'),
]
WALK = [
    (0, 'Держитесь меня, и всё у вас будет хорошо.', "'Stick with me, and everything will be fine for you.' The first word is a polite or plural command, 'hold on to'. Before this, Yulia told him she wants to move to Moscow, and he promised to help. Then he asks a question, expecting praise."),
    (0, 'Потому что я кто?', "'Because who am I?' Russian can leave the question word at the end, for effect. But the answer is not what he hoped."),
    (1, None, "'A bribe-taker!' One word: someone who takes bribes. It's what everybody in the flat calls him. Arkady corrects the boy like a lawyer."),
    (2, None, "'First of all, there hasn't been a trial yet.' After 'no' in the past, the trial takes the ending meaning 'of', and the action word stays in the neuter form. Lyosha waits for the rest."),
    (3, None, "'And second?' The word means 'secondly', and it pairs with 'firstly' from the line before. Here comes the real point."),
    (4, None, "'And second, I can buy you a toy, and your mum can't.' The action word 'can' appears only once: at the end, 'your mum, no' is enough. The boy wants to know why."),
    (5, None, "'Why?' One of the first question words you learn. Arkady answers with the matching word, 'because'."),
    (6, 'Потому что она простая.', "'Because she's naive.' The word normally means 'simple', and about a person it means trusting, easy to fool. In the original he uses much ruder words."),
    (6, 'Её все обманывают.', "'Everybody cheats her.' 'Her' comes first and 'everybody' second: the object can lead the sentence when it's the topic. Lyosha stands up for his mother."),
    (7, None, "'My mum is good!' No 'is' again: just 'mum good'. Arkady backs off, and then he notices the boy can't breathe."),
    (8, 'Хорошая, никто же не говорит.', "'She is good, nobody's saying she isn't.' The little word in the middle adds 'after all'."),
    (8, 'Эй, ты что?', "'Hey, what's wrong?' Literally, 'hey, you what?' Lyosha is having an allergic attack. Arkady shouts for an ambulance; the children call out the American number, and he snaps that they need the Russian one. Then Marina rushes in."),
    (9, 'Лёша, что случилось?', "'Lyosha, what happened?' A question you'll hear in any emergency. Then she helps him breathe."),
    (9, 'Дыши, сынок, дыши!', "'Breathe, son, breathe!' The command comes from the action word 'to breathe', and the middle word is a loving form of 'son'. Arkady tries to explain."),
    (10, None, "'We were only eating caviar!' 'Ate' is in the plural past, because 'we' ate. Of course, that is the problem."),
    (11, None, "'The child told you he has an allergy.' She says 'you' politely, even now. Literally, 'at him there is an allergy'. Arkady's excuse is honest, at least."),
    (12, None, "'I thought you were lying to him because caviar is expensive.' 'Thought' has a man's past ending. After 'I thought', the action word 'lying' stays in the present, where English shifts it to the past. Marina's answer is sharp."),
    (13, None, "'I never lie to my child.' Russian likes a double negative: 'never' and 'not' together. Then Lyosha confesses."),
    (14, None, "'Mum, I gave him my piggy bank for a games console.' The word for 'gave away' is masculine, because Lyosha is a boy. Arkady took the money for the phone app. Marina says that, even for him, this is too much. He shrugs."),
    (15, None, "'What's the problem? I'll buy him the console.' The action word comes first, which sounds offhand, as if it were no big deal. Marina doesn't want his gifts."),
    (16, 'Нам не нужна ваша приставка!', "'We don't need your console!' Literally, 'to us your console is not needed'. The word for 'needed' takes a feminine ending to match the console. Then she warns him."),
    (16, 'Ещё раз подойдёте к ребёнку, пожалеете!', "'Come near my child again and you'll be sorry!' Both action words are in the future. In the original her threat is far more violent. Arkady only remarks on her perfume, then bows."),
    (17, None, "'I'm leaving. Your son will be poor and honest.' After 'will be', the two describing words take a special ending, the one used for what someone becomes. And he walks out, as if he had won."),
]
