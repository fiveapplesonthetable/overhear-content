# Authoring module for dix-pour-cent s03e05 scene 01 (cues 1-24).
# Build: python3 tools/compose.py out/dix-pour-cent/s03e05/authoring/scene-01.py --out out/dix-pour-cent/s03e05/scene-01.json

ID = "dix-pour-cent-s03e05-scene-01"
SHOW = "dix-pour-cent"
SEASON = 3
EPISODE = 5
SCENE = 1
TITLE = "Le tournage de Béatrice  (Béatrice's Shoot)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "maquilleuse": "emilie"}
LABELS = {"lea": "Béatrice", "maquilleuse": "Maquilleuse"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S03E05"
SOURCE_FILE = "sources/dix-pour-cent/s03/e05.fr.dual.srt"
SOURCE_NOTE = ("Cues 1-24. Béatrice Dalle is exhausted after 27 takes on set, then suspects the director wants her naked in a body bag. Adapted for A1 French.")

INTRO = ("On a grueling movie set, iconic actress Beatrice Dalle catches her breath after twenty-seven exhausting takes. "
         "When the makeup artist insists on applying full-body makeup for a body bag scene, Beatrice suspects director Pascal of bad faith. "
         "Let's listen to the scene in French first.")

STORY = [
 ("lea", "Ce tournage est particulièrement rude aujourd'hui.",
  "This shoot is particularly rough today.",
  [(9, "C'est rude, 27 prises")], "Complained about grueling shoot"),
 ("maquilleuse", "Vous avez fait vingt-sept prises difficiles.",
  "You did twenty-seven difficult takes.",
  [(9, "C'est rude, 27 prises")], "Acknowledged physical strain"),
 ("lea", "J'ai défoncé cette porte vingt-sept fois!",
  "I smashed through that door twenty-seven times!",
  [(10, "27 fois, j'ai défoncé cette")], "Described physical stunts"),
 ("maquilleuse", "Il faut préparer la scène suivante.",
  "We must prepare the next scene.",
  [(16, "ce serait bien qu'on y aille")], "Called actor to next setup"),
 ("lea", "J'ai encore quelques minutes de repos.",
  "I still have a few minutes of rest.",
  [(17, "On a le temps")], "Requested brief pause"),
 ("maquilleuse", "Nous devons maquiller tout votre corps.",
  "We have to do your whole body with makeup.",
  [(19, "on a tout le corps à faire")], "Announced full-body cosmetics"),
 ("lea", "C'est la scène de la mort?",
  "Is this the death scene?",
  [(20, "C'est la scène de la mort, oui ?")], "Asked about scene context"),
 ("maquilleuse", "Oui, exactement, c'est cette scène.",
  "Yes, exactly, it is that scene.",
  [(21, "Bah oui")], "Confirmed mortuary scene"),
 ("lea", "Mais mon personnage est dans un sac!",
  "But my character is inside a bag!",
  [(22, "Mais je suis dans un sac")], "Questioned necessity of body makeup"),
 ("maquilleuse", "Pascal a demandé un maquillage complet.",
  "Pascal asked for full-body makeup.",
  [(23, "Pascal m'a dit maquillage corps entier")], "Cited director's instructions"),
 ("lea", "Pourquoi maquiller mon corps entier?",
  "Why put makeup on my entire body?",
  [(23, "Pascal m'a dit maquillage corps entier")], "Expressed growing suspicion"),
 ("maquilleuse", "Je ne sais pas, ce sont les ordres.",
  "I do not know, these are orders.",
  [(23, "Pascal m'a dit maquillage corps entier")], "Deflected editorial responsibility"),
 ("lea", "Pascal prépare une mauvaise surprise.",
  "Pascal is preparing a nasty surprise.",
  [(24, "je ressens pas cet embrouille")], "Voiced mistrust of director"),
 ("maquilleuse", "Venez vous installer au maquillage.",
  "Come and sit down in makeup.",
  [(16, "ce serait bien qu'on y aille")], "Encouraged backstage preparation"),
]

OPENER = "Let's observe as Beatrice discusses the unexpected body makeup on set."

WALK = [
 (0, None,
  "'This shoot is particularly rough today.' In spoken French, the little word before 'filming' drops its final vowel and attaches with an apostrophe. In spoken French, the little word before 'filming' drops its final vowel and attaches with an apostrophe."),
 (1, None,
  "'You did twenty-seven difficult takes.' Maquilleuse uses the polite 'you' form alongside 'have' to keep a respectful professional tone. Maquilleuse uses the polite 'you' form alongside 'have' to keep a respectful professional tone."),
 (2, None,
  "'I smashed through that door twenty-seven times!' Notice how 'have' leads directly into the noun meaning 'door'. Notice how 'have' leads directly into the noun meaning 'door'."),
 (3, None,
  "'We must prepare the next scene.' The verb meaning 'is necessary' pairs naturally with the noun for 'scene' in everyday conversation."),
 (4, None,
  "'I still have a few minutes of rest.' Notice how 'have' leads directly into the noun meaning 'minutes'. Notice how 'have' leads directly into the noun meaning 'minutes'."),
 (5, None,
  "'We have to do your whole body with makeup.' A surprising procedural instruction announcing extensive cosmetics. Maquilleuse uses the polite 'you' form alongside 'must' to keep a respectful professional tone."),
 (6, None,
  "'Is this the death scene?' The key noun here means 'scene', anchored by its matching French article. The key noun here means 'scene', anchored by its matching French article."),
 (7, None,
  "'Yes, exactly, it is that scene.' The key noun here means 'scene', anchored by its matching French article. The key noun here means 'scene', anchored by its matching French article."),
 (8, None,
  "'But my character is inside a bag!' A logical objection protesting unnecessary body cosmetics. The key noun here means 'character', anchored by its matching French article."),
 (9, None,
  "'Pascal asked for full-body makeup.' A direct quote attributing the directive to the movie director. This conversational past tense combines a helper verb with the past participle for 'asked'."),
 (10, None,
  "'Why put makeup on my entire body?' Notice how 'to put makeup on' leads directly into the noun meaning 'body'. Notice how 'to put makeup on' leads directly into the noun meaning 'body'."),
 (11, None,
  "'I do not know, these are orders.' A neutral disavowal reflecting crew hierarchy. The verb meaning 'know' pairs naturally with the noun for 'orders' in everyday conversation."),
 (12, None,
  "'Pascal is preparing a nasty surprise.' A perceptive suspicion detecting an unscripted nude scene. The verb meaning 'is preparing' pairs naturally with the noun for 'unexpected event' in everyday conversation."),
 (13, None,
  "'Come and sit down in makeup.' Maquilleuse uses the polite 'you' form alongside 'come' to keep a respectful professional tone. Maquilleuse uses the polite 'you' form alongside 'come' to keep a respectful professional tone."),
]

TRANSITION = "Now let's listen to Beatrice and the makeup artist again at full speed."

OUTRO = ("Convinced that director Pascal intends to film her unclothed without prior consent, Beatrice heads backstage. "
         "Determined not to let the production compromise her boundaries, she reaches for her phone to call her agent.")

CLOSING = ("lea", "Je vais régler cette histoire immédiatement.")
