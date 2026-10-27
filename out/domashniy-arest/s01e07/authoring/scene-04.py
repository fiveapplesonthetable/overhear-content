# Authoring module for domashniy-arest s01e07 scene 04.

ID = "domashniy-arest-s01e07-scene-04"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 7
SCENE = 4
TITLE = "Чьи это цветы?  (Whose Flowers Are These?)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"

VOICES = {
    "narrator": "sky",
    "anya": "alisa",
    "dean": "anja",
    "marina": "angelina",
}
LABELS = {
    "anya": "Аркадий",
    "dean": "Эдуард Валентинович",
    "marina": "Марина",
}

SOURCE_NAME = "Домашний арест (Domashniy Arest) S1.07"
SOURCE_FILE = "sources/domashniy-arest/s01/e07.ru.dual.srt"
SOURCE_NOTE = (
    "Cues 126–203 (00:07:53–00:10:39). On the communal flat stairwell, Arkady intercepts Marina's former dean Eduard "
    "Valentinovich and a flower courier. For the three-role limit, the courier's question in cue 143 is folded into "
    "Eduard's turn while Arkady, Eduard Valentinovich, and Marina hold the three voices. Colloquial 'здрасте' (127–128) "
    "is standardised to 'Здравствуйте', 'А с какой стати интересуетесь?' (144) is simplified to 'А почему вы "
    "спрашиваете?', the insult 'подлец' (165) and 'что он несёт' (166) are cleaned up for A1, ASR 'Звучите оба' (196, "
    "for 'Замолчите оба') is folded into 'Уходите отсюда оба!', and Arkady's parting shout in cue 203 is covered in "
    "the outro."
)

INTRO = (
    "On the stairwell outside the communal flat. Last time, under Ilona's direction, Samsonov personally paved a "
    "courtyard pothole with a hand roller for a television report and chased off a rude driver who complained about a "
    "puddle. Now Marina's former dean Eduard Valentinovich arrives on the landing with an apology bouquet at the exact "
    "moment a flower courier delivers roses ordered by Arkady, and Arkady snatches the flowers to hand them to Marina "
    "himself. We'll hear it in Russian first; don't worry about catching every word."
)

# (role, ru, en, [(cue, frag), ...], note)
STORY = [
    ("anya", "Эдуард Валентинович? Здравствуйте! Какими судьбами?",
     "Eduard Valentinovich? Hello! What brings you here?",
     [(126, "Эдуард Валентинович"), (128, "Какими судьбами")],
     "colloquial 'здрасте' (127-128) -> standard 'Здравствуйте'"),
    ("dean", "Вы сами знаете, Аркадий Борисович. Где Марина Сергеевна?",
     "You know very well, Arkady Borisovich. Where is Marina Sergeyevna?",
     [(129, "Вы сами знаете"), (129, "Аркадий Борисович"), (143, "где Марина Сергеевна")],
     "courier's question in 143 folded into Eduard's line for the 3-role limit"),
    ("anya", "А почему вы спрашиваете?",
     "And why are you asking?",
     [],
     "simplified from cue 144 'А с какой стати интересуетесь?' for A1"),
    ("dean", "Потому что это моя женщина! Идите к себе.",
     "Because she is my woman! Go to your room.",
     [(145, "что это моя женщина"), (197, "идите к себе")],
     "'С такой, что' -> 'Потому что'"),
    ("anya", "Дай сюда! Марина, доброе утро. Это вам.",
     "Hand it over! Marina, good morning. This is for you.",
     [(157, "Дай сюда"), (158, "Марина"), (158, "доброе утро"), (159, "Это вам")],
     "diminutive 'Мариночка' dropped"),
    ("marina", "Спасибо. Эдуард Валентинович, вы что здесь делаете?",
     "Thank you. Eduard Valentinovich, what are you doing here?",
     [(160, "Спасибо"), (162, "Эдуард Валентинович, вы"), (162, "что здесь делаете")],
     "'вообще' dropped"),
    ("dean", "Я пришёл просить прощения. Я принёс этот букет.",
     "I came to ask for forgiveness. I brought this bouquet.",
     [(163, "Я пришел просить прощения"), (164, "Принес этот букет")],
     ""),
    ("dean", "А он украл мои цветы! Вырвал из рук!",
     "And he stole my flowers! He snatched them from my hands!",
     [(161, "он украл мои цветы"), (165, "вырвал"), (165, "из рук")],
     "insult 'подлец' in 165 omitted"),
    ("anya", "Не слушайте его, Марина! Этот букет заказал я.",
     "Don't listen to him, Marina! I ordered this bouquet.",
     [(167, "Марина, этот букет"), (167, "я заказал")],
     "colloquial 'что он несёт' (166) -> 'Не слушайте его'"),
    ("anya", "У меня чек есть! Вот он, смотрите.",
     "I have a receipt! Here it is, look.",
     [(169, "У меня чек есть. Вот он")],
     "'смотрите' added"),
    ("dean", "Какой чек? Покажите его! Это мои цветы, Марина.",
     "What receipt? Show it to me! These are my flowers, Marina.",
     [(172, "Какой чек"), (172, "Покажите его"), (177, "это мои цветы"), (177, "Марина")],
     ""),
    ("anya", "Мы с Мариной не хотим вас больше видеть!",
     "Marina and I don't want to see you anymore!",
     [(175, "Мы с Мариной не хотим вас больше видеть")],
     ""),
    ("dean", "Марина, извините. Возьмите, пожалуйста, это мой букет.",
     "Marina, I'm sorry. Take it, please, this is my bouquet.",
     [(181, "Марина, извините. Возьмите, это мой букет")],
     ""),
    ("marina", "Мне не нужны ваши цветы! Я не хочу знать, чьи это цветы.",
     "I don't need your flowers! I don't want to know whose flowers these are.",
     [(182, "мне не нужны ваши цветы"), (187, "не хочу знать, чьи это цветы")],
     "'вообще' dropped"),
    ("anya", "Марина, что ты делаешь? Она выбросила ваши цветы!",
     "Marina, what are you doing? She threw out your flowers!",
     [(189, "Марина, что ты делаешь"), (191, "Она выбросила ваши цветы")],
     ""),
    ("marina", "Ничего вам не нужно! Уходите отсюда оба!",
     "You don't need anything! Both of you, get out of here!",
     [(194, "Ничего вам не нужно, уходите отсюда"), (196, "оба")],
     "ASR 'Звучите оба' (196, for 'Замолчите оба') folded into 'Уходите отсюда оба!'"),
]

