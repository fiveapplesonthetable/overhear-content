# Authoring module for dix-pour-cent-s04e05-scene-12.
ID = 'dix-pour-cent-s04e05-scene-12'
SHOW = 'dix-pour-cent'
SEASON = 4
EPISODE = 5
SCENE = 12
TITLE = "Trop de pas  (Too Many Steps)"
LEVEL = "A1 — débutant"
PAIR = 'fr-en'
VOICES = {"narrator": "sky", "bernard": "theo", "sigourney": "emilie"}
LABELS = {"bernard": "Bernard", "sigourney": "Sigourney"}
SOURCE_NAME = 'Dix pour cent (Call My Agent!) S04E05'
SOURCE_FILE = 'sources/dix-pour-cent/s04/e05.fr.dual.srt'
INTRO = "In a Parisian restaurant, American star Sigourney Weaver meets veteran actor Bernard Verley to discuss their upcoming film. Bernard explains that at his age, he strictly limits his physical movement on set to fifteen steps per scene. When Sigourney demonstrates a high-energy swing dance that she added to the script, Bernard reacts with alarm. Let's listen to their conversation in French first."
OPENER = "Let's examine the conversation line by line and explore the French expressions."
TRANSITION = "Now let's listen to the complete discussion once more to reinforce the vocabulary."
OUTRO = "Faced with Sigourney's unstoppable energy and dozens of dancing steps, Bernard Verley runs for the door. When you watch the episode, listen out for the expressions meaning 'like' and 'project'. You'll catch them now. See you next time."
CLOSING = ("sigourney", "Au revoir!")
STORY = [
    ('bernard', "J'aime beaucoup votre projet de film.", 'I like your movie project very much.', [], ''),
    ('sigourney', "C'est un honneur de jouer avec vous.", 'It is an honour to act with you.', [], ''),
    ('bernard', "Mais j'ai une condition très stricte.", 'But I have a very strict condition.', [], ''),
    ('sigourney', 'Ah oui? Laquelle, cher Bernard?', 'Oh yes? Which one, dear Bernard?', [(631, 'Bernard'), (631, 'Bernard')], ''),
    ('bernard', 'Je compte tous mes pas.', 'I count all my steps.', [(632, 'pas')], ''),
    ('bernard', 'Pas plus de quinze pas par scène!', 'No more than fifteen steps per scene!', [(632, 'Pas'), (632, 'Pas')], ''),
    ('sigourney', 'Vraiment? Et pour la scène de danse?', 'Really? And for the dance scene?', [], ''),
    ('bernard', "Une danse lente, très calme, j'espère.", 'A slow dance, very calm, I hope.', [], ''),
    ('sigourney', "Non, j'ai choisi le lindy hop!", 'No, I chose the lindy hop!', [], ''),
    ('bernard', "Le lindy hop? C'est très rapide!", 'The lindy hop? That is very fast!', [], ''),
    ('sigourney', 'Regardez, je vais vous montrer.', 'Look, I am going to show you.', [], ''),
    ('bernard', "Mais qu'est-ce que vous faites?", 'But what are you doing?', [(631, "qu'est-ce")], ''),
    ('sigourney', "Dansez avec moi, c'est formidable!", 'Dance with me, it is wonderful!', [], ''),
    ('bernard', "Non, c'est trop de pas!", 'No, that is too many steps!', [(631, "Bernard ? Qu'est-ce qui se passe ?"), (632, 'Trop de pas !')], ''),
]
WALK = [
    (0, None, "'I like your movie project very much.' Bernard shares his initial artistic interest. Bernard uses the polite 'you' form alongside 'like' to keep a respectful professional tone."),
    (1, None, "'It is an honour to act with you.' Sigourney pays polite respect to her French colleague. Notice how 'act' leads directly into the noun meaning 'honour'."),
    (2, None, "'But I have a very strict condition.' Bernard introduces his personal working constraint. Notice how 'have' leads directly into the noun meaning 'condition'."),
    (3, None, "'Oh yes? Which one, dear Bernard?' Sigourney reacts with friendly attentiveness. In everyday spoken French, rising intonation on 'the key idea' at the end is enough to turn the sentence into a question."),
    (4, None, "'I count all my steps.' Bernard monitors his physical output closely on set. The verb meaning 'count' pairs naturally with the noun for 'steps' in everyday conversation."),
    (5, None, "'No more than fifteen steps per scene!' Bernard states his firm contractual limitation. The key noun here means 'steps', anchored by its matching French article."),
    (6, None, "'Really? And for the dance scene?' Sigourney questions how his rule applies to their choreography. In everyday spoken French, rising intonation on 'scene' at the end is enough to turn the sentence into a question."),
    (7, None, "'A slow dance, very calm, I hope.' Bernard assumes their performance will be low-energy. The verb meaning 'hope' pairs naturally with the noun for 'dance' in everyday conversation."),
    (8, None, "'No, I chose the lindy hop!' Sigourney reveals that she updated the dance to swing jazz. This conversational past tense combines a helper verb with the past verb form for 'chosen'."),
    (9, None, "'The lindy hop? That is very fast!' Bernard worries about the intense physical exertion. The key noun here means 'Lindy Hop', anchored by its matching French article."),
    (10, None, "'Look, I am going to show you.' Sigourney offers a live demonstration right in the dining room. French forms the near future by pairing the present tense of 'to go' directly with 'show'."),
    (11, None, "'But what are you doing?' Bernard gasps as Sigourney hops energetically across the floor. The clause hinges on the everyday verb meaning 'are doing'."),
    (12, None, "'Dance with me, it is wonderful!' Sigourney invites him to share her joy of movement. Dropping the subject pronoun turns the verb for 'dance' into a direct, punchy command."),
    (13, None, "'No, that is too many steps!' Bernard grabs his coat and flees in terror of exceeding his quota. The key noun here means 'steps', anchored by its matching French article."),
]
