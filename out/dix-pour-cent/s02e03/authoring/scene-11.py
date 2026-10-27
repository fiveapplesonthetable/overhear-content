# Authoring module for dix-pour-cent s02e03 scene 11 (cues 259-283).
# Build: python3 tools/compose.py out/dix-pour-cent/s02e03/authoring/scene-11.py --out out/dix-pour-cent/s02e03/scene-11.json

ID = "dix-pour-cent-s02e03-scene-11"
SHOW = "dix-pour-cent"
SEASON = 2
EPISODE = 3
SCENE = 11
TITLE = "Le planning de Nathalie Baye  (Nathalie Baye's Schedule)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "mathias": "marcel"}
LABELS = {"lea": "Noémie", "mathias": "Mathias"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S02E03"
SOURCE_FILE = "sources/dix-pour-cent/s02/e03.fr.dual.srt"
SOURCE_NOTE = ("Cues 259-283. In Mathias's office, Noémie presents an ingenious schedule allowing star client "
               "Nathalie Baye to shoot two films back-to-back, while subtly probing Mathias about their romantic past. "
               "Adapted for A1 French.")

INTRO = ("Inside Mathias's office, Noemie presents a clever calendar solution for star client Nathalie Baye. "
         "While reviewing the tight shooting dates, personal intimacy and office diplomacy collide. "
         "Let's listen to the scene in French first.")

STORY = [
 ("lea", "J'ai trouvé une solution pour Nathalie Baye.",
  "I found a solution for Nathalie Baye.",
  [(260, "j'ai trouvé une solution pour Nathalie Baye.")], "Added J'"),
 ("mathias", "Ah, excellent. Montre-moi ça.",
  "Ah, excellent. Show me that.",
  [(261, "Ah, excellent.")], "Added Montre-moi ça"),
 ("lea", "Voilà le planning de Xavier Beauvois.",
  "Here is Xavier Beauvois's schedule.",
  [(262, "Voilà le planning de Xavier Beauvois.")], ""),
 ("lea", "Celui-ci est celui de Tonie Marshall.",
  "This one is Tonie Marshall's.",
  [(263, "Celui-ci est celui de Tonie Marshall.")], ""),
 ("lea", "Les jours de tournage sont marqués en rouge.",
  "The shooting days are marked in red.",
  [(264, "sont marqués en rouge.")], "Adapted subject"),
 ("lea", "Tout s'emboîte parfaitement ici.",
  "Everything fits together perfectly here.",
  [(265, "Tout s'emboîte parfaitement.")], "Added ici"),
 ("lea", "Nathalie peut faire les deux films.",
  "Nathalie can do both movies.",
  [(266, "Nathalie peut faire")], "Simplified films"),
 ("mathias", "Non, je te dis que ça ne marche pas.",
  "No, I tell you that it does not work.",
  [(270, "Non, je te dis que ça ne marche pas.")], ""),
 ("lea", "Tu le regrettes, Mathias?",
  "Do you regret it, Mathias?",
  [(272, "Tu le regrettes ?")], "Added Mathias"),
 ("mathias", "Ce n'est pas le sujet, on est au travail.",
  "That is not the topic, we are at work.",
  [(273, "Ce n'est pas le sujet, on est au travail.")], ""),
 ("mathias", "Beauvois dépasse toujours les dates.",
  "Beauvois always exceeds the dates.",
  [(274, "Beauvois dépasse toujours")], "Added les dates"),
 ("mathias", "Nathalie a besoin de deux semaines de repos.",
  "Nathalie needs two weeks of rest.",
  [(274, "Nathalie a besoin de deux semaines de repos.")], ""),
 ("lea", "Tu as dit non, donc tu ne regrettes rien.",
  "You said no, so you do not regret anything.",
  [(275, "Tu as dit non, donc tu ne le regrettes pas.")], "Adapted to rien"),
 ("mathias", "Écoute, Noémie, je préfère ne pas en parler ici.",
  "Listen, Noémie, I prefer not to speak of it here.",
  [(276, "Écoute, Noémie, je préfère ne pas en parler ici.")], ""),
 ("lea", "De toute façon, ne t'inquiète pas, Mathias.",
  "In any case, do not worry, Mathias.",
  [(279, "De toute façon, t'inquiète pas, Mathias.")], "Expanded ne"),
 ("lea", "Laisse-moi faire, ça va rentrer.",
  "Leave it to me, it will fit.",
  [(280, "Laisse-moi faire."), (281, "Ça va rentrer.")], ""),
]

OPENER = "Let's explore the conversation line by line and unpack the French phrases."

WALK = [
 (0, None,
  "'I found a solution for Nathalie Baye.' Noemie announces her scheduling breakthrough. "
  "The compound past 'j'ai trouve' expresses completed success with the feminine noun 'solution'."),
 (1, None,
  "'Ah, excellent. Show me that.' Mathias reacts with interest and demands to inspect the plan. "
  "The imperative 'montre-moi' pairs the verb with a hyphenated stressed pronoun."),
 (2, None,
  "'Here is Xavier Beauvois's schedule.' Noemie lays out the first production timetable. "
  "The presentative 'voila' introduces the masculine borrowed noun 'planning'."),
 (3, None,
  "'This one is Tonie Marshall's.' Noemie compares the two competing schedules. "
  "The demonstrative pronouns 'celui-ci' and 'celui de' replace masculine nouns elegantly."),
 (4, None,
  "'The shooting days are marked in red.' Noemie points out the color-coded days. "
  "The prepositional phrase 'en rouge' specifies the marking color of the schedule."),
 (5, None,
  "'Everything fits together perfectly here.' Noemie marvels at the puzzle pieces aligning. "
  "The reflexive verb 's'emboiter' means to interlock or fit snugly into place."),
 (6, None,
  "'Nathalie can do both movies.' Noemie concludes triumphantly. "
  "The modal verb 'peut' followed by the infinitive 'faire' expresses feasibility."),
 (7, None,
  "'No, I tell you that it does not work.' Mathias remains skeptical of the tight logistics. "
  "The idiom 'ca ne marche pas' denotes failure or impracticality in everyday French."),
 (8, None,
  "'Do you regret it, Mathias?' Noemie suddenly changes the subject to their secret past. "
  "The direct object pronoun 'le' refers back to their intimate encounter."),
 (9, None,
  "'That is not the topic, we are at work.' Mathias attempts to restore professional boundaries. "
  "The noun 'sujet' refers to the subject matter of conversation."),
 (10, None,
  "'Beauvois always exceeds the dates.' Mathias cites the director's notorious delays. "
  "The verb 'depasser' means to exceed or overrun allotted time frames."),
 (11, None,
  "'Nathalie needs two weeks of rest.' Mathias defends his star client's physical stamina. "
  "The expression 'avoir besoin de' expresses essential necessity."),
 (12, None,
  "'You said no, so you do not regret anything.' Noemie interprets his hesitation flirtatiously. "
  "The conjunction 'donc' introduces a logical deduction negated with 'ne ... rien'."),
 (13, None,
  "'Listen, Noemie, I prefer not to speak of it here.' Mathias deflects the personal banter. "
  "The pronoun 'en' replaces the unspoken topic before the infinitive 'parler'."),
 (14, None,
  "'In any case, do not worry, Mathias.' Noemie reassures him with confidence. "
  "The adverbial connector 'de toute facon' bridges the conversation gracefully."),
 (15, None,
  "'Leave it to me, it will fit.' Noemie concludes with breezy determination. "
  "The colloquial expression 'ca va rentrer' conveys making tight plans work."),
]

TRANSITION = "Now let's listen to the entire dialogue once more to lock in what you have learned."

OUTRO = ("Noemie demonstrates her logistical genius by aligning two competing film shoots for Nathalie Baye. "
         "Meanwhile, her playful chemistry with Mathias continues to test professional office decorum.")
CLOSING = ("lea", "Laisse-moi faire, ça va rentrer.")
