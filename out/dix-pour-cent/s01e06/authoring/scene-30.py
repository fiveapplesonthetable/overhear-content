# Authoring module for dix-pour-cent s01e06 scene 30 (cues 764-822).
# Build: python3 tools/compose.py out/dix-pour-cent/s01e06/authoring/scene-30.py --out out/dix-pour-cent/s01e06/scene-30.json

ID = "dix-pour-cent-s01e06-scene-30"
SHOW = "dix-pour-cent"
SEASON = 1
EPISODE = 6
SCENE = 30
TITLE = "Le whisky de Samuel et le cinéma  (Samuel's Whiskey and the Movies)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "mathias": "theo", "gabriel": "marcel"}
LABELS = {"lea": "Andréa", "mathias": "Mathias", "gabriel": "Gabriel"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S01E06"
SOURCE_FILE = "sources/dix-pour-cent/s01/e06.fr.dual.srt"
SOURCE_NOTE = (
    "Cues 764-822. That night at ASK, the four partners drink Samuel Kerr's whiskey together and "
    "tease a tipsy Mathias about his mysterious three-day disappearance at his first Cannes Festival; "
    "afterward, everyone heads home and Arlette goes to a late-night cinema with Hervé and Jean Gabin. "
    "Arlette's lines in cues 788, 805, and 821-822 are given to Andréa to stay within three voices."
)

INTRO = (
    "Night has fallen over ASK after Colette's devastating tax audit verdict. Camille, Noémie, and "
    "Hervé search the empty building and find the four partners—Mathias, Andréa, Gabriel, and Arlette—"
    "sitting together in Samuel Kerr's old office with a bottle of his finest whiskey. Listen to the French first."
)

STORY = [
    ("gabriel", "D'abord, on a pensé à un suicide collectif... Enfin, moi. Un suicide collectif tout seul.",
     "First, we thought about a collective suicide... Well, I did. A collective suicide all by myself.",
     [(769, "D'abord, on a pensé à un suicide collectif"), (770, "Enfin, moi. Un suicide collectif tout seul")], ""),
    ("lea", "Mais finalement, on a trouvé le whisky de Samuel, donc on ne se tue pas.",
     "But finally, we found Samuel's whiskey, so we're not killing ourselves.",
     [(774, "Mais finalement, on a trouvé le whisky de Samuel, donc on ne se tue pas")], ""),
    ("lea", "Tu es ivre, Mathias. Je ne t'ai jamais vu ivre!",
     "You are drunk, Mathias. I have never seen you drunk!",
     [(780, "Tu es ivre, Mathias"), (781, "Je ne t'ai jamais vu ivre")], ""),
    ("mathias", "Je ne suis pas ivre, pas du tout!",
     "I am not drunk, not at all!",
     [(782, "Je ne suis pas ivre, pas du tout")], ""),
    ("gabriel", "C'est comme ton premier Festival de Cannes. Tu avais disparu pendant trois jours.",
     "It's like your first Cannes Festival. You had disappeared for three days.",
     [(783, "C'est comme ton premier Festival de Cannes"), (785, "Tu avais disparu pendant trois jours")], ""),
    ("lea", "C'était un jeune homme sobre, toujours très professionnel...",
     "He was a sober young man, always very professional...",
     [(788, "C'était un jeune homme sobre, toujours très professionnel")], "spoken by Arlette in the episode"),
    ("gabriel", "Mais il y avait cette fête dans une villa avec une piscine...",
     "But there was this party in a villa with a swimming pool...",
     [(789, "Mais il y avait cette fête"), (790, "dans une villa avec une piscine")], "'somptueuse' omitted for A1"),
    ("lea", "Ne parlez pas de piscine, s'il vous plaît!",
     "Don't talk about swimming pools, please!",
     [(791, "Ne parlez pas de piscine, s'il vous plaît")], ""),
    ("gabriel", "Qu'est-ce que tu as fait pendant trois jours? On veut savoir!",
     "What did you do for three days? We want to know!",
     [(798, "Qu'est-ce que tu as fait pendant trois jours"), (800, "On veut savoir")], ""),
    ("mathias", "Je ne me souviens pas, Gabriel.",
     "I don't remember, Gabriel.",
     [(799, "Je ne me souviens pas, Gabriel")], ""),
    ("lea", "On va s'en sortir, les enfants. On l'a toujours fait.",
     "We're going to get through this, kids. We always have.",
     [(805, "On va s'en sortir, les enfants. On l'a toujours fait")], "spoken by Arlette in the episode"),
    ("mathias", "Bonne nuit. À bientôt, Camille.",
     "Good night. See you soon, Camille.",
     [(806, "Bonne nuit"), (811, "À bientôt, Camille")], ""),
    ("lea", "Quand tout va mal, il y a toujours le cinéma.",
     "When everything is going badly, there is always the movies.",
     [(821, "Quand tout va mal"), (822, "il y a toujours le cinéma")], "spoken by Arlette to Hervé outside the cinema in the episode"),
]

OPENER = "Let's walk through the scene line by line. Gabriel explains to the assistants what the partners are doing on the floor of Samuel's office."

WALK = [
    (0, None,
     "'First, we thought about a collective suicide... Well, I did. A collective suicide all by myself.' The phrase 'all alone' means 'all by myself'."),
    (1, None,
     "'But finally, we found Samuel's whiskey, so we're not killing ourselves.' Drinking their late founder's whiskey brings the four rivals back together."),
    (2, None,
     "'You are drunk, Mathias. I have never seen you drunk!' The negation 'not... never' wraps around the helper verb 'have'."),
    (3, None,
     "'I am not drunk, not at all!' The fixed phrase 'not of the all' means 'not at all'."),
    (4, None,
     "'It's like your first Cannes Festival. You had disappeared for three days.' Gabriel brings up a legendary agency mystery from twenty years ago."),
    (5, None,
     "'He was a sober young man, always very professional...' Even in his twenties, Mathias was known for being buttoned-up and serious."),
    (6, None,
     "'But there was this party in a villa with a swimming pool...' The imperfect form 'there was' sets the scene of the Cannes party."),
    (7, None,
     "'Don't talk about swimming pools, please!' After Francois Berleand's pool drama and falling into the water at the party, Andrea never wants to hear the word 'pool' again."),
    (8, None,
     "'What did you do for three days? We want to know!' Everyone presses Mathias for his secret."),
    (9, None,
     "'I don't remember, Gabriel.' Mathias smiles enigmatically, keeping the memory of Camille's mother to himself."),
    (10, None,
     "'We're going to get through this, kids. We always have.' The reflexive verb 'to get oneself out of it' means 'to pull through' or 'to manage'."),
    (11, None,
     "'Good night. See you soon, Camille.' Down on the street, Mathias gives his daughter a warm farewell as she stays on at ASK."),
    (12, None,
     "'When everything is going badly, there is always the movies.' As Arlette slips into a late-night cinema with Hervé and her dog Jean Gabin, she sums up the spirit of the whole agency."),
]

TRANSITION = "Now let's listen to the whole scene again from start to finish."

OUTRO = (
    "That concludes Episode 6 and Season 1 of Dix pour cent! Even with a tax audit and personal heartbreak, "
    "the ASK family sticks together for the love of cinema. See you in Season 2!"
)
CLOSING = ("lea", "Quand tout va mal, il y a toujours le cinéma.")
