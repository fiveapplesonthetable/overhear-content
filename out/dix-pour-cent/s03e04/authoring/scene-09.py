# Authoring module for dix-pour-cent s03e04 scene 09 (cues 648-671).
# Build: python3 tools/compose.py out/dix-pour-cent/s03e04/authoring/scene-09.py --out out/dix-pour-cent/s03e04/scene-09.json

ID = "dix-pour-cent-s03e04-scene-09"
SHOW = "dix-pour-cent"
SEASON = 3
EPISODE = 4
SCENE = 9
TITLE = "Pas une machine  (Not a Machine)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "theo": "theo"}
LABELS = {"lea": "Isabelle Huppert", "theo": "L'Assistant"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S03E04"
SOURCE_FILE = "sources/dix-pour-cent/s03/e04.fr.dual.srt"
SOURCE_NOTE = ("Cues 648-671. When an assistant pushes for yet another tight shot, Isabelle Huppert refuses, "
               "arguing that after seven death takes she cannot die on cue like a machine. Adapted for A1 French.")

INTRO = ("Behind the video monitors, the assistant director insists on shooting one more tight take of the death scene. "
         "Exhausted after seven agonizing takes, Isabelle Huppert puts her foot down. "
         "Let's listen to their confrontation in French first.")

OPENER = "Let's explore the conversation line by line and unpack the French phrases."
TRANSITION = "Now let's listen to the entire dialogue once more to lock in what you have learned."

STORY = [
 ("theo", "Isabelle, on va faire une dernière prise.",
  "Isabelle, we are going to do one last take.",
  [(650, "Isabelle, Isabelle, Isabelle."), (651, "On va faire une dernière prise en plan plus serré.")], "Requesting another take"),
 ("theo", "On a besoin d'un plan plus serré.",
  "We need a tighter shot.",
  [(651, "en plan plus serré.")], "Framing need"),
 ("lea", "Oh non, j'en suis à ma septième agonie!",
  "Oh no, I am already on my seventh death scene!",
  [(652, "Oh, non."), (653, "j'en suis quand même à ma septième agonie, là.")], "Protesting exhaustion"),
 ("theo", "Le réalisateur manque encore de matière pour monter.",
  "The director still lacks footage for editing.",
  [(655, "tu m'avais dit que tu manquais de matière.")], "Editing justification"),
 ("lea", "Attends, je t'arrête tout de suite.",
  "Wait, I am stopping you right there.",
  [(657, "Attends, attends, attends."), (658, "Excuse-moi, je t'arrête, là.")], "Halting argument"),
 ("lea", "Moi, je ne suis pas une machine!",
  "I am not a machine!",
  [(660, "Je ne suis pas une machine, tu vois.")], "Asserting humanity"),
 ("lea", "Je ne meurs pas sur commande.",
  "I do not die on command.",
  [(661, "Je meurs pas comme ça sur commande")], "Emotional authenticity"),
 ("lea", "On ne meurt pas en claquant des doigts.",
  "One does not die at the snap of a finger.",
  [(661, "à claquant des doigts.")], "Acting nuance"),
 ("theo", "Je sais bien, mais nous devons assurer le montage.",
  "I know well, but we must secure the editing.",
  [(662, "il faut bien que Cédric puisse monter cette scène en toute sérénité.")], "Defending technical need"),
 ("lea", "Tu dois respecter la vision de ton réalisateur.",
  "You must respect the vision of your director.",
  [(664, "il faudrait que t'apprennes à respecter la vision d'un metteur en scène.")], "Director vision"),
 ("lea", "C'est ça, la vraie fonction d'une assistante.",
  "That is the true job of an assistant.",
  [(665, "Parce que c'est d'abord ça, la fonction d'une assistante.")], "Defining role"),
 ("theo", "D'accord, tu as raison sur ce point.",
  "Okay, you are right on this point.",
  [(669, "Non, mais Isabelle a raison.")], "Conceding argument"),
 ("theo", "Nous avons tout ce qu'il faut maintenant.",
  "We have everything that is needed now.",
  [(669, "Il a tout ce qu'il faut.")], "Agreeing coverage is complete"),
 ("lea", "Parfait, alors je vais me reposer un peu.",
  "Perfect, then I am going to rest a bit.",
  [(670, "Alors, repose-toi bien.")], "Taking break"),
]

WALK = [
 (0, None,
  "'Isabelle, we are going to do one last take.' The assistant asks for another camera take. "
  "The feminine noun phrase 'une derniere prise' refers to the final recording."),
 (1, None,
  "'We need a tighter shot.' The assistant specifies the framing needed. "
  "The idiom 'avoir besoin de' expresses necessity."),
 (2, None,
  "'Oh no, I am already on my seventh death scene!' Isabelle protests the repetition. "
  "The ordinal number 'septieme' indicates the seventh time."),
 (3, None,
  "'The director still lacks footage for editing.' The assistant defends the request with editorial needs. "
  "The noun 'matiere' colloquially means film material or footage."),
 (4, None,
  "'Wait, I am stopping you right there.' Isabelle interrupts the assistant firmly. "
  "The expression 'je t'arrete' halts an ongoing argument."),
 (5, None,
  "'I am not a machine!' Isabelle asserts her humanity as an artist. "
  "The feminine noun 'machine' stands for mechanical automatons."),
 (6, None,
  "'I do not die on command.' Isabelle emphasizes the emotional effort required. "
  "The phrase 'sur commande' means made to order or on cue."),
 (7, None,
  "'One does not die at the snap of a finger.' Isabelle highlights the nuance of dramatic acting. "
  "The idiom 'en claquant des doigts' means effortlessly or instantly."),
 (8, None,
  "'I know well, but we must secure the editing.' The assistant tries to justify the extra camera angle. "
  "The verb 'assurer' means to guarantee or secure."),
 (9, None,
  "'You must respect the vision of your director.' Isabelle reminds the assistant of hierarchy. "
  "The noun 'vision' refers to artistic perspective."),
 (10, None,
  "'That is the true job of an assistant.' Isabelle lectures on professional roles. "
  "The noun 'fonction' means duty or function."),
 (11, None,
  "'Okay, you are right on this point.' The assistant concedes defeat graciously. "
  "The idiom 'avoir raison' means to be right."),
 (12, None,
  "'We have everything that is needed now.' The crew agrees they have enough footage. "
  "The phrase 'tout ce qu'il faut' denotes all necessary material."),
 (13, None,
  "'Perfect, then I am going to rest a bit.' Isabelle claims her well-earned break. "
  "The near future 'je vais me reposer' expresses imminent rest."),
]

OUTRO = ("Isabelle wins the argument with poise, standing up for both artistic craft and her own physical limits. "
         "The crew wraps up the scene, satisfied that the takes already captured are more than enough. "
         "Now, let's review the scene once more.")

CLOSING = ("lea", "Moi, je ne suis pas une machine!")
