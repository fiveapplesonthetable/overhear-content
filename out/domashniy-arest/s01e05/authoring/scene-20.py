ID = "domashniy-arest-s01e05-scene-20"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 5
SCENE = 20
TITLE = "Часы мэра  (The Mayor's Watch)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "grisha": "anja", "kostik": "angelina"}
LABELS = {"anya": "Лавров", "grisha": "Дядя Гриша", "kostik": "Костик"}
SOURCE_NAME = "Домашний арест (Domashniy Arest) S1.05"
SOURCE_FILE = "sources/domashniy-arest/s01/e05.ru.dual.srt"
SOURCE_NOTE = ("Cues 760-809. Arkady is absent -> anya = Лавров (alisa). Zavarzin accompanies Lavrov and is narrated "
               "within the three-role limit. Slang/obscenities cleaned for A1: 'загоним и бабки поделим' (765) -> "
               "'продадим их? И деньги поделим?', 'ссыкло' (779-780) -> 'трус', 'позвоночник трусы не обвалил' (799) "
               "dropped, 'пупсика' (804) -> 'его'. '150' written out in words as 'сто пятьдесят'; 'Ромавира' (ASR typo "
               "in 792) restored to 'Армавира'; 'погасила' (797) -> 'закрыла'.")

INTRO = ("Back in the microloan office that afternoon. Earlier, Uncle Grisha and Kostik took Arkady's Swiss watch in the "
         "communal flat, while Marina begged Major Lavrov to save her son from the collectors. Now Grisha is admiring "
         "his new trophy when Lavrov and Zavarzin walk through the door. We'll hear it in Russian first; don't worry "
         "about catching every word.")

STORY = [
 ("grisha", "Знаешь, что это за часы? Швейцария! Они вечные.",
  "Do you know what kind of watch this is? Switzerland! It'll last forever.",
  [(762, "Знаешь, что это за часы"), (763, "Швейцария"), (764, "Они вечные")], ""),
 ("kostik", "Дядя Гриша, может, продадим их? И деньги поделим?",
  "Uncle Grisha, maybe we sell it? And split the money?",
  [(765, "может"), (765, "их"), (765, "и"), (765, "поделим")],
  "'дядя Гриш' -> 'Дядя Гриша'; slang 'загоним и бабки' -> 'продадим их? И деньги'"),
 ("grisha", "Костик, ты дурак! Это статусная вещь.",
  "Kostik, you're a fool! This is a status piece.",
  [(766, "Костик, ты дурак"), (768, "Это статусная вещь")], ""),
 ("grisha", "Люди увидят такие часы и сразу поймут.",
  "People will see a watch like this and understand right away.",
  [(771, "Люди увидят такие часы"), (772, "и сразу поймут")],
  "split from cue 773 into two short sentences"),
 ("grisha", "Я серьёзный мужчина! И будут общаться со мной по-другому.",
  "I'm a serious man! And they'll treat me differently.",
  [(773, "серьезный мужчина"), (774, "И будут общаться со мной"), (775, "по-другому")],
  "'не китайский болванчик, а' dropped for A1"),
 ("kostik", "Что-то мне не нравится. Предчувствие у меня какое-то плохое.",
  "Something doesn't feel right to me. I have some kind of bad feeling.",
  [(777, "Что-то мне не нравится"), (778, "у меня какое-то"), (779, "плохое"), (781, "предчувствие")], ""),
 ("grisha", "Да потому что ты трус, Костик! — Ничего я не трус!",
  "That's because you're a coward, Kostik! — I am not a coward!",
  [(779, "Да потому что ты"), (780, "Костик. Ничего я не")],
  "'ссыкло' -> 'трус'"),
 ("anya", "Добрый день! Мы хотели вас попросить реструктурировать долг Булинкиной.",
  "Good afternoon! We wanted to ask you to restructure Bulinkina's debt.",
  [(781, "Добрый день"), (787, "Мы хотели вас попросить"), (788, "реструктурировать долг"), (788, "Булинкиной")],
  "'гражданки' dropped to keep sentence <= 8 words"),
 ("grisha", "Вы кто такие? — Родственники! Я её дядя из Армавира.",
  "Who are you? — Relatives! I'm her uncle from Armavir.",
  [(790, "Вы кто такие"), (791, "Родственники"), (792, "Я ее дядя из")],
  "ASR 'Ромавира' restored to 'Армавира'"),
 ("anya", "А это брат Всеволод. Мы очень переживаем.",
  "And this is cousin Vsevolod. We're very worried.",
  [(793, "А это"), (793, "брат Всеволод"), (794, "Мы очень переживаем")],
  "'троюродный' dropped for A1"),
 ("grisha", "Раз вы родственники, давайте сто пятьдесят тысяч рублей!",
  "Since you're relatives, hand over a hundred and fifty thousand roubles!",
  [(795, "раз вы родственники"), (796, "тысяч рублей")],
  "'гоните 150' -> 'давайте сто пятьдесят'"),
 ("anya", "Насколько нам известно, Марина Сергеевна полностью закрыла долг.",
  "As far as we know, Marina Sergeyevna has paid off the debt in full.",
  [(797, "Насколько нам известно, Марина Сергеевна полностью"), (797, "долг")],
  "'погасила' -> 'закрыла'"),
 ("grisha", "Пошли вон отсюда! — Мы не можем оставить в беде родного человека.",
  "Get out of here! — We can't abandon a family member in trouble.",
  [(798, "пошли вон отсюда"), (800, "Мы не можем"), (800, "оставить в беде родного человека")],
  "threat in cue 799 dropped; 'уйти и' dropped to keep sentence <= 8 words"),
 ("anya", "Отдайте, пожалуйста, договор.",
  "Please hand over the contract.",
  [(802, "Отдайте, пожалуйста, договор")], ""),
 ("grisha", "Договор? Отдать? Сейчас! Костик, ломай его!",
  "The contract? Hand it over? Right now! Kostik, break him!",
  [(803, "Договор? Отдать? Сейчас"), (804, "Костик, ломай")],
  "'пупсика' -> 'его'"),
 ("anya", "Всё, хватит! Наши друзья уже всё поняли.",
  "All right, enough! Our friends here have understood everything.",
  [(805, "Все, хватит"), (805, "Наши друзья уже все поняли")], ""),
 ("anya", "Где часы, которые у мэра забрали? До свидания!",
  "Where is the watch you took from the mayor? Goodbye!",
  [(808, "Где часы, которые у мэра забрали"), (809, "До свидания")], ""),
]

