# Authoring module for dix-pour-cent s01e06 scene 12 (cues 323-349).
# Build: python3 tools/compose.py out/dix-pour-cent/s01e06/authoring/scene-12.py --out out/dix-pour-cent/s01e06/scene-12.json

ID = "dix-pour-cent-s01e06-scene-12"
SHOW = "dix-pour-cent"
SEASON = 1
EPISODE = 6
SCENE = 12
TITLE = "La piscine de François  (François's Swimming Pool)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "francois": "marcel", "christophe": "theo"}
LABELS = {"lea": "Andréa", "francois": "François", "christophe": "Christophe"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S01E06"
SOURCE_FILE = "sources/dix-pour-cent/s01/e06.fr.dual.srt"
SOURCE_NOTE = ("Cues 323-349. Andréa tracks down François Berléand at his country house, where he admits he is digging "
               "a swimming pool because he never learned to swim. Andréa reconciles him with Christophe Bel and calls "
               "Christophe to arrange dinner. Adapted for A1 French.")

INTRO = ("Andrea drives out to Francois Berleand's country house to make peace after his violent fight with Christophe Bel. "
         "Climbing over the garden wall, she finds Francois digging a giant hole in his lawn and discovers a surprising "
         "secret that explains all his fears. Let's listen to the scene in French first.")

STORY = [
 ("lea", "François, c'est moi. Je suis là, comme prévu.",
  "François, it's me. I'm here, as planned.",
  [(323, "François, c'est moi"), (323, "Je suis là, comme prévu")], ""),
 ("francois", "Ça suffit! Fox, du calme!",
  "That's enough! Fox, quiet!",
  [(329, "Ça suffit"), (329, "Fox, du calme")], ""),
 ("francois", "Je fais creuser une piscine.",
  "I am having a swimming pool dug.",
  [(330, "Je fais creuser une piscine")], ""),
 ("lea", "Sans blague?",
  "Seriously?",
  [(331, "Sans blague")], ""),
 ("francois", "Je ne supporte plus la honte de ne pas savoir nager.",
  "I cannot take the shame of not knowing how to swim anymore.",
  [(332, "Je supporte plus la honte de ne pas savoir nager")], "Restored 'ne' negation"),
 ("francois", "J'ai refusé tellement de films.",
  "I have turned down so many films.",
  [(333, "J'ai refusé tellement de films")], ""),
 ("lea", "Lesquels? Titanic?",
  "Which ones? Titanic?",
  [(334, "Lesquels ? Titanic")], ""),
 ("lea", "Je suis fière de toi, François.",
  "I am proud of you, François.",
  [(335, "Je suis fière de toi")], ""),
 ("lea", "Je suis vraiment désolée pour Dom Juan.",
  "I am really sorry about Dom Juan.",
  [(337, "Je suis vraiment désolée pour Dom Juan")], ""),
 ("francois", "Je sais que Christophe Bel a de la vision.",
  "I know that Christophe Bel has vision.",
  [(338, "de Bel a de la vision")], ""),
 ("lea", "Tu vas le faire, alors?",
  "Are you going to do it, then?",
  [(339, "Tu vas le faire, alors")], ""),
 ("francois", "Non, c'est trop tard maintenant.",
  "No, it is too late now.",
  [(340, "Non, c'est trop tard maintenant")], ""),
 ("lea", "Christophe le regrette aussi. Il t'admire, tu le sais!",
  "Christophe regrets it too. He admires you, you know that!",
  [(343, "Christophe le regrette aussi"), (344, "Il t'admire, tu le sais")], ""),
 ("francois", "Alors pourquoi il ne m'appelle pas directement?",
  "Then why doesn't he call me directly?",
  [(345, "Alors pourquoi il m'appelle pas directement")], "Restored 'ne' negation"),
 ("lea", "Christophe? C'est Andréa Martel.",
  "Christophe? It's Andréa Martel.",
  [(348, "Christophe ? C'est Andréa Martel")], ""),
 ("lea", "J'espère que tu es libre ce soir, je t'invite à dîner.",
  "I hope you are free tonight, I am inviting you to dinner.",
  [(349, "J'espère que tu es libre ce soir, je t'invite à dîner")], ""),
 ("christophe", "D'accord, avec plaisir.",
  "All right, with pleasure.",
  [], "Phone response connecting to scene 13"),
]

OPENER = "Francois shares his private secret. Let us examine the lines with English notes."

WALK = [
 (0, None, "'Francois, it is me. I am here, as planned.' Andrea announces her arrival at the country house."),
 (1, None, "'That is enough! Fox, quiet!' Francois calms his barking terrier dog Fox. Du calme means quiet."),
 (2, None, "'I am having a swimming pool dug.' Faire creuser means to have dug, using the causative."),
 (3, None, "'Seriously?' Sans blague is a colloquial exclamation meaning no joke or seriously."),
 (4, None, "'I cannot take the shame of not knowing how to swim anymore.' Ne plus means no longer."),
 (5, None, "'I have turned down so many films.' Refuser means to refuse or turn down, and tellement means so many."),
 (6, None, "'Which ones? Titanic?' Andrea teases him with humor. Lesquels means which ones."),
 (7, None, "'I am proud of you, Francois.' Etre fier de means to be proud of someone."),
 (8, None, "'I am really sorry about Dom Juan.' Andrea expresses genuine empathy, and vraiment means truly."),
 (9, None, "'I know that Christophe Bel has vision.' Avoir de la vision means to have creative vision."),
 (10, None, "'Are you going to do it, then?' Andrea encourages him to reconsider the role."),
 (11, None, "'No, it is too late now.' Francois hesitates out of wounded pride. Trop tard means too late."),
 (12, None, "'Christophe regrets it too. He admires you, you know that!' Regretter means to regret, and admirer means to admire."),
 (13, None, "'Then why does he not call me directly?' Directement is an adverb meaning directly or in person."),
 (14, None, "'Christophe? It is Andrea Martel.' Andrea takes initiative right away and dials his number."),
 (15, None, "'I hope you are free tonight, I am inviting you to dinner.' Esperer means to hope, and etre libre means to be free."),
 (16, None, "'All right, with pleasure.' Christophe accepts Andrea's dinner invitation with avec plaisir."),
]

TRANSITION = "Now listen to Andrea and Francois's conversation once more without interruption."
OUTRO = ("Andrea successfully brings Francois back into the fold and arranges to meet Christophe Bel for dinner. "
         "That dinner will test her patience and her relationship with Colette even further. "
         "Here is our closing sentence.")
CLOSING = ("christophe", "D'accord, avec plaisir.")
