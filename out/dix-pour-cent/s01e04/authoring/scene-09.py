# Authoring module for dix-pour-cent s01e04 scene 09 (cues 245-261).
# Build: python3 tools/compose.py out/dix-pour-cent/s01e04/authoring/scene-09.py --out out/dix-pour-cent/s01e04/scene-09.json

ID = "dix-pour-cent-s01e04-scene-09"
SHOW = "dix-pour-cent"
SEASON = 1
EPISODE = 4
SCENE = 9
TITLE = "Dîner chez Mathias  (Dinner at Mathias's)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "mathias": "theo"}
LABELS = {"lea": "Catherine", "mathias": "Mathias"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S01E04"
SOURCE_FILE = "sources/dix-pour-cent/s01/e04.fr.dual.srt"

INTRO = ("After a tense day worrying about the German offer for ASK and StarMédia's proposal, "
         "Mathias is back home having dinner with his wife, Catherine. "
         "Their son Hippolyte isn't at the table tonight, and Catherine starts wondering aloud about the girl he's been seeing: "
         "Andréa's new assistant, Camille, who is secretly Mathias's own daughter. "
         "Let's listen to the French first without worrying about every detail.")

STORY = [
 ("lea", "Hippolyte ne sera pas là pour le dîner.", "Hippolyte won't be here for dinner.",
  [(245, "Hippolyte ne sera pas là pour le dîner")], ""),
 ("mathias", "Il travaille son texte?", "Is he working on his lines?",
  [], "retells cue 246 'Il révise ?' in A1 words"),
 ("lea", "Il ne dit pas, mais j'en doute.", "He doesn't say, but I doubt it.",
  [(247, "Il ne dit pas, mais j'en doute")], ""),
 ("mathias", "Il voit toujours l'assistante d'Andréa?", "Is he still seeing Andréa's assistant?",
  [(248, "Il voit toujours l'assistante d'Andréa")], ""),
 ("lea", "Aucune idée. Il ne me dit rien.", "No idea. He doesn't tell me anything.",
  [(249, "Aucune idée. Il ne me dit rien")], ""),
 ("lea", "Camille, c'est ça? Elle est sympa, non?", "Camille, is that right? She's nice, isn't she?",
  [(250, "Camille, c'est ça"), (251, "Elle est sympa, non")], ""),
 ("mathias", "Je ne la connais pas très bien.", "I don't know her very well.",
  [(252, "Je ne la connais pas très bien")], ""),
 ("lea", "Mais elle travaille à l'agence!", "But she works at the agency!",
  [(253, "Elle"), (253, "travaille")], "'Elle y travaille' -> 'Mais elle travaille à l'agence!'"),
 ("mathias", "Pas avec moi. Un petit peu.", "Not with me. A little bit.",
  [(253, "Pas avec moi"), (254, "Un petit peu")], ""),
 ("mathias", "Peut-être, mais et alors?", "Maybe, but so what?",
  [(255, "Peut-être, mais et alors")], ""),
 ("lea", "Il veut peut-être se marier avec elle!", "Maybe he wants to marry her!",
  [], "retells cue 256 'Il pourrait l'épouser' in A1 words"),
 ("mathias", "Mais qu'est-ce que tu racontes?", "What on earth are you talking about?",
  [(256, "Mais qu'est-ce que tu racontes")], ""),
 ("lea", "Je plaisante, Mathias.", "I'm joking, Mathias.",
  [(257, "Je plaisante, Mathias")], ""),
 ("mathias", "Ce n'est pas très intelligent de sortir avec l'assistante de son agent.", "It's not very smart to go out with his agent's assistant.",
  [(258, "très"), (259, "de sortir avec l'assistante de son agent")], "'malin de sa part' -> 'intelligent'"),
 ("lea", "Dis-lui, alors.", "Tell him, then.",
  [(260, "alors")], "'Dis-le-lui' -> 'Dis-lui'"),
 ("mathias", "Oui, je vais lui parler.", "Yes, I'll talk to him.",
  [], "retells cue 261 'Je le ferai' in A1 near future"),
]

OPENER = "Let's go through their conversation line by line. Catherine begins with news about their son."

WALK = [
 (0, None,
  "'Hippolyte won't be here for dinner.' Future tense of 'to be' wrapped in the two-part negation."),
 (1, None,
  "'Is he working on his lines?' Literally 'his text', the word actors use for their script or lines."),
 (2, None,
  "'He doesn't say, but I doubt it.' The tiny word before 'doubt' means 'of it', because in French you doubt 'of' something."),
 (3, None,
  "'Is he still seeing Andréa's assistant?' Mathias tries to sound casual, though he's anything but."),
 (4, None,
  "'No idea. He doesn't tell me anything.' The negative wraps around the verb 'tells', with the word for 'anything' at the end."),
 (5, "Camille, c'est ça?",
  "'Camille, is that right?' Literally 'that's it?', the easiest way to check a name or a fact."),
 (5, "Elle est sympa, non?",
  "'She's nice, isn't she?' Adding 'no?' at the end turns any statement into a friendly tag question."),
 (6, None,
  "'I don't know her very well.' Mathias lies smoothly to his wife."),
 (7, None,
  "'But she works at the agency!' Catherine is surprised he barely knows a girl from his own office."),
 (8, None,
  "'Not with me. A little bit.' Mathias backs down slightly."),
 (9, None,
  "'Maybe, but so what?' The two words at the end mean 'and so?' or 'so what?'."),
 (10, None,
  "'Maybe he wants to marry her!' Catherine teases him, having no idea why that thought horrifies Mathias."),
 (11, None,
  "'What on earth are you talking about?' Literally 'what is it that you are telling?'. Mathias nearly chokes on his wine."),
 (12, None,
  "'I'm joking, Mathias.' A useful everyday verb for 'to joke' or 'to kid'."),
 (13, None,
  "'It's not very smart to go out with his agent's assistant.' Mathias quickly invents a professional excuse."),
 (14, None,
  "'Tell him, then.' Command form of 'tell' joined by a hyphen to the word for 'to him'."),
 (15, None,
  "'Yes, I'll talk to him.' Near future again: 'I am going to talk to him'."),
]

TRANSITION = "Now let's listen to the whole dinner conversation again."

OUTRO = ("Mathias has one more problem to fix before Hippolyte and Camille get any closer. "
         "See you in the next scene!")
CLOSING = ("lea", "Je plaisante, Mathias!")
