# Authoring module for dix-pour-cent s02e01 scene 13 (cues 366-375).
# Build: python3 tools/compose.py out/dix-pour-cent/s02e01/authoring/scene-13.py --out out/dix-pour-cent/s02e01/scene-13.json

ID = "dix-pour-cent-s02e01-scene-13"
SHOW = "dix-pour-cent"
SEASON = 2
EPISODE = 1
SCENE = 13
TITLE = "La patate chaude  (The Hot Potato)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "gabriel": "theo"}
LABELS = {"lea": "Andréa", "gabriel": "Gabriel"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S02E01"
SOURCE_FILE = "sources/dix-pour-cent/s02/e01.fr.dual.srt"
SOURCE_NOTE = ("Cues 366-375. Gabriel phones Andréa to ask why Mathias passed Virginie Efira to him instead of her. "
               "Gabriel realizes Mathias unloaded a risky situation on him so he would take the blame if it backfired. "
               "Adapted for A1 French.")

INTRO = ("Struggling to handle the fallout from Virginie Efira's scandal, Gabriel calls Andrea on the phone. "
         "Andrea explains why Mathias gave Virginie to him rather than to her, revealing Mathias's cunning calculation. "
         "Let's listen to the scene in French first.")

STORY = [
 ("gabriel", "Andréa? Pourquoi moi et pas vous pour Virginie?",
  "Andréa? Why me and not you for Virginie?",
  [(366, "Pourquoi moi et pas vous")], "Added names for clarity"),
 ("lea", "Parce que j'aurais dit non.",
  "Because I would have said no.",
  [(367, "Parce que j'aurais dit non")], ""),
 ("gabriel", "Bien sûr, il savait que je serais moins méfiant.",
  "Of course, he knew I would be less suspicious.",
  [(368, "il savait que je serais moins")], "Adjusted to masculine agreement"),
 ("gabriel", "Il me refile une patate chaude!",
  "He is passing me a hot potato!",
  [(368, "Il me refile une patate chaude")], ""),
 ("gabriel", "Comme ça, si Virginie se brouille avec l'agence, c'est ma faute.",
  "That way, if Virginie falls out with the agency, it is my fault.",
  [(369, "si Virginie se brouille avec l'agence, c'est ma faute")], ""),
 ("gabriel", "Merci, Mathias!",
  "Thanks, Mathias!",
  [(370, "Merci, Mathias")], ""),
 ("lea", "Je n'avais pas vu ça.",
  "I had not seen that.",
  [(371, "Je n'avais pas vu ça")], ""),
 ("lea", "C'est exactement le genre de chose qu'il ferait!",
  "It is exactly the kind of thing he would do!",
  [(372, "C'est exactement le genre de chose qu'il ferait")], ""),
 ("gabriel", "Pauvre de moi. Attends...",
  "Poor me. Wait...",
  [(373, "Pauvre toi. Attends")], "Adapted to first person"),
 ("lea", "Je dois y aller, je dois parler au maire.",
  "I have to go, I have to speak to the mayor.",
  [(374, "Je dois y aller, je dois parler au maire")], ""),
 ("gabriel", "Tiens-moi au courant. Prends soin de toi.",
  "Keep me posted. Take care of yourself.",
  [(375, "Tiens-moi au courant. Prends soin de toi")], ""),
 ("lea", "D'accord, à bientôt Gabriel.",
  "All right, see you soon Gabriel.",
  [], "Natural telephone closure"),
 ("gabriel", "Bonne chance à Couchey.",
  "Good luck in Couchey.",
  [], "Warm sign-off line"),
]

OPENER = "Gabriel uncovers Mathias's trick. Let us examine the lines with English notes."

WALK = [
 (0, None, "'Andrea? Why me and not you for Virginie?' Gabriel asks why Mathias picked him. Pourquoi means why."),
 (1, None, "'Because I would have said no.' Andrea uses the past conditional j'aurais dit to explain her reaction."),
 (2, None, "'Of course, he knew I would be less suspicious.' Mefiant is an adjective meaning wary or suspicious."),
 (3, None, "'He is passing me a hot potato!' Refiler is an informal French verb meaning to pass along or dump onto someone."),
 (4, None, "'That way, if Virginie falls out with the agency, it is my fault.' Se brouiller means to quarrel or fall out with."),
 (5, None, "'Thanks, Mathias!' Gabriel exclaims with sarcasm. Merci is used ironically here."),
 (6, None, "'I had not seen that.' Andrea admits she had not realized Mathias's ulterior motive."),
 (7, None, "'It is exactly the kind of thing he would do!' Le genre de chose means the type or kind of thing."),
 (8, None, "'Poor me. Wait...' Attends is the familiar imperative of attendre, meaning wait."),
 (9, None, "'I have to go, I have to speak to the mayor.' Andrea cuts the call short to attend her ceremony in Couchey."),
 (10, None, "'Keep me posted. Take care of yourself.' Tenir au courant is a common idiom meaning to keep someone informed."),
 (11, None, "'All right, see you soon Gabriel.' A bientot is a friendly parting phrase meaning see you soon."),
 (12, None, "'Good luck in Couchey.' Bonne chance is the standard French wish for good luck."),
]

TRANSITION = "Now listen to the full phone call once more without interruption."
OUTRO = ("Gabriel now understands how Mathias manipulated him into taking on the crisis. "
         "Meanwhile, Andrea arrives at the town hall of Couchey to receive her mother's medal. "
         "Here is our closing sentence.")
CLOSING = ("gabriel", "Bonne chance à Couchey.")
