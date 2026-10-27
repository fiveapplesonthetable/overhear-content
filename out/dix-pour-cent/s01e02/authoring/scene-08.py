# Authoring module for dix-pour-cent s01e02 scene 08 (cues 244-262, with merged scene 07 = cues 239-243 in the bridge).
# Build: python3 tools/compose.py out/dix-pour-cent/s01e02/authoring/scene-08.py --out out/dix-pour-cent/s01e02/scene-08.json

ID = "dix-pour-cent-s01e02-scene-08"
SHOW = "dix-pour-cent"
SEASON = 1
EPISODE = 2
SCENE = 8
TITLE = "Rencontre à la photocopieuse  (A Meeting at the Photocopier)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "hippolyte": "theo"}
LABELS = {"lea": "Camille", "hippolyte": "Hippolyte"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S01E02"
SOURCE_FILE = "sources/dix-pour-cent/s01/e02.fr.dual.srt"

INTRO = ("Back at the agency, Camille is in trouble again. She had sent Françoise Fabian a green shawl as a gift, "
         "not knowing that actresses think green brings bad luck. She raced across Paris on a hired bike to get it back, "
         "but Françoise had already thrown it in the bin, and it was expensive, too. "
         "Andréa's answer was short: go and do some photocopies. Lots of photocopies. "
         "So now Camille is alone with the photocopier, it jams, and she mutters something rude at it. "
         "Just then a young man strolls in, very relaxed, and very sure of himself. "
         "You'll hear their little conversation in French first. Don't chase every word; just follow who wants what.")

STORY = [
 ("hippolyte", "Bonjour. Tout va bien?", "Hello. Everything okay?",
  [(245, "Bonjour"), (246, "Tout va bien")], ""),
 ("lea", "Bonjour. Il fait des caprices.", "Hello. It's playing up.",
  [(245, "Bonjour"), (247, "Il fait des caprices")], "'il' = the photocopier"),
 ("hippolyte", "Non, il marche très bien.", "No, it's working fine.",
  [(248, "Non, il marche très bien")], ""),
 ("hippolyte", "Le contraste est vraiment bon.", "The contrast is really good.",
  [(249, "Le contraste est vraiment bon")], "he looks at her copies like a photographer"),
 ("hippolyte", "Tu es Camille, c'est ça?", "You're Camille, right?",
  [(250, "Tu es Camille, c'est ça")], ""),
 ("lea", "Oui. Tu travailles ici?", "Yes. Do you work here?",
  [(251, "Oui"), (252, "Tu travailles ici")], "speaker of cue 252 not marked; given to Camille"),
 ("lea", "Je ne t'ai jamais vu.", "I've never seen you.",
  [(253, "Je ne t'ai jamais vu")], "the subtitle writes 'vue'; Camille is speaking to a man, so 'vu'"),
 ("hippolyte", "Je suis acteur. Hippolyte Rivière.", "I'm an actor. Hippolyte Rivière.",
  [(253, "Je suis acteur"), (254, "Hippolyte Rivière")], ""),
 ("hippolyte", "Tu ne m'as pas vu dans les fichiers d'Andréa?", "Haven't you seen me in Andréa's files?",
  [(254, "Tu ne m'as pas vu dans les fichiers d'Andréa")], ""),
 ("lea", "Si. Tu as rendez-vous?", "Yes, I have. Do you have an appointment?",
  [(255, "Si. Tu as rendez-vous")], ""),
 ("hippolyte", "Non, mais je suis content d'être venu.", "No, but I'm glad I came.",
  [(256, "Non, mais je suis content d'être venu")], ""),
 ("lea", "Qu'est-ce que je peux faire pour vous?", "What can I do for you?",
  [(257, "Qu'est-ce que je peux faire pour vous")], "Camille switches to the professional 'vous'"),
 ("hippolyte", "Commence par te détendre.", "Start by relaxing.",
  [(258, "Commence par te détendre")], ""),
 ("hippolyte", "Tu viens prendre un café en terrasse?", "Will you come for a coffee on the terrace?",
  [(259, "prendre un café en terrasse")], "'Et viens' -> 'Tu viens'"),
 ("lea", "Je suis occupée. Il faut un rendez-vous.", "I'm busy. You need an appointment.",
  [(260, "Je suis occupée. Il faut un rendez-vous")], ""),
 ("hippolyte", "Eh bien... merci quand même.", "Well... thanks anyway.",
  [(261, "Eh bien... merci quand même")], ""),
 ("lea", "Bonne journée.", "Have a nice day.",
  [(262, "Bonne journée")], "speaker not marked; given to Camille, who gets the last word"),
]

OPENER = ("Let's go through it slowly. The young man walks in and checks on her with a friendly, everyday question.")

WALK = [
 (0, "Tout va bien?",
  "'Everything okay?' Literally 'all goes well?'. You can ask it of a friend, a colleague, or someone fighting with a machine."),
 (1, "Il fait des caprices.",
  "'It's playing up.' Word for word: it is throwing tantrums. In French a machine is a 'he' or a 'she', never an 'it'. "
  "The photocopier is masculine, so it's 'he'."),
 (2, None,
  "'No, it's working fine.' The verb here is 'to walk', which in French also means 'to work', for machines and for plans. "
  "Then he looks at her copies like an art critic."),
 (3, None,
  "'The contrast is really good.' It's a joke, of course: he's flirting. And he already knows who she is."),
 (4, None,
  "'You're Camille, right?' The tag at the end, literally 'it's that?', turns any sentence into a check. "
  "He uses the casual 'you' straight away, which is very him."),
 (5, None,
  "'Yes. Do you work here?' She answers in the casual form too. A question can be just a sentence with a rising voice."),
 (6, None,
  "'I've never seen you.' The negative is wrapped around the helper verb: not, have, never, then 'seen'. "
  "The little word for 'you' loses its vowel before the verb."),
 (7, None,
  "'I'm an actor. Hippolyte Rivière.' Notice: no word for 'an'. For a job, French just says 'I am actor'."),
 (8, None,
  "'Haven't you seen me in Andréa's files?' A negative question. And now listen to how Camille answers it."),
 (9, "Si.",
  "'Yes, I have.' This is a special yes. When someone asks a negative question and you want to say 'yes, actually', "
  "you don't use the normal word for yes, you use this one. It means 'oh yes I did'."),
 (9, "Tu as rendez-vous?",
  "'Do you have an appointment?' Very assistant-like. She knows the rules now."),
 (10, None,
  "'No, but I'm glad I came.' The word for 'glad' is in the masculine form, because he is a man. Camille stays professional."),
 (11, None,
  "'What can I do for you?' Listen: now she switches to the polite 'you'. It's her way of keeping him at arm's length. "
  "He doesn't take the hint."),
 (12, None,
  "'Start by relaxing.' A casual command: start, then 'by relaxing yourself'."),
 (13, None,
  "'Will you come for a coffee on the terrace?' The French love a coffee outside at a little café table. "
  "And Camille gives the answer Andréa taught her."),
 (14, "Je suis occupée.",
  "'I'm busy.' Here the word for 'busy' has a feminine ending, because Camille is a woman."),
 (14, "Il faut un rendez-vous.",
  "'You need an appointment.' This phrase means 'it is necessary', 'one needs'. Put a thing after it, or a verb, "
  "and you have a rule. He takes it well."),
 (15, None,
  "'Well... thanks anyway.' The last two words mean 'all the same', a polite way to accept a no."),
 (16, None,
  "'Have a nice day.' Camille's last word, polite and a little cool. But something tells us we'll see him again."),
]

TRANSITION = "Right, let's hear them once more, start to finish."

OUTRO = ("That was a nice one to finish on. Keep your ears open for that special yes when you watch, "
         "and I'll see you next time.")
CLOSING = ("lea", "À bientôt!")
