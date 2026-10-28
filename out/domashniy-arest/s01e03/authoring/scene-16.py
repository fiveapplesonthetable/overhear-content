ID = "domashniy-arest-s01e03-scene-16"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 3
SCENE = 16
TITLE = "Звонок Лёле  (Calling Lyolya)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "lyolya": "angelina"}
LABELS = {"anya": "Аркадий", "lyolya": "Лёля"}
SOURCE_NAME = "Домашний арест (Domashniy Arest) S1.03"
SOURCE_FILE = "sources/domashniy-arest/s01/e03.ru.dual.srt"

INTRO = ("Last time, Nina bumped into her old classmate Danila Golovkin in the corridor and they traded warm "
         "compliments while Samson watched jealously. Back in his room, Arkady has thought of a new plan to force "
         "Judge Berg's hand: kidnapping the judge's beloved little dog from the park. He phones his young "
         "girlfriend Lyolya to ask for her help. Let's hear it in Russian first; don't worry about catching every word.")

STORY = [
 ("anya", "Лёля, это очень просто. Приезжаешь сегодня в наш парк.",
  "Lyolya, this is very simple. You come to our park today.",
  [(506, "Лёля, это"), (507, "приезжаешь")],
  "idiom 'проще пареной репы' -> 'очень просто'; 'к нам в парк' -> 'сегодня в наш парк'"),
 ("anya", "Там гуляет девочка с собачкой. Каждый день с трёх до четырёх.",
  "A girl walks a little dog there. Every day from three to four.",
  [(507, "там девочка гуляет"), (507, "с собачкой"), (508, "Каждый день с трёх до четырёх")],
  "'толстенькая' dropped"),
 ("anya", "Собачка маленькая, добрая.",
  "The little dog is small and friendly.",
  [(509, "Собачка маленькая, добрая")], ""),
 ("lyolya", "Аркашенька, ну это же бред! Я не буду воровать собаку.",
  "Arkashenka, come on, this is nonsense! I'm not going to steal a dog.",
  [(510, "Аркашенька, ну это же бред"), (511, "Я не буду воровать собаку")], ""),
 ("anya", "Да это не воровство, послушай! Это абсолютно безопасно.",
  "That's not stealing, listen! It's completely safe.",
  [(512, "Да это не воровство, послушай"), (513, "Это абсолютно безопасно")], ""),
 ("anya", "Ты же помнишь наш посёлок? Охраны там никакой нет.",
  "You remember our village, don't you? There's no security there at all.",
  [(514, "Ты же помнишь"), (514, "охраны никакой нет")],
  "'в этом поселке' (515) folded into the first sentence"),
 ("lyolya", "Нет, я же сказала! Нет, Аркаша.",
  "No, I already told you! No, Arkasha.",
  [(517, "я же сказала, нет, Аркаша")], ""),
 ("anya", "Лёлечка, а ты забыла, кто тебе квартирку сделал?",
  "Lyolechka, have you forgotten who got you your little flat?",
  [(519, "Лёлечка, ты"), (519, "забыла, кто тебе квартирку")],
  "'справил' -> 'сделал'"),
 ("anya", "По программе «Доступное жильё»! Забыла?",
  "Under the 'Affordable Housing' programme! Did you forget?",
  [(520, "По программе «Доступное жилье»"), (521, "Забыла")], ""),
 ("lyolya", "Ты в себе вообще? Я эту квартиру честно заслужила!",
  "Are you in your right mind? I earned that flat honestly!",
  [(522, "Ты в себе вообще"), (523, "эту квартиру, честно")],
  "crude verb in 523 replaced with 'заслужила'"),
 ("anya", "Милая моя, войди в моё положение! Помоги мне, ты слышишь?",
  "My darling, put yourself in my position! Help me, do you hear?",
  [(524, "Милая моя"), (525, "войди в моё положение"), (528, "помоги мне, ты, слышишь")],
  "crude 526-527 dropped"),
 ("lyolya", "Нет, котик, я всё понимаю. Но я не буду воровать собаку.",
  "No, kitten, I understand everything. But I'm not going to steal a dog.",
  [(529, "Нет, котик"), (530, "я все понимаю, но не буду воровать собаку")],
  "split into two sentences"),
 ("lyolya", "Я всё для тебя сделаю, малыш. Хочешь, я к тебе приеду?",
  "I'll do anything for you, baby. Do you want me to come visit you?",
  [(531, "Я все для тебя сделаю, малыш"), (532, "хочешь, я"), (532, "приеду")],
  "crude second half of 532 dropped"),
 ("anya", "Да хочу, только не сейчас. Ладно, пока.",
  "Yes, I want that, just not right now. Fine, bye.",
  [(533, "Да хочу"), (533, "не сейчас только"), (534, "ладно")],
  "'пока' added"),
 ("lyolya", "Ну звони, котик. Давай, целую!",
  "Well, call me, kitten. Bye, kisses!",
  [(535, "звони"), (536, "Давай, целую")], ""),
]

