ID = 'aangan-haveli-s01e04-scene-01'
SHOW, SEASON, EPISODE, SCENE = 'aangan-haveli', 1, 4, 1
TITLE = 'पौने सात बजे  (Six Forty-Five)'
LEVEL, PAIR = 'A1 — beginner', 'hi-en'
LABELS = {'kavya': 'काव्या', 'pratap': 'प्रताप'}

INTRO = ('It is six forty-five in the morning at Courtyard Haveli in Jaipur. While the guests still sleep '
 'upstairs, Pratap sketches a quick street map on paper for Kavya. Listen to the whole Hindi scene '
 'first.')
OPENER = "Now let's walk through the conversation one line at a time."
TRANSITION = "Now let's listen to the whole scene again from start to finish."
OUTRO = ('Left at the gate, across the stone bridge, past the green pharmacy, and left into the small '
 'square—Kavya is off on her dawn mission. See you next time.')
CLOSING = ('kavya', 'चलती हूँ!')

STORY = [('kavya',
  'सुप्रभात, प्रताप जी! क्या ऊपर बाथरूम का पानी सच में ठंडा हो गया है?',
  'Good morning, Pratap! Has the bathroom water upstairs really gone cold already?'),
 ('pratap',
  'बिल्कुल नदी के पानी जैसा ठंडा। यह टूटा हुआ पीतल का वाल्व अपनी जेब में रखो।',
  'Cold as river water. Put this broken brass valve in your pocket.'),
 ('kavya',
  'रख लिया। अब बताइए वह हार्डवेयर दुकान कैसे मिलेगी?',
  'Got it. Now tell me how to find that hardware shop.'),
 ('pratap',
  'हमारे गेट से बाएँ मुड़ो और सीधे पत्थर के पुल तक चलो।',
  'Turn left outside our gate and walk straight to the stone bridge.'),
 ('kavya',
  'गेट से बाएँ, फिर सीधे पुल तक। क्या मुझे पुल पार करना है?',
  'Left at the gate, then straight to the bridge. Do I cross the bridge?'),
 ('pratap',
  'हाँ, पुल पार करो, फिर दाएँ हाथ पर हरी दवा की दुकान दिखेगी।',
  'Yes, cross the bridge, then you will see a green pharmacy on your right.'),
 ('kavya',
  'पुल के बाद दाएँ हाथ पर हरी दवा की दुकान। और उसके बाद?',
  'Past the bridge, the green pharmacy on the right. And after that?'),
 ('pratap',
  'छोटे चौक में बाएँ मुड़ना। वहाँ एक नीला लकड़ी का दरवाज़ा ढूँढो।',
  'Turn left into the small square. Look for a blue wooden door there.'),
 ('kavya', 'क्या दुकान के बाहर कोई बड़ा बोर्ड लगा है?', 'Is there a big sign outside the shop?'),
 ('pratap',
  'दरवाज़े के ऊपर बस एक सुनहरी चाबी बनी है। दुकानदार को यह वाल्व दिखाना।',
  'Only a golden key painted above the door. Show the shopkeeper this valve.'),
 ('kavya',
  'बीस मिलीमीटर, पीतल, बॉयलर वाल्व—मैं पूरे रास्ते यही दोहराती चलूँगी!',
  'Twenty millimetres, brass, boiler valve—I will repeat that the whole way!'),
 ('pratap',
  'तेज़ दौड़ो, काव्या। कमरा चार सवा सात बजे जाग जाता है!',
  'Run fast, Kavya. Room four wakes up at seven fifteen!')]

WALK = [(0,
  None,
  ["'Good morning, Pratap! Has the bathroom water upstairs really gone cold already?' Opening a "
   'yes-or-no question with ',
   (None, 'क्या'),
   ' tells the listener right away that a question is coming, unlike English word-order flips.']),
 (1,
  None,
  ["'Cold as river water. Put this broken brass valve in your pocket.' This everyday phrase ",
   (None, 'नदी के पानी जैसा'),
   " literally means 'like the water of a river'."]),
 (3,
  None,
  ["'Turn left outside our gate and walk straight to the stone bridge.' Two handy direction words sit "
   'side by side here: ',
   (None, 'बाएँ मुड़ो'),
   ' means \'turn left\', and "seedhe" means \'straight ahead\'.']),
 (5,
  None,
  ["'Yes, cross the bridge, then you will see a green pharmacy on your right.' Speakers often say ",
   (None, 'दाएँ हाथ पर'),
   "—literally 'on the right hand'—rather than 'on your right'."]),
 (6,
  None,
  ["'Past the bridge, the green pharmacy on the right. And after that?' The handy chunk ",
   (None, 'और उसके बाद?'),
   " means 'and after that?', keeping any set of directions flowing."]),
 (11,
  None,
  ["'Run fast, Kavya. Room four wakes up at seven fifteen!' For quarter-past times, ",
   (None, 'सवा सात बजे'),
   ' puts "savaa" (\'a quarter more\') before seven to mean \'seven fifteen\'.'])]
