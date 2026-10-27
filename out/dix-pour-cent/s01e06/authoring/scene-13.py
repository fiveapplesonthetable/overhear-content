# Authoring module for dix-pour-cent s01e06 scene 13 (cues 350-381).
# Build: python3 tools/compose.py out/dix-pour-cent/s01e06/authoring/scene-13.py --out out/dix-pour-cent/s01e06/scene-13.json

ID = "dix-pour-cent-s01e06-scene-13"
SHOW = "dix-pour-cent"
SEASON = 1
EPISODE = 6
SCENE = 13
TITLE = "Le dîner de travail  (The Work Dinner)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "colette": "emilie", "christophe": "theo"}
LABELS = {"lea": "Andréa", "colette": "Colette", "christophe": "Christophe"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S01E06"
SOURCE_FILE = "sources/dix-pour-cent/s01/e06.fr.dual.srt"
SOURCE_NOTE = ("Cues 350-381. Christophe's name is added to cue 350 ('Christophe, tu ne peux pas refuser'), "
               "and the complex indirect question in cue 374 is simplified for A1 learners.")

INTRO = ("Determined to save Francois Berleand's role in Dom Juan, Andrea invites director Christophe Bel to dinner. "
         "Back at her apartment, Colette prepares to go home to finish her tax audit, but Andrea convinces her to stay "
         "and gives her a spare toothbrush. Later at the restaurant, Christophe invites Andrea to his birthday party "
         "and boasts about how well he can manipulate people. Let's listen to the scene in French first.")

STORY = [
 ("lea", "Christophe, tu ne peux pas refuser.",
  "Christophe, you cannot say no.",
  [(350, "tu ne peux pas refuser")], "Added name"),
 ("lea", "Mon amour-propre ne me le permet pas.",
  "My pride won't allow it.",
  [(351, "Mon amour-propre ne me le permet pas")], ""),
 ("lea", "J'ai plein de choses à te raconter.",
  "I have lots of things to tell you.",
  [(352, "J'ai plein de choses à te raconter")], ""),
 ("colette", "Non, je dois rentrer chez moi.",
  "No, I have to go home.",
  [(354, "Non, je dois rentrer")], "Clarified destination"),
 ("colette", "J'ai encore une grosse partie de mon rapport à rédiger.",
  "I still have a big part of my report to write.",
  [(355, "J'ai encore une grosse partie de mon rapport à rédiger")], ""),
 ("lea", "Non, reste, s'il te plaît!",
  "No, stay, please!",
  [(356, "Non, reste, s'il te plaît")], ""),
 ("colette", "Tu t'habilles comme ça pour un dîner de travail?",
  "You dress like that for a work dinner?",
  [(360, "Tu t'habilles comme ça pour un dîner de travail")], ""),
 ("lea", "Ce soir, je joue sobre et classe.",
  "Tonight, I play it sober and classy.",
  [(361, "Ce soir, je joue sobre"), (361, "et classe")], "Trimmed 'sexy'"),
 ("lea", "C'est un cadeau pour toi.",
  "It is a present for you.",
  [(364, "C'est pour moi"), (364, "Oui")], "Adapted context"),
 ("lea", "Comme ça tu n'auras plus besoin d'apporter le tien.",
  "That way you won't need to bring your own anymore.",
  [(365, "Comme ça tu n'auras plus besoin d'apporter le tien")], ""),
 ("christophe", "Je fête mon anniversaire demain soir au théâtre.",
  "I celebrate my birthday tomorrow evening at the theatre.",
  [(369, "Je fête mon anniversaire demain soir au théâtre")], ""),
 ("christophe", "J'aimerais vraiment que tu viennes.",
  "I would really like you to come.",
  [(370, "J'aimerais vraiment que tu viennes")], ""),
 ("lea", "En tant que metteur en scène, tu es doué pour obtenir ce que tu veux.",
  "As a director, you are gifted at getting what you want.",
  [(374, "En tant que metteur en scène"), (374, "tu es doué pour"), (374, "ce que tu veux")], "Simplified structure"),
 ("christophe", "Je ne suis pas mauvais.",
  "I am not bad.",
  [(375, "Je ne suis pas mauvais")], ""),
]

OPENER = "Let's break down the scene line by line and explore the key expressions."

WALK = [
 (0, None,
  "'Christophe, you cannot say no.' Andrea corners the stubborn young theatre director over the phone. The verb can in "
  "the negative takes standard French negation."),
 (1, None,
  "'My pride won't allow it.' She insists that she will not take no for an answer. The compound noun for self-respect "
  "or pride is joined with a hyphen."),
 (2, None,
  "'I have lots of things to tell you.' She promises an exciting conversation. The adjective for full is used colloquially "
  "with of to mean tons of or lots of."),
 (3, None,
  "'No, I have to go home.' In Andrea's apartment, Colette gets ready to leave to finish her work."),
 (4, None,
  "'I still have a big part of my report to write.' She explains the crunch on her tax audit. Notice the formal verb for "
  "drafting or writing a report."),
 (5, None,
  "'No, stay, please!' Andrea pulls her back. The imperative form of stay uses the informal second-person ending."),
 (6, None,
  "'You dress like that for a work dinner?' Looking at Andrea's chic outfit, Colette asks suspiciously. The reflexive verb "
  "for getting dressed takes the preposition for like this."),
 (7, None,
  "'Tonight, I play it sober and classy.' Andrea explains her strategy for charming the young director."),
 (8, None,
  "'It is a present for you.' To make Colette feel at home, Andrea hands her a small package containing a spare toothbrush."),
 (9, None,
  "'That way you won't need to bring your own anymore.' Andrea smiles warmly. The conjunction for that way is followed "
  "by the future tense."),
 (10, None,
  "'I celebrate my birthday tomorrow evening at the theatre.' Later at the restaurant, Christophe brings up his plans."),
 (11, None,
  "'I would really like you to come.' He looks across the table and adds warmly. The conditional form of to like is "
  "followed by the subjunctive form of to come."),
 (12, None,
  "'As a director, you are gifted at getting what you want.' Andrea flatters him with a sharp observation. The phrase "
  "literally means in the role of."),
 (13, None,
  "'I am not bad.' Christophe smirks with false modesty. The negation wraps around the verb to be."),
]

TRANSITION = "Now let's listen to the whole dialogue once again from beginning to end."

OUTRO = ("Andrea thinks she can charm Christophe into saving the play, while Colette is slowly moving into her "
         "apartment. Keep the phrase for pride in mind: love of oneself.")

CLOSING = ("christophe", "Je ne suis pas mauvais.")
