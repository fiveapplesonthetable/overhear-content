# Authoring module for dix-pour-cent s04e02 scene 11 (cues 611-640).
# Build: python3 tools/compose.py overhear-content/out/dix-pour-cent/s04e02/authoring/scene-11.py --out overhear-content/out/dix-pour-cent/s04e02/scene-11.json

ID = "dix-pour-cent-s04e02-scene-11"
SHOW = "dix-pour-cent"
SEASON = 4
EPISODE = 2
SCENE = 11
TITLE = "Chez Madame Bonnero  (At Madame Bonnero's)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "bonnero": "emilie"}
LABELS = {"lea": "Andréa", "bonnero": "Madame Bonnero"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S04E02"
SOURCE_FILE = "sources/dix-pour-cent/s04/e02.fr.dual.srt"
SOURCE_NOTE = ("Cues 611-640. Andrea visits Dany Boon's mother, Madame Bonnero, "
               "in Bergues to preserve the agency's bond with the star.")

INTRO = ("Arriving in the northern town of Bergues, Andrea pays an unexpected visit to Dany Boon's mother, Madame Bonnero. "
         "Andrea hopes to preserve the agency's bond with the star, but Madame Bonnero insists on hospitality first. "
         "Let's listen to their conversation in French first.")

OPENER = "Let's examine the conversation line by line and explore the French expressions."
TRANSITION = "Now let's listen to the complete discussion once more to reinforce the vocabulary."

STORY = [
 ("lea", "Bonjour, je cherche Madame Bonnero.",
  "Hello, I am looking for Madame Bonnero.",
  [(611, "Mme Bonnero")], "Greeting mother"),
 ("bonnero", "Oui, c'est moi, qui êtes-vous?",
  "Yes, that is me, who are you?",
  [(611, "Mme Bonnero")], "Inquiring identity"),
 ("lea", "Je viens vous parler de Dany.",
  "I come to speak with you about Dany.",
  [(612, "Je viens vous parler de Dany")], "Stating purpose"),
 ("bonnero", "Je ne parle jamais aux journalistes.",
  "I never talk to journalists.",
  [(613, "Je ne suis pas journaliste")], "Rejecting press"),
 ("lea", "Je ne suis pas une journaliste!",
  "I am not a journalist!",
  [(613, "Je ne suis pas journaliste")], "Denying journalism"),
 ("bonnero", "Qui êtes-vous alors, jeune femme?",
  "Who are you then, young woman?",
  [(613, "Je ne suis pas journaliste")], "Demanding explanation"),
 ("lea", "Entrons, je vous explique tout.",
  "Let's go in, I explain everything.",
  [(616, "je vous explique tout")], "Entering house"),
 ("bonnero", "Venez dans ma cuisine chaleureuse.",
  "Come into my warm kitchen.",
  [(616, "je vous explique tout")], "Inviting inside"),
 ("lea", "Chez ASK, on connaît bien Dany.",
  "At ASK, we know Dany well.",
  [(617, "Chez ASK, on connaît bien Dany")], "Praising bond"),
 ("bonnero", "Mathias s'occupait toujours de lui.",
  "Mathias always took care of him.",
  [(619, "Comme sa famille")], "Mentioning Mathias"),
 ("lea", "Mathias a abandonné le navire.",
  "Mathias abandoned ship.",
  [(627, "abandonné le navire")], "Revealing departure"),
 ("bonnero", "Prenez le temps et mangez bien.",
  "Take the time and eat well.",
  [(634, "mangez bien")], "Offering meal"),
 ("lea", "Je veux bien prendre mon temps.",
  "I really want to take my time.",
  [(638, "prendre mon temps")], "Accepting hospitality"),
 ("bonnero", "Alors, qu'est-ce qu'on mange ensemble?",
  "So, what do we eat together?",
  [(640, "Qu'est-ce qu'on mange")], "Serving food"),
]

WALK = [
 (0, None,
  "'Hello, I am looking for Madame Bonnero.' Andrea arrives at the front door. "
  "The verb 'chercher' means to look for someone or something."),
 (1, None,
  "'Yes, that is me, who are you?' Madame Bonnero greets the visitor cautiously. "
  "The tonic pronoun 'moi' is used after c'est."),
 (2, None,
  "'I come to speak with you about Dany.' Andrea states the reason for her trip. "
  "The verb 'venir' is followed by an infinitive to express purpose."),
 (3, None,
  "'I never talk to journalists.' Madame Bonnero expresses her distrust of the media. "
  "The negative adverb 'jamais' indicates not at any time."),
 (4, None,
  "'I am not a journalist!' Andrea clarifies her professional background. "
  "The feminine indefinite article 'une' agrees with journaliste."),
 (5, None,
  "'Who are you then, young woman?' Madame Bonnero asks for her true identity. "
  "The adverb 'alors' marks a logical transition."),
 (6, None,
  "'Let's go in, I explain everything.' Andrea suggests talking inside. "
  "The imperative 'entrons' proposes entering together."),
 (7, None,
  "'Come into my warm kitchen.' Madame Bonnero welcomes Andrea into her home. "
  "The adjective 'chaleureuse' describes a welcoming atmosphere."),
 (8, None,
  "'At ASK, we know Dany well.' Andrea underscores the agency's closeness with the star. "
  "The preposition 'chez' denotes at the premises of."),
 (9, None,
  "'Mathias always took care of him.' Madame Bonnero remembers the former agent fondly. "
  "The reflexive verb 's'occuper de' means to look after someone."),
 (10, None,
  "'Mathias abandoned ship.' Andrea uses a vivid metaphor for his sudden departure. "
  "The noun 'navire' evokes a seafaring vessel."),
 (11, None,
  "'Take the time and eat well.' Madame Bonnero dispenses motherly wisdom. "
  "The imperative 'prenez' encourages slowing down."),
 (12, None,
  "'I really want to take my time.' Andrea accepts the pause from agency stress. "
  "The phrase 'prendre son temps' means to unhurry."),
 (13, None,
  "'So, what do we eat together?' Madame Bonnero prepares a generous northern meal. "
  "The interrogative pronoun 'qu'est-ce que' asks about the food."),
]

OUTRO = ("Andrea discovers the generous hospitality of Dany Boon's mother in Bergues. "
         "By sharing a simple meal, she begins rebuilding trust to protect the agency. "
         "Now, let's review the scene one last time.")

CLOSING = ("bonnero", "Alors, qu'est-ce qu'on mange ensemble?")
