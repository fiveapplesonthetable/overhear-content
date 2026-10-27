"""s01e10 scene 15: Ставка против своих (A Bet Against His Own)."""

ID = "kukhnya-s01e10-scene-15"
SHOW = "kukhnya"
SEASON = 1
EPISODE = 10
SCENE = 15
TITLE = "Ставка против своих  (A Bet Against His Own)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
VOICES = {"narrator": "sky", "anya": "alisa", "tamara": "anja"}
LABELS = {"anya": "Шеф", "tamara": "Тамара"}
SOURCE_NAME = "Кухня (Kukhnya) S1.10"
SOURCE_FILE = "sources/kukhnya/s01/e10.ru.dual.srt"
SOURCE_NOTE = "Cues 131-141. Chef Barinov calls bookmaker Tamara to place a massive 100,000 ruble bet on his rival football team CSKA to win."

INTRO = (
    "In his private office at Claude Monet, Chef Viktor Barinov desperately needs a quick financial windfall to pay off debts. "
    "Calling bookmaker Tamara, he shocks her by placing a massive hundred-thousand-ruble wager on CSKA to beat his lifelong beloved club Spartak. "
    "Let's listen to their phone call in Russian first."
)

STORY = [
    ("anya", "Тамара, здравствуй, это Витя Баринов беспокоит.",
     "Tamara, hello, this is Vitya Barinov calling.",
     [(131, "Тамарочка, здравствуй"), (132, "Это Витя Баринов тебя беспокоит")], "calling the bookmaker"),
    ("tamara", "Привет, Витя, ты хочешь сделать ставку?",
     "Hi, Vitya, do you want to place a bet?",
     [], "greeting the client"),
    ("anya", "Да, поставь деньги на матч Спартака.",
     "Yes, put money on the Spartak match.",
     [(133, "А я хотел сделать ставочку на Спартак ЦСКА")], "specifying the football match"),
    ("tamara", "Ты ставишь на победу родного Спартака?",
     "Are you betting on your native Spartak's victory?",
     [], "assuming his usual loyalty"),
    ("anya", "Нет, я ставлю на победу ЦСКА!",
     "No, I am betting on a CSKA victory!",
     [(134, "Не-не, на победу ЦСКА"), (135, "ЦСКА")], "shocking the bookmaker"),
    ("tamara", "Ты не шутишь? Это же твои враги!",
     "Are you not joking? They are your enemies!",
     [], "reacting with surprise"),
    ("anya", "Я ставлю ровно сто тысяч рублей!",
     "I bet exactly one hundred thousand rubles!",
     [(136, "Сто тысяч")], "announcing the huge amount"),
    ("tamara", "У тебя есть с собой такие деньги?",
     "Do you have that kind of money with you?",
     [], "checking his solvency"),
    ("anya", "Зарезервируй ставку, я скоро привезу наличные.",
     "Reserve the bet, I will bring cash soon.",
     [(137, "Ты зарезервируй за мной ставочку, а я по почте денежку завезу")], "promising prompt payment"),
    ("tamara", "Хорошо, твоя ставка принята в конторе.",
     "All right, your bet is accepted at the office.",
     [], "confirming the booking"),
    ("anya", "Спасибо, деньги сейчас для меня важнее всего.",
     "Thank you, money right now matters more than anything to me.",
     [(140, "Для меня сейчас деньги важнее принципов")], "justifying his compromise"),
    ("tamara", "Надеюсь, ты понимаешь свой огромный риск.",
     "I hope you understand your huge risk.",
     [], "advising caution on the wager"),
]

OPENER = "Let's examine how Chef Barinov places a risky sports bet over the telephone line by line."

WALK = [
    (0, None,
     "'Tamara, hello, this is Vitya Barinov calling.' The chef opens the phone call using a polite greeting and a third person identifier."),
    (1, None,
     "'Hi, Vitya, do you want to place a bet?' Tamara greets him casually using an infinitive verbal construction."),
    (2, None,
     "'Yes, put money on the Spartak match.' Barinov specifies the contest using an imperative verb and a prepositional phrase."),
    (3, None,
     "'Are you betting on your native Spartak's victory?' The bookmaker assumes his traditional sports allegiance with an adjective."),
    (4, None,
     "'No, I am betting on a CSKA victory!' The chef drops a bombshell by wagering on his bitter rival team."),
    (5, None,
     "'Are you not joking? They are your enemies!' Tamara questions his sanity using an emphatic particle and a plural noun."),
    (6, None,
     "'I bet exactly one hundred thousand rubles!' Barinov states the large sum using a cardinal numeral and a genitive plural noun."),
    (7, None,
     "'Do you have that kind of money with you?' Tamara verifies payment ability with an existential construction."),
    (8, None,
     "'Reserve the bet, I will bring cash soon.' The chef promises prompt delivery using an imperative verb and an accusative object."),
    (9, None,
     "'All right, your bet is accepted at the office.' Tamara registers the wager with a short form passive participle."),
    (10, None,
     "'Thank you, money right now matters more than anything to me.' Barinov justifies his betrayal of loyalty using a comparative adjective."),
    (11, None,
     "'I hope you understand your huge risk.' The bookmaker concludes the conversation with a cautionary statement."),
]

TRANSITION = "Now let's listen to the whole dialogue again at normal conversational speed."

OUTRO = (
    "Now you know how to talk about sports wagers, financial risks, and moral compromises in Russian. "
    "See you next time!"
)

CLOSING = ("anya", "Спасибо, деньги сейчас для меня важнее всего.")
