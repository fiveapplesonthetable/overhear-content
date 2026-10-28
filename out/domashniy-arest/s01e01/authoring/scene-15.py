# domashniy-arest/s01e01/scene-15.py
ID = "domashniy-arest-s01e01-scene-15"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 1
SCENE = 15
TITLE = "Новости по телевизору  (News on TV)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
SOURCE_NAME = "Домашний арест (Domashniy Arest) S1.01"
SOURCE_FILE = "sources/domashniy-arest/s01/e01.ru.dual.srt"
VOICES = {"narrator": "sky", "samson": "anja", "nina": "angelina"}
LABELS = {"samson": "Самсон", "nina": "Нина"}
INTRO = "Meanwhile, in the communal flat, Samson's wife Nina is furious: he went through with that silly, humiliating kiss for the mayor, and he still got no job. Last time, that same mayor, Arkady, was arrested in a café for taking a large bribe, and the news is about to reach the television in this little room. Let's listen in Russian first."
STORY = [
    ("nina", "Ну, Ваня! Ты всё сделал, а работы нет.", "Oh, Vanya! You did everything, and there's no job.", [], "new: clean retelling of cues 577-578 (the humiliating 'kiss' for the mayor)"),
    ("samson", "А что ты кричишь?", "Why are you shouting?", [(580, 'А что ты')], "орёшь-то -> кричишь (plain word)"),
    ("nina", "Что я кричу? Я жить нормально хочу!", "Why am I shouting? I want to live a normal life!", [(582, 'Я жить нормально хочу')], "'Что я кричу?' adapts cue 581 'Че я ору?' (орать -> кричать)"),
    ("samson", "А что я мог сделать?", "And what could I do?", [], "new: plain version of cue 586 'Как тебе подстраховаться?'"),
    ("nina", "Надо было у него расписку взять.", "You should have got a receipt from him.", [(587, 'Надо было у него расписку взять')], ""),
    ("samson", "Расписку? У мэра?", "A receipt? From the mayor?", [], "new"),
    ("nina", "Да! Даже ребёнок знает.", "Yes! Even a child knows.", [(588, 'даже ребенок знает')], "'Да!' new; the speaker of cue 588 is unclear in the source, given to Nina"),
    ("samson", "Юля, иди уроки учи!", "Yulia, go and do your homework!", [(589, 'Иди уроки учи')], "'Юля' added as address (the daughter is listening in)"),
    ("nina", "Ой, смотри! Новости.", "Oh, look! The news.", [], "new: the TV news starts (cue 593)"),
    ("samson", "Задержан мэр города Аркадий Аникеев.", "The town's mayor, Arkady Anikeev, has been detained.", [(593, 'Задержан мэр города'), (593, 'Аркадий Аникеев')], "town name (garbled in the cue) left out"),
    ("samson", "Что? Наш Аркашка?", "What? Our Arkasha?", [], "new: Samson's reaction; Аркашка is the childhood name used in the show (cue 609)"),
    ("samson", "Суд решил: домашний арест по месту прописки.", "The court has decided: house arrest at his registered address.", [(596, 'домашний арест по месту прописки')], "'Суд решил' simplifies 'суд, который избрал меру пресечения' (595-596)"),
    ("nina", "По месту прописки? Это же здесь, у нас!", "At his registered address? But that's here, at our place!", [], "new: Arkady is still registered in the communal flat (scene 16)"),
    ("samson", "Новый мэр — заместитель Аникеева.", "The new mayor is Anikeev's deputy.", [(600, 'заместитель Аникеева')], "simplified from cue 600 (the deputy, Pasha, is appointed acting mayor)"),
    ("samson", "Вот это новости!", "Well, that's news!", [], "new"),
    ("nina", "И работы нет, и мэра нет.", "No job, and no mayor either.", [], "new: Nina's wry summing-up"),
]
OPENER = "Let's take it slowly from the top. Nina speaks first, and she is not calm."
WALK = [
    (0, None, "'Oh, Vanya! You did everything, and there's no job.' Vanya is the everyday form of Ivan, Samson's real name; Samson is only a nickname. The little word in the middle means 'and' with a hint of 'but': it sets up the contrast. Samson doesn't like her tone."),
    (1, None, "'Why are you shouting?' Literally, 'and what are you shouting?' In complaints like this, 'what' often does the job of 'why'. Nina throws the question straight back."),
    (2, 'Что я кричу?', "'Why am I shouting?' The same verb, now with 'I'. Then she gives the real reason."),
    (2, 'Я жить нормально хочу!', "'I want to live a normal life!' Word for word, 'I to live normally want'. Word order is loose in Russian: you can move words around for emphasis and the meaning stays the same. Samson tries to defend himself."),
    (3, None, "'And what could I do?' 'Could' is in the past tense, in the short form a man uses; a woman would add a syllable at the end. Nina knows exactly what he should have done."),
    (4, None, "'You should have got a receipt from him.' The first two words together mean 'it was necessary', a handy way to say 'you should have'. A receipt here is a written note that proves a promise was made. Samson can hardly believe his ears."),
    (5, None, "'A receipt? From the mayor?' After the little word for 'from', the mayor gets a new ending, the one that means 'of'. Nina has no doubts at all."),
    (6, None, "'Yes! Even a child knows.' Their teenage daughter Yulia is listening in, and she clearly agrees. So Samson sends her off."),
    (7, None, "'Yulia, go and do your homework!' Literally, 'go learn your lessons'. Two verbs side by side with no 'and' between them, very natural in speech. Then Nina notices the television."),
    (8, None, "'Oh, look! The news.' The word for news is plural, and it always talks about several pieces of news at once. And here comes the big story."),
    (9, None, "'The town's mayor, Arkady Anikeev, has been detained.' This is television language: the verb comes first, in a short formal form meaning 'detained'. It's the man who cheated Samson. Samson can't believe it."),
    (10, None, "'What? Our Arkasha?' Arkasha, and this cheekier form of it, are what everyone called Arkady when he was a little boy in this very flat. 'Our' makes him one of the family again. The newsreader goes on."),
    (11, None, "'The court has decided: house arrest at his registered address.' In Russia every person is officially registered at one address, and that phrase at the end means exactly that. Nina works it out first."),
    (12, None, "'At his registered address? But that's here, at our place!' The short word after 'that' adds 'but, you know', and the last two words mean 'at our home'. Arkady never moved his registration out of the communal flat. And there's one more piece of news."),
    (13, None, "'The new mayor is Anikeev's deputy.' There's no 'is' in the present tense: a short dash does the job. The deputy is Pasha, the ambitious man we met at the town hall. Samson sums it up."),
    (14, None, "'Well, that's news!' Said with feeling, it means 'what a surprise'. And Nina has the last word."),
    (15, None, "'No job, and no mayor either.' Word for word, 'and of work there's none, and of mayor there's none'. After 'there is no', the missing thing takes the ending for 'of'. The double 'and' works like 'neither, nor'."),
]
TRANSITION = "Now let's hear the whole scene again, from the start."
OUTRO = "And that's the scene: no job and no receipt for Samson, but the man who cheated him is about to move into the room next door. See you next time!"
CLOSING = ("nina", "Пока!")
