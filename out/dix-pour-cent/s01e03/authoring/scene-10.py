# Authoring module for dix-pour-cent s01e03 scene 10 (cues 198-214).
# Build: python3 tools/compose.py out/dix-pour-cent/s01e03/authoring/scene-10.py --out out/dix-pour-cent/s01e03/scene-10.json

ID = "dix-pour-cent-s01e03-scene-10"
SHOW = "dix-pour-cent"
SEASON = 1
EPISODE = 3
SCENE = 10
TITLE = "Trois mois sur un bateau  (Three Months on a Boat)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "gabriel": "theo"}
LABELS = {"lea": "Laura", "gabriel": "Gabriel"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S01E03"
SOURCE_FILE = "sources/dix-pour-cent/s01/e03.fr.dual.srt"

INTRO = ("Gabriel has just finished arguing with Sofia at reception, and promised, once again, to come and see her play. "
         "Now he can finally take a call that's been waiting: Laura Smet, his client. "
         "This morning he gave her what he called the only copy of the new script by the Swedish director Solveig Akerfelt. "
         "Then Laura found out that Mathias had given the very same script to her mother, Nathalie Baye: "
         "the director wants them both, to play a mother and her daughter. "
         "Laura loves the script. The problem is somewhere else, and she's about to tell Gabriel where. "
         "First, the French. Don't try to hold on to every word; just listen to how they sound.")

STORY = [
 ("gabriel", "Quoi? Tu n'aimes pas le scénario?", "What? Don't you like the script?",
  [(198, "Quoi ? Tu n'aimes pas le scénario")], ""),
 ("lea", "Si, je l'adore.", "Yes, I love it.",
  [(198, "Si, je l'adore")], ""),
 ("lea", "Mais trois mois de tournage, sur un bateau, en pleine mer!", "But three months of shooting, on a boat, out at sea!",
  [(199, "Mais trois mois de tournage"), (200, "en pleine mer")], "'soit sur un chalutier, soit sur une île' simplified to 'sur un bateau'"),
 ("lea", "Je ne peux pas supporter ça.", "I can't stand that.",
  [(201, "Je ne peux pas supporter ça")], ""),
 ("gabriel", "Je connais un excellent acupuncteur contre le mal de mer.", "I know an excellent acupuncturist for seasickness.",
  [(202, "Je connais un excellent acupuncteur contre le mal de mer")], ""),
 ("lea", "Non. Je parle de ma mère.", "No. I'm talking about my mother.",
  [(203, "Non"), (204, "Je parle de ma mère")], ""),
 ("lea", "Trois mois! Tu connais un acupuncteur pour ça?", "Three months! Do you know an acupuncturist for that?",
  [(205, "Trois mois ! Tu connais un acupuncteur pour ça")], ""),
 ("gabriel", "Mais tu étais contente!", "But you were happy!",
  [(206, "tu étais")], "'Je croyais que tu étais ravie' simplified"),
 ("lea", "Je l'aime.", "I love her.",
  [(207, "Je l'aime")], ""),
 ("lea", "Mais je ne peux pas être avec elle sur un bateau, jour et nuit!", "But I can't be with her on a boat, day and night!",
  [(208, "mais je ne peux pas être")], "'enfermée ... sur un bateau de pêche 24h/24' simplified"),
 ("gabriel", "Attends. Parle d'abord à Akerfelt.", "Wait. Talk to Akerfelt first.",
  [(210, "attends")], "retells 'Une fois que tu auras parlé à Akerfelt'"),
 ("gabriel", "Après, tu vas voir les choses différemment.", "Afterwards, you'll see things differently.",
  [(211, "les choses"), (212, "différemment")], "future perfect and future simplified to 'tu vas voir'"),
 ("lea", "Si elle est un génie, ce sera encore plus dur de refuser.", "If she's a genius, it'll be even harder to say no.",
  [(213, "Si elle est"), (214, "ce sera encore plus dur de refuser")], "'le génie que je crois' -> 'un génie'"),
 ("gabriel", "Laura, tu ne peux pas refuser!", "Laura, you can't say no!",
  [(214, "Laura, tu ne peux pas refuser")], ""),
 ("lea", "Bon. Je vais lui parler.", "Okay. I'll talk to her.", [], "new: Laura gives in for now"),
]

OPENER = ("Let's go through it gently. Gabriel picks up and immediately fears the worst.")

WALK = [
 (0, "Quoi?",
  "'What?' Short and blunt, the everyday way to react to a surprise."),
 (0, "Tu n'aimes pas le scénario?",
  "'Don't you like the script?' The negative goes around the verb for 'like'; before a vowel the first little word shrinks. "
  "Now listen carefully to the first word of Laura's answer."),
 (1, None,
  "'Yes, I love it.' That's the special yes again, the one you use to contradict a negative question. "
  "Gabriel asked 'don't you like it?', so a plain yes would sound wrong. And the little word for 'it' sits before the verb."),
 (2, None,
  "'But three months of shooting, on a boat, out at sea!' Literally 'in full sea'. You can hear she isn't thrilled."),
 (3, None,
  "'I can't stand that.' The verb 'can' plus another verb in its basic form, with the negative wrapped around 'can'."),
 (4, None,
  "'I know an excellent acupuncturist for seasickness.' Literally 'against the sickness of the sea'. "
  "Gabriel, ever helpful, has completely misunderstood."),
 (5, None,
  "'No. I'm talking about my mother.' In French you 'talk of' something. And the word for 'my' is feminine here, to go with 'mother'."),
 (6, None,
  "'Three months! Do you know an acupuncturist for that?' She throws his own words back at him."),
 (7, None,
  "'But you were happy!' The verb 'to be' in the form for describing how things were. And 'happy' has a feminine ending for Laura."),
 (8, None,
  "'I love her.' Same verb as 'like', and once more the little object word goes before the verb. Here it means 'her'."),
 (9, None,
  "'But I can't be with her on a boat, day and night!' The word for 'her' after 'with' is the same as the word for 'she'."),
 (10, "Attends.",
  "'Wait.' A casual command; you'll hear it all the time."),
 (10, "Parle d'abord à Akerfelt.",
  "'Talk to Akerfelt first.' The phrase in the middle means 'first of all'. Gabriel thinks the director will win her over."),
 (11, None,
  "'Afterwards, you'll see things differently.' The verb 'to go' plus 'see' talks about the near future: you are going to see."),
 (12, None,
  "'If she's a genius, it'll be even harder to say no.' That's the real future tense: 'it will be'. "
  "And 'even more hard' is how French says 'even harder'. Laura is afraid of liking it too much."),
 (13, None,
  "'Laura, you can't say no!' The agent's cry from the heart. A film with mother and daughter would be a big deal for the agency."),
 (14, None,
  "'Okay. I'll talk to her.' Near future again, and that small word before the verb means 'to her'. For now, Laura gives in."),
]

TRANSITION = "Good. Let's listen to the whole call once more."

OUTRO = ("Short and sweet, and you followed all of it. Listen out for that special yes when people answer a negative question. "
         "See you next time.")
CLOSING = ("lea", "Salut, Gabriel!")
