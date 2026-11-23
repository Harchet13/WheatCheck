"""All user-facing text for WheatCheck, per language.

Disease entries are keyed by the class names in best.pt. To add a language,
add an entry to LANGUAGES and a matching dict to TEXT with the same keys.
"""

# Radio-button label -> key into TEXT, in display order.
LANGUAGES = {"English": "en", "ਪੰਜਾਬੀ": "pa", "हिंदी": "hi"}

# Model class -> sample image shown in the landing-page gallery.
GALLERY = {
    'Aphid': 'assets/samples/aphid_1.jpeg',
    'Brown Rust': 'assets/samples/brown_rust_462.png',
    'Mite': 'assets/samples/mite_26.jpeg',
    'Stem fly': 'assets/samples/stem_fly_30.jpeg',
    'Black Rust': 'assets/samples/black_rust_1.jpeg',
    'Common Root Rot': 'assets/samples/common_root_rot_73.png',
    'Leaf Blight': 'assets/samples/leaf_blight_38.jpeg',
    'Septoria': 'assets/samples/septoria_5.png',
    'Tan spot': 'assets/samples/tan_spot_24.jpeg',
    'Blast': 'assets/samples/blast_1.jpeg',
    'Fusarium Head Blight': 'assets/samples/fusarium_head_blight_test_0.png',
    'Mildew': 'assets/samples/mildew_82.png',
    'Smut': 'assets/samples/smut_test_0.png',
    'Yellow Rust': 'assets/samples/yellow_rust_test_3.png',
}

# Online agri-input shops: name -> URL. A URL with {} is a product search,
# filled in with the product's search words. A URL without {} is the shop's home
# page; the app tells farmers to type the product name into the shop's search bar.
# (BigHaat's search pages can't be linked to directly.)
SHOPS = {
    'Amazon': 'https://www.amazon.in/s?k={}',
    'BigHaat': 'https://www.bighaat.com/',
}

# Model class -> products a farmer can buy to act on the remedies, as
# (name to search for, active ingredient or description, product type).
# Names are common Indian brands where one is well known; generic products use
# their plain name. Types are translated via TEXT[lang]['product_types'].
PRODUCTS = {
    'Aphid': [
        ('Confidor', 'Imidacloprid 17.8% SL', 'insecticide'),
        ('Actara', 'Thiamethoxam 25% WG', 'insecticide'),
        ('Neem oil', 'Azadirachtin 1500 ppm', 'bio'),
    ],
    'Brown Rust': [
        ('Tilt', 'Propiconazole 25% EC', 'fungicide'),
        ('Folicur', 'Tebuconazole 25.9% EC', 'fungicide'),
        ('Muriate of Potash', 'Potassium chloride (MOP)', 'fertilizer'),
    ],
    'Mite': [
        ('Thiovit Jet', 'Sulphur 80% WDG', 'miticide'),
        ('Rogor', 'Dimethoate 30% EC', 'insecticide'),
        ('Neem oil', 'Azadirachtin 1500 ppm', 'bio'),
    ],
    'Stem fly': [
        ('Cruiser', 'Thiamethoxam 30% FS', 'seed'),
        ('Gaucho', 'Imidacloprid 48% FS', 'seed'),
    ],
    'Black Rust': [
        ('Tilt', 'Propiconazole 25% EC', 'fungicide'),
        ('Folicur', 'Tebuconazole 25.9% EC', 'fungicide'),
        ('Muriate of Potash', 'Potassium chloride (MOP)', 'fertilizer'),
    ],
    'Common Root Rot': [
        ('Bavistin', 'Carbendazim 50% WP', 'seed'),
        ('Trichoderma viride', 'Bio-fungicide', 'bio'),
        ('NPK 12-32-16', 'Nitrogen-phosphorus-potash', 'fertilizer'),
    ],
    'Leaf Blight': [
        ('Dithane M-45', 'Mancozeb 75% WP', 'fungicide'),
        ('Tilt', 'Propiconazole 25% EC', 'fungicide'),
    ],
    'Septoria': [
        ('Tilt', 'Propiconazole 25% EC', 'fungicide'),
        ('Dithane M-45', 'Mancozeb 75% WP', 'fungicide'),
    ],
    'Tan spot': [
        ('Dithane M-45', 'Mancozeb 75% WP', 'fungicide'),
        ('Custodia', 'Azoxystrobin 11% + Tebuconazole 18.3% SC', 'fungicide'),
    ],
    'Blast': [
        ('Nativo', 'Tebuconazole 50% + Trifloxystrobin 25% WG', 'fungicide'),
        ('Beam', 'Tricyclazole 75% WP', 'fungicide'),
    ],
    'Fusarium Head Blight': [
        ('Folicur', 'Tebuconazole 25.9% EC', 'fungicide'),
        ('Bavistin', 'Carbendazim 50% WP', 'fungicide'),
    ],
    'Mildew': [
        ('Sulfex', 'Sulphur 80% WP', 'fungicide'),
        ('Tilt', 'Propiconazole 25% EC', 'fungicide'),
    ],
    'Smut': [
        ('Vitavax Power', 'Carboxin 37.5% + Thiram 37.5% WS', 'seed'),
        ('Raxil', 'Tebuconazole 2% DS', 'seed'),
    ],
    'Yellow Rust': [
        ('Tilt', 'Propiconazole 25% EC', 'fungicide'),
        ('Nativo', 'Tebuconazole 50% + Trifloxystrobin 25% WG', 'fungicide'),
        ('Muriate of Potash', 'Potassium chloride (MOP)', 'fertilizer'),
    ],
    'Healthy': [
        ('NPK 19-19-19', 'Water-soluble NPK', 'fertilizer'),
        ('Zinc sulphate', 'Zinc sulphate 33%', 'fertilizer'),
    ],
}