OPENER = "Let's go through the scene line by line. First, Uncle Grisha holds up the gold watch that he took from Arkady."

WALK = [
 (0, None,
  "'Do you know what kind of watch this is? Switzerland! It'll last forever.' Remember that the word for 'watch' is plural in Russian, so Grisha says 'they are eternal'."),
 (1, None,
  "'Uncle Grisha, maybe we sell it? And split the money?' Kostik only cares about quick cash."),
 (2, None,
  "'Kostik, you're a fool! This is a status piece.' Grisha refuses to sell the watch."),
 (3, None,
  "'People will see a watch like this and understand right away.' Both future verbs are perfective: people will see it once and immediately get the message."),
 (4, None,
  "'I'm a serious man! And they'll treat me differently.' Literally, 'they will converse with me in a different way'."),
 (5, None,
  "'Something doesn't feel right to me. I have some kind of bad feeling.' The noun for 'premonition' literally combines 'fore-' and 'feeling'."),
 (6, None,
  "'That's because you're a coward, Kostik! — I am not a coward!' Just as Kostik protests, the office door opens and Major Lavrov and Captain Zavarzin step inside."),
 (7, None,
  "'Good afternoon! We wanted to ask you to restructure Bulinkina's debt.' Lavrov speaks with polite bureaucratic calm."),
 (8, None,
  "'Who are you? — Relatives! I'm her uncle from Armavir.' Lavrov invents a cover story on the spot and gestures toward Zavarzin."),
 (9, None,
  "'And this is cousin Vsevolod. We're very worried.' The Russian word for 'brother' is also used for a male cousin."),
 (10, None,
  "'Since you're relatives, hand over a hundred and fifty thousand roubles!' Notice how the word for 'once' at the start of the clause means 'since you are relatives'."),
 (11, None,
  "'As far as we know, Marina Sergeyevna has paid off the debt in full.' Literally, she 'completely closed the debt'."),
 (12, None,
  "'Get out of here! — We can't abandon a family member in trouble.' Literally, 'leave a dear person in trouble'. Lavrov does not budge from the desk."),
 (13, None,
  "'Please hand over the contract.' He asks for Marina's loan agreement as if asking for a receipt."),
 (14, None,
  "'The contract? Hand it over? Right now! Kostik, break him!' Kostik lunges at the officers, and within two seconds Lavrov and Zavarzin twist both collectors' arms and pin them face-down on the desk."),
 (15, None,
  "'All right, enough! Our friends here have understood everything.' Lavrov picks up Marina's contract and pockets it."),
 (16, None,
  "'Where is the watch you took from the mayor? Goodbye!' They unstrap Arkady's gold watch from Grisha's wrist and stroll out of the office."),
]

TRANSITION = "Now let's hear the whole scene once more, from start to finish."

OUTRO = ("So Lavrov and Zavarzin have wiped out Marina's microloan debt and recovered Arkady's Swiss watch in a single "
         "visit. Well done following that confrontation in Russian. See you in the next scene.")
CLOSING = ("anya", "До свидания!")