OPENER = ("Let's walk through the call. Arkady has a plan to steal Judge Berg's dog, and he tries to make it sound "
          "easy to his girlfriend Lyolya.")

WALK = [
 (0, "Лёля, это очень просто.",
  "'Lyolya, this is very simple.' Russian leaves out 'am', 'is', or 'are' in the present tense, linking 'Lyolya' straight to 'simple'."),
 (0, "Приезжаешь сегодня в наш парк.",
  "'You come to our park today.' He uses the present tense to lay out instructions step by step, just as we do "
  "in English."),
 (1, "Там гуляет девочка с собачкой.",
  "'A girl walks a little dog there.' Literally 'there walks a girl with a doggy', using the instrumental case "
  "after 'with'."),
 (1, "Каждый день с трёх до четырёх.",
  "'Every day from three to four.' Both numbers are in the genitive case after 'from' and 'until'."),
 (2, None,
  "'The little dog is small and friendly.' Both adjectives have the feminine ending to match the word for 'little "
  "dog'. Lyolya is not convinced at all."),
 (3, "Аркашенька, ну это же бред!",
  "'Arkashenka, come on, this is nonsense!' Even while calling his plan nonsense, she uses a sweet pet form of his "
  "name."),
 (3, "Я не буду воровать собаку.",
  "'I'm not going to steal a dog.' Literally 'I will not steal a dog', with the accusative ending on 'dog'. Arkady "
  "tries to reassure her."),
 (4, None,
  "'That's not stealing, listen! It's completely safe.' He adds a detail about the rich cottage village where he "
  "and the judge live."),
 (5, "Ты же помнишь наш посёлок?",
  "'You remember our village, don't you?' Here 'you' sets up the idea, while 'village' comes at the end for emphasis."),
 (5, "Охраны там никакой нет.",
  "'There's no security there at all.' With the word for 'there is not', both 'security' and 'no kind of' go into "
  "the genitive case. Lyolya stands firm."),
 (6, None,
  "'No, I already told you! No, Arkasha.' Notice the feminine past ending on 'said'. So Arkady pulls out the same "
  "argument he just used on the judge."),
 (7, None,
  "'Lyolechka, have you forgotten who got you your little flat?' And it turns out Lyolya got her flat through the "
  "very same housing scheme!"),
 (8, None,
  "'Under the Affordable Housing programme! Did you forget?' So Arkady handed out social-housing flats both to the "
  "judge's mother and to his own girlfriend! Lyolya is outraged."),
 (9, "Ты в себе вообще?",
  "'Are you in your right mind?' Literally 'are you in yourself at all?'."),
 (9, "Я эту квартиру честно заслужила!",
  "'I earned that flat honestly!' Seeing that threats don't work, Arkady switches to begging."),
 (10, None,
  "'My darling, put yourself in my position! Help me, do you hear?' Literally 'enter into my position'. Lyolya "
  "answers with plenty of pet names, and a firm 'no'."),
 (11, "Нет, котик, я всё понимаю.",
  "'No, kitten, I understand everything.' 'Kitten' is a very common Russian pet name."),
 (11, "Но я не буду воровать собаку.",
  "'But I'm not going to steal a dog.' Still, she wants to show she cares."),
 (12, None,
  "'I'll do anything for you, baby. Do you want me to come visit you?' Literally 'do you want, I will come to "
  "you?'. Arkady is locked in a crowded communal flat with angry neighbours, so that won't help right now."),
 (13, None,
  "'Yes, I want that, just not right now. Fine, bye.' And Lyolya signs off cheerfully."),
 (14, None,
  "'Well, call me, kitten. Bye, kisses!' Literally 'I kiss you'."),
]

TRANSITION = "Let's listen to the whole phone call again from the beginning."

OUTRO = ("So even though Arkady got Lyolya a flat under the 'Affordable Housing' programme too, she flatly "
         "refuses to steal the judge's dog — which means Arkady will have to find someone else to do it. See you "
         "in the next scene.")
CLOSING = ("lyolya", "Я не буду воровать собаку.")
