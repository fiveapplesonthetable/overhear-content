# Authoring module for dix-pour-cent s02e06 scene 11 (cues 229-260).
# Build: python3 tools/compose.py out/dix-pour-cent/s02e06/authoring/scene-11.py --out out/dix-pour-cent/s02e06/scene-11.json

ID = "dix-pour-cent-s02e06-scene-11"
SHOW = "dix-pour-cent"
SEASON = 2
EPISODE = 6
SCENE = 11
TITLE = "La répétition du discours  (Rehearsing the Speech)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "theo": "theo"}
LABELS = {"lea": "Juliette", "theo": "Le technicien"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S02E06"
SOURCE_FILE = "sources/dix-pour-cent/s02/e06.fr.dual.srt"
SOURCE_NOTE = ("Cues 229-260. On stage at the Cannes Palais, Juliette Binoche rehearses her opening festival speech "
               "while a technician tests her wireless earpiece. Adapted for A1 French.")

INTRO = ("On stage inside the grand festival auditorium in Cannes, Juliette Binoche rehearses her opening ceremony address. "
         "An audio technician tests a discreet wireless earpiece designed to prompt her speech lines seamlessly. "
         "Let's listen to the scene in French first.")

STORY = [
 ("lea", "Bonsoir à tous, merci d'être venus.",
  "Good evening everyone, thank you for coming.",
  [(230, "Bonsoir à tous"), (231, "Merci d'être venus.")], ""),
 ("lea", "C'est avec une immense fierté que je vous accueille ici.",
  "It is with immense pride that I welcome you here.",
  [(232, "C'est avec une immense fierté que je vous accueille ici,")], ""),
 ("lea", "Dans le plus bel endroit du monde: une salle de cinéma.",
  "In the most beautiful place in the world: a movie theater.",
  [(233, "dans le plus bel endroit du monde : une salle de cinéma.")], ""),
 ("theo", "J'ai votre oreillette. Vous voulez l'essayer?",
  "I have your earpiece. Do you want to try it?",
  [(237, "J'ai votre oreillette."), (238, "Vous voulez l'essayer ?")], ""),
 ("lea", "Comment ça fonctionne?",
  "How does it work?",
  [(240, "Comment ça fonctionne ?")], ""),
 ("theo", "Je peux vous montrer si vous voulez.",
  "I can show you if you like.",
  [(242, "Je peux vous montrer si vous voulez.")], ""),
 ("theo", "Ça ne vous dérange pas qu'on se tutoie?",
  "Do you mind if we speak informally?",
  [(244, "Ça ne vous dérange pas qu'on se tutoie ?")], ""),
 ("lea", "Non, pas du tout.",
  "No, not at all.",
  [(245, "Non, pas du tout.")], ""),
 ("theo", "Regardez droit devant vous, comme si je n'étais pas là.",
  "Look straight ahead, as if I were not here.",
  [(246, "regardez droit devant vous, comme si je n'étais pas là.")], ""),
 ("theo", "Je vous entends parfaitement. Ça fonctionne.",
  "I hear you perfectly. It works.",
  [(247, "Je vous entends parfaitement. Ça fonctionne.")], ""),
 ("lea", "D'accord, je vous entends aussi.",
  "Okay, I hear you too.",
  [(249, "D'accord."), (247, "Je vous entends")], "Adapted dialogue"),
 ("theo", "Ne répondez pas. Personne ne sait que vous avez une oreillette.",
  "Do not answer. No one knows that you have an earpiece.",
  [(248, "Ne répondez pas. Personne ne sait que vous avez une oreillette.")], ""),
 ("theo", "C'est juste une voix dans votre tête, comme vos propres pensées.",
  "It is just a voice in your head, like your own thoughts.",
  [(250, "C'est juste une voix dans votre tête."), (251, "Comme vos propres pensées.")], ""),
 ("lea", "Ah, oui! Je comprends maintenant.",
  "Oh, yes! I understand now.",
  [(253, "Ah, oui ! Je comprends maintenant.")], ""),
 ("theo", "Vous me recevez? Faites un pas en arrière.",
  "Do you receive me? Take a step back.",
  [(254, "Vous me recevez ?"), (255, "Faites un pas en arrière.")], ""),
 ("theo", "Très bien, elle est opérationnelle.",
  "Very good, it is operational.",
  [(246, "Bien"), (259, "Elle est opérationnelle.")], "Adapted conclusion"),
]

OPENER = "Let's explore the conversation line by line and unpack the French phrases."

WALK = [
 (0, None,
  "'Good evening everyone, thank you for coming.' Juliette greets the imaginary audience on stage. "
  "The polite expression 'merci d'etre venus' uses the past infinitive to thank guests for having arrived."),
 (1, None,
  "'It is with immense pride that I welcome you here.' Juliette delivers an emotional opening line. "
  "The noun phrase 'une immense fierte' conveys deep personal honor."),
 (2, None,
  "'In the most beautiful place in the world: a movie theater.' Juliette praises the cinema hall. "
  "The superlative structure 'le plus bel endroit' highlights the prestige of the venue."),
 (3, None,
  "'I have your earpiece. Do you want to try it?' The technician interrupts to fit the prompting device. "
  "The noun 'oreillette' refers to the discreet wireless ear receiver."),
 (4, None,
  "'How does it work?' Juliette asks about the technical operation. "
  "The question 'comment ca fonctionne' asks for a functional demonstration."),
 (5, None,
  "'I can show you if you like.' The technician offers a direct demonstration. "
  "The modal verb 'peux' expresses polite capability and assistance."),
 (6, None,
  "'Do you mind if we speak informally?' The technician asks to drop formal address. "
  "The reflexive verb 'se tutoyer' means to address one another with informal pronouns."),
 (7, None,
  "'No, not at all.' Juliette warmly accepts the informal address. "
  "The emphatic negative 'pas du tout' provides an immediate and friendly reassurance."),
 (8, None,
  "'Look straight ahead, as if I were not here.' The technician guides Juliette's stage posture. "
  "The conditional conjunction 'comme si' sets up an imaginary scenario."),
 (9, None,
  "'I hear you perfectly. It works.' The technician checks the sound levels through his microphone. "
  "The adverb 'parfaitement' confirms clear audio transmission."),
 (10, None,
  "'Okay, I hear you too.' Juliette speaks back instinctively into the open microphone. "
  "The adverb 'aussi' indicates reciprocal reception."),
 (11, None,
  "'Do not answer. No one knows that you have an earpiece.' The technician reminds her that the earpiece must remain a secret. "
  "The negative imperative 'ne repondez pas' warns her against speaking aloud."),
 (12, None,
  "'It is just a voice in your head, like your own thoughts.' The technician coaches her mental approach. "
  "The adverb 'juste' minimizes the intrusion of the prompting audio."),
 (13, None,
  "'Oh, yes! I understand now.' Juliette catches on to the technique. "
  "The present tense verb 'comprends' signals immediate comprehension."),
 (14, None,
  "'Do you receive me? Take a step back.' The technician tests the wireless range. "
  "The imperative 'faites un pas en arriere' commands spatial repositioning."),
 (15, None,
  "'Very good, it is operational.' The technician concludes the audio test successfully. "
  "The adjective 'operationnelle' confirms full readiness for the ceremony."),
]

TRANSITION = "Now let's listen to the entire dialogue once more to lock in what you have learned."

OUTRO = ("Juliette Binoche rehearses her Cannes opening speech under the guidance of a sound technician. "
         "Through a hidden wireless earpiece, she learns to receive prompting smoothly without breaking character.")
CLOSING = ("theo", "Très bien, elle est opérationnelle.")
