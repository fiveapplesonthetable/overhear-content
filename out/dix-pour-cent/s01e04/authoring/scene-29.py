# Authoring module for dix-pour-cent s01e04 scene 29 (cues 755-774).
# Build: python3 tools/compose.py out/dix-pour-cent/s01e04/authoring/scene-29.py --out out/dix-pour-cent/s01e04/scene-29.json

ID = "dix-pour-cent-s01e04-scene-29"
SHOW = "dix-pour-cent"
SEASON = 1
EPISODE = 4
SCENE = 29
TITLE = "La vérité sur le toit  (The Truth on the Roof)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "colette": "emilie"}
LABELS = {"lea": "Andréa", "colette": "Colette"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S01E04"
SOURCE_FILE = "sources/dix-pour-cent/s01/e04.fr.dual.srt"
SOURCE_NOTE = ("Cues 755-774. Cue 756 ('Je ne couche pas avec Gabriel') is retold in clean A1 French ('Je ne suis pas "
               "avec Gabriel'), and cue 766 ('pour ses maîtresses') is retold cleanly ('que Samuel gardait à l'hôtel'). "
               "In cue 769 'vus' is written as feminine singular 'vue' since Andréa is addressing Colette.")

INTRO = ("After Gabriel shared the good news with Sofia about her first film role, evening falls over the agency. "
         "Up on the rooftop overlooking Paris, Andréa finds the tax inspector Colette Brancillon looking out at the "
         "view. Earlier today at the Hotel Saint-Georges, Andréa and Gabriel panicked when they saw Colette walk in, "
         "and pretended to be secret lovers asking for their usual room. Now Andréa decides to clear the air. "
         "Listen to the French first, without worrying about catching every word.")

STORY = [
 ("lea", "Belle vue, non?", "Nice view, isn't it?",
  [(755, "Belle vue, non")], ""),
 ("colette", "Très.", "Very.",
  [(755, "Très")], ""),
 ("lea", "Je ne suis pas avec Gabriel.", "I'm not with Gabriel.",
  [(756, "Je ne"), (756, "pas avec Gabriel")], "'couche' retold cleanly as 'suis'"),
 ("colette", "Tu devrais le lui dire. Il a l'air de penser le contraire.",
  "You should tell him. He seems to think the opposite.",
  [(757, "Tu devrais le lui dire, il a l'air de penser le contraire")], ""),
 ("lea", "Non, mais on était là pour nos acteurs, pour négocier des tarifs.",
  "No, but we were there for our actors, to negotiate rates.",
  [(758, "Non, mais"), (759, "On était là pour négocier des tarifs"), (759, "pour nos acteurs")],
  "'préférentiels' omitted for A1"),
 ("colette", "L'envie subite de s'embrasser et de prendre une chambre? Ça arrive.",
  "The sudden urge to kiss and get a room? It happens.",
  [(761, "L'envie subite de s'embrasser et de prendre une chambre ? Ça arrive")], ""),
 ("colette", "Tu es très douée pour séduire les gens.",
  "You're very good at charming people.",
  [(762, "Tu es très douée pour séduire les gens")], ""),
 ("colette", "Cette fille avait raison. Tu es un monstre.",
  "That girl was right. You're a monster.",
  [(763, "Cette fille avait raison. Tu es un monstre")], ""),
 ("lea", "Bon, on faisait semblant. On était là pour voir le directeur.",
  "All right, we were pretending. We were there to see the manager.",
  [(764, "Bon"), (764, "On faisait semblant"), (765, "On était là pour voir le directeur")], ""),
 ("lea", "Pour parler de la chambre que Samuel gardait à l'hôtel.",
  "To talk about the room that Samuel kept at the hotel.",
  [(766, "pour parler de la chambre que Samuel gardait")], "'pour ses maîtresses' replaced by 'à l'hôtel'"),
 ("lea", "On l'a appris hier.", "We found out about it yesterday.",
  [(767, "On l'a appris hier")], ""),
 ("lea", "On vous a vue arriver, et on a paniqué.",
  "We saw you arrive, and we panicked.",
  [(769, "arriver"), (769, "et on a paniqué")], "'vus' -> 'vue' addressing Colette"),
 ("colette", "Non!", "No!",
  [(770, "Non")], "Andréa's 'Non' in 770; legal term 'Dissimuler un abus de biens sociaux' narrated"),
 ("lea", "Si. On avait peur. De vous.", "Yes. We were scared. Of you.",
  [(771, "Si"), (772, "On avait peur. De vous")], ""),
 ("colette", "Vous me tutoyez moins, maintenant.", "You're using 'tu' with me less now.",
  [(773, "Vous me tutoyez moins, maintenant")], ""),
 ("lea", "Je ne sais pas comment me comporter avec vous.",
  "I don't know how to behave around you.",
  [(774, "Je ne sais pas comment me comporter avec vous")], ""),
]

OPENER = ("Let's walk through it line by line. Andréa joins Colette at the edge of the roof.")

WALK = [
 (0, None,
  "'Nice view, isn't it?' Adding the word for 'no' at the end of a remark is the simplest way to say 'isn't it?'"
  " in French."),
 (1, None,
  "'Very.' Just one short word from Colette as she looks out over the rooftops of the city."),
 (2, None,
  "'I'm not with Gabriel.' Andréa wants Colette to know right away that she and Gabriel are not a couple."),
 (3, None,
  "'You should tell him. He seems to think the opposite.' Two little object words sit before 'tell': 'it' and "
  "'to him'. In the second sentence, 'has the air of thinking' is the natural phrase for 'seems to think'."),
 (4, None,
  "'No, but we were there for our actors, to negotiate rates.' Andréa tries one last business excuse, using the "
  "past tense for 'we were'."),
 (5, None,
  "'The sudden urge to kiss and get a room? It happens.' Colette is dry and ironic: she didn't believe their "
  "act at the hotel reception for a single second."),
 (6, None,
  "'You're very good at charming people.' The adjective for 'gifted' or 'good at' has a feminine letter at the "
  "end because she is speaking to Andréa."),
 (7, None,
  "'That girl was right. You're a monster.' Colette remembers Clémentine's dramatic speech outside the clothes "
  "shop earlier in the episode."),
 (8, "Bon, on faisait semblant.",
  "'All right, we were pretending.' Literally 'we were making appearance'. Andréa drops the lie and tells the truth."),
 (8, "On était là pour voir le directeur.",
  "'We were there to see the manager.' Before an infinitive verb, the preposition means 'in order to'."),
 (9, None,
  "'To talk about the room that Samuel kept at the hotel.' The late boss of the agency had been paying for a "
  "hotel room out of company money."),
 (10, None,
  "'We found out about it yesterday.' Literally 'we learned it yesterday', with the word for 'it' shortened before "
  "the helper verb."),
 (11, None,
  "'We saw you arrive, and we panicked.' Both verbs are in the past tense with 'have'."),
 (12, None,
  "'No!' Colette asks if they were trying to hide a misuse of company money, and at first Andréa says no, then "
  "gives in."),
 (13, None,
  "'Yes. We were scared. Of you.' Notice the special word for 'yes' when you contradict a negative, followed by "
  "'we had fear of you'."),
 (14, None,
  "'You're using tu with me less now.' French has a special verb that means 'to address someone as tu'. Colette "
  "notices that Andréa has switched back to the polite 'vous'."),
 (15, None,
  "'I don't know how to behave around you.' For once, tough, confident Andréa is completely disarmed, and Colette "
  "can't help smiling."),
]

TRANSITION = "Now let's hear their whole conversation on the roof again."

OUTRO = ("Telling the truth finally broke the ice between Andréa and Colette. Next, we join Audrey Fleurot and "
         "Mathias at a charity gala, where Mathias has a plan to save Audrey's reputation. See you there.")
CLOSING = ("lea", "Belle vue, non?")
