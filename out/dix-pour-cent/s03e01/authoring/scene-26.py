# Authoring module for dix-pour-cent s03e01 scene 26 (cues 1020-1033).
# Build: python3 tools/compose.py overhear-content/out/dix-pour-cent/s03e01/authoring/scene-26.py --out overhear-content/out/dix-pour-cent/s03e01/scene-26.json

ID = "dix-pour-cent-s03e01-scene-26"
SHOW = "dix-pour-cent"
SEASON = 3
EPISODE = 1
SCENE = 26
TITLE = "Une sélection de films  (A Film Selection)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "jean": "theo"}
LABELS = {"lea": "Andréa", "jean": "Jean"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S03E01"
SOURCE_FILE = "sources/dix-pour-cent/s03/e01.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 1020-1033. Jean Dujardin prepares to leave his retreat and return to Paris with Andrea. "
    "Before leaving, he borrows a film and asks Andrea to make him a movie selection."
)

INTRO = (
    "In his country house, actor Jean Dujardin is finally ready to return to Paris with Andrea. "
    "Before they hit the road, he looks through some films and asks for her help. "
    "Listen to the scene in French first. Don't worry about catching every word."
)

STORY = [
    ("jean", "Allez, c'est l'heure d'y aller.", "Come on, it is time to go.",
     [(1020, "Allez, c'est l'heure d'y aller")], "Jean grabs his things to leave"),
    ("jean", "Dis, c'est celui-là, le film?", "Tell me, is this the movie?",
     [(1021, "Dis, c'est celui-là, le film")], "Jean looks at a DVD case"),
    ("jean", "Où Depardieu a pris une cuite?", "Where Depardieu got totally drunk?",
     [(1021, "où Depardieu s'est pris une cuite")], ""),
    ("jean", "Pour sortir de son rôle?", "To get out of his character?",
     [(1021, "pour sortir de son rôle")], ""),
    ("lea", "Oui, c'est exactement ça.", "Yes, that is exactly it.",
     [(1022, "C'est ça")], "Andrea nods with a smile"),
    ("jean", "Je peux te l'emprunter?", "Can I borrow it from you?",
     [(1023, "Je peux t'emprunter")], ""),
    ("lea", "Bien sûr, vas-y.", "Of course, go ahead.",
     [(1024, "Vas-y")], ""),
    ("lea", "S'il y en a d'autres qui t'intéressent...", "If there are others that interest you...",
     [(1025, "S'il y en a d'autres qui t'intéressent")], ""),
    ("lea", "Prends tout, c'est pour toi.", "Take everything, it is for you.",
     [(1026, "c'est toi")], ""),
    ("jean", "Tu sais quoi?", "You know what?",
     [(1027, "Tu sais quoi")], ""),
    ("jean", "Tu n'as qu'à me faire une sélection.", "Just put together a selection for me.",
     [(1028, "T'as qu'à me faire une sélection, toi")], ""),
    ("lea", "Si tu veux, pas de problème.", "If you want, no problem.",
     [(1029, "Si tu veux")], ""),
    ("lea", "J'ai tout ce qu'il faut à Paris.", "I have everything needed in Paris.",
     [(1030, "J'ai tout ce qu'il faut")], ""),
    ("jean", "Mais on n'a pas les mêmes goûts!", "But we do not have the same tastes!",
     [(1031, "Mais y en a pas forcément les mêmes")], ""),
    ("lea", "Justement, c'est parfait.", "Exactly, that is perfect.",
     [(1033, "Justement")], "Andrea smiles as they get ready to leave"),
]

OPENER = "Let's walk through this relaxed conversation between Andrea and Jean step by step."

WALK = [
    (0, None,
     "'Come on, it is time to go.' Jean announces that he is finally ready to leave."),
    (1, None,
     "'Tell me, is this the movie?' Jean spots an interesting film on the shelf."),
    (2, None,
     "'Where Depardieu got totally drunk?' Jean asks about the legendary story of the actor."),
    (3, None,
     "'To get out of his character?' Jean explains the method used to leave a difficult role."),
    (4, None,
     "'Yes, that is exactly it.' Andrea confirms the anecdote about the famous movie."),
    (5, None,
     "'Can I borrow it from you?' Jean asks politely to take the film with him."),
    (6, None,
     "'Of course, go ahead.' Andrea readily agrees to lend him the DVD."),
    (7, None,
     "'If there are others that interest you...' Andrea generously offers more choices from the shelf."),
    (8, None,
     "'Take everything, it is for you.' Andrea insists that he feel completely free to take them."),
    (9, None,
     "'You know what?' Jean has a sudden spontaneous idea for his agent."),
    (10, None,
     "'Just put together a selection for me.' Jean asks Andrea to pick movies for him to watch."),
    (11, None,
     "'If you want, no problem.' Andrea happily accepts the fun assignment from her star client."),
    (12, None,
     "'I have everything needed in Paris.' Andrea mentions the extensive film library at her apartment."),
    (13, None,
     "'We do not have the same tastes!' Jean points out that their movie preferences differ."),
    (14, None,
     "'Exactly, that is perfect.' Andrea notes that different tastes will help him discover new films."),
]

TRANSITION = "Now listen to the whole scene again at normal speed, and see how much more you catch."
OUTRO = "Jean Dujardin is finally ready to return to Paris, borrowing a film and asking Andrea to curate a movie list for him."
CLOSING = ("jean", "Allez, c'est l'heure d'y aller.")
