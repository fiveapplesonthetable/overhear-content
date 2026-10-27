ID = "dix-pour-cent-s01e05-scene-18"
SHOW = "dix-pour-cent"
SEASON = 1
EPISODE = 5
SCENE = 18
TITLE = "Quelqu'un d'important a oublié  (Someone Important Forgot)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "andrea": "emilie", "gabriel": "theo"}
LABELS = {"lea": "Camille", "andrea": "Andréa", "gabriel": "Gabriel"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S01E05"
SOURCE_FILE = "sources/dix-pour-cent/s01/e05.fr.dual.srt"

INTRO = (
    "At the country hotel restaurant, Gabriel gets sentimental over dinner about how the agents "
    "spend all their time taking care of actors instead of living for themselves, while Andréa "
    "looks for the first excuse to hurry back to Colette in Room Sixteen. Meanwhile in Paris, "
    "Hippolyte brings Camille a birthday cake at midnight. "
    "Let's listen to the scene in French first; don't worry about catching every word."
)

STORY = [
    ("gabriel", "On est ensemble toute la journée, tous les jours.",
     "We're together all day, every day.",
     [(338, "On est ensemble toute la journée, tous les jours")], ""),
    ("gabriel", "Mais on ne profite pas vraiment l'un de l'autre.",
     "But we don't really enjoy each other's company.",
     [(339, "Mais on ne profite pas vraiment l'un de l'autre")], ""),
    ("gabriel", "On ne devrait pas laisser le travail nous définir.",
     "We shouldn't let the job define us.",
     [(341, "On ne devrait pas laisser le travail nous définir")], ""),
    ("gabriel", "Arlette, par exemple. Qu'est-ce qu'on sait d'elle? Ou de Mathias?",
     "Arlette, for example. What do we know about her? Or about Mathias?",
     [(342, "Arlette, par exemple"), (343, "Qu'est-ce qu'on sait d'elle"), (343, "Ou de Mathias")], ""),
    ("andrea", "C'est ça, le travail, Gabriel.",
     "That's what the job is, Gabriel.",
     [(344, "C'est ça, le travail, Gabriel")], ""),
    ("gabriel", "Et nous. Regarde-nous. Qu'est-ce que je sais de toi?",
     "And us. Look at us. What do I know about you?",
     [(345, "Et nous. Regarde-nous"), (346, "Qu'est-ce que je sais de toi")], ""),
    ("gabriel", "On couve trop nos acteurs en oubliant de vivre pour nous-mêmes.",
     "We coddle our actors too much while forgetting to live for ourselves.",
     [(348, "On couve trop nos acteurs en oubliant de vivre pour nous-mêmes")], ""),
    ("andrea", "Oui, tu as raison. Je suis crevée.",
     "Yes, you're right. I'm exhausted.",
     [(349, "as raison"), (350, "Je suis crevée")],
     "spoken 'Ouais, t'as' standardised to 'Oui, tu as'"),
    ("andrea", "Je crois que je vais aller me coucher. Bonne nuit.",
     "I think I'm going to go to bed. Good night.",
     [(350, "Je crois que je vais aller me coucher"), (351, "Bonne nuit")], ""),
    ("lea", "Non, ce n'est pas ça.",
     "No, it isn't that.",
     [(355, "Non"), (355, "pas ça")],
     "spoken 'c'est pas' restored to 'ce n'est pas'"),
    ("lea", "Quelqu'un d'important pour moi a oublié mon anniversaire.",
     "Someone important to me forgot my birthday.",
     [(356, "Quelqu'un d'important pour moi a oublié mon anniversaire")], ""),
    ("lea", "Non, il est passé minuit.",
     "No, it's past midnight.",
     [(358, "Non, il est passé minuit")], ""),
    ("lea", "Il a oublié. C'est trop tard maintenant.",
     "He forgot. It's too late now.",
     [(359, "Il a oublié. C'est trop tard maintenant")], ""),
]

OPENER = "Let's go through it slowly. At the hotel restaurant, Gabriel reflects on their lives at the agency."

WALK = [
    (0, None,
     "'We're together all day, every day.' Notice how the word for 'all' changes from feminine singular for 'the whole day' to masculine plural for 'every day'."),
    (1, None,
     "'But we don't really enjoy each other's company.' The phrase at the end literally means 'the one of the other'."),
    (2, None,
     "'We shouldn't let the job define us.' The conditional form of 'must' means 'should'."),
    (3, "Arlette, par exemple.",
     "'Arlette, for example.' Gabriel thinks about their oldest colleague at the agency."),
    (3, "Qu'est-ce qu'on sait d'elle? Ou de Mathias?",
     "'What do we know about her? Or about Mathias?'"),
    (4, None,
     "'That's what the job is, Gabriel.' Literally 'it is that, the work'."),
    (5, "Et nous. Regarde-nous.",
     "'And us. Look at us.' The pronoun after the hyphen means 'us'."),
    (5, "Qu'est-ce que je sais de toi?",
     "'What do I know about you?' Gabriel has no idea Colette is waiting upstairs in Andréa's room right now."),
    (6, None,
     "'We coddle our actors too much while forgetting to live for ourselves.' The verb literally means 'brood over' like a mother hen."),
    (7, "Oui, tu as raison.",
     "'Yes, you're right.' Literally 'you have reason'."),
    (7, "Je suis crevée.",
     "'I'm exhausted.' A very common informal adjective for being dead tired."),
    (8, "Je crois que je vais aller me coucher.",
     "'I think I'm going to go to bed.' Literally 'go put myself to bed'—Andréa's excuse to hurry back upstairs to Colette."),
    (8, "Bonne nuit.",
     "'Good night.' Meanwhile in Paris, Hippolyte sings happy birthday to Camille with a small cake and tells her turning twenty-three is not the end of the world."),
    (9, None,
     "'No, it isn't that.' Camille explains why she looks sad."),
    (10, None,
     "'Someone important to me forgot my birthday.' After the word for 'someone', French links the adjective with the little word for 'of'."),
    (11, None,
     "'No, it's past midnight.' Hippolyte says there is still time for the person to call, but the clock has already passed twelve."),
    (12, "Il a oublié.",
     "'He forgot.' She means her father, Mathias."),
    (12, "C'est trop tard maintenant.",
     "'It's too late now.'"),
]

TRANSITION = "Now let's hear the whole scene again from start to finish."

OUTRO = (
    "Hippolyte gives Camille a comforting hug as she blows out her birthday candle, while across "
    "Paris, Mathias has no idea he forgot his daughter's birthday. See you in the next scene."
)
CLOSING = ("lea", "C'est trop tard maintenant.")
