# Authoring module for dix-pour-cent s03e03 scene 20 (cues 1219-1230).
# Build: python3 tools/compose.py out/dix-pour-cent/s03e03/authoring/scene-20.py --out out/dix-pour-cent/s03e03/scene-20.json

ID = "dix-pour-cent-s03e03-scene-20"
SHOW = "dix-pour-cent"
SEASON = 3
EPISODE = 3
SCENE = 20
TITLE = "Envoyer à la casse  (Sent to the Scrap Heap)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "gerard": "theo"}
LABELS = {"lea": "Samy", "gerard": "Gérard"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S03E03"
SOURCE_FILE = "sources/dix-pour-cent/s03/e03.fr.dual.srt"
SOURCE_NOTE = ("Cues 1219-1230. Sitting on the curb, Gérard Lanvin confesses to Samy that he sabotaged "
               "their scene out of fear of being outshone by Samy's youth and talent. Adapted for A1 French.")

INTRO = ("Sitting together on the curb outside, Gerard Lanvin stuns Samy by revealing why their scene felt so difficult. "
         "Far from being disappointed in Samy, Gerard admits he panicked in the face of the young man's raw talent and vibrant youth. "
         "Let's listen to their conversation in French first.")

STORY = [
 ("gerard", "Les acteurs ont toujours deux grandes peurs.",
  "Actors always have two great fears.",
  [(1218, "il y a deux grandes peurs chez les acteurs.")], "Introduced common actor insecurities"),
 ("lea", "La peur de quoi, Gérard?",
  "Fear of what, Gerard?",
  [(1221, "Je comprends pas, là.")], "Inquired about actor anxieties"),
 ("gerard", "La peur d'être envoyé à la casse.",
  "The fear of being sent to the scrap heap.",
  [(1219, "Envoyer à la casse.")], "Defined fear of obsolescence"),
 ("lea", "Pourquoi vous me dites ça maintenant?",
  "Why do you tell me that now?",
  [(1221, "Je comprends pas, là.")], "Asked for clarification"),
 ("gerard", "Tu n'as pas été mauvais, Samy.",
  "You were not bad, Samy.",
  [(1222, "T'as pas été mauvais, Samy.")], "Reassured about performance"),
 ("lea", "Vous trouvez vraiment que j'étais bon?",
  "You really think that I was good?",
  [(1223, "T'as même été bon, ouais.")], "Sought validation"),
 ("gerard", "Tu as même été très bon.",
  "You were even very good.",
  [(1223, "T'as même été bon, ouais.")], "Praised acting ability"),
 ("lea", "Alors pourquoi tout s'est mal passé?",
  "Then why did everything go badly?",
  [(1224, "C'est moi qui ai rien fait pour t'aider.")], "Questioned failed scene"),
 ("gerard", "Je n'ai rien fait pour t'aider.",
  "I did nothing to help you.",
  [(1224, "C'est moi qui ai rien fait pour t'aider.")], "Admitted lack of support"),
 ("lea", "Ce n'est pas possible, Gérard!",
  "That is not possible, Gerard!",
  [(1227, "C'est complètement débile")], "Expressed disbelief"),
 ("gerard", "J'ai eu très peur de ton talent.",
  "I was very afraid of your talent.",
  [(1225, "J'ai eu peur de ton talent,")], "Confessed fear of rival talent"),
 ("lea", "Peur de moi? C'est complètement fou!",
  "Afraid of me? That is completely crazy!",
  [(1227, "C'est complètement débile, là, ce que vous m'en racontez.")], "Found confession unbelievable"),
 ("gerard", "J'ai flippé face à ta jeunesse.",
  "I freaked out facing your youth.",
  [(1225, "de ta jeunesse."), (1226, "J'ai flippé.")], "Admitted panic before youth"),
 ("lea", "Je n'arrive pas à y croire.",
  "I cannot bring myself to believe it.",
  [(1228, "Ben oui, c'est débile.")], "Struggled to absorb truth"),
]

OPENER = "Let's observe how Gerard confesses his secret fear of the raw talent of the younger actor."

WALK = [
 (0, None,
  "'Actors always have two great fears.' A general observation on professional artistic insecurity."),
 (1, None,
  "'Fear of what, Gerard?' A direct question prompting an honest explanation."),
 (2, None,
  "'The fear of being sent to the scrap heap.' A vivid idiom describing anxiety over career obsolescence."),
 (3, None,
  "'Why do you tell me that now?' An intrigued inquiry seeking clarification of his motives."),
 (4, None,
  "'You were not bad, Samy.' A reassuring negation correcting his false impression."),
 (5, None,
  "'You really think that I was good?' A hopeful question seeking genuine validation."),
 (6, None,
  "'You were even very good.' An emphatic confirmation offering sincere artistic praise."),
 (7, None,
  "'Then why did everything go badly?' A logical question pressing for the root problem."),
 (8, None,
  "'I did nothing to help you.' A candid admission taking personal responsibility."),
 (9, None,
  "'That is not possible, Gerard!' An incredulous exclamation refusing to blame his mentor."),
 (10, None,
  "'I was very afraid of your talent.' A courageous confession revealing deep professional vulnerability."),
 (11, None,
  "'Afraid of me? That is completely crazy!' An astonished reaction marveling at the star's insecurity."),
 (12, None,
  "'I freaked out facing your youth.' A colloquial admission acknowledging fear of aging."),
 (13, None,
  "'I cannot bring myself to believe it.' A stunned expression absorbing the surprising revelation."),
]

TRANSITION = "Now let's listen to Gerard and Samy again at normal speed."

OUTRO = ("Gerard's honest confession breaks down the barrier between seasoned movie star and anxious newcomer. "
         "Freed from self-doubt, Samy realizes that vulnerability and fear touch even the greatest actors in French cinema.")

CLOSING = ("gerard", "La vérité fait du bien, Samy.")
