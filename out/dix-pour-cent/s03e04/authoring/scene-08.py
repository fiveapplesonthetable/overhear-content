# Authoring module for dix-pour-cent s03e04 scene 08 (cues 637-647).
# Build: python3 tools/compose.py out/dix-pour-cent/s03e04/authoring/scene-08.py --out out/dix-pour-cent/s03e04/scene-08.json

ID = "dix-pour-cent-s03e04-scene-08"
SHOW = "dix-pour-cent"
SEASON = 3
EPISODE = 4
SCENE = 8
TITLE = "La scène d'agonie  (The Agony Scene)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "theo": "theo"}
LABELS = {"lea": "Isabelle Huppert", "theo": "Le Réalisateur"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S03E04"
SOURCE_FILE = "sources/dix-pour-cent/s03/e04.fr.dual.srt"
SOURCE_NOTE = ("Cues 637-647. On a period movie set, Isabelle Huppert delivers a dramatic and poignant "
               "deathbed scene until the director calls cut. Adapted for A1 French.")

INTRO = ("On the movie set of a historical costume drama, Isabelle Huppert performs a dramatic death scene. "
         "Her character bids farewell to her lost love before the director calls cut with praise. "
         "Let's listen to the scene in French first.")

OPENER = "Let's explore the conversation line by line and unpack the French phrases."
TRANSITION = "Now let's listen to the entire dialogue once more to lock in what you have learned."

STORY = [
 ("lea", "Je te pardonne tout, mon enfant.",
  "I forgive you for everything, my child.",
  [(637, "Je te pardonne, mon enfant.")], "Deathbed forgiveness"),
 ("lea", "Ah, j'ai très mal à la jambe.",
  "Ah, my leg hurts very badly.",
  [(638, "Ah, ma jambe.")], "Pain expression"),
 ("lea", "Vous allez me couper la jambe?",
  "Are you going to cut off my leg?",
  [(639, "Vous allez couper ma jambe.")], "Fearing amputation"),
 ("theo", "Non, madame, soyez sans crainte.",
  "No, madam, have no fear.",
  [(640, "Non, soyez sans crainte.")], "Reassurance"),
 ("lea", "Henri, je te vois dans la lumière.",
  "Henri, I see you in the light.",
  [(641, "Henri, je te vois.")], "Visions of beloved"),
 ("lea", "Henri, attends-moi, je te rejoins.",
  "Henri, wait for me, I am joining you.",
  [(642, "Henri, je te rejoins.")], "Rejoining beloved"),
 ("lea", "Promettez-moi une dernière chose avant ma mort.",
  "Promise me one last thing before my death.",
  [(643, "Promettez-moi que mon cœur ira rejoindre le sien.")], "Final wish"),
 ("lea", "Mon cœur ira rejoindre le sien.",
  "My heart will go join his.",
  [(643, "Promettez-moi que mon cœur ira rejoindre le sien.")], "Romantic vow"),
 ("theo", "Je vous le promets, reposez en paix.",
  "I promise you, rest in peace.",
  [(645, "Je vous le promets.")], "Solemn promise"),
 ("lea", "Adieu, le monde s'efface lentement.",
  "Farewell, the world is slowly fading.",
  [(644, "À la flèche.")], "Final breath"),
 ("theo", "Coupez! C'est dans la boîte!",
  "Cut! That is a wrap on this take!",
  [(646, "Coupez, coupez.")], "Director calls cut"),
 ("theo", "Magnifique, Isabelle, bravo pour cette scène.",
  "Magnificent, Isabelle, bravo for this scene.",
  [(647, "Magnifique, Isabelle. Bravo.")], "Praising performance"),
 ("lea", "Merci, cette prise était très intense.",
  "Thank you, this take was very intense.",
  [(647, "Magnifique, Isabelle. Bravo.")], "Actor response"),
 ("theo", "Votre émotion était absolument parfaite.",
  "Your emotion was absolutely perfect.",
  [(647, "Magnifique, Isabelle. Bravo.")], "Final praise"),
]

WALK = [
 (0, None,
  "'I forgive you for everything, my child.' Isabelle begins her character's deathbed scene. "
  "The verb 'pardonner' takes an indirect object."),
 (1, None,
  "'Ah, my leg hurts very badly.' The character cries out in agony. "
  "The expression 'avoir mal a' indicates bodily pain."),
 (2, None,
  "'Are you going to cut off my leg?' The character fears surgical amputation. "
  "The near future 'vous allez couper' expresses imminent action."),
 (3, None,
  "'No, madam, have no fear.' The co-star comforts her in character. "
  "The formal subjunctive 'soyez sans crainte' means do not be afraid."),
 (4, None,
  "'Henri, I see you in the light.' The character experiences a vision of her lost love. "
  "The noun 'lumiere' signifies light."),
 (5, None,
  "'Henri, wait for me, I am joining you.' She speaks her final words to her beloved. "
  "The verb 'rejoindre' means to rejoin or meet up with."),
 (6, None,
  "'Promise me one last thing before my death.' The dying heroine asks for a solemn vow. "
  "The imperative 'promettez-moi' makes a dramatic request."),
 (7, None,
  "'My heart will go join his.' She declares an eternal romantic bond. "
  "The possessive pronoun 'le sien' stands for his heart."),
 (8, None,
  "'I promise you, rest in peace.' The doctor makes a solemn deathbed pledge. "
  "The formula 'reposez en paix' is equivalent to rest in peace."),
 (9, None,
  "'Farewell, the world is slowly fading.' The heroine breathes her final breath. "
  "The farewell 'adieu' marks a permanent departure."),
 (10, None,
  "'Cut! That is a wrap on this take!' The director halts the filming. "
  "The French phrase 'c'est dans la boite' means it is safely in the can."),
 (11, None,
  "'Magnificent, Isabelle, bravo for this scene.' The director praises the actress enthusiastically. "
  "The exclamation 'bravo' expresses warm approval."),
 (12, None,
  "'Thank you, this take was very intense.' Isabelle steps out of character. "
  "The feminine noun 'prise' refers to a film take."),
 (13, None,
  "'Your emotion was absolutely perfect.' The director reiterates his admiration. "
  "The feminine noun 'emotion' describes deep feeling."),
]

OUTRO = ("The crew applauds Isabelle's remarkable performance in the deathbed scene. "
         "Capturing such deep grief requires immense concentration and emotional stamina. "
         "Now, let's review the scene once more.")

CLOSING = ("theo", "Magnifique, Isabelle, bravo pour cette scène.")
