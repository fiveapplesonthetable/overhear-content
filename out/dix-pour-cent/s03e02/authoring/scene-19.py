# Authoring module for dix-pour-cent s03e02 scene 19 (cues 857-901).
# Build: python3 tools/compose.py out/dix-pour-cent/s03e02/authoring/scene-19.py --out out/dix-pour-cent/s03e02/scene-19.json

ID = "dix-pour-cent-s03e02-scene-19"
SHOW = "dix-pour-cent"
SEASON = 3
EPISODE = 2
SCENE = 19
TITLE = "L'avant-première du film  (The Film Premiere)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "julien": "theo", "gabriel": "marcel"}
LABELS = {"lea": "Sofia", "julien": "Julien", "gabriel": "Gabriel"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S03E02"
SOURCE_FILE = "sources/dix-pour-cent/s03/e02.fr.dual.srt"
SOURCE_NOTE = ("Cues 857-886. At the cinema premiere, director Julien takes the stage to introduce his bold indie film, "
               "thanking star Sofia and his dedicated agent Gabriel Sarda. Adapted for A1 French.")

INTRO = ("At a crowded Paris cinema, director Julien takes the stage alongside lead actress Sofia to introduce their indie feature film. "
         "In a moving tribute, Julien publicly thanks Gabriel for saving the production. "
         "Let's listen to the scene in French first.")

STORY = [
 ("julien", "Bonsoir à tous, merci d'être là!",
  "Good evening everyone, thank you for being here!",
  [(859, "Bonsoir à vous."), (860, "merci d'être là.")], "Julien welcomes the audience"),
 ("julien", "Vous allez voir notre film ce soir.",
  "You are going to see our movie tonight.",
  [(861, "Le film que vous allez voir,")], "Julien introduces the screening"),
 ("julien", "C'est un rêve artistique complètement fou!",
  "It is a completely crazy artistic dream!",
  [(870, "ce rêve complètement fou.")], "Julien describes the project"),
 ("lea", "Nous avons partagé une belle aventure.",
  "We shared a beautiful adventure.",
  [(870, "m'avoir suivi")], "Sofia reflects on the work"),
 ("julien", "Merci à toi Sofia, actrice merveilleuse!",
  "Thank you to you Sofia, wonderful actress!",
  [(872, "Merci à toi, Sophia,")], "Julien praises Sofia"),
 ("lea", "Merci Julien pour ta grande confiance.",
  "Thank you Julien for your great trust.",
  [(873, "fait confiance")], "Sofia returns the compliment"),
 ("julien", "Je remercie aussi mon agent Gabriel.",
  "I also thank my agent Gabriel.",
  [(876, "merci à mon agent, Gabriel Sarda.")], "Julien acknowledges Gabriel"),
 ("julien", "Je te remercie du fond du cœur.",
  "I thank you from the bottom of the heart.",
  [(878, "Merci du fond du cœur.")], "Julien expresses deep gratitude"),
 ("gabriel", "C'est mon travail de vous soutenir.",
  "It is my job to support you.",
  [(880, "tu t'es battu.")], "Gabriel stays modest"),
 ("julien", "Tu as remué ciel et terre.",
  "You moved heaven and earth.",
  [(881, "T'as remué ciel et terre")], "Julien highlights Gabriel's efforts"),
 ("julien", "Grâce à toi, le film existe!",
  "Thanks to you, the film exists!",
  [(883, "Et le film est là.")], "Julien credits Gabriel"),
 ("gabriel", "Bravo Julien, nous sommes très fiers.",
  "Bravo Julien, we are very proud.",
  [(884, "merci à toi, Gabriel,")], "Gabriel congratulates Julien"),
 ("julien", "Bonne projection du film à tous!",
  "Enjoy the film screening, everyone!",
  [(886, "Bonne projection à vous.")], "Julien opens the screening"),
 ("lea", "Que la séance commence enfin, Gabriel!",
  "Let the screening finally begin, Gabriel!",
  [(875, "bon film.")], "Sofia looks forward to the film"),
]

OPENER = "Let's examine how Julien and Sofia present their new movie step by step."

WALK = [
 (0, None,
  "'Good evening everyone, thank you for being here!' Julien welcomes the packed theater audience warmly. The verb meaning 'to be' pairs naturally with the noun for 'good evening' in everyday conversation."),
 (1, None,
  "'You are going to see our movie tonight.' Julien announces the premiere presentation of his film. Notice how 'are going' leads directly into the noun meaning 'film'."),
 (2, None,
  "'It is a completely crazy artistic dream!' Julien describes his visionary, eccentric cinematic project. The key noun here means 'dream', anchored by its matching French article."),
 (3, None,
  "'We shared a beautiful adventure.' Sofia reflects on the intense creative journey of filming. This conversational past tense combines a helper verb with the past participle for 'shared'."),
 (4, None,
  "'Thank you to you Sofia, wonderful actress!' Julien honors his lead actress with glowing praise. The key noun here means 'actress', anchored by its matching French article."),
 (5, None,
  "'Thank you Julien for your great trust.' Sofia expresses appreciation for his creative collaboration. The adjective meaning 'great' takes its feminine form here to match the noun it describes."),
 (6, None,
  "'I also thank my agent Gabriel.' Julien turns the spotlight onto his representative. Notice how 'thank' leads directly into the noun meaning 'agent'."),
 (7, None,
  "'I thank you from the bottom of the heart.' Julien offers heartfelt emotional gratitude to Gabriel. The informal 'you' form around 'thank' marks a direct, personal relationship."),
 (8, None,
  "'It is my job to support you.' Gabriel modestly acknowledges his duty as their agent. Notice how 'to support' leads directly into the noun meaning 'job'."),
 (9, None,
  "'You moved heaven and earth.' Julien reminds the crowd how tirelessly Gabriel secured funding. Julien uses the casual singular 'you' with 'have', showing close familiarity."),
 (10, None,
  "'Thanks to you, the film exists!' Julien credits Gabriel for saving the entire production. Dropping the subject pronoun turns the verb for 'exists' into a direct, punchy command."),
 (11, None,
  "'Bravo Julien, we are very proud.' Gabriel congratulates the director on his major milestone. The descriptive adjective for 'proud' agrees in gender and number with its noun."),
 (12, None,
  "'Enjoy the film screening, everyone!' Julien invites the audience to enjoy the movie. The key noun here means 'screening', anchored by its matching French article."),
 (13, None,
  "'Let the screening finally begin, Gabriel!' Sofia looks forward to the audience's reaction. Notice how 'begin' leads directly into the noun meaning 'screening'."),
]

TRANSITION = "Now let's listen to the scene once more from start to finish."

OUTRO = ("Julien's passionate speech honors Sofia and Gabriel before the screening begins, celebrating a hard-won artistic triumph. "
         "Let's review the key expressions and vocabulary from this scene.")

CLOSING = ("lea", "Que la séance commence enfin, Gabriel!")
