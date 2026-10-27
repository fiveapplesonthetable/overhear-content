# Authoring module for dix-pour-cent s01e05 scene 14 (cues 252-264).
# Build: python3 tools/compose.py out/dix-pour-cent/s01e05/authoring/scene-14.py --out out/dix-pour-cent/s01e05/scene-14.json

ID = "dix-pour-cent-s01e05-scene-14"
SHOW = "dix-pour-cent"
SEASON = 1
EPISODE = 5
SCENE = 14
TITLE = "On tourne la scène d'amour demain  (We Shoot the Love Scene Tomorrow)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "julie": "emilie", "samir": "marcel"}
LABELS = {"lea": "Andréa", "julie": "Julie", "samir": "Samir"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S01E05"
SOURCE_FILE = "sources/dix-pour-cent/s01/e05.fr.dual.srt"
SOURCE_NOTE = ("Cues 252-264. Spoken negations ('C'est peut-être pas', 'Je sais pas') are restored to standard A1 "
               "('Ce n'est peut-être pas', 'Je ne sais pas'); Andréa's final quip in cues 263-264 is softened for A1.")

INTRO = ("At the country hotel near the film set, Julie is resting in her room after bruising her back in the horse "
         "fall. In the corridor outside, director Samir tells Andrea that all the delays leave them no choice: they "
         "must shoot the big barn love scene tomorrow morning. When Andrea breaks the news to Julie, the actress tries "
         "to pitch a poetic alternative. Let's hear the scene in French first.")

STORY = [
 ("samir", "Avec tous ces retards, il nous reste une demi-journée dans la grange.",
  "With all these delays, we have half a day left in the barn.",
  [(252, "Avec tous ces retards, il nous reste une demi-journée dans la grange")], ""),
 ("samir", "J'ai dû réécrire le planning.",
  "I had to rewrite the schedule.",
  [(253, "J'ai dû réécrire le planning")], ""),
 ("samir", "On tourne la scène d'amour demain.",
  "We shoot the love scene tomorrow.",
  [(254, "On tourne la scène d'amour demain")], ""),
 ("lea", "Ce n'est peut-être pas le bon moment.",
  "Maybe it is not the right time.",
  [(254, "peut-être pas le bon moment")], "'C'est' -> 'Ce n'est'"),
 ("samir", "C'est demain, on n'a pas le choix!",
  "It is tomorrow, we have no choice!",
  [(255, "C'est demain, on n'a pas le choix")], ""),
 ("lea", "On va y arriver, Samir.",
  "We are going to manage, Samir.",
  [(256, "On va y arriver, Samir")], ""),
 ("samir", "Si tu le dis. Dis-le aux acteurs, je suis trop occupé.",
  "If you say so. Tell the actors, I am too busy.",
  [(256, "Si tu le dis"), (257, "Dis-le aux acteurs, je suis trop occupé")], ""),
 ("julie", "Pourquoi il y a toujours des scènes d'amour?",
  "Why are there always love scenes?",
  [(258, "Pourquoi il y a toujours des scènes d'amour")], ""),
 ("julie", "Ce serait tellement plus fort de le suggérer symboliquement.",
  "It would be so much stronger to suggest it symbolically.",
  [(259, "Ce serait tellement plus fort de le suggérer symboliquement")], ""),
 ("lea", "C'est-à-dire?",
  "Meaning what?",
  [(260, "C'est-à-dire")], ""),
 ("julie", "Je ne sais pas.",
  "I don't know.",
  [(261, "sais pas")], "Restored 'ne'"),
 ("julie", "Une rivière qui coule? Des animaux qui gambadent dans les bois?",
  "A flowing river? Animals frolicking in the woods?",
  [(262, "Une rivière qui coule"), (262, "Des animaux qui gambadent dans les bois")], ""),
 ("lea", "Oui! Le public préférerait voir des lapins dans les bois.",
  "Yes! The audience would prefer to see rabbits in the woods.",
  [(263, "Le public préférerait voir des lapins")], "Softened crude remark"),
 ("lea", "Plutôt que toi et JoeyStarr ensemble à l'écran!",
  "Rather than you and JoeyStarr together on screen!",
  [(264, "plutôt que toi et JoeyStarr")], "Softened crude verb"),
]

OPENER = "Let's go through the scene line by line and look at how each sentence works."

WALK = [
 (0, None,
  "'With all these delays, we have half a day left in the barn.' The impersonal construction literally means 'there remains to us'."),
 (1, None,
  "'I had to rewrite the schedule.' Notice the past participle of 'must' with a circumflex accent."),
 (2, None,
  "'We shoot the love scene tomorrow.' In French cinema, the verb for turning camera reels means to shoot or film."),
 (3, None,
  "'Maybe it is not the right time.' Andréa tries to buy time for her reluctant actress."),
 (4, None,
  "'It is tomorrow, we have no choice!' Samir is completely inflexible."),
 (5, None,
  "'We are going to manage, Samir.' The pronoun 'there' combines with the verb for 'arriving' to mean 'to pull it off'."),
 (6, None,
  "'If you say so. Tell the actors, I am too busy.' Samir leaves the hard conversation to the agents."),
 (7, None,
  "'Why are there always love scenes?' Inside the hotel bedroom, Julie groans at the news."),
 (8, None,
  "'It would be so much stronger to suggest it symbolically.' She argues for an artistic compromise using the conditional."),
 (9, None,
  "'Meaning what?' This hyphenated phrase literally means 'that is to say'."),
 (10, None,
  "'I don't know.' Put on the spot, Julie scrambles for an example."),
 (11, None,
  "'A flowing river? Animals frolicking in the woods?' She pitches vintage poetic cinema metaphors."),
 (12, None,
  "'Yes! The audience would prefer to see rabbits in the woods.' Andréa replies with dry, affectionate sarcasm."),
 (13, None,
  "'Rather than you and JoeyStarr together on screen!' She reminds Julie what the public really paid to see."),
]

TRANSITION = "Now let's hear the whole conversation again from start to finish."

OUTRO = ("Julie's woodland rabbits do not stand a chance against Samir's shooting schedule, and now Gabriel has to "
         "convince JoeyStarr down the hall. Remember the verb for shooting a film: to turn.")

CLOSING = ("samir", "On tourne la scène d'amour demain.")
