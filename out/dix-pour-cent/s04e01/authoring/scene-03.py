# Authoring module for dix-pour-cent s04e01 scene 03 (cues 74-178).
# Build: python3 tools/compose.py out/dix-pour-cent/s04e01/authoring/scene-03.py --out out/dix-pour-cent/s04e01/scene-03.json

ID = "dix-pour-cent-s04e01-scene-03"
SHOW = "dix-pour-cent"
SEASON = 4
EPISODE = 1
SCENE = 3
TITLE = "La nouvelle direction  (The New Leadership)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "gabriel": "theo", "arlette": "emilie"}
LABELS = {"lea": "Andréa", "gabriel": "Gabriel", "arlette": "Arlette"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S04E01"
SOURCE_FILE = "sources/dix-pour-cent/s04/e01.fr.dual.srt"
SOURCE_NOTE = ("Cues 74-178. Andrea presents her ambitious strategy to the agency while Gabriel warns her about Charlotte's movie. Adapted for A1 French.")

INTRO = ("Back at the agency, Andrea Martel takes the reins as general director following Mathias Barneville's departure. "
         "Determined to prove that ASK remains strong despite industry rumors, she rallies Gabriel and Arlette around an aggressive new strategy focused on television series and emerging talent. "
         "Yet behind her confident front, Andrea struggles with her blunder over Charlotte Gainsbourg's dreadful screenplay. "
         "Let's listen to the scene in French first.")

STORY = [
 ("gabriel", "Le départ de Mathias fragilise notre agence.",
  "Mathias's departure weakens our agency.",
  [(81, "Il rejoint StarMédia")], "Analyzed rival's damaging exit"),
 ("lea", "C'est l'occasion de repenser notre travail.",
  "It is the opportunity to rethink our work.",
  [(75, "une belle occasion de repenser l'agence")], "Framed crisis as reform opportunity"),
 ("lea", "J'ai dit oui à Charlotte trop vite.",
  "I said yes to Charlotte too quickly.",
  [(88, "avant de l'avoir lu")], "Admitted hasty professional blunder"),
 ("gabriel", "Elle ne peut pas tourner ce navet!",
  "She cannot shoot this dud!",
  [(99, "dans ce navet")], "Opposed artistic disaster"),
 ("gabriel", "Dis-lui simplement la vérité sans attendre.",
  "Simply tell her the truth without waiting.",
  [(102, "dis la vérité")], "Urged honest correction"),
 ("lea", "Nous devons d'abord sauver la face.",
  "We must first save face.",
  [(125, "sauver la face")], "Prioritized public reputation"),
 ("lea", "Tout le monde attend notre chute.",
  "Everyone expects our downfall.",
  [(126, "se serre la ceinture")], "Identified industry skepticism"),
 ("lea", "Nous allons prouver notre grande force.",
  "We are going to prove our great strength.",
  [(130, "on s'agrandit")], "Expressed bold corporate ambition"),
 ("lea", "Recrutons immédiatement de nouveaux grands talents.",
  "Let's immediately recruit great new talent.",
  [(131, "recruter de nouveaux talents")], "Proposed proactive talent expansion"),
 ("lea", "Nous devons aussi miser sur les séries.",
  "We must also bet on television series.",
  [(134, "miser à fond sur les séries")], "Advocated diversification into television"),
 ("arlette", "Ne sacrifions pas le cinéma d'auteur!",
  "Let's not sacrifice arthouse cinema!",
  [(136, "Ne tuons pas le cinéma")], "Defended traditional cinema heritage"),
 ("lea", "Les séries apportent des revenus réguliers.",
  "Series bring regular income.",
  [(137, "les projets sur plusieurs saisons, c'est des revenus")], "Justified commercial rationale"),
 ("lea", "Ces nouveaux projets vont nous sauver.",
  "These new projects are going to save us.",
  [(140, "qui va nous sauver")], "Concluded strategic rallying speech"),
 ("gabriel", "Reste à régler le problème de Charlotte.",
  "It remains to resolve Charlotte's problem.",
  [(102, "dis la vérité")], "Reminded leader of unresolved crisis"),
]

OPENER = "Let's observe as Andrea outlines her bold expansion plan to Gabriel and Arlette."

WALK = [
 (0, None,
  "'Mathias's departure weakens our agency.' A realistic assessment recognizing the immediate vulnerability caused by a senior partner's exit."),
 (1, None,
  "'It is the opportunity to rethink our work.' An energetic pivot framing executive turmoil as a chance for positive reinvention."),
 (2, None,
  "'I said yes to Charlotte too quickly.' A private admission acknowledging a reckless editorial commitment."),
 (3, None,
  "'She cannot shoot this dud!' An outspoken artistic reaction protesting the actress starring in poor-quality material."),
 (4, None,
  "'Simply tell her the truth without waiting.' A sensible recommendation urging transparency before the project advances."),
 (5, None,
  "'We must first save face.' A strategic priority demanding an impression of stability before industry competitors."),
 (6, None,
  "'Everyone expects our downfall.' A sobering observation noting widespread rival expectations of agency decline."),
 (7, None,
  "'We are going to prove our great strength.' A defiant declaration affirming ASK's resilience and vitality."),
 (8, None,
  "'Let's immediately recruit great new talent.' A proactive policy calling for the aggressive scouting of fresh artists."),
 (9, None,
  "'We must also bet on television series.' An innovative shift seeking profitable multi-season broadcast opportunities."),
 (10, None,
  "'Let's not sacrifice arthouse cinema!' A principled artistic defense safeguarding cinematic tradition against commercialization."),
 (11, None,
  "'Series bring regular income.' A practical financial argument highlighting steady recurring revenues."),
 (12, None,
  "'These new projects are going to save us.' An optimistic rallying cry uniting the team behind forward-looking endeavors."),
 (13, None,
  "'It remains to resolve Charlotte's problem.' A sobering closing reminder that the immediate star client dilemma is far from solved."),
]

TRANSITION = "Now let's listen to Andrea, Gabriel, and Arlette debating their future again at full speed."

OUTRO = ("Andrea lays out a compelling vision for the agency, inspiring her colleagues to embrace new creative horizons. "
         "Yet she knows that before she can conquer the future, she must somehow extricate Charlotte Gainsbourg from a disastrous commitment.")

CLOSING = ("lea", "Je vais trouver une solution.")