TEXT = {
    'en': {
        'title': 'WheatCheck - Wheat Disease Detection',
        'tagline': 'Snap a photo of your wheat and find out what is wrong and how to treat it.',
        'intro': [
            {
                'heading': 'Safeguarding Global Food Security',
                'paragraphs': [
                    'Wheat feeds billions of people, but pests and diseases destroy an estimated 21.5% of the world’s wheat every year. That is about 209 million tonnes, worth around $31 billion.',
                ],
            },
            {
                'heading': 'Understanding the Challenge',
                'paragraphs': [
                    'Fungi, bacteria, viruses and insects can all attack wheat. Diseases such as rusts, powdery mildew and blight, and pests such as aphids and stem flies, can ruin a field if they are not caught early. The losses hurt farmers first, and then push up food prices for everyone.',
                ],
            },
        ],
        'about': [
            {
                'heading': 'The Role of Technology in Early Detection',
                'paragraphs': [
                    'WheatCheck uses artificial intelligence (AI) to recognise wheat diseases and pests from a single photo. Finding a problem early lets farmers act before it spreads, protecting their yield and income.',
                ],
                'image': 'assets/farmer.webp',
            },
            {
                'heading': 'How It Works',
                'items': [
                    'Take a photo: photograph the affected leaf, stem or ear with your phone.',
                    'Analysis: a machine-learning model trained on about 13,000 wheat photos checks it for 14 diseases and pests.',
                    'Diagnosis: the app names the problem and shows how sure it is.',
                    'Action: you get the causes, prevention and remedies, with products you can buy.',
                ],
                'numbered': True,
            },
            {
                'heading': 'The Impact',
                'paragraphs': [
                    'Catching disease early means smaller losses, less wasted spraying and better profits for farmers, and a more secure food supply for everyone.',
                ],
            },
            {
                'heading': 'Join the Movement',
                'paragraphs': [
                    'Share WheatCheck with other farmers and help protect one of the world’s most important crops.',
                ],
            },
        ],
        'steps_heading': 'Steps to use the app',
        'steps': [
            'Take a clear, close photo of the affected leaf, stem or ear',
            'Upload the photo below',
            'Tap Analyze to see the problem and how to treat it',
        ],
        'upload_label': 'Upload your photo',
        'analyze_button': 'Analyze',
        'upload_first': 'Please upload a photo first.',
        'image_heading': 'Your photo',
        'no_disease': 'No disease or pest found. Your crop looks healthy.',
        'healthy_tip': 'Keep it strong with balanced fertilizer:',
        'low_confidence': 'The app isn’t sure about this photo. Please take another one using the tips below.',
        'photo_tips_heading': 'Tips for a good photo',
        'photo_tips': [
            'Fill the photo with the affected leaf or ear.',
            'Take it in daylight and avoid shadows.',
            'Hold the phone steady so the photo is sharp.',
        ],
        'disease_label': 'Detected',
        'confidence_label': 'Confidence',
        'causes_label': 'Causes',
        'preventions_label': 'Prevention',
        'remedies_label': 'Remedies',
        'how_to_button': '▶️ How to use',
        'samples_button': '🖼️ Sample images',
        'about_button': 'ℹ️ About',
        'samples_intro': 'These are the diseases and pests WheatCheck can recognise.',
        'animation_captions': [
            'Take a clear photo of the sick leaf or ear',
            'Upload the photo',
            'Tap Analyze',
            'See the problem and buy the remedy',
        ],
        'buy_heading': '🛒 Where to buy',
        'shop_search_hint': 'BigHaat opens on its home page: type the name in bold into its search bar.',
        'buy_note': 'Always read the product label for dose and safety, and check with your local agriculture officer or Krishi Vigyan Kendra before spraying.',
        'product_types': {
            'fungicide': 'Fungicide',
            'insecticide': 'Insecticide',
            'miticide': 'Miticide',
            'fertilizer': 'Fertilizer',
            'bio': 'Organic / bio-control',
            'seed': 'Seed treatment',
        },
        'disease_names': {
            'Aphid': 'Aphid',
            'Brown Rust': 'Brown Rust',
            'Mite': 'Mite',
            'Stem fly': 'Stem Fly',
            'Black Rust': 'Black Rust',
            'Common Root Rot': 'Common Root Rot',
            'Leaf Blight': 'Leaf Blight',
            'Septoria': 'Septoria Leaf Blotch',
            'Tan spot': 'Tan Spot',
            'Blast': 'Wheat Blast',
            'Fusarium Head Blight': 'Fusarium Head Blight',
            'Mildew': 'Powdery Mildew',
            'Smut': 'Loose Smut',
            'Yellow Rust': 'Yellow Rust',
        },
        'diseases': {
            'Aphid': {
                'description': 'Aphids are tiny, soft-bodied green or dark insects, about the size of a pinhead. They cluster on leaves and ears and suck the plant’s sap.',
                'causes': [
                    'Aphids multiply fast in cool, cloudy weather, usually from January to March.',
                    'Too much nitrogen fertilizer makes plants soft and more attractive to aphids.',
                ],
                'preventions': [
                    'Sow on time; late-sown wheat is attacked more.',
                    'Don’t use more nitrogen fertilizer than recommended.',
                    'Protect ladybirds and other natural enemies by not spraying unless needed.',
                ],
                'remedies': [
                    'Spray an insecticide when you see about 5 aphids per ear.',
                    'For a light attack or organic farming, spray neem oil.',
                ],
            },
            'Brown Rust': {
                'description': 'Brown (leaf) rust shows as small, round, orange-brown powdery pustules scattered over the leaves. It spreads in mild, humid weather and reduces green leaf area, yield and grain weight.',
                'causes': [
                    'Caused by the fungus Puccinia triticina.',
                    'Its spores blow in on the wind from infected fields.',
                ],
                'preventions': [
                    'Sow rust-resistant varieties recommended for your area.',
                    'Use balanced fertilizer with enough potash; too much nitrogen increases rust.',
                ],
                'remedies': [
                    'Spray a fungicide such as propiconazole or tebuconazole as soon as you see pustules.',
                    'Repeat after 15 days if the disease continues.',
                ],
            },
            'Mite': {
                'description': 'Mites are tiny eight-legged pests, reddish-brown to black, that are hard to see without a lens. They suck sap, leaving leaves speckled, yellow and dry, especially in hot, dry weather.',
                'causes': [
                    'Dry weather and water stress favour mites.',
                    'They spread on the wind, on machinery and with crop residue.',
                ],
                'preventions': [
                    'Irrigate on time; well-watered crops suffer less.',
                    'Remove weeds and old crop residue, where mites breed.',
                ],
                'remedies': [
                    'When you see damage, spray wettable sulphur or a recommended product such as dimethoate.',
                    'Neem oil can help with a light attack.',
                ],
            },
            'Stem fly': {
                'description': 'Stem flies are small flies whose maggots tunnel inside wheat stems. Young plants show a dried central shoot ("dead heart"); older plants can produce white, empty ears.',
                'causes': [
                    'The flies lay eggs on young plants; the maggots bore into the stem and feed inside it.',
                    'Crops at the seedling stage are most at risk.',
                ],
                'preventions': [
                    'Treat seed with an insecticide such as thiamethoxam or imidacloprid before sowing.',
                    'Sow at the recommended time and keep the field free of grassy weeds.',
                ],
                'remedies': [
                    'Pull out and destroy plants with dead hearts.',
                    'If many plants are attacked, ask your agriculture officer which insecticide to use.',
                ],
            },
            'Black Rust': {
                'description': 'Black (stem) rust forms long, dark reddish-brown pustules on stems and leaves that turn black as the crop ripens. Badly affected stems weaken and break, and the grain shrivels.',
                'causes': [
                    'Caused by the fungus Puccinia graminis.',
                    'It favours warm, humid weather; its spores travel long distances on the wind.',
                ],
                'preventions': [
                    'Sow rust-resistant varieties.',
                    'Avoid very late sowing, which exposes the crop to more heat while the grain fills.',
                ],
                'remedies': [
                    'Spray a fungicide such as propiconazole or tebuconazole when pustules appear.',
                    'Repeat after 15 days if needed.',
                ],
            },
            'Common Root Rot': {
                'description': 'Root rot fungi attack the roots and the base of the stem, which turn dark brown. Plants grow poorly, turn yellow and may produce white, empty ears.',
                'causes': [
                    'Caused mainly by the fungus Bipolaris sorokiniana, which lives in soil, crop residue and seed.',
                    'Dry, warm soil and stressed plants make it worse.',
                ],
                'preventions': [
                    'Sow healthy seed treated with a fungicide such as carbendazim or tebuconazole.',
                    'Rotate wheat with non-cereal crops such as pulses or mustard.',
                    'Apply balanced fertilizer at sowing.',
                ],
                'remedies': [
                    'Rotted roots can’t be cured, so focus on seed treatment and soil health for the next crop.',
                    'Mix Trichoderma bio-fungicide into farmyard manure and apply it to the soil.',
                ],
            },
            'Leaf Blight': {
                'description': 'Leaf blight starts as small, reddish-brown oval spots with yellow edges, usually on the lower leaves. The spots join up and the leaves dry out early.',
                'causes': [
                    'Caused by fungi such as Bipolaris sorokiniana and Alternaria species.',
                    'Warm, humid weather after the ears come out favours it.',
                ],
                'preventions': [
                    'Sow resistant varieties and treated seed.',
                    'Use balanced fertilizer; weak, under-fed crops suffer more.',
                ],
                'remedies': [
                    'Spray mancozeb or propiconazole when spots first appear.',
                    'Repeat after 15 days if the disease spreads.',
                ],
            },
            'Septoria': {
                'description': 'Septoria leaf blotch causes long, pale-brown blotches on the leaves, with tiny black dots (spore cases) inside them. It starts on the lower leaves and moves up.',
                'causes': [
                    'Caused by the fungus Zymoseptoria tritici (Septoria tritici).',
                    'It survives on crop stubble and spreads by rain splash in cool, wet weather.',
                ],
                'preventions': [
                    'Sow resistant varieties.',
                    'After harvest, plough infected stubble into the soil or remove it.',
                ],
                'remedies': [
                    'Spray propiconazole or mancozeb when blotches appear on the upper leaves.',
                    'Repeat after 15 days in wet weather.',
                ],
            },
            'Tan spot': {
                'description': 'Tan spot starts as small, light-brown spots with a yellow ring on the leaves, which grow into larger oval patches. Badly affected leaves dry out early.',
                'causes': [
                    'Caused by the fungus Pyrenophora tritici-repentis.',
                    'It survives on wheat stubble, so it is worst where wheat follows wheat.',
                ],
                'preventions': [
                    'Rotate wheat with other crops.',
                    'Bury or remove infected stubble, and sow clean seed.',
                ],
                'remedies': [
                    'At the first signs, spray mancozeb, or a mix of azoxystrobin and tebuconazole.',
                    'Repeat after 15 days if needed.',
                ],
            },
            'Blast': {
                'description': 'Wheat blast bleaches the ears, often all at once above a dark mark on the ear’s stalk, leaving shrivelled grain or none. It appeared in Brazil in 1985 and reached Bangladesh in 2016.',
                'causes': [
                    'Caused by the fungus Magnaporthe oryzae (Triticum type).',
                    'Warm, wet weather when the ears come out favours it; it can also spread on seed.',
                ],
                'preventions': [
                    'Sow clean, treated seed from a disease-free area.',
                    'Sow at the recommended time and avoid excess nitrogen.',
                ],
                'remedies': [
                    'Spray tebuconazole plus trifloxystrobin (or tricyclazole) as the ears come out, and again 10–15 days later.',
                    'Report suspected blast to your agriculture officer; it is a new disease in South Asia.',
                ],
            },
            'Fusarium Head Blight': {
                'description': 'Fusarium head blight turns part or all of the ear pale or bleached, often with pink-orange fungal growth. The grain shrivels and can contain toxins harmful to people and animals.',
                'causes': [
                    'Caused by Fusarium fungi, which survive on maize and wheat residue.',
                    'Warm, wet weather during flowering favours infection.',
                ],
                'preventions': [
                    'Avoid sowing wheat straight after maize, and bury crop residue.',
                    'Sow resistant varieties and clean seed.',
                ],
                'remedies': [
                    'Spray tebuconazole at flowering if the weather is warm and wet.',
                    'Keep affected grain separate, and don’t feed mouldy grain to animals.',
                ],
            },
            'Mildew': {
                'description': 'Powdery mildew shows as white, powdery patches on leaves and stems that later turn grey with tiny black dots. It thrives in cool, humid weather and can cut yield by up to 40%.',
                'causes': [
                    'Caused by the fungus Blumeria graminis.',
                    'Dense crops and too much nitrogen fertilizer make it worse.',
                ],
                'preventions': [
                    'Sow resistant varieties.',
                    'Avoid excess nitrogen and very dense sowing.',
                ],
                'remedies': [
                    'Spray wettable sulphur or propiconazole when patches appear.',
                    'Repeat after 15 days if needed.',
                ],
            },
            'Smut': {
                'description': 'Loose smut replaces the grain in the ear with a mass of black, powdery spores, leaving a bare stalk once the spores blow away. Infected plants look normal until the ears come out.',
                'causes': [
                    'Caused by the fungus Ustilago tritici.',
                    'The fungus lives inside infected seed, so seed carries it from one season to the next.',
                ],
                'preventions': [
                    'Treat seed with carboxin plus thiram, or tebuconazole, before sowing.',
                    'Use certified seed from a healthy crop.',
                ],
                'remedies': [
                    'Spraying doesn’t help once the ears are infected.',
                    'Cover smutted ears with a plastic bag, pull them out and bury them before the spores spread.',
                ],
            },
            'Yellow Rust': {
                'description': 'Yellow (stripe) rust shows as bright yellow-orange powdery stripes along the leaves; the powder rubs off on your fingers. It spreads fast in cool, humid weather (about 10–20°C), often starting in patches.',
                'causes': [
                    'Caused by the fungus Puccinia striiformis.',
                    'Its spores blow in on the wind; in north India it is most common from December to February.',
                ],
                'preventions': [
                    'Sow rust-resistant varieties recommended for your area.',
                    'Check your field regularly from December, especially near trees and in shaded patches.',
                ],
                'remedies': [
                    'As soon as you see stripes, spray propiconazole, or a mix of tebuconazole and trifloxystrobin.',
                    'Repeat after 15 days if needed.',
                ],
            },
        },
    },
    'hi': {
        'title': 'वीटचेक - गेहूँ रोग की पहचान',
        'tagline': 'अपनी गेहूँ की फसल की फ़ोटो लें और जानें कि उसे क्या रोग है और उसका इलाज क्या है।',
        'intro': [
            {
                'heading': 'दुनिया की खाद्य सुरक्षा की रक्षा',
                'paragraphs': [
                    'गेहूँ दुनिया भर में अरबों लोगों का पेट भरता है, लेकिन कीट और रोग हर साल दुनिया के गेहूँ का अनुमानित 21.5% नष्ट कर देते हैं। यह लगभग 20.9 करोड़ टन गेहूँ है, जिसकी कीमत करीब 31 अरब डॉलर है।',
                ],
            },
            {
                'heading': 'चुनौती को समझें',
                'paragraphs': [
                    'गेहूँ पर फफूंद, बैक्टीरिया, वायरस और कीट, सभी हमला कर सकते हैं। रतुआ, चूर्णिल आसिता और झुलसा जैसे रोग, और माहू व तना मक्खी जैसे कीट, समय पर पहचान न होने पर पूरा खेत बर्बाद कर सकते हैं। इसका नुकसान सबसे पहले किसान को होता है, और फिर अनाज महँगा होने से सबको।',
                ],
            },
        ],
        'about': [
            {
                'heading': 'जल्दी पहचान में तकनीक की भूमिका',
                'paragraphs': [
                    'वीटचेक आर्टिफ़िशियल इंटेलिजेंस (AI) की मदद से सिर्फ़ एक फ़ोटो से गेहूँ के रोग और कीट पहचानता है। समस्या का जल्दी पता चलने से किसान उसके फैलने से पहले कदम उठा सकते हैं और अपनी उपज व कमाई बचा सकते हैं।',
                ],
                'image': 'assets/farmer.webp',
            },
            {
                'heading': 'यह कैसे काम करता है',
                'items': [
                    'फ़ोटो लें: अपने फ़ोन से प्रभावित पत्ती, तने या बाली की फ़ोटो खींचें।',
                    'जाँच: गेहूँ की लगभग 13,000 तस्वीरों पर प्रशिक्षित एक मशीन-लर्निंग मॉडल उसमें 14 रोगों और कीटों की जाँच करता है।',
                    'पहचान: ऐप समस्या का नाम बताता है, और यह भी कि वह कितना निश्चित है।',
                    'कार्रवाई: आपको कारण, रोकथाम और उपाय मिलते हैं, साथ में खरीदने लायक दवाएँ और खाद भी।',
                ],
                'numbered': True,
            },
            {
                'heading': 'प्रभाव',
                'paragraphs': [
                    'रोग की जल्दी पहचान से नुकसान कम होता है, बेवजह छिड़काव बचता है और किसान का मुनाफ़ा बढ़ता है। इससे सबके लिए अनाज की आपूर्ति भी सुरक्षित रहती है।',
                ],
            },
            {
                'heading': 'हमारे साथ जुड़ें',
                'paragraphs': [
                    'वीटचेक को दूसरे किसानों के साथ साझा करें और दुनिया की सबसे ज़रूरी फसलों में से एक को बचाने में मदद करें।',
                ],
            },
        ],
        'steps_heading': 'ऐप का उपयोग करने के चरण',
        'steps': [
            'प्रभावित पत्ती, तने या बाली की साफ़ और नज़दीक से फ़ोटो लें',
            'नीचे फ़ोटो अपलोड करें',
            'समस्या और उसका इलाज देखने के लिए "जाँच करें" दबाएँ',
        ],
        'upload_label': 'अपनी फ़ोटो अपलोड करें',
        'analyze_button': 'जाँच करें',
        'upload_first': 'कृपया पहले एक फ़ोटो अपलोड करें।',
        'image_heading': 'आपकी फ़ोटो',
        'no_disease': 'कोई रोग या कीट नहीं मिला। आपकी फसल स्वस्थ दिखती है।',
        'healthy_tip': 'संतुलित खाद से इसे मज़बूत रखें:',
        'low_confidence': 'ऐप इस फ़ोटो को लेकर निश्चित नहीं है। कृपया नीचे दिए सुझावों के साथ दूसरी फ़ोटो लें।',
        'photo_tips_heading': 'अच्छी फ़ोटो के लिए सुझाव',
        'photo_tips': [
            'प्रभावित पत्ती या बाली फ़ोटो में बड़ी और साफ़ दिखे।',
            'दिन की रोशनी में फ़ोटो लें और छाया से बचें।',
            'फ़ोन को स्थिर रखें ताकि फ़ोटो धुंधली न हो।',
        ],
        'disease_label': 'पहचान',
        'confidence_label': 'निश्चितता',
        'causes_label': 'कारण',
        'preventions_label': 'रोकथाम',
        'remedies_label': 'उपाय',
        'how_to_button': '▶️ उपयोग कैसे करें',
        'samples_button': '🖼️ नमूना तस्वीरें',
        'about_button': 'ℹ️ जानकारी',
        'samples_intro': 'ये वे रोग और कीट हैं जिन्हें वीटचेक पहचान सकता है।',
        'animation_captions': [
            'बीमार पत्ती या बाली की साफ़ फ़ोटो लें',
            'फ़ोटो अपलोड करें',
            '"जाँच करें" दबाएँ',
            'समस्या देखें और दवा खरीदें',
        ],
        'buy_heading': '🛒 कहाँ से खरीदें',
        'shop_search_hint': 'BigHaat अपने होम पेज पर खुलता है: मोटे अक्षरों में लिखा नाम उसके सर्च बार में लिखें।',
        'buy_note': 'मात्रा और सुरक्षा के लिए हमेशा उत्पाद का लेबल पढ़ें, और छिड़काव से पहले अपने स्थानीय कृषि अधिकारी या कृषि विज्ञान केंद्र से सलाह लें।',
        'product_types': {
            'fungicide': 'फफूंदनाशक',
            'insecticide': 'कीटनाशक',
            'miticide': 'माइटनाशक',
            'fertilizer': 'खाद',
            'bio': 'जैविक',
            'seed': 'बीज उपचार',
        },
        'disease_names': {
            'Aphid': 'माहू (चेपा)',
            'Brown Rust': 'भूरा रतुआ',
            'Mite': 'माइट (बरुथी)',
            'Stem fly': 'तना मक्खी',
            'Black Rust': 'काला रतुआ',
            'Common Root Rot': 'जड़ सड़न',
            'Leaf Blight': 'पत्ती झुलसा',
            'Septoria': 'सेप्टोरिया पत्ती धब्बा',
            'Tan spot': 'टैन स्पॉट',
            'Blast': 'गेहूँ ब्लास्ट',
            'Fusarium Head Blight': 'फ्यूजेरियम बाली झुलसा',
            'Mildew': 'चूर्णिल आसिता (पाउडरी मिल्ड्यू)',
            'Smut': 'खुला कंडुआ (लूज़ स्मट)',
            'Yellow Rust': 'पीला रतुआ',
        },
        'diseases': {
            'Aphid': {
                'description': 'माहू (चेपा) छोटे, मुलायम शरीर वाले हरे या गहरे रंग के कीट हैं, जो आलपिन के सिरे जितने बड़े होते हैं। ये पत्तियों और बालियों पर झुंड में बैठकर पौधे का रस चूसते हैं।',
                'causes': [
                    'ठंडे और बादल वाले मौसम में, आमतौर पर जनवरी से मार्च तक, माहू तेज़ी से बढ़ते हैं।',
                    'ज़्यादा नाइट्रोजन खाद से पौधे नरम हो जाते हैं और माहू को ज़्यादा आकर्षित करते हैं।',
                ],
                'preventions': [
                    'समय पर बुवाई करें; पछेती बोई गई फसल पर हमला ज़्यादा होता है।',
                    'अनुशंसित मात्रा से ज़्यादा नाइट्रोजन खाद न डालें।',
                    'लेडीबर्ड भृंग जैसे मित्र कीटों को बचाएँ; बिना ज़रूरत छिड़काव न करें।',
                ],
                'remedies': [
                    'जब प्रति बाली लगभग 5 माहू दिखें, तब कीटनाशक का छिड़काव करें।',
                    'हल्के हमले या जैविक खेती में नीम तेल का छिड़काव करें।',
                ],
            },
            'Brown Rust': {
                'description': 'भूरा रतुआ पत्तियों पर बिखरे हुए छोटे, गोल, नारंगी-भूरे पाउडर जैसे फफोलों के रूप में दिखता है। यह हल्के गर्म और नम मौसम में फैलता है, और पत्तियों का हरा भाग, उपज और दाने का वज़न घटाता है।',
                'causes': [
                    'पक्सीनिया ट्रिटिसिना नामक फफूंद से होता है।',
                    'इसके बीजाणु हवा के साथ रोगी खेतों से उड़कर आते हैं।',
                ],
                'preventions': [
                    'अपने क्षेत्र के लिए अनुशंसित रतुआ-रोधी किस्में बोएँ।',
                    'पर्याप्त पोटाश वाली संतुलित खाद डालें; ज़्यादा नाइट्रोजन से रतुआ बढ़ता है।',
                ],
                'remedies': [
                    'फफोले दिखते ही प्रोपिकोनाज़ोल या टेबुकोनाज़ोल जैसे फफूंदनाशक का छिड़काव करें।',
                    'रोग बना रहे तो 15 दिन बाद दोबारा छिड़काव करें।',
                ],
            },
            'Mite': {
                'description': 'माइट (बरुथी) आठ टाँगों वाले बहुत छोटे जीव हैं, जो लाल-भूरे से काले रंग के होते हैं और बिना लेंस के मुश्किल से दिखते हैं। ये रस चूसते हैं, जिससे पत्तियों पर चित्तियाँ पड़ जाती हैं और वे पीली होकर सूख जाती हैं, ख़ासकर गर्म और सूखे मौसम में।',
                'causes': [
                    'सूखा मौसम और पानी की कमी माइट को बढ़ाते हैं।',
                    'ये हवा, मशीनों और फसल के अवशेषों के साथ फैलते हैं।',
                ],
                'preventions': [
                    'समय पर सिंचाई करें; अच्छी तरह सिंचित फसल पर असर कम होता है।',
                    'खरपतवार और पिछली फसल के अवशेष हटाएँ, जिनमें माइट पलते हैं।',
                ],
                'remedies': [
                    'नुकसान दिखने पर घुलनशील गंधक (सल्फ़र) या डाइमेथोएट जैसी अनुशंसित दवा का छिड़काव करें।',
                    'हल्के हमले में नीम तेल भी मदद कर सकता है।',
                ],
            },
            'Stem fly': {
                'description': 'तना मक्खी छोटी मक्खियाँ हैं जिनकी सूंडियाँ (मैगट) गेहूँ के तने के अंदर सुरंग बनाती हैं। छोटे पौधों में बीच की गोभ सूख जाती है ("डेड हार्ट"), और बड़े पौधों में सफ़ेद, खाली बालियाँ निकल सकती हैं।',
                'causes': [
                    'मक्खी छोटे पौधों पर अंडे देती है; उनसे निकली सूंडियाँ तने में घुसकर अंदर से खाती हैं।',
                    'अंकुर अवस्था की फसल पर सबसे ज़्यादा ख़तरा होता है।',
                ],
                'preventions': [
                    'बुवाई से पहले बीज को थायामेथोक्साम या इमिडाक्लोप्रिड जैसे कीटनाशक से उपचारित करें।',
                    'अनुशंसित समय पर बुवाई करें और खेत को घास वाले खरपतवारों से साफ़ रखें।',
                ],
                'remedies': [
                    '"डेड हार्ट" वाले पौधों को उखाड़कर नष्ट करें।',
                    'ज़्यादा पौधे प्रभावित हों तो अपने कृषि अधिकारी से पूछें कि कौन-सा कीटनाशक इस्तेमाल करें।',
                ],
            },
            'Black Rust': {
                'description': 'काला रतुआ तनों और पत्तियों पर लंबे, गहरे लाल-भूरे फफोले बनाता है, जो फसल पकने पर काले हो जाते हैं। ज़्यादा प्रभावित तने कमज़ोर होकर टूट जाते हैं और दाने सिकुड़ जाते हैं।',
                'causes': [
                    'पक्सीनिया ग्रैमिनिस नामक फफूंद से होता है।',
                    'यह गर्म और नम मौसम में बढ़ता है; इसके बीजाणु हवा से बहुत दूर तक जाते हैं।',
                ],
                'preventions': [
                    'रतुआ-रोधी किस्में बोएँ।',
                    'बहुत पछेती बुवाई से बचें, ताकि दाना भरते समय फसल ज़्यादा गर्मी में न आए।',
                ],
                'remedies': [
                    'फफोले दिखने पर प्रोपिकोनाज़ोल या टेबुकोनाज़ोल जैसे फफूंदनाशक का छिड़काव करें।',
                    'ज़रूरत हो तो 15 दिन बाद दोबारा छिड़काव करें।',
                ],
            },
            'Common Root Rot': {
                'description': 'जड़ सड़न की फफूंद जड़ों और तने के निचले हिस्से पर हमला करती है, जो गहरे भूरे हो जाते हैं। पौधे कमज़ोर रहते हैं, पीले पड़ जाते हैं और उनमें सफ़ेद, खाली बालियाँ निकल सकती हैं।',
                'causes': [
                    'मुख्य रूप से बाइपोलैरिस सोरोकिनियाना फफूंद से होता है, जो मिट्टी, फसल अवशेषों और बीज में रहती है।',
                    'सूखी, गर्म मिट्टी और कमज़ोर पौधों में यह ज़्यादा फैलता है।',
                ],
                'preventions': [
                    'कार्बेन्डाज़िम या टेबुकोनाज़ोल से उपचारित स्वस्थ बीज बोएँ।',
                    'गेहूँ के बाद दलहन या सरसों जैसी गैर-अनाज फसलें लें।',
                    'बुवाई के समय संतुलित खाद डालें।',
                ],
                'remedies': [
                    'सड़ी जड़ें ठीक नहीं हो सकतीं, इसलिए अगली फसल के लिए बीज उपचार और मिट्टी की सेहत पर ध्यान दें।',
                    'ट्राइकोडर्मा जैविक फफूंदनाशक को गोबर की खाद में मिलाकर मिट्टी में डालें।',
                ],
            },
            'Leaf Blight': {
                'description': 'पत्ती झुलसा छोटे, लाल-भूरे अंडाकार धब्बों से शुरू होता है जिनके किनारे पीले होते हैं, आमतौर पर निचली पत्तियों पर। धब्बे आपस में मिल जाते हैं और पत्तियाँ समय से पहले सूख जाती हैं।',
                'causes': [
                    'बाइपोलैरिस सोरोकिनियाना और अल्टरनेरिया जैसी फफूंद से होता है।',
                    'बालियाँ निकलने के बाद गर्म और नम मौसम में यह बढ़ता है।',
                ],
                'preventions': [
                    'रोग-रोधी किस्में और उपचारित बीज बोएँ।',
                    'संतुलित खाद डालें; कमज़ोर फसल पर इसका असर ज़्यादा होता है।',
                ],
                'remedies': [
                    'धब्बे दिखते ही मैन्कोज़ेब या प्रोपिकोनाज़ोल का छिड़काव करें।',
                    'रोग फैले तो 15 दिन बाद दोबारा छिड़काव करें।',
                ],
            },
            'Septoria': {
                'description': 'सेप्टोरिया पत्ती धब्बा रोग में पत्तियों पर लंबे, हल्के भूरे धब्बे बनते हैं, जिनके अंदर छोटे काले बिंदु (बीजाणु-कोष) होते हैं। यह निचली पत्तियों से शुरू होकर ऊपर बढ़ता है।',
                'causes': [
                    'ज़ाइमोसेप्टोरिया ट्रिटिसी (सेप्टोरिया ट्रिटिसी) फफूंद से होता है।',
                    'यह फसल के ठूँठ पर जीवित रहता है और ठंडे, गीले मौसम में बारिश की छींटों से फैलता है।',
                ],
                'preventions': [
                    'रोग-रोधी किस्में बोएँ।',
                    'कटाई के बाद रोगी ठूँठ को जुताई करके मिट्टी में दबा दें या हटा दें।',
                ],
                'remedies': [
                    'ऊपरी पत्तियों पर धब्बे दिखने पर प्रोपिकोनाज़ोल या मैन्कोज़ेब का छिड़काव करें।',
                    'गीले मौसम में 15 दिन बाद दोबारा छिड़काव करें।',
                ],
            },
            'Tan spot': {
                'description': 'टैन स्पॉट पत्तियों पर पीले घेरे वाले छोटे, हल्के भूरे धब्बों से शुरू होता है, जो बढ़कर बड़े अंडाकार धब्बे बन जाते हैं। ज़्यादा प्रभावित पत्तियाँ जल्दी सूख जाती हैं।',
                'causes': [
                    'पाइरेनोफ़ोरा ट्रिटिसी-रेपेंटिस फफूंद से होता है।',
                    'यह गेहूँ के ठूँठ पर जीवित रहता है, इसलिए जहाँ लगातार गेहूँ बोया जाता है वहाँ ज़्यादा होता है।',
                ],
                'preventions': [
                    'गेहूँ के साथ फसल चक्र अपनाएँ।',
                    'रोगी ठूँठ को मिट्टी में दबाएँ या हटाएँ, और साफ़ बीज बोएँ।',
                ],
                'remedies': [
                    'शुरुआती लक्षण दिखते ही मैन्कोज़ेब, या एज़ोक्सीस्ट्रोबिन और टेबुकोनाज़ोल के मिश्रण का छिड़काव करें।',
                    'ज़रूरत हो तो 15 दिन बाद दोबारा छिड़काव करें।',
                ],
            },
            'Blast': {
                'description': 'गेहूँ ब्लास्ट में बालियाँ सफ़ेद पड़ जाती हैं, अक्सर बाली की डंठल पर एक काले निशान के ऊपर का पूरा हिस्सा एक साथ। दाने सिकुड़ जाते हैं या बनते ही नहीं। यह रोग 1985 में ब्राज़ील में दिखा और 2016 में बांग्लादेश पहुँचा।',
                'causes': [
                    'मैग्नापोर्थे ओराइज़ी (ट्रिटिकम प्रकार) फफूंद से होता है।',
                    'बालियाँ निकलते समय गर्म और गीला मौसम इसे बढ़ाता है; यह बीज से भी फैल सकता है।',
                ],
                'preventions': [
                    'रोग-मुक्त क्षेत्र का साफ़, उपचारित बीज बोएँ।',
                    'अनुशंसित समय पर बुवाई करें और ज़्यादा नाइट्रोजन न डालें।',
                ],
                'remedies': [
                    'बालियाँ निकलते समय टेबुकोनाज़ोल और ट्राइफ्लॉक्सीस्ट्रोबिन (या ट्राइसाइक्लाज़ोल) का छिड़काव करें, और 10–15 दिन बाद दोहराएँ।',
                    'ब्लास्ट का शक हो तो अपने कृषि अधिकारी को बताएँ; दक्षिण एशिया में यह नया रोग है।',
                ],
            },
            'Fusarium Head Blight': {
                'description': 'फ्यूजेरियम बाली झुलसा में बाली का कुछ हिस्सा या पूरी बाली फीकी या सफ़ेद पड़ जाती है, अक्सर गुलाबी-नारंगी फफूंद के साथ। दाने सिकुड़ जाते हैं और उनमें इंसानों और पशुओं के लिए हानिकारक विष हो सकते हैं।',
                'causes': [
                    'फ्यूजेरियम फफूंद से होता है, जो मक्का और गेहूँ के अवशेषों पर जीवित रहती है।',
                    'फूल आने के समय गर्म और गीला मौसम संक्रमण बढ़ाता है।',
                ],
                'preventions': [
                    'मक्का के ठीक बाद गेहूँ बोने से बचें, और फसल अवशेष मिट्टी में दबाएँ।',
                    'रोग-रोधी किस्में और साफ़ बीज बोएँ।',
                ],
                'remedies': [
                    'फूल आने के समय मौसम गर्म और गीला हो तो टेबुकोनाज़ोल का छिड़काव करें।',
                    'प्रभावित अनाज को अलग रखें, और फफूंद लगा अनाज पशुओं को न खिलाएँ।',
                ],
            },
            'Mildew': {
                'description': 'चूर्णिल आसिता में पत्तियों और तनों पर सफ़ेद, पाउडर जैसे धब्बे बनते हैं, जो बाद में छोटे काले बिंदुओं के साथ सलेटी हो जाते हैं। यह ठंडे, नम मौसम में पनपता है और उपज 40% तक घटा सकता है।',
                'causes': [
                    'ब्लूमेरिया ग्रैमिनिस फफूंद से होता है।',
                    'घनी फसल और ज़्यादा नाइट्रोजन खाद इसे बढ़ाते हैं।',
                ],
                'preventions': [
                    'रोग-रोधी किस्में बोएँ।',
                    'ज़्यादा नाइट्रोजन और बहुत घनी बुवाई से बचें।',
                ],
                'remedies': [
                    'धब्बे दिखने पर घुलनशील गंधक या प्रोपिकोनाज़ोल का छिड़काव करें।',
                    'ज़रूरत हो तो 15 दिन बाद दोबारा छिड़काव करें।',
                ],
            },
            'Smut': {
                'description': 'खुला कंडुआ बाली में दानों की जगह काले, पाउडर जैसे बीजाणुओं का ढेर बना देता है; बीजाणु उड़ जाने के बाद सिर्फ़ खाली डंठल बचती है। बालियाँ निकलने तक रोगी पौधे सामान्य दिखते हैं।',
                'causes': [
                    'उस्टिलैगो ट्रिटिसी फफूंद से होता है।',
                    'फफूंद रोगी बीज के अंदर रहती है, इसलिए बीज के ज़रिए एक मौसम से अगले मौसम तक पहुँचती है।',
                ],
                'preventions': [
                    'बुवाई से पहले बीज को कार्बोक्सिन + थायरम, या टेबुकोनाज़ोल से उपचारित करें।',
                    'स्वस्थ फसल का प्रमाणित बीज इस्तेमाल करें।',
                ],
                'remedies': [
                    'बाली में रोग आने के बाद छिड़काव से फ़ायदा नहीं होता।',
                    'रोगी बालियों को पॉलीथीन की थैली से ढककर उखाड़ें, और बीजाणु फैलने से पहले ज़मीन में दबा दें।',
                ],
            },
            'Yellow Rust': {
                'description': 'पीला रतुआ पत्तियों पर नसों के साथ-साथ चमकीली पीली-नारंगी, पाउडर जैसी धारियों के रूप में दिखता है; यह पाउडर उँगलियों पर लग जाता है। यह ठंडे, नम मौसम (लगभग 10–20°C) में तेज़ी से फैलता है और अक्सर खेत में टुकड़ों में शुरू होता है।',
                'causes': [
                    'पक्सीनिया स्ट्राइफ़ॉर्मिस फफूंद से होता है।',
                    'इसके बीजाणु हवा से आते हैं; उत्तर भारत में यह ज़्यादातर दिसंबर से फरवरी तक दिखता है।',
                ],
                'preventions': [
                    'अपने क्षेत्र के लिए अनुशंसित रतुआ-रोधी किस्में बोएँ।',
                    'दिसंबर से खेत की नियमित जाँच करें, ख़ासकर पेड़ों के पास और छाया वाले हिस्सों में।',
                ],
                'remedies': [
                    'धारियाँ दिखते ही प्रोपिकोनाज़ोल, या टेबुकोनाज़ोल और ट्राइफ्लॉक्सीस्ट्रोबिन के मिश्रण का छिड़काव करें।',
                    'ज़रूरत हो तो 15 दिन बाद दोबारा छिड़काव करें।',
                ],
            },
        },
    },
    'pa': {
        'title': 'ਵੀਟਚੈੱਕ - ਕਣਕ ਦੇ ਰੋਗਾਂ ਦੀ ਪਛਾਣ',
        'tagline': 'ਆਪਣੀ ਕਣਕ ਦੀ ਫ਼ੋਟੋ ਖਿੱਚੋ ਅਤੇ ਜਾਣੋ ਕਿ ਉਸਨੂੰ ਕੀ ਰੋਗ ਹੈ ਅਤੇ ਉਸਦਾ ਇਲਾਜ ਕੀ ਹੈ।',
        'intro': [
            {
                'heading': 'ਦੁਨੀਆ ਦੀ ਖੁਰਾਕ ਸੁਰੱਖਿਆ ਦੀ ਰਾਖੀ',
                'paragraphs': [
                    'ਕਣਕ ਦੁਨੀਆ ਭਰ ਦੇ ਅਰਬਾਂ ਲੋਕਾਂ ਦਾ ਢਿੱਡ ਭਰਦੀ ਹੈ, ਪਰ ਕੀੜੇ ਅਤੇ ਰੋਗ ਹਰ ਸਾਲ ਦੁਨੀਆ ਦੀ ਕਣਕ ਦਾ ਅੰਦਾਜ਼ਨ 21.5% ਤਬਾਹ ਕਰ ਦਿੰਦੇ ਹਨ। ਇਹ ਲਗਭਗ 20.9 ਕਰੋੜ ਟਨ ਕਣਕ ਬਣਦੀ ਹੈ, ਜਿਸਦੀ ਕੀਮਤ ਲਗਭਗ 31 ਅਰਬ ਡਾਲਰ ਹੈ।',
                ],
            },
            {
                'heading': 'ਚੁਣੌਤੀ ਨੂੰ ਸਮਝੋ',
                'paragraphs': [
                    'ਕਣਕ ਉੱਤੇ ਉੱਲੀ, ਬੈਕਟੀਰੀਆ, ਵਾਇਰਸ ਅਤੇ ਕੀੜੇ, ਸਾਰੇ ਹਮਲਾ ਕਰ ਸਕਦੇ ਹਨ। ਕੁੰਗੀ, ਚਿੱਟਾ ਰੋਗ ਅਤੇ ਝੁਲਸ ਵਰਗੇ ਰੋਗ, ਅਤੇ ਚੇਪਾ ਤੇ ਤਣੇ ਦੀ ਮੱਖੀ ਵਰਗੇ ਕੀੜੇ, ਸਮੇਂ ਸਿਰ ਪਛਾਣ ਨਾ ਹੋਣ ’ਤੇ ਪੂਰਾ ਖੇਤ ਬਰਬਾਦ ਕਰ ਸਕਦੇ ਹਨ। ਇਸਦਾ ਨੁਕਸਾਨ ਸਭ ਤੋਂ ਪਹਿਲਾਂ ਕਿਸਾਨ ਨੂੰ ਹੁੰਦਾ ਹੈ, ਅਤੇ ਫਿਰ ਅਨਾਜ ਮਹਿੰਗਾ ਹੋਣ ਨਾਲ ਸਾਰਿਆਂ ਨੂੰ।',
                ],
            },
        ],
        'about': [
            {
                'heading': 'ਜਲਦੀ ਪਛਾਣ ਵਿੱਚ ਤਕਨੀਕ ਦੀ ਭੂਮਿਕਾ',
                'paragraphs': [
                    'ਵੀਟਚੈੱਕ ਆਰਟੀਫ਼ੀਸ਼ੀਅਲ ਇੰਟੈਲੀਜੈਂਸ (AI) ਦੀ ਮਦਦ ਨਾਲ ਸਿਰਫ਼ ਇੱਕ ਫ਼ੋਟੋ ਤੋਂ ਕਣਕ ਦੇ ਰੋਗਾਂ ਅਤੇ ਕੀੜਿਆਂ ਦੀ ਪਛਾਣ ਕਰਦਾ ਹੈ। ਸਮੱਸਿਆ ਦਾ ਜਲਦੀ ਪਤਾ ਲੱਗਣ ਨਾਲ ਕਿਸਾਨ ਉਸਦੇ ਫੈਲਣ ਤੋਂ ਪਹਿਲਾਂ ਕਦਮ ਚੁੱਕ ਸਕਦੇ ਹਨ ਅਤੇ ਆਪਣੀ ਫ਼ਸਲ ਤੇ ਕਮਾਈ ਬਚਾ ਸਕਦੇ ਹਨ।',
                ],
                'image': 'assets/farmer.webp',
            },
            {
                'heading': 'ਇਹ ਕਿਵੇਂ ਕੰਮ ਕਰਦਾ ਹੈ',
                'items': [
                    'ਫ਼ੋਟੋ ਖਿੱਚੋ: ਆਪਣੇ ਫ਼ੋਨ ਨਾਲ ਪ੍ਰਭਾਵਿਤ ਪੱਤੇ, ਤਣੇ ਜਾਂ ਸਿੱਟੇ ਦੀ ਫ਼ੋਟੋ ਖਿੱਚੋ।',
                    'ਜਾਂਚ: ਕਣਕ ਦੀਆਂ ਲਗਭਗ 13,000 ਤਸਵੀਰਾਂ ’ਤੇ ਸਿਖਾਇਆ ਗਿਆ ਮਸ਼ੀਨ-ਲਰਨਿੰਗ ਮਾਡਲ ਉਸ ਵਿੱਚ 14 ਰੋਗਾਂ ਅਤੇ ਕੀੜਿਆਂ ਦੀ ਜਾਂਚ ਕਰਦਾ ਹੈ।',
                    'ਪਛਾਣ: ਐਪ ਸਮੱਸਿਆ ਦਾ ਨਾਮ ਦੱਸਦੀ ਹੈ, ਅਤੇ ਇਹ ਵੀ ਕਿ ਉਸਨੂੰ ਕਿੰਨਾ ਯਕੀਨ ਹੈ।',
                    'ਕਾਰਵਾਈ: ਤੁਹਾਨੂੰ ਕਾਰਨ, ਰੋਕਥਾਮ ਅਤੇ ਇਲਾਜ ਮਿਲਦੇ ਹਨ, ਨਾਲ ਹੀ ਖਰੀਦਣ ਲਈ ਦਵਾਈਆਂ ਅਤੇ ਖਾਦਾਂ ਵੀ।',
                ],
                'numbered': True,
            },
            {
                'heading': 'ਅਸਰ',
                'paragraphs': [
                    'ਰੋਗ ਦੀ ਜਲਦੀ ਪਛਾਣ ਨਾਲ ਨੁਕਸਾਨ ਘਟਦਾ ਹੈ, ਬੇਲੋੜੇ ਛਿੜਕਾਅ ਤੋਂ ਬਚਾਅ ਹੁੰਦਾ ਹੈ ਅਤੇ ਕਿਸਾਨ ਦਾ ਮੁਨਾਫ਼ਾ ਵਧਦਾ ਹੈ। ਇਸ ਨਾਲ ਸਾਰਿਆਂ ਲਈ ਅਨਾਜ ਦੀ ਸਪਲਾਈ ਵੀ ਸੁਰੱਖਿਅਤ ਰਹਿੰਦੀ ਹੈ।',
                ],
            },
            {
                'heading': 'ਸਾਡੇ ਨਾਲ ਜੁੜੋ',
                'paragraphs': [
                    'ਵੀਟਚੈੱਕ ਨੂੰ ਹੋਰ ਕਿਸਾਨਾਂ ਨਾਲ ਸਾਂਝਾ ਕਰੋ ਅਤੇ ਦੁਨੀਆ ਦੀਆਂ ਸਭ ਤੋਂ ਜ਼ਰੂਰੀ ਫ਼ਸਲਾਂ ਵਿੱਚੋਂ ਇੱਕ ਨੂੰ ਬਚਾਉਣ ਵਿੱਚ ਮਦਦ ਕਰੋ।',
                ],
            },
        ],
        'steps_heading': 'ਐਪ ਵਰਤਣ ਦੇ ਕਦਮ',
        'steps': [
            'ਪ੍ਰਭਾਵਿਤ ਪੱਤੇ, ਤਣੇ ਜਾਂ ਸਿੱਟੇ ਦੀ ਸਾਫ਼ ਅਤੇ ਨੇੜਿਓਂ ਫ਼ੋਟੋ ਖਿੱਚੋ',
            'ਹੇਠਾਂ ਫ਼ੋਟੋ ਅੱਪਲੋਡ ਕਰੋ',
            'ਸਮੱਸਿਆ ਅਤੇ ਉਸਦਾ ਇਲਾਜ ਦੇਖਣ ਲਈ "ਜਾਂਚ ਕਰੋ" ਦਬਾਓ',
        ],
        'upload_label': 'ਆਪਣੀ ਫ਼ੋਟੋ ਅੱਪਲੋਡ ਕਰੋ',
        'analyze_button': 'ਜਾਂਚ ਕਰੋ',
        'upload_first': 'ਕਿਰਪਾ ਕਰਕੇ ਪਹਿਲਾਂ ਇੱਕ ਫ਼ੋਟੋ ਅੱਪਲੋਡ ਕਰੋ।',
        'image_heading': 'ਤੁਹਾਡੀ ਫ਼ੋਟੋ',
        'no_disease': 'ਕੋਈ ਰੋਗ ਜਾਂ ਕੀੜਾ ਨਹੀਂ ਮਿਲਿਆ। ਤੁਹਾਡੀ ਫ਼ਸਲ ਸਿਹਤਮੰਦ ਲੱਗਦੀ ਹੈ।',
        'healthy_tip': 'ਸੰਤੁਲਿਤ ਖਾਦ ਨਾਲ ਇਸਨੂੰ ਮਜ਼ਬੂਤ ਰੱਖੋ:',
        'low_confidence': 'ਐਪ ਨੂੰ ਇਸ ਫ਼ੋਟੋ ਬਾਰੇ ਯਕੀਨ ਨਹੀਂ ਹੈ। ਕਿਰਪਾ ਕਰਕੇ ਹੇਠਾਂ ਦਿੱਤੇ ਸੁਝਾਵਾਂ ਨਾਲ ਹੋਰ ਫ਼ੋਟੋ ਖਿੱਚੋ।',
        'photo_tips_heading': 'ਵਧੀਆ ਫ਼ੋਟੋ ਲਈ ਸੁਝਾਅ',
        'photo_tips': [
            'ਪ੍ਰਭਾਵਿਤ ਪੱਤਾ ਜਾਂ ਸਿੱਟਾ ਫ਼ੋਟੋ ਵਿੱਚ ਵੱਡਾ ਅਤੇ ਸਾਫ਼ ਦਿਸੇ।',
            'ਦਿਨ ਦੀ ਰੋਸ਼ਨੀ ਵਿੱਚ ਫ਼ੋਟੋ ਖਿੱਚੋ ਅਤੇ ਛਾਂ ਤੋਂ ਬਚੋ।',
            'ਫ਼ੋਨ ਨੂੰ ਟਿਕਾ ਕੇ ਰੱਖੋ ਤਾਂ ਜੋ ਫ਼ੋਟੋ ਧੁੰਦਲੀ ਨਾ ਹੋਵੇ।',
        ],
        'disease_label': 'ਪਛਾਣ',
        'confidence_label': 'ਯਕੀਨ',
        'causes_label': 'ਕਾਰਨ',
        'preventions_label': 'ਰੋਕਥਾਮ',
        'remedies_label': 'ਇਲਾਜ',
        'how_to_button': '▶️ ਵਰਤੋਂ ਕਿਵੇਂ ਕਰੀਏ',
        'samples_button': '🖼️ ਨਮੂਨਾ ਤਸਵੀਰਾਂ',
        'about_button': 'ℹ️ ਜਾਣਕਾਰੀ',
        'samples_intro': 'ਇਹ ਉਹ ਰੋਗ ਅਤੇ ਕੀੜੇ ਹਨ ਜਿਨ੍ਹਾਂ ਦੀ ਵੀਟਚੈੱਕ ਪਛਾਣ ਕਰ ਸਕਦਾ ਹੈ।',
        'animation_captions': [
            'ਬਿਮਾਰ ਪੱਤੇ ਜਾਂ ਸਿੱਟੇ ਦੀ ਸਾਫ਼ ਫ਼ੋਟੋ ਖਿੱਚੋ',
            'ਫ਼ੋਟੋ ਅੱਪਲੋਡ ਕਰੋ',
            '"ਜਾਂਚ ਕਰੋ" ਦਬਾਓ',
            'ਸਮੱਸਿਆ ਦੇਖੋ ਅਤੇ ਦਵਾਈ ਖਰੀਦੋ',
        ],
        'buy_heading': '🛒 ਕਿੱਥੋਂ ਖਰੀਦੀਏ',
        'shop_search_hint': 'BigHaat ਆਪਣੇ ਹੋਮ ਪੇਜ ’ਤੇ ਖੁੱਲ੍ਹਦਾ ਹੈ: ਮੋਟੇ ਅੱਖਰਾਂ ਵਿੱਚ ਲਿਖਿਆ ਨਾਮ ਉਸਦੇ ਸਰਚ ਬਾਰ ਵਿੱਚ ਲਿਖੋ।',
        'buy_note': 'ਮਾਤਰਾ ਅਤੇ ਸੁਰੱਖਿਆ ਲਈ ਹਮੇਸ਼ਾ ਉਤਪਾਦ ਦਾ ਲੇਬਲ ਪੜ੍ਹੋ, ਅਤੇ ਛਿੜਕਾਅ ਤੋਂ ਪਹਿਲਾਂ ਆਪਣੇ ਸਥਾਨਕ ਖੇਤੀਬਾੜੀ ਅਫ਼ਸਰ ਜਾਂ ਕ੍ਰਿਸ਼ੀ ਵਿਗਿਆਨ ਕੇਂਦਰ ਤੋਂ ਸਲਾਹ ਲਓ।',
        'product_types': {
            'fungicide': 'ਉੱਲੀਨਾਸ਼ਕ',
            'insecticide': 'ਕੀਟਨਾਸ਼ਕ',
            'miticide': 'ਜੂੰ-ਨਾਸ਼ਕ',
            'fertilizer': 'ਖਾਦ',
            'bio': 'ਜੈਵਿਕ',
            'seed': 'ਬੀਜ ਸੋਧ',
        },
        'disease_names': {
            'Aphid': 'ਚੇਪਾ',
            'Brown Rust': 'ਭੂਰੀ ਕੁੰਗੀ',
            'Mite': 'ਜੂੰ (ਮਾਈਟ)',
            'Stem fly': 'ਤਣੇ ਦੀ ਮੱਖੀ',
            'Black Rust': 'ਕਾਲੀ ਕੁੰਗੀ',
            'Common Root Rot': 'ਜੜ੍ਹ ਗਲਣ',
            'Leaf Blight': 'ਪੱਤਾ ਝੁਲਸ',
            'Septoria': 'ਸੈਪਟੋਰੀਆ ਪੱਤਾ ਧੱਬਾ',
            'Tan spot': 'ਟੈਨ ਸਪਾਟ',
            'Blast': 'ਕਣਕ ਦਾ ਬਲਾਸਟ',
            'Fusarium Head Blight': 'ਫਿਊਜ਼ੇਰੀਅਮ ਸਿੱਟਾ ਝੁਲਸ',
            'Mildew': 'ਚਿੱਟਾ ਰੋਗ (ਪਾਊਡਰੀ ਮਿਲਡਿਊ)',
            'Smut': 'ਕਾਂਗਿਆਰੀ',
            'Yellow Rust': 'ਪੀਲੀ ਕੁੰਗੀ',
        },
        'diseases': {
            'Aphid': {
                'description': 'ਚੇਪਾ ਛੋਟੇ, ਨਰਮ ਸਰੀਰ ਵਾਲੇ ਹਰੇ ਜਾਂ ਗੂੜ੍ਹੇ ਰੰਗ ਦੇ ਕੀੜੇ ਹਨ, ਜੋ ਪਿੰਨ ਦੇ ਸਿਰੇ ਜਿੰਨੇ ਹੁੰਦੇ ਹਨ। ਇਹ ਪੱਤਿਆਂ ਅਤੇ ਸਿੱਟਿਆਂ ’ਤੇ ਝੁੰਡਾਂ ਵਿੱਚ ਬੈਠ ਕੇ ਪੌਦੇ ਦਾ ਰਸ ਚੂਸਦੇ ਹਨ।',
                'causes': [
                    'ਠੰਢੇ ਅਤੇ ਬੱਦਲਵਾਈ ਵਾਲੇ ਮੌਸਮ ਵਿੱਚ, ਆਮ ਤੌਰ ’ਤੇ ਜਨਵਰੀ ਤੋਂ ਮਾਰਚ ਤੱਕ, ਚੇਪਾ ਤੇਜ਼ੀ ਨਾਲ ਵਧਦਾ ਹੈ।',
                    'ਵੱਧ ਨਾਈਟ੍ਰੋਜਨ ਖਾਦ ਨਾਲ ਪੌਦੇ ਨਰਮ ਹੋ ਜਾਂਦੇ ਹਨ ਅਤੇ ਚੇਪੇ ਨੂੰ ਵੱਧ ਖਿੱਚਦੇ ਹਨ।',
                ],
                'preventions': [
                    'ਸਮੇਂ ਸਿਰ ਬਿਜਾਈ ਕਰੋ; ਪਛੇਤੀ ਬੀਜੀ ਫ਼ਸਲ ’ਤੇ ਹਮਲਾ ਵੱਧ ਹੁੰਦਾ ਹੈ।',
                    'ਸਿਫ਼ਾਰਸ਼ ਤੋਂ ਵੱਧ ਨਾਈਟ੍ਰੋਜਨ ਖਾਦ ਨਾ ਪਾਓ।',
                    'ਲੇਡੀਬਰਡ ਭੂੰਡੀ ਵਰਗੇ ਮਿੱਤਰ ਕੀੜਿਆਂ ਨੂੰ ਬਚਾਓ; ਬਿਨਾਂ ਲੋੜ ਛਿੜਕਾਅ ਨਾ ਕਰੋ।',
                ],
                'remedies': [
                    'ਜਦੋਂ ਹਰ ਸਿੱਟੇ ’ਤੇ ਲਗਭਗ 5 ਚੇਪੇ ਦਿਸਣ, ਤਾਂ ਕੀਟਨਾਸ਼ਕ ਦਾ ਛਿੜਕਾਅ ਕਰੋ।',
                    'ਹਲਕੇ ਹਮਲੇ ਜਾਂ ਜੈਵਿਕ ਖੇਤੀ ਵਿੱਚ ਨਿੰਮ ਦੇ ਤੇਲ ਦਾ ਛਿੜਕਾਅ ਕਰੋ।',
                ],
            },
            'Brown Rust': {
                'description': 'ਭੂਰੀ ਕੁੰਗੀ ਪੱਤਿਆਂ ’ਤੇ ਖਿੱਲਰੇ ਹੋਏ ਛੋਟੇ, ਗੋਲ, ਸੰਤਰੀ-ਭੂਰੇ ਧੂੜੇ ਵਰਗੇ ਧੱਬਿਆਂ ਦੇ ਰੂਪ ਵਿੱਚ ਦਿਸਦੀ ਹੈ। ਇਹ ਹਲਕੇ ਗਰਮ ਅਤੇ ਨਮੀ ਵਾਲੇ ਮੌਸਮ ਵਿੱਚ ਫੈਲਦੀ ਹੈ, ਅਤੇ ਪੱਤਿਆਂ ਦਾ ਹਰਾ ਹਿੱਸਾ, ਝਾੜ ਅਤੇ ਦਾਣੇ ਦਾ ਭਾਰ ਘਟਾਉਂਦੀ ਹੈ।',
                'causes': [
                    'ਪਕਸੀਨੀਆ ਟ੍ਰਿਟੀਸੀਨਾ ਨਾਮ ਦੀ ਉੱਲੀ ਕਾਰਨ ਹੁੰਦੀ ਹੈ।',
                    'ਇਸਦੇ ਬੀਜਾਣੂ ਹਵਾ ਨਾਲ ਰੋਗੀ ਖੇਤਾਂ ਤੋਂ ਉੱਡ ਕੇ ਆਉਂਦੇ ਹਨ।',
                ],
                'preventions': [
                    'ਆਪਣੇ ਇਲਾਕੇ ਲਈ ਸਿਫ਼ਾਰਸ਼ ਕੀਤੀਆਂ ਕੁੰਗੀ-ਰੋਧਕ ਕਿਸਮਾਂ ਬੀਜੋ।',
                    'ਪੂਰੀ ਪੋਟਾਸ਼ ਵਾਲੀ ਸੰਤੁਲਿਤ ਖਾਦ ਪਾਓ; ਵੱਧ ਨਾਈਟ੍ਰੋਜਨ ਨਾਲ ਕੁੰਗੀ ਵਧਦੀ ਹੈ।',
                ],
                'remedies': [
                    'ਧੱਬੇ ਦਿਸਦੇ ਹੀ ਪ੍ਰੋਪੀਕੋਨਾਜ਼ੋਲ ਜਾਂ ਟੈਬੂਕੋਨਾਜ਼ੋਲ ਵਰਗੇ ਉੱਲੀਨਾਸ਼ਕ ਦਾ ਛਿੜਕਾਅ ਕਰੋ।',
                    'ਰੋਗ ਜਾਰੀ ਰਹੇ ਤਾਂ 15 ਦਿਨਾਂ ਬਾਅਦ ਦੁਬਾਰਾ ਛਿੜਕਾਅ ਕਰੋ।',
                ],
            },
            'Mite': {
                'description': 'ਜੂੰ (ਮਾਈਟ) ਅੱਠ ਲੱਤਾਂ ਵਾਲੇ ਬਹੁਤ ਛੋਟੇ ਜੀਵ ਹਨ, ਜੋ ਲਾਲ-ਭੂਰੇ ਤੋਂ ਕਾਲੇ ਰੰਗ ਦੇ ਹੁੰਦੇ ਹਨ ਅਤੇ ਲੈਂਜ਼ ਤੋਂ ਬਿਨਾਂ ਮੁਸ਼ਕਲ ਨਾਲ ਦਿਸਦੇ ਹਨ। ਇਹ ਰਸ ਚੂਸਦੇ ਹਨ, ਜਿਸ ਨਾਲ ਪੱਤਿਆਂ ’ਤੇ ਦਾਗ਼ ਪੈ ਜਾਂਦੇ ਹਨ ਅਤੇ ਉਹ ਪੀਲੇ ਹੋ ਕੇ ਸੁੱਕ ਜਾਂਦੇ ਹਨ, ਖ਼ਾਸ ਕਰਕੇ ਗਰਮ ਅਤੇ ਖੁਸ਼ਕ ਮੌਸਮ ਵਿੱਚ।',
                'causes': [
                    'ਖੁਸ਼ਕ ਮੌਸਮ ਅਤੇ ਪਾਣੀ ਦੀ ਘਾਟ ਜੂੰ ਨੂੰ ਵਧਾਉਂਦੇ ਹਨ।',
                    'ਇਹ ਹਵਾ, ਮਸ਼ੀਨਾਂ ਅਤੇ ਫ਼ਸਲ ਦੀ ਰਹਿੰਦ-ਖੂੰਹਦ ਨਾਲ ਫੈਲਦੀ ਹੈ।',
                ],
                'preventions': [
                    'ਸਮੇਂ ਸਿਰ ਸਿੰਚਾਈ ਕਰੋ; ਚੰਗੀ ਤਰ੍ਹਾਂ ਸਿੰਜੀ ਫ਼ਸਲ ’ਤੇ ਅਸਰ ਘੱਟ ਹੁੰਦਾ ਹੈ।',
                    'ਨਦੀਨ ਅਤੇ ਪਿਛਲੀ ਫ਼ਸਲ ਦੀ ਰਹਿੰਦ-ਖੂੰਹਦ ਹਟਾਓ, ਜਿਨ੍ਹਾਂ ਵਿੱਚ ਜੂੰ ਪਲਦੀ ਹੈ।',
                ],
                'remedies': [
                    'ਨੁਕਸਾਨ ਦਿਸਣ ’ਤੇ ਘੁਲਣਸ਼ੀਲ ਗੰਧਕ (ਸਲਫ਼ਰ) ਜਾਂ ਡਾਈਮੈਥੋਏਟ ਵਰਗੀ ਸਿਫ਼ਾਰਸ਼ ਕੀਤੀ ਦਵਾਈ ਦਾ ਛਿੜਕਾਅ ਕਰੋ।',
                    'ਹਲਕੇ ਹਮਲੇ ਵਿੱਚ ਨਿੰਮ ਦਾ ਤੇਲ ਵੀ ਮਦਦ ਕਰ ਸਕਦਾ ਹੈ।',
                ],
            },
            'Stem fly': {
                'description': 'ਤਣੇ ਦੀ ਮੱਖੀ ਛੋਟੀਆਂ ਮੱਖੀਆਂ ਹਨ ਜਿਨ੍ਹਾਂ ਦੀਆਂ ਸੁੰਡੀਆਂ ਕਣਕ ਦੇ ਤਣੇ ਦੇ ਅੰਦਰ ਸੁਰੰਗਾਂ ਬਣਾਉਂਦੀਆਂ ਹਨ। ਛੋਟੇ ਪੌਦਿਆਂ ਵਿੱਚ ਵਿਚਕਾਰਲੀ ਗੋਭ ਸੁੱਕ ਜਾਂਦੀ ਹੈ ("ਡੈੱਡ ਹਾਰਟ"), ਅਤੇ ਵੱਡੇ ਪੌਦਿਆਂ ਵਿੱਚ ਚਿੱਟੇ, ਖਾਲੀ ਸਿੱਟੇ ਨਿਕਲ ਸਕਦੇ ਹਨ।',
                'causes': [
                    'ਮੱਖੀ ਛੋਟੇ ਪੌਦਿਆਂ ’ਤੇ ਆਂਡੇ ਦਿੰਦੀ ਹੈ; ਉਨ੍ਹਾਂ ਤੋਂ ਨਿਕਲੀਆਂ ਸੁੰਡੀਆਂ ਤਣੇ ਵਿੱਚ ਵੜ ਕੇ ਅੰਦਰੋਂ ਖਾਂਦੀਆਂ ਹਨ।',
                    'ਪੁੰਗਰਨ ਵੇਲੇ ਦੀ ਛੋਟੀ ਫ਼ਸਲ ਨੂੰ ਸਭ ਤੋਂ ਵੱਧ ਖ਼ਤਰਾ ਹੁੰਦਾ ਹੈ।',
                ],
                'preventions': [
                    'ਬਿਜਾਈ ਤੋਂ ਪਹਿਲਾਂ ਬੀਜ ਨੂੰ ਥਾਇਆਮੈਥੋਕਸਮ ਜਾਂ ਇਮੀਡਾਕਲੋਪ੍ਰਿਡ ਵਰਗੇ ਕੀਟਨਾਸ਼ਕ ਨਾਲ ਸੋਧੋ।',
                    'ਸਿਫ਼ਾਰਸ਼ ਕੀਤੇ ਸਮੇਂ ’ਤੇ ਬਿਜਾਈ ਕਰੋ ਅਤੇ ਖੇਤ ਨੂੰ ਘਾਹ ਵਾਲੇ ਨਦੀਨਾਂ ਤੋਂ ਸਾਫ਼ ਰੱਖੋ।',
                ],
                'remedies': [
                    '"ਡੈੱਡ ਹਾਰਟ" ਵਾਲੇ ਪੌਦਿਆਂ ਨੂੰ ਪੁੱਟ ਕੇ ਨਸ਼ਟ ਕਰੋ।',
                    'ਜੇ ਬਹੁਤ ਪੌਦੇ ਪ੍ਰਭਾਵਿਤ ਹੋਣ ਤਾਂ ਆਪਣੇ ਖੇਤੀਬਾੜੀ ਅਫ਼ਸਰ ਤੋਂ ਪੁੱਛੋ ਕਿ ਕਿਹੜਾ ਕੀਟਨਾਸ਼ਕ ਵਰਤਣਾ ਹੈ।',
                ],
            },
            'Black Rust': {
                'description': 'ਕਾਲੀ ਕੁੰਗੀ ਤਣਿਆਂ ਅਤੇ ਪੱਤਿਆਂ ’ਤੇ ਲੰਮੇ, ਗੂੜ੍ਹੇ ਲਾਲ-ਭੂਰੇ ਧੱਬੇ ਬਣਾਉਂਦੀ ਹੈ, ਜੋ ਫ਼ਸਲ ਪੱਕਣ ਵੇਲੇ ਕਾਲੇ ਹੋ ਜਾਂਦੇ ਹਨ। ਵੱਧ ਪ੍ਰਭਾਵਿਤ ਤਣੇ ਕਮਜ਼ੋਰ ਹੋ ਕੇ ਟੁੱਟ ਜਾਂਦੇ ਹਨ ਅਤੇ ਦਾਣੇ ਸੁੰਗੜ ਜਾਂਦੇ ਹਨ।',
                'causes': [
                    'ਪਕਸੀਨੀਆ ਗ੍ਰੈਮੀਨਿਸ ਨਾਮ ਦੀ ਉੱਲੀ ਕਾਰਨ ਹੁੰਦੀ ਹੈ।',
                    'ਇਹ ਗਰਮ ਅਤੇ ਨਮੀ ਵਾਲੇ ਮੌਸਮ ਵਿੱਚ ਵਧਦੀ ਹੈ; ਇਸਦੇ ਬੀਜਾਣੂ ਹਵਾ ਨਾਲ ਬਹੁਤ ਦੂਰ ਤੱਕ ਜਾਂਦੇ ਹਨ।',
                ],
                'preventions': [
                    'ਕੁੰਗੀ-ਰੋਧਕ ਕਿਸਮਾਂ ਬੀਜੋ।',
                    'ਬਹੁਤ ਪਛੇਤੀ ਬਿਜਾਈ ਤੋਂ ਬਚੋ, ਤਾਂ ਜੋ ਦਾਣਾ ਭਰਨ ਵੇਲੇ ਫ਼ਸਲ ਵੱਧ ਗਰਮੀ ਵਿੱਚ ਨਾ ਆਵੇ।',
                ],
                'remedies': [
                    'ਧੱਬੇ ਦਿਸਣ ’ਤੇ ਪ੍ਰੋਪੀਕੋਨਾਜ਼ੋਲ ਜਾਂ ਟੈਬੂਕੋਨਾਜ਼ੋਲ ਵਰਗੇ ਉੱਲੀਨਾਸ਼ਕ ਦਾ ਛਿੜਕਾਅ ਕਰੋ।',
                    'ਲੋੜ ਹੋਵੇ ਤਾਂ 15 ਦਿਨਾਂ ਬਾਅਦ ਦੁਬਾਰਾ ਛਿੜਕਾਅ ਕਰੋ।',
                ],
            },
            'Common Root Rot': {
                'description': 'ਜੜ੍ਹ ਗਲਣ ਦੀ ਉੱਲੀ ਜੜ੍ਹਾਂ ਅਤੇ ਤਣੇ ਦੇ ਹੇਠਲੇ ਹਿੱਸੇ ’ਤੇ ਹਮਲਾ ਕਰਦੀ ਹੈ, ਜੋ ਗੂੜ੍ਹੇ ਭੂਰੇ ਹੋ ਜਾਂਦੇ ਹਨ। ਪੌਦੇ ਕਮਜ਼ੋਰ ਰਹਿੰਦੇ ਹਨ, ਪੀਲੇ ਪੈ ਜਾਂਦੇ ਹਨ ਅਤੇ ਉਨ੍ਹਾਂ ਵਿੱਚ ਚਿੱਟੇ, ਖਾਲੀ ਸਿੱਟੇ ਨਿਕਲ ਸਕਦੇ ਹਨ।',
                'causes': [
                    'ਮੁੱਖ ਤੌਰ ’ਤੇ ਬਾਈਪੋਲੈਰਿਸ ਸੋਰੋਕਿਨੀਆਨਾ ਉੱਲੀ ਕਾਰਨ ਹੁੰਦਾ ਹੈ, ਜੋ ਮਿੱਟੀ, ਫ਼ਸਲ ਦੀ ਰਹਿੰਦ-ਖੂੰਹਦ ਅਤੇ ਬੀਜ ਵਿੱਚ ਰਹਿੰਦੀ ਹੈ।',
                    'ਖੁਸ਼ਕ, ਗਰਮ ਮਿੱਟੀ ਅਤੇ ਕਮਜ਼ੋਰ ਪੌਦਿਆਂ ਵਿੱਚ ਇਹ ਵੱਧ ਫੈਲਦਾ ਹੈ।',
                ],
                'preventions': [
                    'ਕਾਰਬੈਂਡਾਜ਼ਿਮ ਜਾਂ ਟੈਬੂਕੋਨਾਜ਼ੋਲ ਨਾਲ ਸੋਧਿਆ ਤੰਦਰੁਸਤ ਬੀਜ ਬੀਜੋ।',
                    'ਕਣਕ ਤੋਂ ਬਾਅਦ ਦਾਲਾਂ ਜਾਂ ਸਰ੍ਹੋਂ ਵਰਗੀਆਂ ਗ਼ੈਰ-ਅਨਾਜ ਫ਼ਸਲਾਂ ਲਓ।',
                    'ਬਿਜਾਈ ਵੇਲੇ ਸੰਤੁਲਿਤ ਖਾਦ ਪਾਓ।',
                ],
                'remedies': [
                    'ਗਲ ਚੁੱਕੀਆਂ ਜੜ੍ਹਾਂ ਠੀਕ ਨਹੀਂ ਹੋ ਸਕਦੀਆਂ, ਇਸ ਲਈ ਅਗਲੀ ਫ਼ਸਲ ਲਈ ਬੀਜ ਸੋਧ ਅਤੇ ਮਿੱਟੀ ਦੀ ਸਿਹਤ ’ਤੇ ਧਿਆਨ ਦਿਓ।',
                    'ਟ੍ਰਾਈਕੋਡਰਮਾ ਜੈਵਿਕ ਉੱਲੀਨਾਸ਼ਕ ਨੂੰ ਰੂੜੀ ਦੀ ਖਾਦ ਵਿੱਚ ਮਿਲਾ ਕੇ ਮਿੱਟੀ ਵਿੱਚ ਪਾਓ।',
                ],
            },
            'Leaf Blight': {
                'description': 'ਪੱਤਾ ਝੁਲਸ ਛੋਟੇ, ਲਾਲ-ਭੂਰੇ ਅੰਡਾਕਾਰ ਧੱਬਿਆਂ ਨਾਲ ਸ਼ੁਰੂ ਹੁੰਦਾ ਹੈ ਜਿਨ੍ਹਾਂ ਦੇ ਕਿਨਾਰੇ ਪੀਲੇ ਹੁੰਦੇ ਹਨ, ਆਮ ਤੌਰ ’ਤੇ ਹੇਠਲੇ ਪੱਤਿਆਂ ’ਤੇ। ਧੱਬੇ ਆਪਸ ਵਿੱਚ ਮਿਲ ਜਾਂਦੇ ਹਨ ਅਤੇ ਪੱਤੇ ਸਮੇਂ ਤੋਂ ਪਹਿਲਾਂ ਸੁੱਕ ਜਾਂਦੇ ਹਨ।',
                'causes': [
                    'ਬਾਈਪੋਲੈਰਿਸ ਸੋਰੋਕਿਨੀਆਨਾ ਅਤੇ ਆਲਟਰਨੇਰੀਆ ਵਰਗੀਆਂ ਉੱਲੀਆਂ ਕਾਰਨ ਹੁੰਦਾ ਹੈ।',
                    'ਸਿੱਟੇ ਨਿਕਲਣ ਤੋਂ ਬਾਅਦ ਗਰਮ ਅਤੇ ਨਮੀ ਵਾਲੇ ਮੌਸਮ ਵਿੱਚ ਇਹ ਵਧਦਾ ਹੈ।',
                ],
                'preventions': [
                    'ਰੋਗ-ਰੋਧਕ ਕਿਸਮਾਂ ਅਤੇ ਸੋਧਿਆ ਬੀਜ ਬੀਜੋ।',
                    'ਸੰਤੁਲਿਤ ਖਾਦ ਪਾਓ; ਕਮਜ਼ੋਰ ਫ਼ਸਲ ’ਤੇ ਇਸਦਾ ਅਸਰ ਵੱਧ ਹੁੰਦਾ ਹੈ।',
                ],
                'remedies': [
                    'ਧੱਬੇ ਦਿਸਦੇ ਹੀ ਮੈਨਕੋਜ਼ੈਬ ਜਾਂ ਪ੍ਰੋਪੀਕੋਨਾਜ਼ੋਲ ਦਾ ਛਿੜਕਾਅ ਕਰੋ।',
                    'ਰੋਗ ਫੈਲੇ ਤਾਂ 15 ਦਿਨਾਂ ਬਾਅਦ ਦੁਬਾਰਾ ਛਿੜਕਾਅ ਕਰੋ।',
                ],
            },
            'Septoria': {
                'description': 'ਸੈਪਟੋਰੀਆ ਪੱਤਾ ਧੱਬਾ ਰੋਗ ਵਿੱਚ ਪੱਤਿਆਂ ’ਤੇ ਲੰਮੇ, ਹਲਕੇ ਭੂਰੇ ਧੱਬੇ ਬਣਦੇ ਹਨ, ਜਿਨ੍ਹਾਂ ਦੇ ਅੰਦਰ ਛੋਟੇ ਕਾਲੇ ਬਿੰਦੂ (ਬੀਜਾਣੂ-ਥੈਲੀਆਂ) ਹੁੰਦੇ ਹਨ। ਇਹ ਹੇਠਲੇ ਪੱਤਿਆਂ ਤੋਂ ਸ਼ੁਰੂ ਹੋ ਕੇ ਉੱਪਰ ਵੱਲ ਵਧਦਾ ਹੈ।',
                'causes': [
                    'ਜ਼ਾਈਮੋਸੈਪਟੋਰੀਆ ਟ੍ਰਿਟੀਸੀ (ਸੈਪਟੋਰੀਆ ਟ੍ਰਿਟੀਸੀ) ਉੱਲੀ ਕਾਰਨ ਹੁੰਦਾ ਹੈ।',
                    'ਇਹ ਫ਼ਸਲ ਦੇ ਮੁੱਢਾਂ ’ਤੇ ਜਿਊਂਦਾ ਰਹਿੰਦਾ ਹੈ ਅਤੇ ਠੰਢੇ, ਗਿੱਲੇ ਮੌਸਮ ਵਿੱਚ ਮੀਂਹ ਦੇ ਛਿੱਟਿਆਂ ਨਾਲ ਫੈਲਦਾ ਹੈ।',
                ],
                'preventions': [
                    'ਰੋਗ-ਰੋਧਕ ਕਿਸਮਾਂ ਬੀਜੋ।',
                    'ਵਾਢੀ ਤੋਂ ਬਾਅਦ ਰੋਗੀ ਮੁੱਢਾਂ ਨੂੰ ਵਾਹ ਕੇ ਮਿੱਟੀ ਵਿੱਚ ਦੱਬ ਦਿਓ ਜਾਂ ਹਟਾ ਦਿਓ।',
                ],
                'remedies': [
                    'ਉੱਪਰਲੇ ਪੱਤਿਆਂ ’ਤੇ ਧੱਬੇ ਦਿਸਣ ’ਤੇ ਪ੍ਰੋਪੀਕੋਨਾਜ਼ੋਲ ਜਾਂ ਮੈਨਕੋਜ਼ੈਬ ਦਾ ਛਿੜਕਾਅ ਕਰੋ।',
                    'ਗਿੱਲੇ ਮੌਸਮ ਵਿੱਚ 15 ਦਿਨਾਂ ਬਾਅਦ ਦੁਬਾਰਾ ਛਿੜਕਾਅ ਕਰੋ।',
                ],
            },
            'Tan spot': {
                'description': 'ਟੈਨ ਸਪਾਟ ਪੱਤਿਆਂ ’ਤੇ ਪੀਲੇ ਘੇਰੇ ਵਾਲੇ ਛੋਟੇ, ਹਲਕੇ ਭੂਰੇ ਧੱਬਿਆਂ ਨਾਲ ਸ਼ੁਰੂ ਹੁੰਦਾ ਹੈ, ਜੋ ਵਧ ਕੇ ਵੱਡੇ ਅੰਡਾਕਾਰ ਧੱਬੇ ਬਣ ਜਾਂਦੇ ਹਨ। ਵੱਧ ਪ੍ਰਭਾਵਿਤ ਪੱਤੇ ਜਲਦੀ ਸੁੱਕ ਜਾਂਦੇ ਹਨ।',
                'causes': [
                    'ਪਾਇਰੀਨੋਫ਼ੋਰਾ ਟ੍ਰਿਟੀਸੀ-ਰੀਪੈਂਟਿਸ ਉੱਲੀ ਕਾਰਨ ਹੁੰਦਾ ਹੈ।',
                    'ਇਹ ਕਣਕ ਦੇ ਮੁੱਢਾਂ ’ਤੇ ਜਿਊਂਦਾ ਰਹਿੰਦਾ ਹੈ, ਇਸ ਲਈ ਜਿੱਥੇ ਲਗਾਤਾਰ ਕਣਕ ਬੀਜੀ ਜਾਂਦੀ ਹੈ ਉੱਥੇ ਵੱਧ ਹੁੰਦਾ ਹੈ।',
                ],
                'preventions': [
                    'ਕਣਕ ਨਾਲ ਫ਼ਸਲੀ ਚੱਕਰ ਅਪਣਾਓ।',
                    'ਰੋਗੀ ਮੁੱਢਾਂ ਨੂੰ ਮਿੱਟੀ ਵਿੱਚ ਦੱਬੋ ਜਾਂ ਹਟਾਓ, ਅਤੇ ਸਾਫ਼ ਬੀਜ ਬੀਜੋ।',
                ],
                'remedies': [
                    'ਸ਼ੁਰੂਆਤੀ ਲੱਛਣ ਦਿਸਦੇ ਹੀ ਮੈਨਕੋਜ਼ੈਬ, ਜਾਂ ਐਜ਼ੋਕਸੀਸਟ੍ਰੋਬਿਨ ਅਤੇ ਟੈਬੂਕੋਨਾਜ਼ੋਲ ਦੇ ਮਿਸ਼ਰਣ ਦਾ ਛਿੜਕਾਅ ਕਰੋ।',
                    'ਲੋੜ ਹੋਵੇ ਤਾਂ 15 ਦਿਨਾਂ ਬਾਅਦ ਦੁਬਾਰਾ ਛਿੜਕਾਅ ਕਰੋ।',
                ],
            },
            'Blast': {
                'description': 'ਕਣਕ ਦੇ ਬਲਾਸਟ ਵਿੱਚ ਸਿੱਟੇ ਚਿੱਟੇ ਪੈ ਜਾਂਦੇ ਹਨ, ਅਕਸਰ ਸਿੱਟੇ ਦੀ ਡੰਡੀ ’ਤੇ ਇੱਕ ਕਾਲੇ ਨਿਸ਼ਾਨ ਤੋਂ ਉੱਪਰ ਦਾ ਸਾਰਾ ਹਿੱਸਾ ਇੱਕੋ ਵਾਰ। ਦਾਣੇ ਸੁੰਗੜ ਜਾਂਦੇ ਹਨ ਜਾਂ ਬਣਦੇ ਹੀ ਨਹੀਂ। ਇਹ ਰੋਗ 1985 ਵਿੱਚ ਬ੍ਰਾਜ਼ੀਲ ਵਿੱਚ ਦਿਸਿਆ ਅਤੇ 2016 ਵਿੱਚ ਬੰਗਲਾਦੇਸ਼ ਪਹੁੰਚਿਆ।',
                'causes': [
                    'ਮੈਗਨਾਪੋਰਥੇ ਓਰਾਈਜ਼ੀ (ਟ੍ਰਿਟੀਕਮ ਕਿਸਮ) ਉੱਲੀ ਕਾਰਨ ਹੁੰਦਾ ਹੈ।',
                    'ਸਿੱਟੇ ਨਿਕਲਣ ਵੇਲੇ ਗਰਮ ਅਤੇ ਗਿੱਲਾ ਮੌਸਮ ਇਸਨੂੰ ਵਧਾਉਂਦਾ ਹੈ; ਇਹ ਬੀਜ ਰਾਹੀਂ ਵੀ ਫੈਲ ਸਕਦਾ ਹੈ।',
                ],
                'preventions': [
                    'ਰੋਗ-ਮੁਕਤ ਇਲਾਕੇ ਦਾ ਸਾਫ਼, ਸੋਧਿਆ ਬੀਜ ਬੀਜੋ।',
                    'ਸਿਫ਼ਾਰਸ਼ ਕੀਤੇ ਸਮੇਂ ’ਤੇ ਬਿਜਾਈ ਕਰੋ ਅਤੇ ਵੱਧ ਨਾਈਟ੍ਰੋਜਨ ਨਾ ਪਾਓ।',
                ],
                'remedies': [
                    'ਸਿੱਟੇ ਨਿਕਲਣ ਵੇਲੇ ਟੈਬੂਕੋਨਾਜ਼ੋਲ ਅਤੇ ਟ੍ਰਾਈਫਲੌਕਸੀਸਟ੍ਰੋਬਿਨ (ਜਾਂ ਟ੍ਰਾਈਸਾਈਕਲਾਜ਼ੋਲ) ਦਾ ਛਿੜਕਾਅ ਕਰੋ, ਅਤੇ 10–15 ਦਿਨਾਂ ਬਾਅਦ ਦੁਹਰਾਓ।',
                    'ਬਲਾਸਟ ਦਾ ਸ਼ੱਕ ਹੋਵੇ ਤਾਂ ਆਪਣੇ ਖੇਤੀਬਾੜੀ ਅਫ਼ਸਰ ਨੂੰ ਦੱਸੋ; ਦੱਖਣੀ ਏਸ਼ੀਆ ਵਿੱਚ ਇਹ ਨਵਾਂ ਰੋਗ ਹੈ।',
                ],
            },
            'Fusarium Head Blight': {
                'description': 'ਫਿਊਜ਼ੇਰੀਅਮ ਸਿੱਟਾ ਝੁਲਸ ਵਿੱਚ ਸਿੱਟੇ ਦਾ ਕੁਝ ਹਿੱਸਾ ਜਾਂ ਪੂਰਾ ਸਿੱਟਾ ਫਿੱਕਾ ਜਾਂ ਚਿੱਟਾ ਪੈ ਜਾਂਦਾ ਹੈ, ਅਕਸਰ ਗੁਲਾਬੀ-ਸੰਤਰੀ ਉੱਲੀ ਨਾਲ। ਦਾਣੇ ਸੁੰਗੜ ਜਾਂਦੇ ਹਨ ਅਤੇ ਉਨ੍ਹਾਂ ਵਿੱਚ ਇਨਸਾਨਾਂ ਅਤੇ ਪਸ਼ੂਆਂ ਲਈ ਨੁਕਸਾਨਦੇਹ ਜ਼ਹਿਰ ਹੋ ਸਕਦੇ ਹਨ।',
                'causes': [
                    'ਫਿਊਜ਼ੇਰੀਅਮ ਉੱਲੀ ਕਾਰਨ ਹੁੰਦਾ ਹੈ, ਜੋ ਮੱਕੀ ਅਤੇ ਕਣਕ ਦੀ ਰਹਿੰਦ-ਖੂੰਹਦ ’ਤੇ ਜਿਊਂਦੀ ਰਹਿੰਦੀ ਹੈ।',
                    'ਫੁੱਲ ਆਉਣ ਵੇਲੇ ਗਰਮ ਅਤੇ ਗਿੱਲਾ ਮੌਸਮ ਲਾਗ ਨੂੰ ਵਧਾਉਂਦਾ ਹੈ।',
                ],
                'preventions': [
                    'ਮੱਕੀ ਤੋਂ ਤੁਰੰਤ ਬਾਅਦ ਕਣਕ ਬੀਜਣ ਤੋਂ ਬਚੋ, ਅਤੇ ਫ਼ਸਲ ਦੀ ਰਹਿੰਦ-ਖੂੰਹਦ ਮਿੱਟੀ ਵਿੱਚ ਦੱਬੋ।',
                    'ਰੋਗ-ਰੋਧਕ ਕਿਸਮਾਂ ਅਤੇ ਸਾਫ਼ ਬੀਜ ਬੀਜੋ।',
                ],
                'remedies': [
                    'ਫੁੱਲ ਆਉਣ ਵੇਲੇ ਮੌਸਮ ਗਰਮ ਅਤੇ ਗਿੱਲਾ ਹੋਵੇ ਤਾਂ ਟੈਬੂਕੋਨਾਜ਼ੋਲ ਦਾ ਛਿੜਕਾਅ ਕਰੋ।',
                    'ਪ੍ਰਭਾਵਿਤ ਅਨਾਜ ਨੂੰ ਵੱਖਰਾ ਰੱਖੋ, ਅਤੇ ਉੱਲੀ ਲੱਗਿਆ ਅਨਾਜ ਪਸ਼ੂਆਂ ਨੂੰ ਨਾ ਖੁਆਓ।',
                ],
            },
            'Mildew': {
                'description': 'ਚਿੱਟੇ ਰੋਗ ਵਿੱਚ ਪੱਤਿਆਂ ਅਤੇ ਤਣਿਆਂ ’ਤੇ ਚਿੱਟੇ, ਧੂੜੇ ਵਰਗੇ ਧੱਬੇ ਬਣਦੇ ਹਨ, ਜੋ ਬਾਅਦ ਵਿੱਚ ਛੋਟੇ ਕਾਲੇ ਬਿੰਦੂਆਂ ਨਾਲ ਸਲੇਟੀ ਹੋ ਜਾਂਦੇ ਹਨ। ਇਹ ਠੰਢੇ, ਨਮੀ ਵਾਲੇ ਮੌਸਮ ਵਿੱਚ ਵਧਦਾ ਹੈ ਅਤੇ ਝਾੜ 40% ਤੱਕ ਘਟਾ ਸਕਦਾ ਹੈ।',
                'causes': [
                    'ਬਲੂਮੇਰੀਆ ਗ੍ਰੈਮੀਨਿਸ ਉੱਲੀ ਕਾਰਨ ਹੁੰਦਾ ਹੈ।',
                    'ਸੰਘਣੀ ਫ਼ਸਲ ਅਤੇ ਵੱਧ ਨਾਈਟ੍ਰੋਜਨ ਖਾਦ ਇਸਨੂੰ ਵਧਾਉਂਦੇ ਹਨ।',
                ],
                'preventions': [
                    'ਰੋਗ-ਰੋਧਕ ਕਿਸਮਾਂ ਬੀਜੋ।',
                    'ਵੱਧ ਨਾਈਟ੍ਰੋਜਨ ਅਤੇ ਬਹੁਤ ਸੰਘਣੀ ਬਿਜਾਈ ਤੋਂ ਬਚੋ।',
                ],
                'remedies': [
                    'ਧੱਬੇ ਦਿਸਣ ’ਤੇ ਘੁਲਣਸ਼ੀਲ ਗੰਧਕ ਜਾਂ ਪ੍ਰੋਪੀਕੋਨਾਜ਼ੋਲ ਦਾ ਛਿੜਕਾਅ ਕਰੋ।',
                    'ਲੋੜ ਹੋਵੇ ਤਾਂ 15 ਦਿਨਾਂ ਬਾਅਦ ਦੁਬਾਰਾ ਛਿੜਕਾਅ ਕਰੋ।',
                ],
            },
            'Smut': {
                'description': 'ਕਾਂਗਿਆਰੀ ਸਿੱਟੇ ਵਿੱਚ ਦਾਣਿਆਂ ਦੀ ਥਾਂ ਕਾਲੇ, ਧੂੜੇ ਵਰਗੇ ਬੀਜਾਣੂਆਂ ਦਾ ਢੇਰ ਬਣਾ ਦਿੰਦੀ ਹੈ; ਬੀਜਾਣੂ ਉੱਡ ਜਾਣ ਤੋਂ ਬਾਅਦ ਸਿਰਫ਼ ਖਾਲੀ ਡੰਡੀ ਬਚਦੀ ਹੈ। ਸਿੱਟੇ ਨਿਕਲਣ ਤੱਕ ਰੋਗੀ ਪੌਦੇ ਆਮ ਵਰਗੇ ਹੀ ਦਿਸਦੇ ਹਨ।',
                'causes': [
                    'ਅਸਟੀਲੈਗੋ ਟ੍ਰਿਟੀਸੀ ਉੱਲੀ ਕਾਰਨ ਹੁੰਦੀ ਹੈ।',
                    'ਉੱਲੀ ਰੋਗੀ ਬੀਜ ਦੇ ਅੰਦਰ ਰਹਿੰਦੀ ਹੈ, ਇਸ ਲਈ ਬੀਜ ਰਾਹੀਂ ਇੱਕ ਸੀਜ਼ਨ ਤੋਂ ਅਗਲੇ ਸੀਜ਼ਨ ਤੱਕ ਪਹੁੰਚਦੀ ਹੈ।',
                ],
                'preventions': [
                    'ਬਿਜਾਈ ਤੋਂ ਪਹਿਲਾਂ ਬੀਜ ਨੂੰ ਕਾਰਬੋਕਸਿਨ + ਥਾਇਰਮ, ਜਾਂ ਟੈਬੂਕੋਨਾਜ਼ੋਲ ਨਾਲ ਸੋਧੋ।',
                    'ਤੰਦਰੁਸਤ ਫ਼ਸਲ ਦਾ ਤਸਦੀਕਸ਼ੁਦਾ ਬੀਜ ਵਰਤੋ।',
                ],
                'remedies': [
                    'ਸਿੱਟੇ ਵਿੱਚ ਰੋਗ ਆਉਣ ਤੋਂ ਬਾਅਦ ਛਿੜਕਾਅ ਦਾ ਫ਼ਾਇਦਾ ਨਹੀਂ ਹੁੰਦਾ।',
                    'ਰੋਗੀ ਸਿੱਟਿਆਂ ਨੂੰ ਪਲਾਸਟਿਕ ਦੇ ਲਿਫ਼ਾਫ਼ੇ ਨਾਲ ਢੱਕ ਕੇ ਪੁੱਟੋ, ਅਤੇ ਬੀਜਾਣੂ ਫੈਲਣ ਤੋਂ ਪਹਿਲਾਂ ਜ਼ਮੀਨ ਵਿੱਚ ਦੱਬ ਦਿਓ।',
                ],
            },
            'Yellow Rust': {
                'description': 'ਪੀਲੀ ਕੁੰਗੀ ਪੱਤਿਆਂ ’ਤੇ ਨਾੜਾਂ ਦੇ ਨਾਲ-ਨਾਲ ਚਮਕੀਲੀਆਂ ਪੀਲੀਆਂ-ਸੰਤਰੀ, ਧੂੜੇ ਵਰਗੀਆਂ ਧਾਰੀਆਂ ਦੇ ਰੂਪ ਵਿੱਚ ਦਿਸਦੀ ਹੈ; ਇਹ ਧੂੜਾ ਉਂਗਲਾਂ ’ਤੇ ਲੱਗ ਜਾਂਦਾ ਹੈ। ਇਹ ਠੰਢੇ, ਨਮੀ ਵਾਲੇ ਮੌਸਮ (ਲਗਭਗ 10–20°C) ਵਿੱਚ ਤੇਜ਼ੀ ਨਾਲ ਫੈਲਦੀ ਹੈ ਅਤੇ ਅਕਸਰ ਖੇਤ ਵਿੱਚ ਟੁਕੜਿਆਂ ਵਿੱਚ ਸ਼ੁਰੂ ਹੁੰਦੀ ਹੈ।',
                'causes': [
                    'ਪਕਸੀਨੀਆ ਸਟ੍ਰਾਈਫ਼ਾਰਮਿਸ ਉੱਲੀ ਕਾਰਨ ਹੁੰਦੀ ਹੈ।',
                    'ਇਸਦੇ ਬੀਜਾਣੂ ਹਵਾ ਨਾਲ ਆਉਂਦੇ ਹਨ; ਉੱਤਰੀ ਭਾਰਤ ਵਿੱਚ ਇਹ ਜ਼ਿਆਦਾਤਰ ਦਸੰਬਰ ਤੋਂ ਫ਼ਰਵਰੀ ਤੱਕ ਦਿਸਦੀ ਹੈ।',
                ],
                'preventions': [
                    'ਆਪਣੇ ਇਲਾਕੇ ਲਈ ਸਿਫ਼ਾਰਸ਼ ਕੀਤੀਆਂ ਕੁੰਗੀ-ਰੋਧਕ ਕਿਸਮਾਂ ਬੀਜੋ।',
                    'ਦਸੰਬਰ ਤੋਂ ਖੇਤ ਦੀ ਲਗਾਤਾਰ ਜਾਂਚ ਕਰੋ, ਖ਼ਾਸ ਕਰਕੇ ਰੁੱਖਾਂ ਦੇ ਨੇੜੇ ਅਤੇ ਛਾਂ ਵਾਲੇ ਹਿੱਸਿਆਂ ਵਿੱਚ।',
                ],
                'remedies': [
                    'ਧਾਰੀਆਂ ਦਿਸਦੇ ਹੀ ਪ੍ਰੋਪੀਕੋਨਾਜ਼ੋਲ, ਜਾਂ ਟੈਬੂਕੋਨਾਜ਼ੋਲ ਅਤੇ ਟ੍ਰਾਈਫਲੌਕਸੀਸਟ੍ਰੋਬਿਨ ਦੇ ਮਿਸ਼ਰਣ ਦਾ ਛਿੜਕਾਅ ਕਰੋ।',
                    'ਲੋੜ ਹੋਵੇ ਤਾਂ 15 ਦਿਨਾਂ ਬਾਅਦ ਦੁਬਾਰਾ ਛਿੜਕਾਅ ਕਰੋ।',
                ],
            },
        },
    },
}
