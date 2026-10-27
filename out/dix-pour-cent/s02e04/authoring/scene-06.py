# Authoring module for dix-pour-cent s02e04 scene 06 (cues 137-173).
# Build: python3 tools/compose.py out/dix-pour-cent/s02e04/authoring/scene-06.py --out out/dix-pour-cent/s02e04/scene-06.json

ID = "dix-pour-cent-s02e04-scene-06"
SHOW = "dix-pour-cent"
SEASON = 2
EPISODE = 4
SCENE = 6
TITLE = "La confession d'Andréa  (Andréa's Confession)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "gabriel": "theo"}
LABELS = {"lea": "Andréa", "gabriel": "Gabriel"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S02E04"
SOURCE_FILE = "sources/dix-pour-cent/s02/e04.fr.dual.srt"
SOURCE_NOTE = ("Cues 137-173. Following Hicham's departure, a visibly stressed Andréa confesses to Gabriel "
               "that she had an unexpected encounter with Hicham after a wild night out with Aymeline Val. "
               "Adapted for A1 French.")

INTRO = ("Alone in Gabriel's office, Gabriel asks Andrea why she seemed so unnerved by Hicham's presence. "
         "Andrea drops her guard and confesses a shocking secret that leaves Gabriel stunned and amused. "
         "Let's listen to the scene in French first.")

STORY = [
 ("gabriel", "Ça va? Tu avais l'air tendue.",
  "Are you okay? You seemed tense.",
  [(137, "Ça va ?"), (138, "Tu avais l'air tendu.")], "Gabriel asks gently"),
 ("lea", "Je ne supporte pas ses ordres.",
  "I cannot stand his orders.",
  [(139, "Je ne supporte pas qu'il me donne des ordres.")], "Andrea vents her frustration"),
 ("gabriel", "Il ne peut pas nous virer.",
  "He cannot fire us.",
  [(141, "C'est pas comme s'il pouvait nous virer")], "Gabriel reassures her"),
 ("lea", "Je ne vais pas m'aplatir.",
  "I will not bow down.",
  [(143, "Je ne vais pas m'aplatir devant lui.")], "Andrea insists on dignity"),
 ("gabriel", "C'est à cause d'Aymeline Val?",
  "Is it because of Aymeline Val?",
  [(147, "C'est à cause d'Aymeline Val ?")], "Gabriel guesses"),
 ("gabriel", "Est-ce qu'il a couché avec elle?",
  "Did he sleep with her?",
  [(148, "Il l'a eue ?")], "Gabriel asks"),
 ("lea", "On a couché tous les deux, ensemble.",
  "We both slept together, the two of us.",
  [(149, "On l'a eue tous les deux, ensemble.")], "Andrea drops the bombshell"),
 ("gabriel", "Non, ce n'est pas vrai!",
  "No, that is not true!",
  [(150, "Non... Non, c'est pas vrai.")], "Gabriel is in disbelief"),
 ("lea", "C'était une erreur, il m'a provoquée.",
  "It was a mistake, he provoked me.",
  [(151, "C'était une erreur."), (153, "Il m'a provoqué.")], "Andrea defends herself"),
 ("gabriel", "Tu couches avec des hommes maintenant?",
  "You sleep with men now?",
  [(164, "tu couches avec des hommes ?")], "Gabriel teases her"),
 ("lea", "Non, c'était une petite exception.",
  "No, it was a tiny exception.",
  [(158, "Non, c'était une exception.")], "Andrea denies any change"),
 ("gabriel", "Alors, c'était comment avec Hicham?",
  "So, what was it like with Hicham?",
  [(168, "C'était comment ?")], "Gabriel inquires mischievously"),
 ("lea", "C'était très lourd et poilu!",
  "It was very heavy and hairy!",
  [(169, "Lourd et poilu.")], "Andrea delivers her punchline"),
]

OPENER = "Let's examine Andrea's surprising confession step by step to appreciate the comic banter between the two friends."

WALK = [
 (0, None,
  "'Are you okay? You seemed tense.' Gabriel checks in on his visibly agitated colleague."),
 (1, None,
  "'I cannot stand his orders.' Andrea explains that she rebels instinctively against Hicham's bossy attitude."),
 (2, None,
  "'He cannot fire us.' Gabriel reminds her that their client relationships make them irreplaceable at the agency."),
 (3, None,
  "'I will not bow down.' Andrea refuses to flatter the boss or show weakness."),
 (4, None,
  "'Is it because of Aymeline Val?' Gabriel suspects the tension relates to their shared client Aymeline."),
 (5, None,
  "'Did he sleep with her?' Gabriel bluntly asks if Hicham scored with the model."),
 (6, None,
  "'We both slept together, the two of us.' Andrea reveals that she and Hicham had a three-way encounter."),
 (7, None,
  "'No, that is not true!' Gabriel reacts with sheer astonishment and shock."),
 (8, None,
  "'It was a mistake, he provoked me.' Andrea rationalizes the incident as a competitive reaction after being challenged."),
 (9, None,
  "'You sleep with men now?' Gabriel playfully teases Andrea about her sudden departure from her usual dating preferences."),
 (10, None,
  "'No, it was a tiny exception.' Andrea insists the one-night stand was completely out of character."),
 (11, None,
  "'So, what was it like with Hicham?' Gabriel cannot resist probing for funny personal details."),
 (12, None,
  "'It was very heavy and hairy!' Andrea's candid summary leaves Gabriel in stitches."),
]

TRANSITION = "Now let's listen to the scene once more from start to finish."

OUTRO = ("Andrea's hilarious confession strengthens the bond of trust between Gabriel and her, "
         "even as the workplace dynamics become delightfully chaotic. "
         "Let's review the conversational expressions and vocabulary from this scene.")

CLOSING = ("lea", "C'était très lourd et poilu!")
