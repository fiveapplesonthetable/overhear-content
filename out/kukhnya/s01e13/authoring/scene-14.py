# Authoring module for kukhnya-s01e13-scene-14.
ID = 'kukhnya-s01e13-scene-14'
SHOW = 'kukhnya'
SEASON = 1
EPISODE = 13
SCENE = 14
TITLE = 'Честный разговор  (An Honest Conversation)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'kostya': 'Костя', 'nastya': 'Настя'}
SOURCE_NAME = 'Кухня (Kukhnya) S1.13'
SOURCE_FILE = 'sources/kukhnya/s01/e13.ru.dual.srt'
INTRO = "Kostya has come to Nastya's flat expecting a romantic evening. Nastya, though, has something honest to say. Here is their conversation in Russian first."
OPENER = "Let's go back through it gently, a line at a time."
TRANSITION = "Now let's listen to the whole conversation again from start to finish."
OUTRO = "Kostya takes it well, and the two of them settle for a calm night. If you ever need to say 'I feel obliged', you have the words now. Until next time."
CLOSING = ('kostya', 'Пока!')
STORY = [
    ('nastya', 'Костя, подожди секунду, не спеши.', 'Kostya, wait a second, do not rush.', [], ''),
    ('kostya', 'Настя, что случилось, почему ты грустная?', 'Nastya, what happened, why are you sad?', [(192, 'Что')], ''),
    ('nastya', 'Сегодня у нас ничего не получится.', 'Nothing will work out between us today.', [(193, 'сегодня')], ''),
    ('kostya', 'Давай выпьем ещё немного сока!', 'Let us drink a little more juice!', [], ''),
    ('nastya', 'Нет, Костя, дело совсем не в этом.', 'No, Kostya, that is not the point.', [(195, 'Нет.')], ''),
    ('nastya', 'Я не хочу поступать не по любви.', 'I do not want to act without love.', [], ''),
    ('nastya', 'Я просто очень благодарна за твою помощь.', 'I am simply very grateful for your help.', [], ''),
    ('kostya', 'Ты думаешь, что ты обязана мне?', 'Do you think that you owe me?', [], ''),
    ('nastya', 'Да, я чувствую себя нечестным человеком.', 'Yes, I feel like a dishonest person.', [], ''),
    ('nastya', 'Давай сегодня просто спокойно поспим.', 'Let us just sleep quietly tonight.', [(196, 'Сегодня')], ''),
    ('kostya', 'Хорошо, давай сегодня просто поспим.', 'All right, let us just sleep tonight.', [], ''),
    ('nastya', 'Костя, ты правда понимаешь мои чувства?', 'Kostya, do you really understand my feelings?', [], ''),
    ('kostya', 'Да, Настя, всё совершенно нормально.', 'Yes, Nastya, everything is completely fine.', [], ''),
]
WALK = [
    (0, None, "'Kostya, wait a second, do not rush.' Both are orders to a friend. 'Podozhdi' is 'wait' and 'ne speshi' is 'don't hurry'. 'Sekundu' ends in 'u' because you wait for a second."),
    (1, None, "'Nastya, what happened, why are you sad?' 'Sluchilos' is 'happened', and it ends in 'os' because 'chto' counts as neuter. 'Grustnaya' ends in 'aya' because the sad one is a woman."),
    (2, None, "'Nothing will work out between us today.' 'U nas' is 'at us', which is how Russian says 'between us' here. 'Poluchitsya' is 'will turn out', and with 'nichego ne' in front it says nothing will."),
    (3, None, "'Let us drink a little more juice!' 'Vypem' is 'let's drink up', and the 'vy' at the front adds 'all the way'. 'Soka' is 'of juice', since Russians say 'a bit of juice' with that ending."),
    (4, None, "'No, Kostya, that is not the point.' 'Delo' means 'matter', and 'ne v etom' is 'not in this'. It's the usual way to say 'that's not the point'."),
    (5, None, "'I do not want to act without love.' 'Ne po lyubvi' is 'not out of love'. There are two 'ne' in the sentence, one for 'I don't want' and one for 'not out of love', and they don't cancel each other."),
    (6, None, "'I am simply very grateful for your help.' 'Blagodarna' is 'grateful', in a woman's form. It's built from 'blago', good, and 'darit', to give. 'Za' is 'for'."),
    (7, None, "'Do you think that you owe me?' 'Obyazana' is 'obliged', again with the 'a' of a woman. 'Mne' is 'to me', so she is obliged to him. 'Dumaesh, chto' is 'you think that', and the comma is mandatory."),
    (8, None, "'Yes, I feel like a dishonest person.' 'Chuvstvuyu sebya' is literally 'I feel myself'. 'Nechestny' is 'not honest', and it's 'ne' plus 'chestny', which is the way Russians make opposites."),
    (9, None, "'Let us just sleep quietly tonight.' 'Pospim' is 'let's sleep for a while', and the 'po' at the front makes it short. 'Spokoyno' means 'calmly'."),
    (10, None, "'All right, let us just sleep tonight.' Kostya copies her sentence and shortens it. Echoing someone's words is how Russians say 'yes, I agree'."),
    (11, None, "'Kostya, do you really understand my feelings?' 'Chuvstva' means 'feelings' and belongs to the family of 'chuvstvuyu', 'I feel'. 'Pravda' means 'truth', but here it means 'really'."),
    (12, None, "'Yes, Nastya, everything is completely fine.' 'Vsyo' means 'everything' and 'sovershenno' means 'completely'. 'Normalno' is the same as English 'normal', with an 'o' ending, because Russian adverbs end in 'o'."),
]
