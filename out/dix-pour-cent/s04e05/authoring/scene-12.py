# Authoring module for dix-pour-cent s04e05 scene 12 (cues 610-632).
# Build: python3 tools/compose.py overhear-content/out/dix-pour-cent/s04e05/authoring/scene-12.py --out overhear-content/out/dix-pour-cent/s04e05/scene-12.json

ID = "dix-pour-cent-s04e05-scene-12"
SHOW = "dix-pour-cent"
SEASON = 4
EPISODE = 5
SCENE = 12
TITLE = "Trop de pas  (Too Many Steps)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "bernard": "theo"}
LABELS = {"lea": "Sigourney", "bernard": "Bernard"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S04E05"
SOURCE_FILE = "sources/dix-pour-cent/s04/e05.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 610-632. Bernard Verley explains his strict physical condition to Sigourney Weaver: no more than fifteen steps per scene. "
    "When Sigourney enthusiastically demonstrates their new high-energy Lindy Hop dance routine, Bernard panics and flees the scene."
)

INTRO = (
    "In a Parisian restaurant, American star Sigourney Weaver meets veteran actor Bernard Verley to discuss their upcoming film. "
    "Bernard explains that at his age, he strictly limits his physical movement on set to fifteen steps per scene. "
    "When Sigourney demonstrates a high-energy swing dance that she added to the script, Bernard reacts with alarm. "
    "Let's listen to their conversation in French first."
)

OPENER = "Let's examine the conversation line by line and explore the French expressions."
TRANSITION = "Now let's listen to the complete discussion once more to reinforce the vocabulary."

STORY = [
    ("bernard", "J'aime beaucoup votre projet de film.",
     "I like your movie project very much.",
     [(610, "Par contre, je ne choisis plus les films comme avant.")], "Bernard expresses his initial enthusiasm"),
    ("lea", "C'est un honneur de jouer avec vous.",
     "It is an honour to act with you.",
     [(600, "Nous les acteurs, nous sommes masochistes")], "Sigourney flatters her legendary co-star"),
    ("bernard", "Mais j'ai une condition très stricte.",
     "But I have a very strict condition.",
     [(610, "Par contre, je ne choisis plus les films")], "Bernard introduces his unique filming rule"),
    ("lea", "Ah oui? Laquelle, cher Bernard?",
     "Oh yes? Which one, dear Bernard?",
     [(611, "C'est-à-dire?"), (614, "Et maintenant?")], "Sigourney asks with genuine curiosity"),
    ("bernard", "Je compte tous mes pas.",
     "I count all my steps.",
     [(618, "Pour les scènes debout, je compte mes pas.")], "Bernard explains his reliance on his pedometer"),
    ("bernard", "Pas plus de quinze pas par scène!",
     "No more than fifteen steps per scene!",
     [(620, "Pas plus de 15 pas par scène."), (621, "C'est dans mon contrat.")], "Bernard states his contractual limit"),
    ("lea", "Vraiment? Et pour la scène de danse?",
     "Really? And for the dance scene?",
     [(623, "Et la scène de danse?")], "Sigourney inquires about their musical sequence"),
    ("bernard", "Une danse lente, très calme, j'espère.",
     "A slow dance, very calm, I hope.",
     [(624, "C'est un slow, ça va aller...")], "Bernard anticipates a relaxed slow waltz"),
    ("lea", "Non, j'ai choisi le lindy hop!",
     "No, I chose the lindy hop!",
     [(625, "Pas du tout! Je l'ai fait changer: c'est un lindy hop.")], "Sigourney announces the energetic dance style"),
    ("bernard", "Le lindy hop? C'est très rapide!",
     "The lindy hop? That is very fast!",
     [(626, "Lindy... Lindy quoi?")], "Bernard expresses growing panic"),
    ("lea", "Regardez, je vais vous montrer.",
     "Look, I am going to show you.",
     [(627, "Je vais vous montrer.")], "Sigourney jumps up to perform the choreography"),
    ("bernard", "Mais qu'est-ce que vous faites?",
     "But what are you doing?",
     [(630, "Qu'est-ce qu'elle fait?")], "Bernard watches in horror at the fast footwork"),
    ("lea", "Dansez avec moi, c'est formidable!",
     "Dance with me, it is wonderful!",
     [(630, "Qu'est-ce qu'elle fait?")], "Sigourney attempts to pull him into the dance"),
    ("bernard", "Non, c'est trop de pas!",
     "No, that is too many steps!",
     [(631, "Bernard? Qu'est-ce qui se passe?"), (632, "Trop de pas!")], "Bernard panics and leaves immediately"),
]

WALK = [
    (0, None,
     "'I like your movie project very much.' Bernard shares his initial artistic interest. "
     "The adverb 'beaucoup' modifies the verb 'aimer'."),
    (1, None,
     "'It is an honour to act with you.' Sigourney pays polite respect to her French colleague. "
     "The noun 'honneur' designates honor or privilege."),
    (2, None,
     "'But I have a very strict condition.' Bernard introduces his personal working constraint. "
     "The adjective 'stricte' describes an inflexible rule."),
    (3, None,
     "'Oh yes? Which one, dear Bernard?' Sigourney reacts with friendly attentiveness. "
     "The interrogative pronoun 'laquelle' asks which one."),
    (4, None,
     "'I count all my steps.' Bernard monitors his physical output closely on set. "
     "The masculine noun 'pas' indicates a walking step."),
    (5, None,
     "'No more than fifteen steps per scene!' Bernard states his firm contractual limitation. "
     "The numeral 'quinze' means fifteen."),
    (6, None,
     "'Really? And for the dance scene?' Sigourney questions how his rule applies to their choreography. "
     "The noun phrase 'scene de danse' refers to a dance sequence."),
    (7, None,
     "'A slow dance, very calm, I hope.' Bernard assumes their performance will be low-energy. "
     "The feminine adjective 'lente' means slow."),
    (8, None,
     "'No, I chose the lindy hop!' Sigourney reveals that she updated the dance to swing jazz. "
     "The compound past 'ai choisi' comes from 'choisir'."),
    (9, None,
     "'The lindy hop? That is very fast!' Bernard worries about the intense physical exertion. "
     "The adjective 'rapide' means quick or speedy."),
    (10, None,
     "'Look, I am going to show you.' Sigourney offers a live demonstration right in the dining room. "
     "The infinitive 'montrer' means to show."),
    (11, None,
     "'But what are you doing?' Bernard gasps as Sigourney hops energetically across the floor. "
     "The question 'qu'est-ce que' asks what."),
    (12, None,
     "'Dance with me, it is wonderful!' Sigourney invites him to share her joy of movement. "
     "The imperative 'dansez' addresses Bernard with polite respect."),
    (13, None,
     "'No, that is too many steps!' Bernard grabs his coat and flees in terror of exceeding his quota. "
     "The quantifier 'trop de' expresses an excessive amount."),
]

OUTRO = (
    "Faced with Sigourney's unstoppable energy and dozens of dancing steps, Bernard Verley runs for the door. "
    "His abrupt departure leaves Sigourney and her agents facing another hilarious casting catastrophe. "
    "Now let's listen to the scene one last time."
)

CLOSING = ("lea", "Attendez, Bernard, revenez danser!")