OPENER = "Now let's go through it piece by piece. Arkady spots Marina's former dean Eduard Valentinovich on the stairs:"

WALK = [
    (0, "Эдуард Валентинович? Здравствуйте!",
     "'Eduard Valentinovich? Hello!' Arkady greets Marina's former dean on the stairs with cheerful confidence."),
    (0, "Какими судьбами?",
     "'What brings you here?' Literally, by what fates — a common Russian greeting when you bump into someone unexpectedly."),
    (1, "Вы сами знаете, Аркадий Борисович.",
     "'You know very well yourself, Arkady Borisovich.' Eduard replies coldly and refuses to join in the joke."),
    (1, "Где Марина Сергеевна?",
     "'Where is Marina Sergeyevna?' Eduard has come to apologize to Marina after running home the night before."),
    (2, None,
     "'And why are you asking?' Arkady blocks the landing and pretends that Eduard has no business being there."),
    (3, "Потому что это моя женщина!",
     "'Because she is my woman!' Eduard flares up defensively on the stairwell."),
    (3, "Идите к себе.",
     "'Go to your room!' Notice the reflexive prepositional phrase meaning to your own place."),
    (4, "Дай сюда!",
     "'Hand it over!' Arkady abruptly snatches the bouquet from the flower delivery courier on the stairs."),
    (4, "Марина, доброе утро.",
     "'Marina, good morning.' Arkady turns smoothly as Marina steps out into the corridor."),
    (4, "Это вам.",
     "'This is for you.' Arkady holds out the flowers with a charming smile."),
    (5, "Спасибо.",
     "'Thank you.' Marina accepts the bouquet before realizing who is standing on the landing."),
    (5, "Эдуард Валентинович, вы что здесь делаете?",
     "'Eduard Valentinovich, what are you doing here?' She looks surprised to see her dean on the stairs."),
    (6, "Я пришёл просить прощения.",
     "'I came to ask for forgiveness.' The verb to ask takes the genitive case of the noun for forgiveness."),
    (6, "Я принёс этот букет.",
     "'I brought this bouquet.' Eduard explains that he brought flowers to apologize to her."),
    (7, "А он украл мои цветы!",
     "'And he stole my flowers!' Eduard points an accusing finger at Arkady on the landing."),
    (7, "Вырвал из рук!",
     "'He snatched them from my hands!' Eduard assumes Arkady stole his flowers from his hands."),
    (8, "Не слушайте его, Марина!",
     "'Don't listen to him, Marina!' Arkady interrupts immediately to defend himself."),
    (8, "Этот букет заказал я.",
     "'I ordered this bouquet.' Placing the pronoun at the end of the sentence gives it strong emphasis."),
    (9, "У меня чек есть!",
     "'I have a receipt!' Arkady triumphantly pulls out the paper delivery receipt."),
    (9, "Вот он, смотрите.",
     "'Here it is, look.' He waves the receipt right in Eduard's face."),
    (10, "Какой чек? Покажите его!",
     "'What receipt? Show it to me!' Eduard demands to inspect the paper slip."),
    (10, "Это мои цветы, Марина.",
     "'These are my flowers, Marina.' Eduard insists that the bouquet belongs to him."),
    (11, None,
     "'Marina and I don't want to see you anymore!' Notice the Russian phrase 'we with Marina'."),
    (12, "Марина, извините.",
     "'Marina, I'm sorry.' Eduard steps closer to plead his case with her."),
    (12, "Возьмите, пожалуйста, это мой букет.",
     "'Take it, please, this is my bouquet.' He attempts to hand her his second bouquet."),
    (13, "Мне не нужны ваши цветы!",
     "'I don't need your flowers!' The dative pronoun 'to me' is used with the short adjective for needed."),
    (13, "Я не хочу знать, чьи это цветы.",
     "'I don't want to know whose flowers these are.' The question word for whose agrees in the plural with flowers."),
    (14, "Марина, что ты делаешь?",
     "'Marina, what are you doing?' Arkady cries out as Marina throws the bouquets down the stairs."),
    (14, "Она выбросила ваши цветы!",
     "'She threw out your flowers!' And Arkady immediately turns to Eduard with a broad grin."),
    (15, "Ничего вам не нужно!",
     "'You don't need anything!' Marina tells both men that their arguing is ridiculous."),
    (15, "Уходите отсюда оба!",
     "'Both of you, get out of here!' Marina chases both suitors off the landing."),
]

TRANSITION = "Now let's listen to the whole stairwell scene again from start to finish."

OUTRO = (
    "Marina pushes Eduard into her room to have it out with him and slams the door in Arkady's face, while Arkady "
    "shouts after her down the corridor that this old man is stealing her best years. Here's one last line from the scene:"
)

CLOSING = ("marina", "Мне не нужны ваши цветы!")
