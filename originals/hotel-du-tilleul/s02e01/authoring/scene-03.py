# Authoring module for hotel-du-tilleul-s02e01-scene-03.
ID = 'hotel-du-tilleul-s02e01-scene-03'
SHOW = 'hotel-du-tilleul'
SEASON = 2
EPISODE = 1
SCENE = 3
TITLE = 'Verre et poussière  (Glass and Dust)'
LEVEL = 'A1 — débutant'
PAIR = 'fr-en'
LABELS = {'claire': 'Claire', 'nadia': 'Nadia', 'etienne': 'Étienne'}
INTRO = ('Claire pushes the narrow white door open, and morning light filters through dusty glass panes into a '
         'quiet forgotten room. Nadia and Etienne step inside behind her in amazement. Listen to the whole scene first.')
OPENER = "Let's step back into the dusty glass room and take it slowly."
TRANSITION = "Now let's listen to the whole scene again from the start."
OUTRO = ('Room 9 is a dry, sunlit glass tea room, and something tall is waiting under a white sheet in the '
         "corner. Let's find out what it is next time.")
CLOSING = ('etienne', "À tout à l'heure!")
STORY = [
    ('claire',
     "Regardez ces grandes fenêtres en verre, face au tilleul de la cour!",
     'Look at these tall glass windows, facing the courtyard linden tree!'),
    ('nadia',
     "Les volets sont fermés dehors, c'est pour ça que personne n'a rien vu depuis la cour!",
     "The shutters are closed outside, that's why nobody noticed anything from the courtyard!"),
    ('etienne',
     "Je me souviens maintenant! Mon oncle appelait ça le salon de thé d'hiver quand j'avais dix ans!",
     'Now I remember! My uncle called this the winter tea room when I was ten!'),
    ('claire',
     'Pourquoi cacher une si belle pièce derrière une bibliothèque?',
     'Why hide such a beautiful room behind a bookcase?'),
    ('etienne',
     "Le toit en verre a eu une fuite un printemps pluvieux, et personne n'avait d'argent pour le réparer.",
     'The glass roof leaked one rainy spring, and nobody had the money to fix it.'),
    ('nadia',
     "Regardez le sol en pierre, Étienne: il est sec, pas une goutte d'eau!",
     'Look at the stone floor, Etienne: it is dry, not one drop of water!'),
    ('claire',
     'La personne qui a réparé le toit de la cour a aussi réparé ce plafond!',
     'Whoever fixed the courtyard roof also fixed this ceiling!'),
    ('nadia',
     'Étienne, vous voyez combien de petites tables de café on peut mettre ici?',
     'Etienne, do you see how many little café tables we can fit in here?'),
    ('etienne',
     'Attendez! Pour garder notre protection du patrimoine, on a promis un café de lecture ouvert au public!',
     'Wait! To keep our heritage protection, we promised a reading café open to the public!'),
    ('claire',
     'Et voici exactement la pièce que la lettre de la mairie demandait!',
     'And here is exactly the room the City Hall letter asked for!'),
    ('nadia',
     'Du pain chaud, du thé chaud, le soleil du matin et zéro vent froid!',
     'Warm bread, hot tea, morning sun and zero cold wind!'),
    ('etienne',
     "Attendez, qu'est-ce qu'il y a dans le coin, sous ce grand drap blanc?",
     'Wait, what is in the corner, under that big white sheet?'),
]
WALK = [
    (1, None,
     ["'The shutters are closed outside, that's why nobody noticed anything from the courtyard!' The chunk",
      (None, "c'est pour ça que"),
      "is how French says 'that's why', literally 'it is for that that'."]),
    (2, 'Je me souviens maintenant!',
     ["'Now I remember!' French remembers 'oneself':",
      (None, 'Je me souviens'),
      "carries an extra little 'me' that English leaves out."]),
    (3, None,
     "'Why hide such a beautiful room behind a bookcase?' Claire asks with a bare infinitive, literally "
     "'why to hide', and French needs no 'do' or 'did' to make the question."),
    (4, None,
     ["'The glass roof leaked one rainy spring, and nobody had the money to fix it.' Etienne says the roof",
      (None, 'a eu une fuite'),
      "literally 'had a leak', rather than using a separate word for leaking."]),
    (5, None,
     ["'Look at the stone floor, Etienne: it is dry, not one drop of water!' A stone floor is",
      (None, 'le sol en pierre'),
      "literally 'the floor in stone': in French the material comes after the thing."]),
    (7, None,
     "'Etienne, do you see how many little cafe tables we can fit in here?' Nadia jokes with everyone, but "
     "she still gives her boss the polite 'you'."),
    (10, None,
     ["'Warm bread, hot tea, morning sun and zero cold wind!' Listen to",
      (None, 'Du pain chaud, du thé chaud'),
      "where French puts 'some' before the bread and tea, and the word for 'hot' after them."]),
]
