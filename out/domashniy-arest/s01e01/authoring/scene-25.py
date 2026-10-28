# domashniy-arest/s01e01/scene-25.py
ID = "domashniy-arest-s01e01-scene-25"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 1
SCENE = 25
TITLE = "Всё чисто  (All Clean)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
SOURCE_NAME = "Домашний арест (Domashniy Arest) S1.01"
SOURCE_FILE = "sources/domashniy-arest/s01/e01.ru.dual.srt"
VOICES = {"narrator": "sky", "samson": "anja", "anya": "alisa", "nina": "angelina"}
LABELS = {"samson": "Самсон", "anya": "Аркадий", "nina": "Нина"}
INTRO = "Back in the communal flat, the water has stopped at last. Last time, Arkady admitted that he has nothing left, and Samson, furious, tore out the leaking pipe and flooded the shared bathroom. Now somebody has to clean it all up, and Nina is not happy. We'll hear it in Russian first; don't worry about catching every word."
STORY = [
    ("samson", "Нин, только не сердись, ладно? Он всё помоет.", "Nina, just don't be angry, okay? He'll wash everything.", [(956, 'только не сердись, ладно')], "second sentence adapted from cue 957 'Он ещё всё замоет' (замоет -> помоет, 'ещё' dropped)"),
    ("nina", "Да, правильно он всё сказал. Вот моё королевство.", "Yes, he said it right. Here's my kingdom.", [(959, 'правильно он всё сказал'), (960, 'Вот моё королевство')], "'Да,' at the start"),
    ("samson", "Нин, ты что?", "Nina, what's wrong?", [], "new; plain form of cue 961 'Чё ты, Нин?' (чё -> что)"),
    ("nina", "Лучше бы я тебе тогда сказала нет.", "I should have said no to you back then.", [(962, 'Лучше бы я тебе тогда')], "'в ЗАГСе' (at the registry office) dropped; word order made plain"),
    ("samson", "Аркаша, давай убирать!", "Arkasha, let's clean up!", [(965, 'Давай убирать')], "'Аркаша' added so it is clear he is talking to Arkady"),
    ("anya", "Что я делаю?", "What am I doing?", [(967, 'Что я делаю')], ""),
    ("samson", "Вытирай пол. Вот так.", "Wipe the floor. Like that.", [], "new; simplifies cue 968 'Не замочи тут, промокни!' and cue 969 'Вот как раз'"),
    ("anya", "Садитесь и держите дверь. Никто не войдёт.", "Sit down and hold the door. Nobody will come in.", [(970, 'садитесь'), (971, 'Никто не войдёт')], "to the old neighbour; 'и держите дверь' made explicit (the toilet has no latch; cue 972 'Держите')"),
    ("anya", "Завтра мы поставим защёлку.", "Tomorrow we'll put on a latch.", [(972, 'Завтра мы поставим защёлку')], ""),
    ("samson", "Нин, я всё помыл. Всё чисто.", "Nina, I washed everything. It's all clean.", [(977, 'Всё чисто')], "'я всё помыл' from cue 976 'я всё замыл' (замыл -> помыл); 'как в аптеке' dropped"),
    ("anya", "Ты помыл?", "You washed it?", [], "new; Arkady did the scrubbing, Samson takes the credit (true to the scene)"),
    ("samson", "Правда, Нин, всё нормально. Скажи что-нибудь, пожалуйста.", "Honestly, Nina, everything's fine. Say something, please.", [(978, 'правда, Нин'), (983, 'Пожалуйста')], "'всё пучком' -> 'всё нормально'; 'скажи что-нибудь' for cue 982 'подай хоть признак жизни'"),
    ("nina", "Без комментариев.", "No comment.", [(984, 'Без комментариев')], ""),
    ("anya", "Что с ней?", "What's the matter with her?", [], "new: Arkady asks"),
    ("samson", "Обиделась. У неё всегда так.", "She's offended. She's always like that.", [(985, 'Обиделась'), (986, 'у нее всегда так')], ""),
    ("anya", "А потом?", "And then?", [], "new"),
    ("samson", "Потом пройдёт.", "Then it passes.", [(987, 'потом пройдет')], ""),
]
OPENER = "Let's go back through it slowly. The bathroom is under water, and Samson tries to calm his wife."
WALK = [
    (0, 'Нин, только не сердись, ладно?', "'Nina, just don't be angry, okay?' He uses the short, loving form of her name, and the verb is a command with 'not' in front: don't get angry. Then he makes a promise on somebody else's behalf."),
    (0, 'Он всё помоет.', "'He'll wash everything.' He means Arkady, of course. The verb is in the future: the washing hasn't started yet. Nina answers bitterly."),
    (1, None, "'Yes, he said it right. Here's my kingdom.' A few minutes ago Samson shouted that this bathroom was her kingdom. Now she agrees with him, and it hurts. Samson doesn't understand."),
    (2, None, "'Nina, what's wrong?' Literally, 'Nina, you what?' A very common, very casual way to ask what's going on. And Nina says the hardest line of the scene."),
    (3, None, "'I should have said no to you back then.' The little word near the start makes a wish about the past: 'it would have been better if I had said'. She means their wedding day. Notice the verb ends in 'a', because Nina is a woman. Samson turns to Arkady instead."),
    (4, None, "'Arkasha, let's clean up!' He calls the mayor by his childhood name, and 'let's' is one handy word followed by the verb. Arkady looks at the mop in his hands."),
    (5, None, "'What am I doing?' The mayor of the town, on his knees in a flooded toilet. Samson shows him how."),
    (6, None, "'Wipe the floor. Like that.' A plain command, then two little words that mean 'just so', 'like this'. Next, the old neighbour needs the toilet, and the door has no latch. Arkady explains, very politely."),
    (7, None, "'Sit down and hold the door. Nobody will come in.' He uses the polite form with the old lady: both commands end in the same polite ending. And he adds a promise."),
    (8, None, "'Tomorrow we'll put on a latch.' The old lady thanks the dear mayor for his care for pensioners. She doesn't mean it kindly. Meanwhile Samson goes to report to Nina."),
    (9, None, "'Nina, I washed everything. It's all clean.' Here the verb is in the past, with no ending for a man. Arkady, who did the actual washing, can't quite believe it."),
    (10, None, "'You washed it?' Just two words and a question in his voice. Samson keeps trying with Nina."),
    (11, None, "'Honestly, Nina, everything's fine. Say something, please.' The middle word in the second sentence means 'anything at all'. But she answers like a politician."),
    (12, None, "'No comment.' The same two words a mayor might say to a reporter. Arkady is puzzled."),
    (13, None, "'What's the matter with her?' Literally, 'what is with her?' Samson knows his wife well."),
    (14, None, "'She's offended. She's always like that.' The first word is a whole sentence: a past verb with a feminine ending, so we know it's about her. Arkady wants to know what happens next."),
    (15, None, "'And then?' The small word in front means 'and', with a touch of 'but'. And the husband has the answer."),
    (16, None, "'Then it passes.' He sounds very sure. Let's hope he is right."),
]
TRANSITION = "Now let's listen to the whole scene once more."
OUTRO = "That's the end of this scene, and the flat is clean again, more or less. When you watch, listen for Nina's two cold words to her husband; you'll catch them now. See you next time!"
CLOSING = ("samson", "Давай, пока!")
