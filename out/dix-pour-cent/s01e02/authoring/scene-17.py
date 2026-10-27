ID = "dix-pour-cent-s01e02-scene-17"
SHOW = "dix-pour-cent"
SEASON = 1
EPISODE = 2
SCENE = 17
TITLE = "Line et Françoise, une vieille histoire  (Line and Françoise, an Old Story)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "herve": "theo"}
LABELS = {"lea": "Camille", "herve": "Hervé"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S01E02"
SOURCE_FILE = "sources/dix-pour-cent/s01/e02.fr.dual.srt"
SOURCE_NOTE = ("Cues 491-521. Merged scene 18 (cues 522-538: Camille asks Sofia to send photos to a casting director; "
               "Gabriel explains the brunette among the blondes) is mentioned in the outro.")

INTRO = ("At the café, Arlette has just told Andréa that she will put her life insurance into the agency, because "
         "the agency is all the family she has. Back at the assistants' desks, the talk is about Gabriel's bold idea: "
         "Line Renaud, the singer and actress, to replace Françoise Fabian in Gabor's film. Hervé, who knows every "
         "piece of gossip in Paris, explains to Camille why that idea is so cheeky. Here it is in French first; "
         "just follow the story, not every word.")

STORY = [
 ("herve", "C'est culotté de la part de Gabriel.", "That's cheeky of Gabriel.",
  [(491, "C'est culotté de la part de Gabriel")], ""),
 ("lea", "Tu trouves ça culotté?", "You think it's cheeky?", [(492, "Tu trouves ça culotté")], ""),
 ("herve", "Oui! Il y a une vieille histoire entre Line et Françoise.", "Yes! There's an old story between Line and Françoise.",
  [(495, "histoire entre Line et Françoise")], "'Oui! Il y a une vieille' added"),
 ("lea", "Quelle histoire?", "What story?", [(496, "Quelle histoire")], ""),
 ("herve", "Elles ne peuvent pas se sentir.", "They can't stand each other.", [(497, "Elles ne peuvent pas se sentir")], ""),
 ("lea", "Ah bon? Je n'ai jamais entendu ça.", "Really? I've never heard that.",
  [(498, "Ah bon ? Je n'ai jamais entendu ça")], ""),
 ("herve", "Line était une chanteuse connue. Françoise était une jeune actrice.",
  "Line was a well-known singer. Françoise was a young actress.",
  [(502, "Line était une chanteuse connue")], "'Françoise était une jeune actrice' simplifies cue 504 (just out of drama school)"),
 ("herve", "Françoise avait un amoureux. Devine qui!", "Françoise had a boyfriend. Guess who!", [],
  "new; from cue 504 'où elle avait rencontré...' and 505 'Devinez qui' (tu form, as Hervé uses tu with Camille)"),
 ("lea", "Je ne sais pas.", "I don't know.", [(506, "Je ne sais pas")], ""),
 ("herve", "Samuel!", "Samuel!", [(507, "Samuel")], ""),
 ("lea", "Françoise était avec Samuel?", "Françoise was with Samuel?", [(508, "Françoise était avec Samuel")], ""),
 ("herve", "Oui! Et un jour, elle le présente à Line.", "Yes! And one day, she introduces him to Line.",
  [(508, "Oui"), (509, "elle le présente à Line")], "storytelling present, as in the cue"),
 ("herve", "Depuis, les deux femmes ne se parlent plus.", "Since then, the two women don't speak to each other any more.",
  [(512, "Les deux femmes")], "'se sont brouillées... jamais réconciliées' simplified"),
 ("herve", "Line est devenue une star, et Françoise a fait du cinéma d'auteur.",
  "Line became a star, and Françoise made art-house films.",
  [(514, "Line est devenue une star"), (515, "cinéma d'auteur")], "'du music-hall' dropped"),
 ("herve", "Au fond, Françoise aurait aimé être chanteuse.", "Deep down, Françoise would have liked to be a singer.",
  [(517, "Au fond"), (518, "Françoise aurait aimé être chanteuse")], ""),
 ("herve", "Et Line, une actrice de cinéma.", "And Line, a film actress.", [(519, "Et Line, une actrice")],
  "'de la Nouvelle Vague' -> 'de cinéma'"),
 ("lea", "Chacune déteste l'autre?", "Each one hates the other?", [(520, "Chacune déteste l'autre")],
  "'pour avoir fait ce qu'elle n'a pas fait' dropped"),
 ("herve", "Exactement.", "Exactly.", [(521, "Exactement")], ""),
]

OPENER = ("Let's go through it together. Hervé starts with a word that means bold, a little too bold.")

WALK = [
 (0, None,
  "'That's cheeky of Gabriel.' The adjective comes from an old word for trousers: someone who has the nerve. And "
  "the phrase after it means 'on the part of', so: cheeky, coming from Gabriel."),
 (1, None,
  "'You think it's cheeky?' The verb here is 'to find', used for opinions, just like 'do you find it cheeky?' "
  "Camille is new, so she doesn't see the problem."),
 (2, None,
  "'Yes! There's an old story between Line and Françoise.' Three little words at the start mean 'there is'. "
  "You'll hear them constantly."),
 (3, None,
  "'What story?' The question word agrees with the noun; story is feminine, so it takes the feminine spelling, "
  "though it sounds the same."),
 (4, None,
  "'They can't stand each other.' Literally 'they can't smell each other'. The little reflexive word makes it "
  "mutual: each other. That's the first grammar point of the scene."),
 (5, None,
  "'Really? I've never heard that.' The word for 'never' takes the place of the usual 'not' in the two-part "
  "negative. Hervé settles in to tell the story."),
 (6, None,
  "'Line was a well-known singer. Françoise was a young actress.' This past tense sets the scene: what things "
  "were like back then. It's the second grammar point: the tense for background and description."),
 (7, None,
  "'Françoise had a boyfriend. Guess who!' The same background tense for 'had', then a casual command. Camille "
  "has no idea."),
 (8, None,
  "'I don't know.' The classic two-part negative around the verb 'to know'."),
 (9, None,
  "'Samuel!' Their late boss, the founder of the agency, whose funeral is this week."),
 (10, None,
  "'Françoise was with Samuel?' To be 'with' someone means to be their partner, in French as in English. "
  "Camille is amazed."),
 (11, None,
  "'Yes! And one day, she introduces him to Line.' French storytellers often switch to the present to make the "
  "key moment vivid. The little word before the verb means 'him'."),
 (12, None,
  "'Since then, the two women don't speak to each other any more.' The reflexive word again, for 'each other', "
  "and the negative with 'any more' at the end."),
 (13, None,
  "'Line became a star, and Françoise made art-house films.' Now two completed past events. Notice the first "
  "uses the verb 'to be' as its helper, because it means 'to become'."),
 (14, None,
  "'Deep down, Françoise would have liked to be a singer.' A form for things that didn't happen: she would have "
  "liked it. Just learn it as one block."),
 (15, None,
  "'And Line, a film actress.' Hervé doesn't repeat the verb; we understand it: Line would have liked to be an "
  "actress."),
 (16, None,
  "'Each one hates the other?' The first word means 'each one' and has a feminine form here, because we're "
  "talking about two women."),
 (17, None,
  "'Exactly.' And that, Hervé says, is why Gabriel's idea is so cheeky."),
]

TRANSITION = "Now the whole story again."

OUTRO = ("That's the old story, and right after it Camille hurries to reception to ask Sofia a favour: send some "
         "photos to a casting director. You did well with all those past tenses; see you next time.")
CLOSING = ("herve", "Tu me suis?")
