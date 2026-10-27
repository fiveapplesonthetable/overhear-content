# Authoring module for dix-pour-cent s01e04 scene 11 (cues 291-309).
# Build: python3 tools/compose.py out/dix-pour-cent/s01e04/authoring/scene-11.py --out out/dix-pour-cent/s01e04/scene-11.json

ID = "dix-pour-cent-s01e04-scene-11"
SHOW = "dix-pour-cent"
SEASON = 1
EPISODE = 4
SCENE = 11
TITLE = "Un monstre de séduction  (A Monster of Seduction)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "clementine": "emilie"}
LABELS = {"lea": "Andréa", "clementine": "Clémentine"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S01E04"
SOURCE_FILE = "sources/dix-pour-cent/s01/e04.fr.dual.srt"
SOURCE_NOTE = ("Cues 291-309. Only two female voices exist (lucie and emilie), so Colette's brief farewell in cue 308 "
               "is narrated. Clémentine's literary insults (297, 303) and Andréa's slang in 306 are simplified to "
               "clean A1 French.")

INTRO = ("Inside the clothes shop, Andréa has just tried to invite the tax inspector Colette Brancillon to dinner, "
         "and Colette coolly replied that she can read Andréa's lonely life — and her many short-lived girlfriends "
         "— right in her expense receipts. Andréa denied everything. Yet the moment the two women step out onto the "
         "pavement, Andréa's dramatic ex-girlfriend Clémentine ambushes her right in front of Colette. Listen to "
         "the French first, without worrying about catching every word.")

STORY = [
 ("lea", "Clémentine! Qu'est-ce que tu fais ici?", "Clémentine! What are you doing here?",
  [(291, "Clémentine ! Qu'est-ce que tu")], "interrupted question completed"),
 ("clementine", "Je dois faire ça pour guérir.", "I have to do this in order to heal.",
  [(292, "Je dois faire ça pour guérir")], ""),
 ("lea", "D'accord, mais une autre fois!", "Okay, but another time!",
  [(293, "mais une autre fois")], "'Soit' -> 'D'accord'"),
 ("clementine", "Tu es un monstre de séduction.", "You're a monster of seduction.",
  [(294, "Tu es un monstre de séduction")], ""),
 ("lea", "Clémentine, écoute.", "Clémentine, listen.",
  [(295, "Clémentine, écoute")], ""),
 ("clementine", "Tu m'as dévorée comme une hyène!", "You devoured me like a hyena!",
  [(296, "Tu m'as dévorée comme une hyène")], ""),
 ("lea", "C'est ridicule. Ça n'a pas duré un mois!", "That's ridiculous. It didn't last a month!",
  [(298, "C'est ridicule"), (299, "Ça n'a pas duré un mois")], ""),
 ("clementine", "Je parle de sentiments! J'avais des sentiments pour toi.", "I'm talking about feelings! I had feelings for you.",
  [(299, "Je parle de sentiments"), (300, "J'avais des sentiments pour toi")], ""),
 ("clementine", "Et tu as demandé à ton assistante de me quitter!", "And you asked your assistant to break up with me!",
  [(301, "et tu as demandé à ton")], "'assistant' -> feminine 'assistante'; slang 'larguer' -> 'quitter'"),
 ("lea", "Non, c'est faux!", "No, that's not true!",
  [(302, "Non, c'est faux")], ""),
 ("clementine", "Tu es pourrie! Mais c'est fini.", "You're rotten! But it's over.",
  [(302, "Pourri")], "feminine 'pourrie' for Andréa; cue 303 simplified"),
 ("clementine", "Je te pardonne.", "I forgive you.",
  [(305, "Je te pardonne")], ""),
 ("lea", "Tu as besoin d'un nouveau médecin, tu es folle!", "You need a new doctor, you're crazy!",
  [(306, "besoin d'un nouveau")], "'psy, espèce de cinglé' softened to A1"),
 ("lea", "Les gens sont malades, non?", "People are crazy, aren't they?",
  [(307, "Les gens sont malades")], "'hein' -> 'non'"),
 ("lea", "Oui? Allô?", "Yes? Hello?",
  [(309, "Oui")], "answering her phone after Colette walks off"),
]

OPENER = ("Let's walk through it line by line. Andréa steps out of the shop with Colette and walks straight into "
          "Clémentine.")

WALK = [
 (0, None,
  "'Clémentine! What are you doing here?' The long question phrase after Clémentine's name is the everyday spoken "
  "way to ask 'what'."),
 (1, None,
  "'I have to do this in order to heal.' The first verb means 'must' or 'have to', and the preposition before "
  "'heal' means 'in order to'."),
 (2, None,
  "'Okay, but another time!' Andréa desperately wants to get rid of her before Colette hears too much."),
 (3, None,
  "'You're a monster of seduction.' Clémentine is an actress, and she delivers her speech as if she were on stage."),
 (4, None,
  "'Clémentine, listen.' A casual command for one person, with no pronoun."),
 (5, None,
  "'You devoured me like a hyena!' The past participle has an extra feminine letter at the end because the object "
  "word before the auxiliary refers to Clémentine."),
 (6, None,
  "'That's ridiculous. It didn't last a month!' The two-part negative wraps around the auxiliary verb in the past."),
 (7, None,
  "'I'm talking about feelings! I had feelings for you.' The second verb is in the past form used for how things "
  "used to be."),
 (8, None,
  "'And you asked your assistant to break up with me!' Listeners who remember the first episode know that this is "
  "completely true: Andréa made poor Camille do it."),
 (9, None,
  "'No, that's not true!' Literally 'it is false', with Colette standing right there listening to every word."),
 (10, None,
  "'You're rotten! But it's over.' Clémentine's grand tragedy reaches its climax."),
 (11, None,
  "'I forgive you.' The little object word for 'you' sits right in front of the verb. Having delivered her big "
  "forgiveness line, Clémentine stalks away."),
 (12, None,
  "'You need a new doctor, you're crazy!' Literally 'you have need of a new doctor', and the adjective at the end "
  "is the feminine form of 'crazy'."),
 (13, None,
  "'People are crazy, aren't they?' Literally 'people are sick, no?'. Andréa turns to Colette with an awkward "
  "smile, but Colette simply bids Ms Martel a polite goodbye and walks off."),
 (14, None,
  "'Yes? Hello?' Saved by the bell, Andréa answers her ringing phone."),
]

TRANSITION = "Now let's hear the whole scene again from start to finish."

OUTRO = ("So much for convincing Colette that she doesn't have a string of ex-girlfriends. Back at the agency, "
         "Audrey Fleurot is arriving for her meeting with Augustin. See you in the next scene.")
CLOSING = ("lea", "Merci, au revoir.")
