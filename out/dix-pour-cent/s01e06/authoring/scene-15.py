# Authoring module for dix-pour-cent s01e06 scene 15 (cues 423-439).
# Build: python3 tools/compose.py out/dix-pour-cent/s01e06/authoring/scene-15.py --out out/dix-pour-cent/s01e06/scene-15.json

ID = "dix-pour-cent-s01e06-scene-15"
SHOW = "dix-pour-cent"
SEASON = 1
EPISODE = 6
SCENE = 15
TITLE = "L'audition de Sofia  (Sofia's Audition)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "constance": "emilie", "gabriel": "theo"}
LABELS = {"lea": "Sofia", "constance": "Constance", "gabriel": "Gabriel"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S01E06"
SOURCE_FILE = "sources/dix-pour-cent/s01/e06.fr.dual.srt"
SOURCE_NOTE = ("Cues 423-439. Gabriel's opening encouragement is added before Sofia enters the studio; colloquial "
               "'se frotter à moi' in cue 433 is adapted to 'se battre avec moi' for A1 learners.")

INTRO = ("At the dance and casting studio, Sofia arrives for her big callback in Luc Besson's action film. Gabriel "
         "urges her to stay natural and relaxed, but when the casting director asks for the action scene, Sofia launches "
         "into an over-the-top combat performance that takes everyone by surprise. Let's listen to the scene in French first.")

STORY = [
 ("gabriel", "Ne t'inquiète pas, sois naturelle.",
  "Don't worry, be natural.",
  [(424, "On y va")], "Gabriel's encouragement"),
 ("constance", "Sofia, on y va?",
  "Sofia, shall we go?",
  [(423, "Sofia"), (424, "On y va")], ""),
 ("lea", "Oui, je suis prête.",
  "Yes, I am ready.",
  [(425, "Désolée, oui")], "A1 adaptation"),
 ("lea", "Je m'appelle Sofia Leprince, j'ai 25 ans.",
  "My name is Sofia Leprince, I am twenty-five years old.",
  [(426, "Je m'appelle Sofia Leprince, j'ai 25 ans")], ""),
 ("lea", "Et mon agent est Gabriel Sarda chez ASK.",
  "And my agent is Gabriel Sarda at ASK.",
  [(427, "et mon agent est Gabriel Sarda chez ASK")], ""),
 ("constance", "Parfait! On commence tout de suite.",
  "Perfect! We start right away.",
  [(428, "Parfait"), (428, "On commence")], ""),
 ("constance", "D'abord la chorégraphie, ensuite votre scène, d'accord?",
  "First the choreography, then your scene, okay?",
  [(429, "D'abord la chorégraphie, ensuite votre scène, d'accord")], ""),
 ("lea", "D'accord, quand vous voulez.",
  "Okay, whenever you want.",
  [(430, "D'accord"), (431, "Quand vous voulez")], ""),
 ("lea", "Ils veulent se battre avec moi?",
  "They want to fight with me?",
  [(433, "Ils veulent se frotter à moi")], "'se frotter' -> 'se battre'"),
 ("lea", "Je cours plus vite qu'eux!",
  "I run faster than them!",
  [(434, "Je cours plus vite qu'eux")], ""),
 ("lea", "Maintenant je suis là, maintenant je ne suis plus là!",
  "Now I am here, now I am no longer here!",
  [(435, "Maintenant je suis là, maintenant je suis plus là")], "Restored 'ne'"),
 ("lea", "Vous me voyez atterrir comme une héroïne?",
  "Do you see me landing like a heroine?",
  [(436, "Vous me voyez"), (436, "atterrir comme")], "Simplified Lara Croft reference"),
 ("constance", "Ce n'est pas du tout ce que j'avais demandé.",
  "This is not at all what I had asked for.",
  [(438, "C'est pas du tout ce que j'avais demandé")], "Restored 'ne'"),
]

OPENER = "Now let's walk through the audition scene line by line and examine the key French phrases."

WALK = [
 (0, None,
  "'Don't worry, be natural.' In the studio hallway, Gabriel reassures his nervous client. The imperative form of the verb "
  "to worry uses the reflexive pronoun after the negative particle."),
 (1, None,
  "'Sofia, shall we go?' The casting director opens the door and calls her in. The pronoun for there combines with the verb to "
  "go to form the everyday phrase shall we begin."),
 (2, None,
  "'Yes, I am ready.' Sofia steps forward with a polite smile. The feminine adjective takes an extra letter at the end."),
 (3, None,
  "'My name is Sofia Leprince, I am twenty-five years old.' Facing the camera, she introduces herself. Remember that French "
  "expresses age with the verb to have."),
 (4, None,
  "'And my agent is Gabriel Sarda at ASK.' She proudly adds her agency representation."),
 (5, None,
  "'Perfect! We start right away.' Constance nods briskly and sets the pace."),
 (6, None,
  "'First the choreography, then your scene, okay?' She lays out the audition schedule. The adverb for first introduces "
  "the sequence."),
 (7, None,
  "'Okay, whenever you want.' Sofia agrees politely. The phrase literally says when you want."),
 (8, None,
  "'They want to fight with me?' Launching straight into her dialogue, Sofia shouts with intense energy. The reflexive verb to fight takes the "
  "preposition with."),
 (9, None,
  "'I run faster than them!' She boasts about her speed. The comparative adverb for more is followed by the stressed pronoun "
  "for them."),
 (10, None,
  "'Now I am here, now I am no longer here!' She jumps around the room. The negative particle combined with more means no "
  "longer or not anymore."),
 (11, None,
  "'Do you see me landing like a heroine?' She strikes a dramatic pose. The verb to see takes the direct object pronoun me."),
 (12, None,
  "'This is not at all what I had asked for.' Staring in deadpan silence, Constance stops her. Notice the past perfect tense "
  "describing an earlier instruction."),
]

TRANSITION = "Let's listen to Sofia's audition one more time from beginning to end."

OUTRO = ("Sofia gave the audition everything she had, but her intense kung-fu styling was not what Constance had in "
         "mind. Remember the phrase for starting right away: all of a continuation.")

CLOSING = ("constance", "Ce n'est pas du tout ce que j'avais demandé.")
