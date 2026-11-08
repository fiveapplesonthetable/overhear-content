# Authoring module for linden-courtyard-fr-s01e03-scene-07.
ID = 'linden-courtyard-fr-s01e03-scene-07'
SHOW = 'linden-courtyard-fr'
SEASON = 1
EPISODE = 3
SCENE = 7
TITLE = 'Returning the Notebook  (Le carnet rendu)'
LEVEL = 'A1 — débutant'
PAIR = 'en-fr'
LABELS = {'hannah': 'Hannah', 'caleb': 'Caleb'}
INTRO = "Hannah remonte jusqu'à la porte du grenier pour rapporter à Caleb son carnet de cuir oublié, tout en s'efforçant de paraître naturelle malgré ses soupçons d'inspection secrète. Tendez d'abord l'oreille."
OPENER = 'Détaillons tranquillement chaque phrase de cette courte visite.'
TRANSITION = 'Écoutons encore une fois cet échange avec toute sa fluidité.'
OUTRO = "Caleb a récupéré ses notes sans se douter de rien, mais ce radiateur qui tiédit annonce des ennuis pour la nuit. Plus qu'une scène dans ce troisième épisode: direction le sous-sol! À très vite!"
CLOSING = ('caleb', 'Have a good night!')
STORY = [('hannah', 'Excuse me, Caleb? Sorry to disturb you.', 'Excusez-moi, Caleb? Désolée de vous déranger.'),
 ('caleb', 'Oh, my leather notebook! Thank you! I was just looking for it.', 'Oh, mon carnet en cuir! Merci! Je le cherchais justement.'),
 ('hannah', 'You left it by the soup cup on the front counter.', "Vous l'avez laissé près du bol de soupe sur le comptoir d'accueil."),
 ('caleb',
  'All my street notes from this week are in here. You saved me.',
  'Toutes mes notes de terrain de la semaine sont là-dedans. Vous me sauvez.'),
 ('hannah',
  'We are glad you find our courtyard peaceful for your... work.',
  'Nous sommes ravis que vous trouviez notre cour paisible pour votre... travail.'),
 ('caleb',
  'Very peaceful! Though did you hear a funny metal knock just now?',
  "Très paisible! Mais avez-vous entendu un drôle de coup métallique à l'instant?"),
 ('hannah',
  'Yes! It sounded like it came from the heating pipe in the corner.',
  'Oui! On aurait dit que cela venait du tuyau de chauffage dans le coin.'),
 ('caleb',
  'Feel the radiator. The bottom is warm, while the top is turning cool.',
  'Touche le radiateur. Le bas est chaud, alors que le haut devient froid.'),
 ('hannah',
  'Oh! Sometimes old pipes have a little air bubble at night.',
  "Oh! Parfois les vieux tuyaux ont une petite bulle d'air la nuit."),
 ('caleb',
  'I have a warm blanket, so I am quite comfortable tonight.',
  "J'ai une couverture chaude, donc je suis tout à fait bien installé ce soir."),
 ('hannah',
  'Thank you for being so patient! Graham will check the basement right away.',
  "Merci d'être aussi compréhensif! Graham va vérifier la cave tout de suite."),
 ('caleb', 'Good night, Hannah. See you at breakfast.', 'Bonne nuit, Hannah. À demain au petit-déjeuner.')]
WALK = [(0,
  None,
  ["'Excusez-moi, Caleb? Désolée de vous déranger.' En frappant doucement à une porte, la formule",
   (None, 'Sorry to disturb you'),
   "s'excuse avec délicatesse d'interrompre quelqu'un."]),
 (1,
  None,
  ["'Oh, mon carnet en cuir! Merci! Je le cherchais justement.' L'imparfait d'action en cours se rend par le prétérit progressif dans",
   (None, 'was just looking for it'),
   'où la préposition finale reste soudée au sens de chercher.']),
 (2,
  None,
  ["'Vous l'avez laissé près du bol de soupe sur le comptoir d'accueil.' Ici la petite préposition spatiale dans",
   (None, 'by the soup cup'),
   'signifie "juste à côté de, tout près de".']),
 (3,
  None,
  ["'Toutes mes notes de terrain de la semaine sont là-dedans. Vous me sauvez.' Pour montrer l'intérieur d'un carnet qu'on tient entre les "
   'mains, on dit',
   (None, 'in here'),
   'tandis que le prétérit',
   (None, 'You saved me'),
   'constate le service déjà rendu.']),
 (4,
  None,
  ['\'Nous sommes ravis que vous trouviez notre cour paisible pour votre... travail.\' Sans conjonction "que" ni subjonctif après un '
   'adjectif de joie, Hannah enchaîne directement',
   (None, 'you find our courtyard peaceful'),
   "avec l'adjectif attribut après l'objet."]),
 (5,
  None,
  ["'Très paisible! Mais avez-vous entendu un drôle de coup métallique à l'instant?' Selon le contexte,",
   (None, 'funny'),
   'ne veut pas seulement dire comique, mais aussi bizarre ou inhabituel, suivi de',
   (None, 'just now'),
   "à l'instant même."]),
 (6,
  None,
  ["'Oui! On aurait dit que cela venait du tuyau de chauffage dans le coin.' Pour décrire une impression auditive, l'anglais idiomatique "
   'emploie',
   (None, 'It sounded like'),
   'on aurait dit au bruit que.']),
 (7,
  None,
  ["'Touchez le radiateur. Le haut est chaud, alors que le bas refroidit.' Accompagné d'un adjectif de température,",
   (None, 'turning cool'),
   'décrit une fonte progressive de la chaleur qui tiédit peu à peu.']),
 (8,
  None,
  ["'Oh! Parfois les vieux tuyaux ont une petite bulle d'air la nuit.' Alors qu'on utilise une autre préposition pour le matin ou le soir, "
   'la nuit prend la préposition ponctuelle dans',
   (None, 'at night'),
   'sans article.']),
 (9,
  None,
  ["'J'ai une couverture chaude, donc je suis tout à fait bien installé ce soir.' Devant un adjectif positif, l'intensifieur",
   (None, 'quite comfortable'),
   'rassure poliment en signifiant "tout à fait à l\'aise".']),
 (10,
  None,
  ['\'Merci d\'être aussi compréhensif! Graham va vérifier la cave tout de suite.\' Après "merci", la préposition appelle la forme '
   'nominale du verbe être dans',
   (None, 'for being so patient'),
   'avant',
   (None, 'right away'),
   'immédiatement.']),
 (11,
  None,
  ["'Bonne nuit, Hannah. À demain au petit-déjeuner.' En se quittant le soir, le rendez-vous du lendemain se fixe d'un léger",
   (None, 'at breakfast'),
   'au moment du petit-déjeuner.'])]
