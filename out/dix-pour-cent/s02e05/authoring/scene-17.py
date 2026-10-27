# Authoring module for dix-pour-cent s02e05 scene 17 (cues 497-549).
# Build: python3 tools/compose.py out/dix-pour-cent/s02e05/authoring/scene-17.py --out out/dix-pour-cent/s02e05/scene-17.json

ID = "dix-pour-cent-s02e05-scene-17"
SHOW = "dix-pour-cent"
SEASON = 2
EPISODE = 5
SCENE = 17
TITLE = "La scène secrète  (The Secret Scene)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "gabriel": "theo"}
LABELS = {"lea": "Élisabeth", "gabriel": "Gabriel"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S02E05"
SOURCE_FILE = "sources/dix-pour-cent/s02/e05.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 497-549. Gabriel has lunch with funding committee representative Élisabeth Lecœur to discuss "
    "Julien Doré's musical film. While praising the script, Gabriel accidentally reveals an unedited, bizarrely violent "
    "scene that was omitted from the official proposal."
)

INTRO = (
    "At a restaurant, Gabriel meets with Élisabeth Lecœur to discuss financing for Julien Doré's musical film. "
    "While discussing the screenplay, Gabriel accidentally mentions a shocking scene that was never included in her draft. "
    "Listen to the scene in French first."
)

STORY = [
    ("lea", "J'adore vraiment le nouveau scénario de Julien Doré.",
     "I really love Julien Doré's new screenplay.",
     [(507, "j'adore le projet de Julien Doré.")], ""),
    ("gabriel", "C'est un projet très original et ambitieux.",
     "It is a very original and ambitious project.",
     [(508, "C'est fantastique."), (515, "C'est bien au-dessus.")], ""),
    ("lea", "Je trouve son écriture particulièrement mature.",
     "I find his writing particularly mature.",
     [(515, "ça montre une vraie maturité..."), (516, "C'est très mature.")], ""),
    ("gabriel", "Oui, mais ce film pousse les limites assez loin.",
     "Yes, but this movie pushes the boundaries quite far.",
     [(518, "Ce film pousse les limites assez loin.")], ""),
    ("lea", "Vous ne craignez pas une interdiction aux mineurs?",
     "Are you not afraid of an age restriction?",
     [(519, "Vous ne craignez pas qu'il reçoive une interdiction aux moins de 18 ans ?")], ""),
    ("gabriel", "Il n'y a rien de trop explicite dans le texte.",
     "There is nothing too explicit in the text.",
     [(521, "Il n'y a rien d'explicite là-dedans.")], ""),
    ("gabriel", "Sauf peut-être cette scène près du lac.",
     "Except maybe that scene near the lake.",
     [(523, "Cette scène où il..."), (538, "près du lac...")], ""),
    ("lea", "De quelle scène parlez-vous exactement?",
     "Which scene are you talking about exactly?",
     [(526, "Non, je ne vous suis pas."), (536, "C'est quoi alors, cette scène ?")], ""),
    ("gabriel", "La scène où la femme coupe le machin de l'homme.",
     "The scene where the woman cuts off the man's thing.",
     [(525, "La scène où elle lui coupe... son machin.")], ""),
    ("lea", "Je n'ai jamais lu cette séquence dans mon dossier!",
     "I never read this sequence in my file!",
     [(526, "Non, je ne vous suis pas."), (529, "On n'a peut-être pas eu la même version")], ""),
    ("gabriel", "Pardon, je crois que j'ai fait une grosse gaffe.",
     "Sorry, I think that I made a big blunder.",
     [(531, "Pardon, j'ai fait une gaffe.")], ""),
    ("lea", "Avez-vous envoyé une version édulcorée au comité?",
     "Did you send a toned-down version to the committee?",
     [(532, "J'espère qu'il ne fait pas partie de ces auteurs"), (533, "qui nous envoient une version édulcorée")], ""),
    ("gabriel", "Non, pas du tout, c'était juste un premier brouillon.",
     "No, not at all, it was just a first draft.",
     [(534, "Non, pas du tout."), (535, "Non, je ne crois pas.")], ""),
    ("lea", "Racontez-moi quand même la fin de cette scène.",
     "Tell me the end of this scene anyway.",
     [(536, "C'est quoi alors, cette scène ?"), (539, "Eh bien, il y a une séquence")], ""),
    ("gabriel", "Elle fait cuire le morceau sur un barbecue.",
     "She cooks the piece on a barbecue.",
     [(545, "et elle le fait cuire"), (546, "sur une sorte de barbecue")], ""),
    ("lea", "Gabriel, votre client est totalement fou!",
     "Gabriel, your client is completely crazy!",
     [(548, "La saucisse, c'est pour ?"), (549, "Excusez-moi.")], "")
]

