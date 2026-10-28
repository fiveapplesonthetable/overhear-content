# Authoring module for dix-pour-cent s03e06 scene 01 (cues 1-127).
# Build: python3 tools/compose.py out/dix-pour-cent/s03e06/authoring/scene-01.py --out out/dix-pour-cent/s03e06/scene-01.json

ID = "dix-pour-cent-s03e06-scene-01"
SHOW = "dix-pour-cent"
SEASON = 3
EPISODE = 6
SCENE = 1
TITLE = "Le coupable démasqué  (The Culprit Unmasked)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "mathias": "theo", "hicham": "marcel"}
LABELS = {"lea": "Andréa", "mathias": "Mathias", "hicham": "Hicham"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S03E06"
SOURCE_FILE = "sources/dix-pour-cent/s03/e06.fr.dual.srt"
SOURCE_NOTE = ("Cues 1-127. Nathan confirms the leaked contract was photocopied at ASK. Andrea confronts Mathias, and Hicham sells his shares. Adapted for A1 French.")

INTRO = ("At the talent agency, IT specialist Nathan confirms that the leaked movie contract was photocopied in their own offices in the middle of the night. "
         "Andrea confronts Mathias over his maneuvers to take control of ASK. "
         "When Hicham Janowski suddenly offers to sell his shares, the corporate battle reaches an unexpected turning point. "
         "Let's listen to the scene in French first.")

STORY = [
 ("lea", "Le contrat secret a été photocopié ici.",
  "The secret contract was photocopied here.",
  [(3, "ça a bien été photocopié ici")], "Identified leak location"),
 ("mathias", "J'ai agi pour protéger notre agence.",
  "I acted to protect our agency.",
  [(94, "Je suis en train d'essayer de sauver")], "Defended unauthorized actions"),
 ("lea", "Tu as trahi la confiance de tous.",
  "You betrayed everyone's trust.",
  [(96, "c'est moi qui suis le traître")], "Condemned breach of trust"),
 ("mathias", "Je veux seulement sauver notre avenir.",
  "I only want to save our future.",
  [(94, "Je suis en train d'essayer de sauver")], "Asserted protective motives"),
 ("hicham", "Cette situation devient totalement insupportable.",
  "This situation is becoming completely unbearable.",
  [(102, "Félicitations, Mathias, t'as gagné")], "Expressed complete exasperation"),
 ("mathias", "Nous devons rester unis aujourd'hui.",
  "We must remain united today.",
  [(27, "on se tait et on observe la bête")], "Appealed for solidarity"),
 ("hicham", "Tu as gagné, je quitte l'agence.",
  "You won, I am leaving the agency.",
  [(102, "Félicitations, Mathias, t'as gagné")], "Conceded corporate battle"),
 ("hicham", "Je te vends mes parts maintenant.",
  "I sell you my shares right now.",
  [(103, "Je te vends mes parts")], "Agreed to transfer shares"),
 ("mathias", "J'accepte cette offre avec plaisir.",
  "I accept this offer with pleasure.",
  [(103, "Je te vends mes parts")], "Accepted buyout terms"),
 ("mathias", "Ce soir, nous fêterons cette victoire.",
  "Tonight, we will celebrate this victory.",
  [(110, "on va fêter les 30 ans")], "Anticipated evening celebration"),
 ("mathias", "J'annoncerai la nouvelle direction devant tous.",
  "I will announce the new management before everyone.",
  [(111, "le changement de direction")], "Outlined leadership plan"),
 ("lea", "As-tu une solution pour les Américains?",
  "Do you have a solution for the Americans?",
  [(114, "une solution pour contrer les Américains")], "Questioned crisis strategy"),
 ("mathias", "Je sais exactement quoi faire.",
  "I know exactly what to do.",
  [(116, "Je sais ce que je fais")], "Projected complete confidence"),
 ("lea", "Nous verrons bien ce soir.",
  "We shall see tonight.",
  [(27, "on se tait et on observe la bête")], "Reserved final judgment"),
]

OPENER = "Let's observe as Andrea, Mathias, and Hicham face off over the control of the agency."

WALK = [
 (0, None,
  "'The secret contract was photocopied here.' The verb meaning 'has' pairs naturally with the noun for 'business contract' in everyday conversation."),
 (1, None,
  "'I acted to protect our agency.' Notice how the short vowel drops before a vowel sound around 'I have', making the phrase flow smoothly as one unit. Notice how the short vowel drops before a vowel sound around 'I have', making the phrase flow smoothly as one unit."),
 (2, None,
  "'You betrayed everyone's trust.' This conversational past tense combines a helper verb with the past participle for 'betrayed'. This conversational past tense combines a helper verb with the past participle for 'betrayed'."),
 (3, None,
  "'I only want to save our future.' The verb meaning 'want' pairs naturally with the noun for 'future' in everyday conversation."),
 (4, None,
  "'This situation is becoming completely unbearable.' Notice how 'becomes' leads directly into the noun meaning 'state of affairs'. Notice how 'becomes' leads directly into the noun meaning 'state of affairs'."),
 (5, None,
  "'We must remain united today.' Notice how the short vowel drops before a vowel sound around 'must', making the phrase flow smoothly as one unit. Notice how the short vowel drops before a vowel sound around 'must', making the phrase flow smoothly as one unit."),
 (6, None,
  "'You won, I am leaving the agency.' A sudden surrender conceding defeat to a persistent rival. Notice how 'have' leads directly into the noun meaning 'the agency'."),
 (7, None,
  "'I sell you my shares right now.' The reflexive pronoun sits right in front of the verb for 'sell', turning the action back onto the subject."),
 (8, None,
  "'I accept this offer with pleasure.' A triumphal acceptance seizing the long-awaited opportunity. Notice how 'agree' leads directly into the noun meaning 'offer'."),
 (9, None,
  "'Tonight, we will celebrate this victory.' The verb meaning 'will celebrate' pairs naturally with the noun for 'evening hours' in everyday conversation."),
 (10, None,
  "'I will announce the new management before everyone.' Notice how 'will announce' leads directly into the noun meaning 'management'. Notice how 'will announce' leads directly into the noun meaning 'management'."),
 (11, None,
  "'Do you have a solution for the Americans?' Inverting the verb and pronoun around 'have you' creates a crisp, polished question. Inverting the verb and pronoun around 'have you' creates a crisp, polished question."),
 (12, None,
  "'I know exactly what to do.' The clause hinges on the everyday verb meaning 'know'."),
 (13, None,
  "'We shall see tonight.' The verb meaning 'will see' pairs naturally with the noun for 'evening hours' in everyday conversation."),
]

TRANSITION = "Now let's listen to the partners confronting each other again at full speed."

OUTRO = ("With Hicham walking away and selling his shares, Mathias positions himself as the undisputed leader of ASK. "
         "Yet Andrea remains skeptical of his claims, wondering how he will handle the American studio's two million dollar claim.")

CLOSING = ("lea", "La soirée sera décisive.")
