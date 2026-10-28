# Authoring module for dix-pour-cent s04e05 scene 04 (cues 64-208).
# Build: python3 tools/compose.py out/dix-pour-cent/s04e05/authoring/scene-04.py --out out/dix-pour-cent/s04e05/scene-04.json

ID = "dix-pour-cent-s04e05-scene-04"
SHOW = "dix-pour-cent"
SEASON = 4
EPISODE = 5
SCENE = 4
TITLE = "Exigences de star  (A Star's Demands)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "sigourney": "emilie"}
LABELS = {"lea": "Camille", "sigourney": "Sigourney"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S04E05"
SOURCE_FILE = "sources/dix-pour-cent/s04/e05.fr.dual.srt"
SOURCE_NOTE = ("Cues 64-208. At the Hotel de Crillon, Sigourney rejects a quiet suite meant for elderly guests "
               "and orders exercise equipment, wondering when Andrea will finally arrive.")

INTRO = ("Settling into her luxurious suite at the Hôtel de Crillon, Sigourney Weaver immediately expresses dissatisfaction with the quiet room assigned to her. "
         "Refusing to be treated as a sedate senior citizen, the energetic actress demands a view of the bustling Place de la Concorde along with fitness equipment. "
         "Let's listen to their conversation in French first.")

STORY = [
    ("lea", "Voici votre splendide suite au Crillon.",
     "Here is your splendid suite at the Crillon.",
     [(68, "l'hôtel de Crillon.")], "Camille shows Sigourney into the prestigious Parisian hotel room"),
    ("sigourney", "Pourquoi m'avoir donné une chambre si calme?",
     "Why give me such a quiet room?",
     [(69, "chambres les plus calmes"), (71, "besoin de me reposer?")], "Sigourney expresses displeasure with the secluded courtyard view"),
    ("lea", "L'hôtel réserve ces chambres aux clients âgés.",
     "The hotel reserves these rooms for elderly guests.",
     [(72, "clients les plus âgés")], "Camille gently explains the hotelier's intention"),
    ("sigourney", "Mais je n'ai pas besoin de repos!",
     "But I do not need rest!",
     [(71, "besoin de me reposer?")], "Sigourney energetically refutes the assumption"),
    ("sigourney", "Je veux voir la Place de la Concorde!",
     "I want to see the Place de la Concorde!",
     [(73, "Place de la Concorde.")], "Sigourney insists on vibrant street views of Paris"),
    ("lea", "Je vais demander un changement de chambre.",
     "I will request a change of room.",
     [], "new: Camille quickly accommodates her client's wishes"),
    ("sigourney", "Faites monter un bon vélo d'appartement.",
     "Have a good stationary bicycle brought up.",
     [(74, "vélo elliptique.")], "Sigourney places orders for daily workouts"),
    ("sigourney", "Et apportez aussi un tapis de course.",
     "And bring up a treadmill as well.",
     [(74, "tapis de course")], "Sigourney lists her full exercise regimen"),
    ("lea", "Je transmets vos demandes au personnel.",
     "I will pass your requests to the staff.",
     [], "new: Camille promises immediate concierge action"),
    ("sigourney", "Et quand arrive votre patronne Andréa?",
     "And when is your boss Andrea arriving?",
     [(76, "Et Andréa? Elle vient?")], "Sigourney inquires about her primary agent"),
    ("lea", "Elle arrive très bientôt, madame Weaver.",
     "She is arriving very soon, Madame Weaver.",
     [(77, "Bientôt.")], "Camille reassures the expectant actress"),
    ("sigourney", "J'ai hâte de discuter de mon contrat.",
     "I look forward to discussing my contract.",
     [], "new: Sigourney indicates her readiness for serious film talk"),
    ("lea", "Elle vous expliquera tous les détails.",
     "She will explain all the details to you.",
     [], "new: Camille assures her of Andrea's complete preparation"),
    ("sigourney", "Parfait, je vais commencer ma gymnastique.",
     "Perfect, I will start my exercises.",
     [], "new: Sigourney prepares to limber up before the meeting"),
]

OPENER = "Let's explore Camille and Sigourney's hotel suite conversation line by line."

WALK = [
    (0, None,
     "'Here is your splendid suite at the Crillon.' Camille welcomes Sigourney into the opulent reception room of the five-star hotel. Camille uses the polite 'you' form alongside 'suite' to keep a respectful professional tone."),
    (1, None,
     "'Why give me such a quiet room?' Sigourney questions the overly serene atmosphere facing an inner courtyard. Notice how 'to have' leads directly into the noun meaning 'room'."),
    (2, None,
     "'The hotel reserves these rooms for elderly guests.' Camille explains that management believed a peaceful setting suited a veteran star. The descriptive adjective for 'elderly' agrees in gender and number with its noun."),
    (3, None,
     "'But I do not need rest!' Sigourney pushes back vigorously against any elderly stereotypes. The verb meaning 'have' pairs naturally with the noun for 'need' in everyday conversation."),
    (4, None,
     "'I want to see the Place de la Concorde!' Sigourney demands sweeping windows overlooking Paris's grandest monument and traffic. The verb meaning 'want' pairs naturally with the noun for 'square' in everyday conversation."),
    (5, None,
     "'I will request a change of room.' Camille promptly contacts reception to arrange a higher front-facing suite. French forms the near future by pairing the present tense of 'to go' directly with 'to request'."),
    (6, None,
     "'Have a good stationary bicycle brought up.' Sigourney requests indoor cardio gear for her morning training. The verb meaning 'make' pairs naturally with the noun for 'bicycle' in everyday conversation."),
    (7, None,
     "'And bring up a treadmill as well.' Sigourney emphasizes her desire to maintain an intensive fitness routine during her shoot. Notice how 'bring' leads directly into the noun meaning 'mat'."),
    (8, None,
     "'I will pass your requests to the staff.' Camille notes down the equipment specifications for the concierge team. Camille uses the polite 'you' form alongside 'pass on' to keep a respectful professional tone."),
    (9, None,
     "'And when is your boss Andrea arriving?' Sigourney asks when the agency head will arrive to talk business. Sigourney uses the polite 'you' form alongside 'arrives' to keep a respectful professional tone."),
    (10, None,
     "'She is arriving very soon, Madame Weaver.' Camille promises that Andrea has resolved her domestic crisis and is en route. The verb meaning 'arrives' pairs naturally with the noun for 'madam' in everyday conversation."),
    (11, None,
     "'I look forward to discussing my contract.' Sigourney signals her eager anticipation regarding her French film project. Notice how 'have' leads directly into the noun meaning 'haste'."),
    (12, None,
     "'She will explain all the details to you.' Camille confirms that Andrea will present full contract terms and shooting dates. Camille uses the polite 'you' form alongside 'will explain' to keep a respectful professional tone."),
    (13, None,
     "'Perfect, I will start my exercises.' Sigourney wraps up the talk by launching straight into dynamic stretches. Notice how 'am going' leads directly into the noun meaning 'gymnastics'."),
]

TRANSITION = "Now let's listen to Camille and Sigourney's exchange once more from start to finish."

OUTRO = ("Sigourney Weaver sets a brisk, commanding tone at the Crillon, demanding high energy from herself and the agency. "
         "Let's review the key vocabulary of luxury hotels, physical fitness, and professional assertiveness from this scene.")

CLOSING = ("lea", "Une cliente très sportive et exigeante.")