OPENER = "Let's examine how Gabriel accidentally reveals a shocking movie scene."

WALK = [
    (0, None,
     "'I really love Julien Doré's new screenplay.' Élisabeth expresses high enthusiasm for the project. "
     "The adverb vraiment emphasizes genuine appreciation."),
    (1, None,
     "'It is a very original and ambitious project.' Gabriel supports his client's artistic vision. "
     "The adjective ambitieux describes high artistic aspirations."),
    (2, None,
     "'I find his writing particularly mature.' She compliments the depth of the text. "
     "The feminine noun écriture refers to screenwriting style."),
    (3, None,
     "'Yes, but this movie pushes the boundaries quite far.' Gabriel hints at daring content. "
     "The idiom pousser les limites means to push the boundaries."),
    (4, None,
     "'Are you not afraid of an age restriction?' Élisabeth wonders about censorship ratings. "
     "The verb craignez comes from the irregular verb craindre."),
    (5, None,
     "'There is nothing too explicit in the text.' Gabriel tries to sound reassuring. "
     "The indefinite expression rien de takes a masculine adjective."),
    (6, None,
     "'Except maybe that scene near the lake.' Gabriel unwittingly opens a dangerous topic. "
     "The preposition sauf means except."),
    (7, None,
     "'Which scene are you talking about exactly?' Élisabeth asks for immediate clarification. "
     "The interrogative adjective quelle agrees with the feminine noun scène."),
    (8, None,
     "'The scene where the woman cuts off the man's thing.' Gabriel blurted out the shocking detail. "
     "The colloquial noun machin means thing or thingy."),
    (9, None,
     "'I never read this sequence in my file!' Élisabeth reacts with utter shock. "
     "The compound past n'ai jamais lu indicates past reading."),
    (10, None,
     "'Sorry, I think that I made a big blunder.' Gabriel realizes his terrible mistake. "
     "The feminine noun gaffe designates an embarrassing blunder."),
    (11, None,
     "'Did you send a toned-down version to the committee?' Élisabeth becomes suspicious of deception. "
     "The adjective édulcorée means sanitized or toned down."),
    (12, None,
     "'No, not at all, it was just a first draft.' Gabriel scrambles to minimize the slip. "
     "The masculine noun brouillon denotes a rough draft."),
    (13, None,
     "'Tell me the end of this scene anyway.' Élisabeth demands full transparency. "
     "The imperative racontez-moi requests a detailed explanation."),
    (14, None,
     "'She cooks the piece on a barbecue.' Gabriel confesses the absurd climax sheepishly. "
     "The causative construction fait cuire means to cook."),
    (15, None,
     "'Gabriel, your client is completely crazy!' Élisabeth concludes in disbelief. "
     "The adjective fou describes irrational or eccentric behavior.")
]

TRANSITION = "Now let's listen to the embarrassing conversation once more at normal pace."

OUTRO = (
    "Gabriel's clumsy slip of the tongue leaves Élisabeth stunned by Julien Doré's wild imagination. "
    "Listen to the hilarious conversation once more in French."
)

CLOSING = ("lea", "Gabriel, votre client est totalement fou!")
