# Authoring module for dix-pour-cent s01e03 scene 15 (cues 340-374).
# Build: python3 tools/compose.py out/dix-pour-cent/s01e03/authoring/scene-15.py --out out/dix-pour-cent/s01e03/scene-15.json

ID = "dix-pour-cent-s01e03-scene-15"
SHOW = "dix-pour-cent"
SEASON = 1
EPISODE = 3
SCENE = 15
TITLE = "Mère et fille, trois mois  (Mother and Daughter, Three Months)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "laura": "emilie", "mathias": "theo"}
LABELS = {"lea": "Nathalie", "laura": "Laura", "mathias": "Mathias"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S01E03"
SOURCE_FILE = "sources/dix-pour-cent/s01/e03.fr.dual.srt"
SOURCE_NOTE = ("Cues 340-374. Nathalie is the viewpoint character (lea). In the second half of the scene the episode "
               "cuts between Laura with Gabriel and Nathalie with Mathias; Gabriel's question is narrated so Mathias "
               "carries the male voice.")

INTRO = ("While Colette Brancillon settles in to audit the agency's accounts, Nathalie Baye and her daughter Laura "
         "Smet arrive together at ASK and step into the lift. Both have read Solveig Akerfelt's script, and while "
         "they are face to face they pretend to be delighted. Yet the moment they step out of the lift, each "
         "actress pulls her own agent aside for a private word in his office. Listen to the French first and let "
         "the rhythm of the conversation wash over you.")

STORY = [
 ("lea", "C'est un super scénario, non?", "It's a great script, isn't it?",
  [(340, "C'est un super scénario, non")], ""),
 ("laura", "Oui, c'est fort! Mais tu n'aimes pas le froid.", "Yes, it's powerful! But you don't like the cold.",
  [(341, "C'est fort"), (343, "Tu n'aimes pas le froid")], ""),
 ("laura", "Ça ne t'inquiète pas?", "Doesn't that worry you?",
  [(343, "Ça ne t'inquiète pas")], ""),
 ("lea", "Non, ça peut créer quelque chose d'intense.", "No, it can create something intense.",
  [(344, "Non"), (344, "ça peut créer quelque chose d'intense")], ""),
 ("laura", "On est ensemble dans chaque scène. C'est beaucoup.", "We're together in every scene. That's a lot.",
  [(345, "On est ensemble dans chaque scène"), (346, "C'est beaucoup")], ""),
 ("lea", "Tiens-toi droite.", "Stand up straight.",
  [(350, "Tiens-toi")], "subtitle has masculine 'droit'; feminine 'droite' used for Laura"),
 ("mathias", "Bonjour, Nathalie. Bonjour, Laura. On y va?", "Hello, Nathalie. Hello, Laura. Shall we go?",
  [(352, "Bonjour, Nathalie"), (353, "Laura"), (354, "On y va")], ""),
 ("lea", "Mathias, je peux te voir seul d'abord?", "Mathias, can I see you alone first?",
  [(355, "Je peux te voir seul d'abord")], ""),
 ("mathias", "Bien sûr.", "Of course.",
  [(355, "Bien sûr")], ""),
 ("laura", "Tu ne connais pas ma mère. Trois mois avec elle, non!", "You don't know my mother. Three months with her, no!",
  [(358, "trois mois"), (359, "Non"), (360, "Tu ne connais pas ma mère")], "Laura in parallel to Gabriel"),
 ("lea", "Impossible! Pourquoi tu ne m'as pas prévenue?", "Impossible! Why didn't you warn me?",
  [(367, "Impossible ! Pourquoi tu ne m'as pas prévenue")], ""),
 ("mathias", "Mais vous vous entendez très bien!", "But you get on very well!",
  [(368, "vous entendre")], "'Vous semblez si bien vous entendre' simplified to present"),
 ("lea", "Oui, on s'entend bien.", "Yes, we get on well.",
  [(369, "On s'entend bien")], ""),
 ("lea", "Mais une mère et une fille seules pendant trois mois, elles vont se tuer!", "But a mother and a daughter alone for three months, they're going to kill each other!",
  [(370, "Mais une mère et une fille seules pendant trois mois, elles vont se tuer")], ""),
 ("mathias", "Mais c'est le scénario!", "But that's the script!",
  [(372, "C'est le scénario")], ""),
 ("lea", "Oui, c'est ça qui est beau. Je veux le jouer, pas le vivre!", "Yes, that's what's beautiful. I want to act it, not live it!",
  [(373, "Oui, c'est ça qui est beau. Je veux le jouer"), (374, "pas le vivre")], ""),
]

OPENER = ("Let's go through it line by line. Mother and daughter are in the lift, each waiting for the other to "
          "blink first.")

WALK = [
 (0, None,
  "'It's a great script, isn't it?' Putting the word for 'no' at the end of a statement turns it into 'isn't it?' "
  "or 'right?'."),
 (1, "Oui, c'est fort!",
  "'Yes, it's powerful!' Literally 'it is strong', a common way to praise a story or performance."),
 (1, "Mais tu n'aimes pas le froid.",
  "'But you don't like the cold.' Laura tries gently to put her mother off the shoot."),
 (2, None,
  "'Doesn't that worry you?' The little word for 'you' shrinks before the verb because the verb starts with a "
  "vowel."),
 (3, None,
  "'No, it can create something intense.' After the phrase for 'something', French always links the adjective with "
  "a short word meaning 'of'."),
 (4, None,
  "'We're together in every scene. That's a lot.' Laura tries a second hint, and still her mother doesn't budge."),
 (5, None,
  "'Stand up straight.' Literally 'hold yourself straight'. Even in the lift, Nathalie cannot stop mothering her "
  "thirty-year-old daughter."),
 (6, None,
  "'Hello, Nathalie. Hello, Laura. Shall we go?' Literally 'we go there?'. Mathias and Gabriel are waiting outside "
  "the lift."),
 (7, None,
  "'Mathias, can I see you alone first?' The phrase at the end means 'first of all'. Meanwhile Laura asks Gabriel "
  "for the exact same private chat."),
 (8, None,
  "'Of course.' Literally 'well sure'. The doors close on two separate offices."),
 (9, None,
  "'You don't know my mother. Three months with her, no!' In Gabriel's office, Laura says the verb for knowing a "
  "person. Now listen to Nathalie in Mathias's office."),
 (10, None,
  "'Impossible! Why didn't you warn me?' The past participle at the end has a feminine letter because the shortened "
  "object word before the auxiliary refers to Nathalie."),
 (11, None,
  "'But you get on very well!' Literally 'you hear each other very well'. In French, getting along with someone is "
  "understanding or hearing each other."),
 (12, None,
  "'Yes, we get on well.' Here she uses the casual word for 'we', so the verb is singular."),
 (13, None,
  "'But a mother and a daughter alone for three months, they're going to kill each other!' Near future again, with "
  "the reflexive word meaning 'each other'."),
 (14, None,
  "'But that's the script!' Mathias points out that the film is about that very tension."),
 (15, "Oui, c'est ça qui est beau.",
  "'Yes, that's what's beautiful.' Literally 'it is that which is beautiful'."),
 (15, "Je veux le jouer, pas le vivre!",
  "'I want to act it, not live it!' The verb for playing a game also means acting a role, and the little word for "
  "'it' sits in front of both verbs."),
]

TRANSITION = "Let's hear the whole scene again."

OUTRO = ("So neither mother nor daughter wants to spend three months trapped with the other, and next they have "
         "to confess it in the same room. See you in the next scene.")
CLOSING = ("laura", "Laisse tomber.")
