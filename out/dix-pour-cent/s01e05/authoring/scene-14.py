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
  "Samir explains the crunch: with all these delays, we have half a day left in the barn. The impersonal construction "
  "literally says there remains to us."),
 (1, None,
  "He adds that he had to rewrite the schedule. Notice the past participle of the verb must with a circumflex accent on "
  "the vowel."),
 (2, None,
  "Then he drops the bombshell: we shoot the love scene tomorrow. In French cinema, the verb for turning a camera reels "
  "means to shoot or film."),
 (3, None,
  "Thinking of how tense Julie and JoeyStarr still are, Andrea replies cautiously: maybe it is not the right time."),
 (4, None,
  "Samir is inflexible: it is tomorrow, we have no choice!"),
 (5, None,
  "Andrea tries to reassure him: we are going to manage, Samir. The pronoun for there combines with the verb for arriving "
  "to mean to manage or pull it off."),
 (6, None,
  "Samir shrugs — if you say so — and leaves the hard part to her: tell the actors, I am too busy."),
 (7, None,
  "Inside the hotel room, Julie groans at the news and asks: why are there always love scenes?"),
 (8, None,
  "She argues that it would be so much stronger to suggest it symbolically, using the conditional form of to be."),
 (9, None,
  "Andrea raises an eyebrow and asks: meaning what? This hyphenated phrase literally means that is to say."),
 (10, None,
  "Put on the spot, Julie says: I do not know."),
 (11, None,
  "Then she pitches old-fashioned cinema metaphors: a flowing river, or animals frolicking in the woods?"),
 (12, None,
  "Andrea answers with dry sarcasm: yes, the audience would prefer to see rabbits in the woods!"),
 (13, None,
  "And she finishes the thought: rather than you and JoeyStarr together on screen!"),
]

TRANSITION = "Now let's hear the whole conversation again from start to finish."

OUTRO = ("Julie's woodland rabbits do not stand a chance against Samir's shooting schedule, and now Gabriel has to "
         "convince JoeyStarr down the hall. Remember the verb for shooting a film: to turn.")

CLOSING = ("samir", "On tourne la scène d'amour demain.")
