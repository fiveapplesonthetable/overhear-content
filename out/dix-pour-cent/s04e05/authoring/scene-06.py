ID = "dix-pour-cent-s04e05-scene-06"
SHOW = "dix-pour-cent"
SEASON = 4
EPISODE = 5
SCENE = 6
TITLE = "Un mauvais pressentiment  (A Bad Feeling)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "gabriel": "theo"}
LABELS = {"lea": "Andréa", "gabriel": "Gabriel"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S04E05"
SOURCE_FILE = "sources/dix-pour-cent/s04/e05.fr.dual.srt"

INTRO = ("Gabriel goes to Andrea's office to share his suspicions about the new agent, Elise Formain. "
         "We'll hear their conversation in French first, but don't worry about catching every word.")

STORY = [
 ("gabriel", "Je cherche des infos sur Élise Formain.", "I am looking for info on Elise Formain.",
  [(274, "je cherche"), (274, "des infos sur Élise Formain.")], "Simplified"),
 ("gabriel", "J'ai un mauvais pressentiment.", "I have a bad feeling.",
  [(275, "J'ai un mauvais pressentiment.")], ""),
 ("lea", "Tu la trouvais sympa.", "You found her nice.",
  [(276, "tu la trouvais sympa")], "Simplified"),
 ("gabriel", "Elle a demandé les numéros de Bellucci et Dujardin.", "She asked for Bellucci and Dujardin's numbers.",
  [(282, "Elle m'a demandé les numéros de Bellucci et Dujardin.")], "Simplified"),
 ("lea", "Non, ce n'est pas possible.", "No, it is not possible.",
  [(283, "Non ! Non !")], "Simplified"),
 ("lea", "Elle est peut-être pire que Mathias.", "She is perhaps worse than Mathias.",
  [(284, "Elle est peut-être pire que Mathias.")], ""),
 ("gabriel", "Elle va nous dévorer comme des sashimis.", "She is going to eat us like sashimi.",
  [(287, "Elle va nous dévorer comme des sashimis.")], ""),
 ("lea", "On n'a pas assez de preuves.", "We do not have enough evidence.",
  [(289, "on n'a pas assez de preuves.")], ""),
 ("gabriel", "Il faut fouiller son téléphone.", "We must go through her phone.",
  [(290, "Il faut fouiller son téléphone.")], ""),
 ("lea", "C'est ce que je fais.", "That is what I do.",
  [(291, "C'est ce que je fais quand je rencontre un mec.")], "Simplified"),
 ("lea", "Comment on va accéder à son téléphone?", "How are we going to access her phone?",
  [(294, "comment on va accéder à son téléphone ?")], ""),
 ("gabriel", "Tu es tellement naïve parfois.", "You are so innocent sometimes.",
  [(295, "t'es tellement naïve parfois.")], "Removed putain")
]

OPENER = "Let's walk through it. Gabriel is doing some research."

WALK = [
 (0, None,
  "'I am looking for info on Elise Formain.' Gabriel confesses that he is investigating their new colleague."),
 (1, None,
  "'I have a bad feeling.' He suspects she is up to no good."),
 (2, None,
  "'You found her nice.' Andrea reminds him that he actually liked the new agent at first."),
 (3, None,
  "'She asked for Bellucci and Dujardin's numbers.' He reveals her bold attempt to get his client contacts."),
 (4, None,
  "'No, it is not possible.' Andrea refuses to believe it at first."),
 (5, None,
  "'She is perhaps worse than Mathias.' Andrea realizes the new agent is extremely dangerous."),
 (6, None,
  "'She is going to eat us like sashimi.' Gabriel uses a colorful metaphor to express his fear."),
 (7, None,
  "'We do not have enough evidence.' Andrea points out that they need concrete proof of her betrayal."),
 (8, None,
  "'We must go through her phone.' He suggests a highly unethical way to find the evidence."),
 (9, None,
  "'That is what I do.' Andrea admits she uses this trick sometimes."),
 (10, None,
  "'How are we going to access her phone?' She wonders how they could possibly pull off such a heist."),
 (11, None,
  "'You are so innocent sometimes.' He tells her not to worry, as he already has a plan.")
]

TRANSITION = "Now let's hear the scene once more."
OUTRO = "Gabriel and Andrea are plotting to steal a phone. Let's see if it works. See you next time."
CLOSING = ("lea", "D'accord!")
