ID = "domashniy-arest-s01e03-scene-14"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 3
SCENE = 14
TITLE = "Звонок соседу  (A Neighbourly Call)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "judge": "anja", "golovkin": "angelina"}
LABELS = {"anya": "Аркадий", "judge": "Илья Олегович", "golovkin": "Головкин"}
SOURCE_NAME = "Домашний арест (Domashniy Arest) S1.03"
SOURCE_FILE = "sources/domashniy-arest/s01/e03.ru.dual.srt"

INTRO = ("Last time, Golovkin suggested confessing for eight years in prison, until Arkady discovered that the "
         "judge is his own neighbour, Ilya Olegovich Berg. At Berg's house, his bossy wife Sofochka is washing "
         "their tiny dog Lyutik in the bathroom and scolding Berg for not watching him in the park when Arkady "
         "phones the judge right in front of Golovkin. Let's listen in Russian first; don't worry about catching "
         "every word.")

STORY = [
 ("judge", "Судья Берг, слушаю.",
  "Judge Berg speaking.",
  [(454, "Судья Берг, слушаю")], ""),
 ("anya", "Алло, Илюша, здравствуй. Это Аникеев.",
  "Hello, Ilyusha, hi. It's Anikeev.",
  [(455, "Алло, Илюша, здравствуй"), (457, "Это Аникеев")], ""),
 ("judge", "Здравствуйте. Я узнал. Что вы хотели?",
  "Hello. I recognised your voice. What did you want?",
  [(456, "Здравствуйте"), (458, "Я узнал, что вы хотели")],
  "cue 458 punctuated as two short sentences"),
 ("anya", "А что ты такой неласковый? Это не по-соседски.",
  "Why are you so unfriendly? That's not very neighbourly.",
  [(459, "А что ты такой неласковый"), (460, "Не по-соседски")],
  "'Это' added"),
 ("judge", "Мне с вами вообще общаться нельзя. Всего доброго.",
  "I'm not allowed to talk to you at all. Good day.",
  [(461, "мне с вами вообще общаться нельзя"), (462, "Всего доброго")],
  "'подсудимый' dropped"),
 ("anya", "Постой, не клади трубку! У меня есть деловое предложение.",
  "Wait, don't hang up! I have a business offer.",
  [(463, "Постой, не клади трубку"), (464, "деловое предложение")],
  "cue 464 shortened"),
 ("anya", "Ты выпустишь меня под подписку о невыезде. И ты мне больше ничем не обязан.",
  "You'll release me on a travel ban. And you won't owe me anything anymore.",
  [(465, "под подписку о невыезде"), (466, "ты мне больше ничем не обязан")],
  "cue 465 'А что, если ты меня выпустишь' -> 'Ты выпустишь меня'"),
 ("judge", "Интересно. А я тебе и так ничем не обязан.",
  "Interesting. I don't owe you anything anyway.",
  [(467, "интересно, я тебе и так ничем не обязан")],
  "split after 'Интересно'"),
 ("anya", "Да ты что? А кто твоей маме квартиру сделал?",
  "Really? And who got your mother a flat?",
  [(468, "Да ты что"), (469, "А кто твоей маме")],
  "'квартирку' -> 'квартиру'"),
 ("anya", "По программе «Доступное жильё»! Забыл?",
  "Under the 'Affordable Housing' programme! Did you forget?",
  [(469, "по программе «Доступное жилье»")],
  "'Забыл?' added"),
 ("judge", "Моя мама имела право на квартиру. Она пенсионерка.",
  "My mother had a right to the flat. She is a pensioner.",
  [(471, "моя мама"), (471, "имела право на"), (471, "она пенсионерка")],
  "cue 471 split into two short sentences"),
 ("anya", "Здесь полгорода имели право! Но в очереди она не стояла.",
  "Half the town had the right here! But she didn't stand in the queue.",
  [(472, "здесь полгорода имели право"), (473, "она не стояла")],
  "'В очереди-то' -> 'Но в очереди'"),
 ("anya", "А что, если об этом узнают на суде?",
  "And what if they find out about this in court?",
  [(475, "на суде")],
  "crude cue 475 dropped; 'эта информация на суде всплывет' -> 'об этом узнают на суде'"),
 ("judge", "Тогда я дам тебе ещё два года! За махинации с недвижимостью.",
  "Then I'll give you two more years! For property fraud.",
  [(476, "за махинации с недвижимостью")],
  "'еще пару лет впаяю' -> 'дам тебе ещё два года'"),
 ("golovkin", "Вы квартиры очередников по блату раздавали? Я пятнадцать лет в очереди стою!",
  "Did you hand out waiting-list flats through connections? I've been standing in the queue for fifteen years!",
  [(479, "Вы квартиры очередников по блату раздавали"), (480, "стою")],
  "cue 480 '15 лет' written out as words; 'в очереди' added"),
 ("anya", "Уходите, пожалуйста. Мне очень нужно подумать.",
  "Leave, please. I really need to think.",
  [(481, "уходите, пожалуйста"), (482, "Мне очень нужно подумать")], ""),
 ("golovkin", "До свидания. Я с вами свяжусь.",
  "Goodbye. I'll be in touch with you.",
  [(483, "До свидания, я с вами свяжусь")], ""),
]

