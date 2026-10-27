# Authoring module for dix-pour-cent s03e05 scene 27 (cue 1057).
# Build: python3 tools/compose.py overhear-content/out/dix-pour-cent/s03e05/authoring/scene-27.py --out overhear-content/out/dix-pour-cent/s03e05/scene-27.json

ID = "dix-pour-cent-s03e05-scene-27"
SHOW = "dix-pour-cent"
SEASON = 3
EPISODE = 5
SCENE = 27
TITLE = "L'hésitation de Gabriel  (Gabriel's Hesitation)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "gabriel": "theo"}
LABELS = {"lea": "Arlette", "gabriel": "Gabriel"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S03E05"
SOURCE_FILE = "sources/dix-pour-cent/s03/e05.fr.dual.srt"
SOURCE_NOTE = ("Cue 1057. Gabriel tracks down Arlette in her office at ASK to gauge her loyalty "
               "and seek reassurance before their secret plans unfold.")

INTRO = ("Inside the quiet hallway of ASK, Gabriel searches anxiously for Arlette to seek her guidance. "
         "Finding the veteran agent in her office with her dog Jean Gabin, Gabriel tries to test the waters without revealing too much. "
         "Let's listen to their conversation in French first.")

OPENER = "Let's examine the conversation line by line and explore the French expressions."
TRANSITION = "Now let's listen to the complete discussion once more to reinforce the vocabulary."

STORY = [
 ("gabriel", "Arlette, tu es là?",
  "Arlette, are you there?",
  [(1057, "Hein ?")], "Looking for Arlette"),
 ("lea", "Hein, qu'est-ce qui se passe?",
  "Huh, what is going on?",
  [(1057, "Hein ?")], "Looking up surprised"),
 ("gabriel", "Je te cherchais partout ici.",
  "I was looking everywhere for you here.",
  [(1057, "Hein ?")], "Explaining search"),
 ("lea", "Tu as l'air très nerveux.",
  "You look very nervous.",
  [(1057, "Hein ?")], "Noticing anxiety"),
 ("gabriel", "Les choses changent vite maintenant.",
  "Things are changing fast now.",
  [(1057, "Hein ?")], "Hinting at changes"),
 ("lea", "L'agence a connu des tempêtes.",
  "The agency has weathered storms before.",
  [(1057, "Hein ?")], "Recalling past history"),
 ("gabriel", "Tu resterais toujours avec nous?",
  "Would you still stay with us?",
  [(1057, "Hein ?")], "Asking about loyalty"),
 ("lea", "Je reste fidèle à mes amis.",
  "I remain loyal to my friends.",
  [(1057, "Hein ?")], "Affirming allegiance"),
 ("gabriel", "Andréa et moi comptons sur toi.",
  "Andrea and I count on you.",
  [(1057, "Hein ?")], "Expressing reliance"),
 ("lea", "Ne fais pas de bêtises, Gabriel.",
  "Do not do anything foolish, Gabriel.",
  [(1057, "Hein ?")], "Warning caution"),
 ("gabriel", "Nous voulons simplement nous protéger.",
  "We simply want to protect ourselves.",
  [(1057, "Hein ?")], "Justifying secrecy"),
 ("lea", "La loyauté est essentielle ici.",
  "Loyalty is essential here.",
  [(1057, "Hein ?")], "Emphasizing principle"),
 ("gabriel", "Merci pour ta sagesse, Arlette.",
  "Thank you for your wisdom, Arlette.",
  [(1057, "Hein ?")], "Thanking senior agent"),
 ("lea", "Garde ton calme aujourd'hui.",
  "Keep your calm today.",
  [(1057, "Hein ?")], "Advising composure"),
]

WALK = [
 (0, None,
  "'Arlette, are you there?' Gabriel asks as he looks into her office. "
  "The subject pronoun 'tu' addresses his senior colleague informally."),
 (1, None,
  "'Huh, what is going on?' Arlette looks up surprised from her paperwork. "
  "The informal interjection 'hein' expresses surprise or a request for clarification."),
 (2, None,
  "'I was looking everywhere for you here.' Gabriel explains he has been roaming the agency corridors. "
  "The imperfect tense 'cherchais' indicates ongoing past action."),
 (3, None,
  "'You look very nervous.' Arlette observes his visible anxiety immediately. "
  "The idiom 'avoir l'air' means to appear or look a certain way."),
 (4, None,
  "'Things are changing fast now.' Gabriel hints at the turbulent shifts taking place at ASK. "
  "The adverb 'vite' means quickly or fast."),
 (5, None,
  "'The agency has weathered storms before.' Arlette recalls her decades of experience in the agency business. "
  "The past participle 'connu' comes from connaitre."),
 (6, None,
  "'Would you still stay with us?' Gabriel tests whether she would follow them if they leave. "
  "The conditional 'resterais' poses a hypothetical question."),
 (7, None,
  "'I remain loyal to my friends.' Arlette states her core personal principle. "
  "The adjective 'fidele' expresses steadfast commitment and allegiance."),
 (8, None,
  "'Andrea and I count on you.' Gabriel emphasizes the close bond between the three agents. "
  "The verbal idiom 'compter sur' means to rely upon someone."),
 (9, None,
  "'Do not do anything foolish, Gabriel.' Arlette cautions him with maternal intuition. "
  "The negative imperative 'ne fais pas' advises prudence."),
 (10, None,
  "'We simply want to protect ourselves.' Gabriel defends their motives for acting behind Hicham's back. "
  "The adverb 'simplement' qualifies their intentions."),
 (11, None,
  "'Loyalty is essential here.' Arlette underscores the foundational virtue of their profession. "
  "The noun 'loyaute' signifies trust and fidelity."),
 (12, None,
  "'Thank you for your wisdom, Arlette.' Gabriel appreciates her steadying presence. "
  "The noun 'sagesse' denotes sound judgment and life experience."),
 (13, None,
  "'Keep your calm today.' Arlette offers parting advice before returning to her work. "
  "The imperative 'garde' instructs him to remain composed."),
]

OUTRO = ("Arlette's calm perspective reminds Gabriel of the deep history and emotional stakes at ASK. "
         "Unbeknownst to both of them, a catastrophic misunderstanding is already about to explode across the agency. "
         "Now, let's review the scene one last time.")

CLOSING = ("lea", "Garde ton calme aujourd'hui.")
