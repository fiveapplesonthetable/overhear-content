ID = 'aangan-haveli-s01e01-scene-01'
SHOW, SEASON, EPISODE, SCENE = 'aangan-haveli', 1, 1, 1
TITLE = 'हैंडल ऊपर उठाइए  (Lift the Handle)'
LEVEL, PAIR = 'A1 — beginner', 'hi-en'
LABELS = {'kavya': 'काव्या', 'pratap': 'प्रताप'}

INTRO = ('Kavya arrives early for her very first morning shift at Courtyard Haveli on Champa Lane in '
 'Jaipur. Behind the front desk, veteran handyman Pratap already has hot tea waiting. Listen to '
 'the Hindi conversation first without worrying about catching every word.')
OPENER = "Now let's walk through the conversation one line at a time."
TRANSITION = "Now let's listen to the whole scene again from start to finish."
OUTRO = ('Kavya is inside, the eight brass keys are hanging on the board, and her first morning in Jaipur '
 "has begun. Don't worry if a few phrases went past quickly; you will hear them again all week. "
 'See you next time.')
CLOSING = ('kavya', 'फिर मिलेंगे!')

STORY = [('kavya', 'नमस्ते! सुनिए जी, क्या दरवाज़ा बंद है?', 'Hello! Excuse me, is the door locked?'),
 ('pratap',
  'नमस्ते। नहीं, पहले हैंडल ऊपर उठाइए, फिर धक्का दीजिए।',
  'Hello. No, lift the handle up first, then push.'),
 ('kavya',
  'अरे, खुल गया! शुक्रिया। मैं काव्या हूँ, नई रिसेप्शनिस्ट।',
  'Oh, it opened! Thank you. I am Kavya, the new receptionist.'),
 ('pratap', 'मैं प्रताप हूँ। तुम दस मिनट जल्दी आ गईं।', 'I am Pratap. You arrived ten minutes early.'),
 ('kavya',
  'पहले दिन मैं हमेशा तेज़ चलती हूँ। कंप्यूटर कहाँ है?',
  'On my first day I always walk fast. Where is the computer?'),
 ('pratap',
  'दराज़ में। यहाँ हम यह बड़ा काग़ज़ का रजिस्टर और पेंसिल इस्तेमाल करते हैं।',
  'In the drawer. Here we use this big paper register and a pencil.'),
 ('kavya', 'काग़ज़ का रजिस्टर? सच में?', 'A paper register? Really?'),
 ('pratap',
  'बिजली जाने पर भी काग़ज़ हमेशा काम करता है।',
  'Paper still works when the power goes out.'),
 ('kavya', 'सही बात है! और ये चाबियाँ हैं?', 'Fair point! And are these the keys?'),
 ('pratap',
  'हाँ, आठ कमरे, पीतल की आठ चाबियाँ। आज कमरा चार की मेहमान आ रही हैं।',
  "Yes, eight rooms, eight brass keys. Room four's guest arrives today."),
 ('kavya',
  'बहुत अच्छा। मुझे जो कुछ जानना ज़रूरी है, सब बता दीजिए।',
  'Great. Please tell me everything I need to know.'),
 ('pratap',
  'पहला नियम: पहले गरम चाय पियो, फिर घंटी का जवाब दो।',
  'Rule one: drink hot tea first, then answer the bell.')]

WALK = [(0,
  None,
  ["'Hello! Excuse me, is the door locked?' ",
   (None, 'सुनिए जी,'),
   " literally means 'please listen', and adding 'ji' makes it the warm, everyday North Indian way to "
   "get a stranger's attention politely."]),
 (1,
  None,
  ["'Hello. No, lift the handle up first, then push.' Pratap links ",
   (None, 'पहले'),
   " for 'first' with ",
   (None, 'फिर'),
   " for 'then' to lay out two quick steps in order."]),
 (2,
  None,
  ["'Oh, it opened! Thank you. I am Kavya, the new receptionist.' Hindi puts 'am' right at the end, so ",
   (None, 'मैं काव्या हूँ,'),
   " runs word-for-word as 'I Kavya am'."]),
 (3,
  None,
  ["'I am Pratap. You arrived ten minutes early.' Pratap chooses ",
   (None, 'तुम'),
   ", the friendly mid-level 'you' that an older colleague naturally uses with a younger teammate."]),
 (4,
  None,
  ["'On my first day I always walk fast. Where is the computer?' Because Kavya is a woman, ",
   (None, 'चलती हूँ।'),
   " carries the long 'ee' sound for 'I walk', whereas a man says 'chalta hoon'."]),
 (6,
  None,
  ["'A paper register? Really?' The two-word phrase ",
   (None, 'सच में?'),
   " literally asks 'in truth?' and works everywhere English speakers say 'really?' or 'seriously?'."]),
 (8,
  None,
  ["'Fair point! And are these the keys?' One singular 'chaabee' becomes ",
   (None, 'चाबियाँ'),
   " in the plural by softening the final vowel and adding nasal 'yaan'."]),
 (11,
  None,
  ["'Rule one: drink hot tea first, then answer the bell.' Here Pratap drops into friendly 'tum' "
   'requests with ',
   (None, 'गरम चाय पियो,'),
   " meaning 'drink hot tea'—warm and welcoming rather than stiff."])]
