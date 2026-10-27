# Authoring module for dix-pour-cent s04e05 scene 09 (cues 425-433).
# Build: python3 tools/compose.py overhear-content/out/dix-pour-cent/s04e05/authoring/scene-09.py --out overhear-content/out/dix-pour-cent/s04e05/scene-09.json

ID = "dix-pour-cent-s04e05-scene-09"
SHOW = "dix-pour-cent"
SEASON = 4
EPISODE = 5
SCENE = 9
TITLE = "Renvoi de la crèche  (Expelled from Daycare)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "directrice": "emilie", "lea": "lucie"}
LABELS = {"directrice": "Directrice", "lea": "Andréa"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S04E05"
SOURCE_FILE = "sources/dix-pour-cent/s04/e05.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 425-433. Andrea arrives late at the daycare center Les Coccinelles to pick up baby Flora. "
    "The director angrily confronts her for abandoning the child and expels Flora, leaving Andrea to return home alone."
)

INTRO = (
    "At the daycare center Les Coccinelles, the director angrily confronts Andrea Martel for arriving very late. "
    "Because Andrea left baby Flora behind without notifying the staff, the director makes an uncompromising decision. "
    "Let's listen to their confrontation in French first."
)

OPENER = "Let's examine the confrontation line by line and explore the French expressions."
TRANSITION = "Now let's listen to the complete discussion once more to reinforce the vocabulary."

STORY = [
    ("directrice", "Vous êtes en retard, madame Martel!",
     "You are late, Madame Martel!",
     [(425, "Comment avez-vous pu la laisser ici sans nous prévenir?")], "The director greets Andrea with anger"),
    ("lea", "Je sais, j'ai eu une urgence.",
     "I know, I had an emergency.",
     [(425, "sans nous prévenir?")], "Andrea explains her delay"),
    ("directrice", "Vous avez laissé votre fille seule!",
     "You left your daughter alone!",
     [(425, "Comment avez-vous pu la laisser ici")], "The director emphasizes the abandonment"),
    ("lea", "Elle était en sécurité ici.",
     "She was safe here.",
     [(426, "Vous avez évoqué le lien de confiance.")], "Andrea defends the environment"),
    ("directrice", "C'est un manque de respect total.",
     "It is a complete lack of respect.",
     [(426, "C'était un signe de confiance.")], "The director criticizes Andrea's attitude"),
    ("lea", "C'était une preuve de confiance!",
     "It was proof of trust!",
     [(426, "C'était un signe de confiance.")], "Andrea attempts a justification"),
    ("directrice", "Non, c'est inacceptable pour nous.",
     "No, it is unacceptable for us.",
     [(427, "Dites au revoir à la crèche Les Coccinelles.")], "The director refuses to compromise"),
    ("directrice", "Dites au revoir à la crèche!",
     "Say goodbye to the daycare!",
     [(427, "Dites au revoir à la crèche Les Coccinelles.")], "The director expels Flora permanently"),
    ("lea", "Vous renvoyez Flora pour ça?",
     "Are you expelling Flora for that?",
     [(428, "Sans blague. Salut, Capu.")], "Andrea reacts with disbelief"),
    ("directrice", "Oui, nous appliquons le règlement.",
     "Yes, we enforce the rules.",
     [(431, "Je vais en informer le siège.")], "The director stands by daycare policy"),
    ("lea", "Très bien, au revoir, madame.",
     "Very well, goodbye, madame.",
     [(428, "Sans blague. Salut, Capu."), (432, "Faites donc.")], "Andrea departs with dignity"),
    ("directrice", "Vous êtes vraiment folle!",
     "You are really crazy!",
     [(429, "Tu es folle! Elle est folle.")], "The director mutters in shock"),
    ("lea", "Viens, Flora, on rentre à la maison.",
     "Come, Flora, we are going home.",
     [(433, "Bonne nuit, ma chérie.")], "Andrea gathers her baby warmly"),
    ("lea", "Bonne nuit, mon petit bébé.",
     "Goodnight, my little baby.",
     [(433, "Bonne nuit, ma chérie.")], "Andrea comforts her daughter at bedtime"),
]

WALK = [
    (0, None,
     "'You are late, Madame Martel!' The director expresses her immediate frustration. "
     "The prepositional phrase 'en retard' means late."),
    (1, None,
     "'I know, I had an emergency.' Andrea justifies her arrival with a serious excuse. "
     "The noun 'urgence' refers to an emergency."),
    (2, None,
     "'You left your daughter alone!' The director reproaches Andrea for leaving Flora unattended. "
     "The adjective 'seule' describes being alone."),
    (3, None,
     "'She was safe here.' Andrea argues that the daycare is a protected place. "
     "The feminine noun 'securite' designates safety."),
    (4, None,
     "'It is a complete lack of respect.' The director condemns the late pickup. "
     "The masculine noun 'manque' means lack or shortage."),
    (5, None,
     "'It was proof of trust!' Andrea reframes her lateness as total confidence in the staff. "
     "The feminine noun 'preuve' signifies proof."),
    (6, None,
     "'No, it is unacceptable for us.' The director rejects Andrea's rationalization. "
     "The adjective 'inacceptable' means unacceptable."),
    (7, None,
     "'Say goodbye to the daycare!' The director delivers the severe consequence. "
     "The noun 'creche' designates a daycare center."),
    (8, None,
     "'Are you expelling Flora for that?' Andrea is shocked by the sudden expulsion. "
     "The verb 'renvoyez' comes from 'renvoyer', to dismiss or expel."),
    (9, None,
     "'Yes, we enforce the rules.' The director insists on strict administrative regulations. "
     "The noun 'reglement' means rules or regulations."),
    (10, None,
     "'Very well, goodbye, madame.' Andrea accepts the verdict coldly without pleading. "
     "The phrase 'tres bien' serves as a formal acknowledgment."),
    (11, None,
     "'You are really crazy!' The director watches Andrea leave in bewilderment. "
     "The feminine adjective 'folle' means crazy or insane."),
    (12, None,
     "'Come, Flora, we are going home.' Andrea speaks gently to her infant daughter. "
     "The verb form 'rentre' comes from 'rentrer', to return home."),
    (13, None,
     "'Goodnight, my little baby.' Andrea tucks Flora safely into her crib for the night. "
     "The masculine noun 'bebe' designates a baby."),
]

OUTRO = (
    "After facing the strict director's anger, Andrea walks away with Flora in her arms. "
    "Though she maintains her pride, she now faces the immense challenge of finding another childcare solution. "
    "Now let's listen to the scene one last time."
)

CLOSING = ("lea", "Dors bien, ma petite Flora adorée!")
