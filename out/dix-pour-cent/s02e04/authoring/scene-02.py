# Authoring module for dix-pour-cent-s02e04-scene-02.
ID = 'dix-pour-cent-s02e04-scene-02'
SHOW = 'dix-pour-cent'
SEASON = 2
EPISODE = 4
SCENE = 2
TITLE = "L'arrivée d'Isabelle Adjani  (Adjani Arrives)"
LEVEL = 'A1 — débutant'
PAIR = 'fr-en'
LABELS = {'andrea': 'Andréa', 'isabelle': 'Isabelle', 'mathias': 'Mathias'}
SOURCE_NAME = 'Dix pour cent (Call My Agent!) S02E04'
SOURCE_FILE = 'sources/dix-pour-cent/s02/e04.fr.dual.srt'
INTRO = "At the ASK offices, acclaimed French screen star Isabelle Adjani arrives to meet her agents. When Andrea mentions that young visionary director Sacha Hartman has a magnificent part for her, Isabelle expresses interest while insisting on proper artistic protocol. Let's listen to the scene in French first."
OPENER = "Let's examine how Andrea pitches the exciting new role to Isabelle Adjani."
TRANSITION = "Now let's listen to the whole elegant exchange between Andrea and Isabelle again at full speed."
OUTRO = 'Isabelle agrees to meet Sacha Hartman, on the condition that Andrea acts with utmost discretion. Andrea immediately hurries to her office to arrange the high-profile meeting. See you next time!'
CLOSING = ('isabelle', 'Bonne soirée!')
STORY = [
    ('andrea', "Bonjour Isabelle, tu vas bien aujourd'hui?", 'Hello Isabelle, are you doing well today?', [(22, '-Bonjour, Isabelle. -Bonjour.'), (23, '-Tu vas bien ? -Très bien.')], ''),
    ('isabelle', 'Très bien, Andréa, merci beaucoup.', 'Very well, Andréa, thank you very much.', [(23, '-Très bien.')], ''),
    ('isabelle', "Tu t'occupes du réalisateur Sacha Hartman?", 'Do you handle the director Sacha Hartman?', [(25, 'Le prochain film de Sacha Hartman.'), (26, "-C'est l'un des tiens ? -Je m'occupe de lui.")], ''),
    ('andrea', "Oui, je m'occupe de lui.", 'Yes, I take care of him.', [(26, "-Je m'occupe de lui.")], ''),
    ('isabelle', "J'adore son travail, il est très talentueux.", 'I love his work, he is very talented.', [(27, "Je l'adore."), (31, "C'est ça. Très talentueux.")], ''),
    ('isabelle', "Décrocher une Palme d'Or, c'est formidable.", "Winning a Palme d'Or, that is wonderful.", [(28, "Décrocher une Palme d'Or avec un premier film..."), (29, "C'est beau.")], ''),
    ('andrea', 'Il a un très beau rôle pour toi.', 'He has a very fine role for you.', [(35, 'Il a un très beau rôle pour toi.')], ''),
    ('isabelle', 'Vraiment? Mais je ne sollicite jamais les rôles.', 'Really? But I never solicit roles.', [(36, '-Vraiment ? -Oui.'), (38, "Ce n'est pas vraiment mon style"), (39, 'de solliciter des rôles.')], ''),
    ('mathias', "Isabelle préfère qu'un réalisateur lui demande.", 'Isabelle prefers that a director asks her.', [(41, "Isabelle aime qu'un réalisateur demande. C'est juste, c'est comme ça que ça marche.")], ''),
    ('andrea', 'Les réalisateurs aiment aussi se sentir désirés.', 'Directors also like to feel wanted.', [(43, 'Les réalisateurs aiment se sentir désirés.')], ''),
    ('isabelle', 'On ferait mieux de lire le scénario.', 'We had better read the script.', [(45, "On ferait mieux de lire le scénario d'abord, ne nous précipitons pas.")], ''),
    ('andrea', 'Sacha est à Paris en ce moment.', 'Sacha is in Paris right now.', [(47, 'Sacha est à Paris en ce moment.')], ''),
    ('isabelle', "D'accord, mais s'il te plaît, sois discrète.", 'All right, but please, be discreet.', [(49, "D'accord, alors."), (51, '-Attends... -Sois discret !')], ''),
    ('andrea', "Oui, bien sûr, je l'appelle maintenant.", 'Yes, of course, I call him now.', [(50, "Je l'appelle maintenant."), (52, 'Oui, bien sûr.')], ''),
]
WALK = [
    (0, None, "'Hello Isabelle, are you doing well today?' Literally 'you go well', French asks about someone's health and mood with 'go' rather than 'do' or 'be'."),
    (1, None, "'Very well, Andrea, thank you very much.' Pairing 'thanks' with 'a lot' is the standard warm reply you'll hear everywhere, never 'very much' word-for-word."),
    (2, None, "'Do you handle the director Sacha Hartman?' Saying 'occupy yourself of someone' is the idiomatic way in French to ask whether an agent represents a client."),
    (3, None, "'Yes, I take care of him.' Andrea echoes that same expression back, ending on the stressed word meaning 'him' after 'of'."),
    (4, None, "'I love his work, he is very talented.' Because 'his' or 'her' matches the thing owned in French rather than the owner, the word before 'work' looks identical either way."),
    (5, None, "'Winning a Golden Palm, that is wonderful.' Opening with a vivid action that literally means 'to unhook' pictures snagging Cannes's top prize off a high peg."),
    (6, None, "'He has a very fine role for you.' Ending on the emphatic casual 'you' after 'for' signals the warm familiarity between agent and star."),
    (7, None, "'Really? But I never solicit roles.' Wrapping the action in the negative with 'never' expresses 'never' cleanly without any extra word meaning 'not'."),
    (8, None, "'Isabelle prefers that a director asks her.' Notice how 'to her' slips right in front of 'asks' in French, whereas English puts 'her' at the end."),
    (9, None, "'Directors also like to feel wanted.' Talking about directors in general requires 'the' up front in French, unlike English where bare 'directors' stands alone."),
    (10, None, "'We had better read the script.' Everyday speech leans on a tiny subject word that literally means 'one' to say 'we', paired here with 'would do better to'."),
    (11, None, "'Sacha is in Paris right now.' Cities take the single-letter pointer meaning 'at' or 'to' in French, and the closing three words mean 'in this moment'."),
    (12, None, "'All right, but please, be discreet.' Built from 'if it pleases you' with casual 'you', this polite request precedes a sounded final consonant on 'discreet' for Andrea."),
    (13, None, "'Yes, of course, I call him now.' French happily uses the present with 'now' for an immediate promise where English reaches for 'I'll call him'."),
]
