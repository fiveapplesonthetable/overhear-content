# Authoring module for dix-pour-cent s01e05 scene 10 (cues 177-204).
# Build: python3 tools/compose.py out/dix-pour-cent/s01e05/authoring/scene-10.py --out out/dix-pour-cent/s01e05/scene-10.json

ID = "dix-pour-cent-s01e05-scene-10"
SHOW = "dix-pour-cent"
SEASON = 1
EPISODE = 5
SCENE = 10
TITLE = "Envoyez des fleurs à Marie-Sophie  (Send Flowers to Marie-Sophie)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "noemie": "emilie", "mathias": "marcel"}
LABELS = {"lea": "Camille", "noemie": "Noémie", "mathias": "Mathias"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S01E05"
SOURCE_FILE = "sources/dix-pour-cent/s01/e05.fr.dual.srt"
SOURCE_NOTE = ("Cues 177-204. Camille is the viewpoint character (lea). Zinedine Soualem's brief visit asking about "
               "Almodóvar's next film is covered through Noémie's replies and narration, and Hervé's exclamation in "
               "cue 197 is given to Noémie to stay within three speaking roles.")

INTRO = ("In Mathias's office, Arlette and the head screenwriter Marie-Sophie Garnier have just dropped a bombshell: "
         "fed up with the arrogant soap star Jonathan Joubert after eight years of tantrums, the writers of Happy "
         "Ever After are going to kill off his beloved character, Doctor Ryan. Mathias steps out to the assistants' "
         "desks to try to save his client with a bouquet of flowers, just as the actor Zinedine Soualem walks in "
         "unannounced. Listen to the French first, without worrying about catching every word.")

STORY = [
 ("mathias", "Noémie, envoyez des fleurs à Marie-Sophie Garnier, s'il vous plaît.", "Noémie, send flowers to Marie-Sophie Garnier, please.",
  [(179, "Noémie, envoyez des fleurs à Marie-Sophie Garnier, s'il vous plaît")], ""),
 ("mathias", "Signez le mot: Chère Marie-Sophie, je suis désolé.", "Sign the note: Dear Marie-Sophie, I am sorry.",
  [(180, "Signez le mot"), (180, "Chère Marie-Sophie, je suis désolé")], "guillemets removed"),
 ("mathias", "Un nouveau départ. Signé Jonathan Joubert.", "A new start. Signed Jonathan Joubert.",
  [(181, "Nouveau départ"), (181, "Signé Jonathan Joubert")], ""),
 ("noemie", "Mathias, Zinedine Soualem est là.", "Mathias, Zinedine Soualem is here.",
  [(182, "Mathias, Zinedine Soualem est là")], ""),
 ("mathias", "Pas maintenant!", "Not now!",
  [(183, "Pas maintenant")], ""),
 ("noemie", "Non, Mathias n'est pas là.", "No, Mathias isn't here.",
  [(185, "Mathias n'est pas là"), (185, "Non")], "Noémie covering for Mathias"),
 ("noemie", "Il peut vous appeler quand il veut. Au revoir!", "He can call you whenever he wants. Goodbye!",
  [(190, "Il peut"), (190, "appeler quand il veut"), (192, "Au revoir")], "Zinedine's 'm'appeler' -> Noémie's 'vous appeler'"),
 ("noemie", "C'est bon, il est parti.", "It's fine, he's gone.",
  [(193, "C'est bon, il est parti")], ""),
 ("mathias", "N'oublie pas les fleurs pour Marie-Sophie Garnier.", "Don't forget the flowers for Marie-Sophie Garnier.",
  [(194, "N'oublie pas les fleurs pour Marie-Sophie Garnier")], ""),
 ("noemie", "Bien sûr. Interflora, s'il vous plaît.", "Of course. Interflora, please.",
  [(195, "Bien sûr"), (202, "Interflora, s'il vous plaît")], ""),
 ("lea", "C'est vrai qu'ils vont tuer Ryan?", "Is it true that they're going to kill off Ryan?",
  [(196, "C'est vrai qu'ils vont tuer Ryan")], ""),
 ("noemie", "Ce n'est pas possible!", "That's not possible!",
  [(197, "Pas possible")], "Hervé's line given to Noémie"),
 ("lea", "Ma mère va être très triste.", "My mother is going to be very sad.",
  [(198, "Ma mère va être")], "'dévastée' simplified to A1 'triste'"),
 ("lea", "Elle regarde la série tous les jours!", "She watches the series every day!",
  [(198, "Elle regarde"), (198, "tous les jours")], "'ça' -> 'la série'"),
 ("lea", "Si je lui dis ça, elle va organiser des manifestations!", "If I tell her that, she's going to organise protests!",
  [(199, "Si je lui dis, elle va organiser des")], "'manifs' written out in full"),
 ("lea", "Ça va faire du bruit dans le salon de coiffure de ma mère!", "That's going to make a stir in my mother's hairdressing salon!",
  [(201, "dans le salon de ma mère")], "'un sacré buzz' simplified to A1 'du bruit'"),
]

OPENER = ("Let's walk through it step by step. Mathias comes out of his office and gives Noémie an urgent task.")

WALK = [
 (0, None,
  "'Noémie, send flowers to Marie-Sophie Garnier, please.' Notice that Mathias uses the formal command here in the "
  "open office."),
 (1, None,
  "'Sign the note: Dear Marie-Sophie, I am sorry.' The adjective for 'dear' is in its feminine form with a grave "
  "accent. Of course Jonathan Joubert has no idea he is apologising."),
 (2, None,
  "'A new start. Signed Jonathan Joubert.' Mathias is Dictating a fake apology on his actor's behalf."),
 (3, None,
  "'Mathias, Zinedine Soualem is here.' Zinedine Soualem is another actor on Mathias's list, and he has just "
  "walked in."),
 (4, None,
  "'Not now!' Mathias ducks back into his office and shuts the door."),
 (5, None,
  "'No, Mathias isn't here.' Loyal Noémie lies without blinking. Zinedine asks her if Mathias knows he speaks "
  "Spanish for Almodóvar's next film."),
 (6, None,
  "'He can call you whenever he wants. Goodbye!' Literally 'when he wants'. Noémie politely sends the actor on his "
  "way."),
 (7, None,
  "'It's fine, he's gone.' The verb 'to leave' takes the verb 'to be' as its helper in the past. Mathias pokes his "
  "head back out."),
 (8, None,
  "'Don't forget the flowers for Marie-Sophie Garnier.' Now that they are alone, Mathias switches back to the "
  "informal command with Noémie."),
 (9, None,
  "'Of course. Interflora, please.' As Noémie orders the flowers, Camille and Hervé talk about the news."),
 (10, None,
  "'Is it true that they're going to kill off Ryan?' Near future with the verb 'to go' plus 'kill'."),
 (11, None,
  "'That's not possible!' Doctor Ryan is the star of the daytime soap."),
 (12, None,
  "'My mother is going to be very sad.' Camille's mother in the south of France is a huge fan."),
 (13, None,
  "'She watches the series every day!' Literally 'all the days', the standard French phrase for 'every day'."),
 (14, None,
  "'If I tell her that, she's going to organise protests!' The indirect object word before 'say' means 'to her'."),
 (15, None,
  "'That's going to make a stir in my mother's hairdressing salon!' Literally 'make noise in the hairdressing "
  "salon of my mother'. And that gives Camille an idea."),
]

TRANSITION = "Now let's listen to the whole scene again."

OUTRO = ("Camille knows just how much the women in her mother's hairdressing salon love Doctor Ryan. Meanwhile, "
         "out in the countryside at the chateau, Andréa and Gabriel have a plan of their own for Julie Gayet and "
         "JoeyStarr. See you in the next scene.")
CLOSING = ("lea", "Pauvre Ryan!")

if __name__ == "__main__":
    import subprocess, sys
    from pathlib import Path
    root = Path(__file__).resolve().parents[4]
    out = Path(__file__).resolve().parents[1] / f"scene-{SCENE:02d}.json"
    sys.exit(subprocess.call([sys.executable, str(root / "tools/compose.py"), __file__, "--out", str(out)], cwd=root))