OPENER = ("Let's go back through the call. Judge Berg answers his phone at home, and Arkady greets him like an "
          "old friend.")

WALK = [
 (0, None,
  "'Judge Berg speaking.' Literally 'Judge Berg, I am listening' — a standard formal way to answer the phone."),
 (1, None,
  "'Hello, Ilyusha, hi. It's Anikeev.' Arkady uses the informal greeting 'hi' and the pet name 'Ilyusha'. Berg "
  "immediately puts up a wall."),
 (2, None,
  "'Hello. I recognised your voice. What did you want?' Notice that Berg answers with the formal 'hello' and "
  "calls Arkady by the polite 'you'. Arkady complains."),
 (3, "А что ты такой неласковый?",
  "'Why are you so unfriendly?' Literally 'not-affectionate'."),
 (3, "Это не по-соседски.",
  "'That's not very neighbourly.' Adverbs built with this prefix and suffix mean 'in the manner of': here, "
  "'like a neighbour'. Berg reminds him of the law."),
 (4, "Мне с вами вообще общаться нельзя.",
  "'I'm not allowed to talk to you at all.' Literally 'to me with you at all to communicate is forbidden'."),
 (4, "Всего доброго.",
  "'Good day.' Literally 'of everything good' — a polite, final goodbye. Arkady stops him before he hangs up."),
 (5, "Постой, не клади трубку!",
  "'Wait, don't hang up!' Literally 'don't put down the receiver'."),
 (5, "У меня есть деловое предложение.",
  "'I have a business offer.' Now Arkady lays out the deal."),
 (6, "Ты выпустишь меня под подписку о невыезде.",
  "'You'll release me on a travel ban.' He uses the perfective future: 'you will let me out'."),
 (6, "И ты мне больше ничем не обязан.",
  "'And you won't owe me anything anymore.' Literally 'obliged to me by nothing'. Notice how Berg now drops the "
  "formal 'you' too."),
 (7, None,
  "'Interesting. I don't owe you anything anyway.' That little pair of words in the middle means 'even so, as it "
  "is'. So Arkady reminds him of a favour."),
 (8, "Да ты что?",
  "'Really?' An everyday expression of disbelief."),
 (8, "А кто твоей маме квартиру сделал?",
  "'And who got your mother a flat?' Literally 'made a flat for your mum', with 'your mum' in the dative case."),
 (9, None,
  "'Under the Affordable Housing programme! Did you forget?' That's the town housing scheme for people in need. "
  "Berg defends himself."),
 (10, None,
  "'My mother had a right to the flat. She is a pensioner.' 'A right to' uses the preposition 'onto' plus the "
  "accusative. Arkady points out the catch."),
 (11, "Здесь полгорода имели право!",
  "'Half the town had the right here!'"),
 (11, "Но в очереди она не стояла.",
  "'But she didn't stand in the queue.' Ordinary people wait years on the housing waiting list. Then Arkady tries "
  "to blackmail the judge."),
 (12, None,
  "'And what if they find out about this in court?' Literally 'if about this they find out on the court'. Berg "
  "turns the threat right back on him."),
 (13, "Тогда я дам тебе ещё два года!",
  "'Then I'll give you two more years!'"),
 (13, "За махинации с недвижимостью.",
  "'For property fraud.' After all, Arkady was the mayor who signed the papers! Berg hangs up, and suddenly "
  "Golovkin, who has heard every word in the room, speaks up in shock."),
 (14, "Вы квартиры очередников по блату раздавали?",
  "'Did you hand out waiting-list flats through connections?' 'Through connections' — pulling strings for friends "
  "— is a classic Russian phrase."),
 (14, "Я пятнадцать лет в очереди стою!",
  "'I've been standing in the queue for fifteen years!' Russian uses the present tense for an action that started "
  "in the past and is still going on. Arkady has just confessed his own housing fraud to a lawyer who has been "
  "waiting in that very queue for fifteen years! Arkady quickly sends him out."),
 (15, None,
  "'Leave, please. I really need to think.' And Golovkin leaves very quietly."),
 (16, None,
  "'Goodbye. I'll be in touch with you.' Literally 'I will connect with you'."),
]

TRANSITION = "Let's listen to the whole scene again from start to finish."

OUTRO = ("So Judge Berg refuses to be blackmailed, and Arkady accidentally reveals his housing-list fraud right in "
         "front of Golovkin, who has waited fifteen years in that queue. Keep that moment in mind for the court "
         "hearing later; see you next time.")
CLOSING = ("anya", "Мне очень нужно подумать.")
