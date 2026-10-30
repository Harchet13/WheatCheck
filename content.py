"""All user-facing text for WheatCheck, per language.

Disease entries are keyed by the class names in best.pt. To add a language,
add an entry to LANGUAGES and a matching dict to TEXT with the same keys.
"""

# Radio-button label -> key into TEXT, in display order.
LANGUAGES = {"English": "en", "ਪੰਜਾਬੀ": "pa", "हिंदी": "hi"}

# Model class -> sample image shown in the landing-page gallery.
GALLERY = {
    'Aphid': 'assets/samples/aphid_1.jpeg',
    'Brown Rust': 'assets/samples/brown_rust_3.jpeg',
    'Mite': 'assets/samples/mite_26.jpeg',
    'Stem fly': 'assets/samples/stem_fly_30.jpeg',
    'Black Rust': 'assets/samples/black_rust_1.jpeg',
    'Common Root Rot': 'assets/samples/common_root_rot_55.jpeg',
    'Leaf Blight': 'assets/samples/leaf_blight_38.jpeg',
    'Septoria': 'assets/samples/septoria_5.png',
    'Tan spot': 'assets/samples/tan_spot_24.jpeg',
    'Blast': 'assets/samples/blast_1.jpeg',
    'Fusarium Head Blight': 'assets/samples/fusarium_head_blight_test_0.png',
    'Mildew': 'assets/samples/mildew_82.png',
    'Smut': 'assets/samples/smut_test_0.png',
    'Yellow Rust': 'assets/samples/yellow_rust_256.png',
}

TEXT = {
    'en': {
        'title': 'WheatCheck - Wheat Disease Detection',
        'intro': [
            {
                'heading': 'Safeguarding Global Food Security',
                'paragraphs': [
                    'Wheat is one of the most vital crops for human consumption, feeding billions of people worldwide. However, this essential crop is under constant threat from a wide range of diseases caused by pathogens and pests. Every year, these threats result in significant losses—equivalent to 21.5% of global wheat production. This translates to an astonishing 209 million tonnes of wheat, valued at an estimated $31 billion, lost annually.',
                ],
            },
            {
                'heading': 'Understanding the Challenge',
                'paragraphs': [
                    'The challenge of wheat disease is multifaceted. Wheat crops are susceptible to various pathogens, including fungi, bacteria, viruses, and pests, each capable of devastating entire fields if not detected and managed early. Diseases like rusts, mildew, and blight, alongside pests like aphids and stem flies, can drastically reduce yield quality and quantity. The economic impact is profound, affecting not only farmers but also the global food supply chain, leading to increased prices and food insecurity in vulnerable regions.',
                ],
            },
        ],
        'about': [
            {
                'heading': 'The Role of Technology in Early Detection',
                'paragraphs': [
                    'In response to these challenges, technology offers a powerful solution. The Wheat Detection web app harnesses the power of artificial intelligence and machine learning to identify diseases in wheat crops at an early stage. By analyzing images of wheat fields, the app can accurately detect signs of disease, enabling farmers to take prompt action. Early detection is critical in preventing the spread of disease, protecting crop yields, and ensuring a stable food supply.',
                ],
                'image': 'assets/farmer.webp',
            },
            {
                'heading': 'How It Works',
                'items': [
                    'Image Capture: Farmers capture images of their wheat fields using a smartphone or drone.',
                    'Analysis: The app processes these images using advanced machine learning algorithms trained to recognize specific disease patterns.',
                    'Diagnosis: The app provides an instant diagnosis, identifying the type of disease and offering suggestions for treatment.',
                    'Actionable Insights: Farmers receive recommendations on how to manage the detected disease, including optimal pesticide use and agronomic practices to mitigate the impact.',
                ],
                'numbered': True,
            },
            {
                'heading': 'The Impact',
                'paragraphs': [
                    'By integrating this technology into their farming practices, farmers can significantly reduce the losses caused by wheat diseases. The Wheat Detection app not only helps in preserving crop yields but also contributes to global efforts in achieving food security and reducing hunger. The economic benefits are also substantial, allowing farmers to maximize their profits and ensuring that the wheat market remains stable.',
                ],
            },
            {
                'heading': 'Join the Movement',
                'paragraphs': [
                    'As we move towards a future where technology plays an integral role in agriculture, the Wheat Detection app is at the forefront of this revolution. Join us in protecting one of the world’s most important crops and securing the future of global food security.',
                ],
            },
        ],
        'steps_heading': 'Steps to use the app',
        'steps': [
            'Take a clear image',
            'Upload the image',
            'Analyze the image and the name and confidence level of the disease along with the causes, preventions, and remedies will be displayed in the result panel below',
        ],
        'upload_label': 'Upload your image',
        'analyze_button': 'Analyze',
        'upload_first': 'Please upload an image first.',
        'image_heading': 'Image Visualization',
        'result_heading': 'This wheat crop has been affected by:',
        'no_disease': 'No Disease Detected',
        'low_confidence': "The model isn't confident about this image. Try a clearer, closer photo of the affected part of the plant.",
        'disease_label': 'Disease',
        'confidence_label': 'Confidence level',
        'causes_label': 'Causes',
        'preventions_label': 'Preventions',
        'remedies_label': 'Remedies',
        'disease_names': {
            'Aphid': 'Aphid',
            'Brown Rust': 'Brown Rust',
            'Mite': 'Mite',
            'Stem fly': 'Stem Fly',
            'Black Rust': 'Black Rust',
            'Common Root Rot': 'Common Root Rot',
            'Leaf Blight': 'Leaf Blight',
            'Septoria': 'Septoria',
            'Tan spot': 'Tan Spot',
            'Blast': 'Blast',
            'Fusarium Head Blight': 'Fusarium Head Blight',
            'Mildew': 'Mildew',
            'Smut': 'Smut',
            'Yellow Rust': 'Yellow Rust',
        },
        'diseases': {
            'Aphid': {
                'description': 'Aphids are a group of sap-sucking, soft-bodied insects that are about the size of a pinhead.',
                'causes': [
                    'Aphids infest wheat plants by sucking sap, leading to reduced yield.',
                ],
                'preventions': [
                    'Plant resistant wheat varieties.',
                    'Use insecticidal soaps or neem oil.',
                    'Encourage natural predators like ladybugs.',
                ],
                'remedies': [
                    'Apply insecticides if infestations are severe.',
                    'Use cultural practices like crop rotation to disrupt aphid life cycles.',
                ],
            },
            'Brown Rust': {
                'description': 'Brown rust tends to develops in late summer and results in a significant loss of green leaf area and, hence, yield and specific weight.',
                'causes': ['Caused by the fungus Puccinia triticina.'],
                'preventions': [
                    'Plant resistant wheat varieties.',
                    'Apply fungicides as a preventive measure.',
                ],
                'remedies': [
                    'Use fungicides when the disease is detected early.',
                    'Remove and destroy infected plant debris.',
                ],
            },
            'Mite': {
                'description': 'Mites are tiny, reddish-brown to black, eight-legged arachnids that infest wheat crops, particularly in hot, dry conditions. They spread via wind, machinery, and infected plant material.',
                'causes': [
                    'Mites infest wheat plants, sucking sap and transmitting viruses.',
                ],
                'preventions': [
                    'Use mite-resistant wheat varieties.',
                    'Apply miticides if necessary.',
                    'Proper irrigation can help reduce the risk of infestation.',
                ],
                'remedies': ['Apply appropriate miticides.', 'Maintain proper field hygiene.'],
            },
            'Stem fly': {
                'description': 'The wheat stem sawfly (Cephus cinctus) is a primitive, wasp-like insect from the family Cephidae in the order Hymenoptera (i.e. bees, wasps, and ants). Its larvae are significant pests of spring and winter wheat, leading to reduced quality and yield of the crops.',
                'causes': [
                    'Stem flies lay eggs on wheat plants, and larvae burrow into stems.',
                ],
                'preventions': [
                    'Plant early to avoid peak stem fly activity.',
                    'Use insecticides as a preventive measure.',
                ],
                'remedies': [
                    'Apply insecticides at the larval stage.',
                    'Remove and destroy infested plants.',
                ],
            },
            'Black Rust': {
                'description': 'Black Rust affects the stems and leaves of wheat plants, causing significant yield losses and economic damage. It produces black or dark brown raised pustules containing rust-colored spores. If not controlled, it can quickly spread and devastate entire fields.',
                'causes': ['Caused by the fungus Puccinia graminis.'],
                'preventions': [
                    'Plant resistant wheat varieties.',
                    'Use fungicides preventively.',
                ],
                'remedies': [
                    'Apply fungicides when symptoms appear.',
                    'Destroy infected plant debris.',
                ],
            },
            'Common Root Rot': {
                'description': 'Wheat root rots are caused by various fungi that invade the roots and crown tissue of wheat plants. Infected plants have destroyed crown and root tissues, resulting in halted water and nutrient uptake.',
                'causes': ['Caused by fungi such as Bipolaris sorokiniana.'],
                'preventions': [
                    'Use disease-free seeds.',
                    'Implement crop rotation with non-host crops.',
                ],
                'remedies': ['Apply appropriate fungicides.', 'Improve soil drainage.'],
            },
            'Leaf Blight': {
                'description': 'Reddish brown oval spots appear on young seedlings with bright yellow margins. In severe cases, several spots coalesce to cause drying of leaves.',
                'causes': ['Caused by fungi such as Bipolaris and Alternaria species.'],
                'preventions': ['Plant resistant varieties.', 'Use fungicides preventively.'],
                'remedies': [
                    'Apply fungicides at the onset of symptoms.',
                    'Remove and destroy infected plant residues.',
                ],
            },
            'Septoria': {
                'description': 'Septoria tritici blotch survives on stubble between seasons. In late autumn and early winter, rain or heavy dew triggers the release of wind-borne ascospores from perithecia in the stubble, allowing the disease to spread over large distances.',
                'causes': ['Caused by the fungus Septoria tritici.'],
                'preventions': ['Plant resistant varieties.', 'Use fungicides preventively.'],
                'remedies': [
                    'Apply fungicides when symptoms appear.',
                    'Remove and destroy infected leaves.',
                ],
            },
            'Tan spot': {
                'description': 'Tan spot, also known as yellow leaf spot, is an economically significant disease in wheat grown in the U.S. and Canada. It initially appears as small, brown spots on the leaves of susceptible wheat varieties.',
                'causes': ['Caused by the fungus Pyrenophora tritici-repentis.'],
                'preventions': ['Plant resistant varieties.', 'Use crop rotation and clean seed.'],
                'remedies': [
                    'Apply fungicides at early signs of infection.',
                    'Remove and destroy infected plant debris.',
                ],
            },
            'Blast': {
                'description': 'Wheat blast is a devastating disease that emerged in Brazil in the 1980s and has since spread to nearby and distant countries. Climate change is expected to facilitate its spread, particularly in tropical regions.',
                'causes': ['Caused by the fungus Magnaporthe oryzae.'],
                'preventions': [
                    'Plant resistant varieties.',
                    'Avoid excessive nitrogen fertilization.',
                ],
                'remedies': [
                    'Apply fungicides at the first sign of symptoms.',
                    'Practice crop rotation.',
                ],
            },
            'Fusarium Head Blight': {
                'description': 'Fusarium Head Blight is a severe fungal disease leading to contaminated grain with mycotoxins. It results in reduced yield, poor grain quality, and significant economic losses for wheat producers.',
                'causes': ['Caused by fungi of the Fusarium species.'],
                'preventions': ['Plant resistant varieties.', 'Use crop rotation and clean seed.'],
                'remedies': [
                    'Apply fungicides at the flowering stage.',
                    'Avoid planting in fields with high Fusarium pressure.',
                ],
            },
            'Mildew': {
                'description': 'Powdery mildew in wheat begins as surface patches of white mycelium and can eventually cover the entire leaf, with mature infections showing black spore cases. This wind-borne disease thrives in cool, wet weather and can cause yield losses of up to 40%.',
                'causes': ['Caused by the fungus Blumeria graminis.'],
                'preventions': ['Plant resistant varieties.', 'Apply fungicides preventively.'],
                'remedies': [
                    'Apply fungicides when symptoms appear.',
                    'Ensure good air circulation in the field.',
                ],
            },
            'Smut': {
                'description': 'Loose smut has a wide distribution and can occur anywhere wheat is produced. Mild symptoms may be present prior to heading, including yellowish leaf streaks and stiff, dark green leaves.',
                'causes': ['Caused by fungi like the Ustilago species.'],
                'preventions': [
                    'Use smut-resistant varieties.',
                    'Treat seeds with fungicides before planting.',
                ],
                'remedies': ['Destroy infected plants.', 'Use appropriate fungicides.'],
            },
            'Yellow Rust': {
                'description': 'The characteristic symptom of yellow rust is of parallel rows of yellowish orange coloured pustules on the leaves of adult plants. Epidemics of yellow rust often start as individual plants, usually in the autumn.',
                'causes': ['Caused by the fungus Puccinia striiformis.'],
                'preventions': ['Plant resistant varieties.', 'Apply fungicides preventively.'],
                'remedies': [
                    'Apply fungicides when symptoms appear.',
                    'Remove and destroy infected plant debris.',
                ],
            },
        },
    },
    'hi': {
        'title': 'वीटचेक - गेहूँ रोग का पता लगाये',
        'intro': [
            {
                'heading': 'वैश्विक खाद्य सुरक्षा की रक्षा करना',
                'paragraphs': [
                    'गेहूं मानव उपभोग के लिए सबसे महत्वपूर्ण फसलों में से एक है, जो दुनिया भर में अरबों लोगों का पेट भरता है। हालाँकि, यह आवश्यक फसल रोगजनकों और कीटों के कारण होने वाली विभिन्न प्रकार की बीमारियों से लगातार खतरे में है। हर साल, इन खतरों के परिणामस्वरूप महत्वपूर्ण नुकसान होता है - जो वैश्विक गेहूं उत्पादन के 21.5% के बराबर है। इसका मतलब है कि आश्चर्यजनक रूप से 209 मिलियन टन गेहूं, जिसकी अनुमानित कीमत 31 बिलियन डॉलर है, हर साल नष्ट हो जाता है।',
                ],
            },
            {
                'heading': 'चुनौती को समझना',
                'paragraphs': [
                    'गेहूं की बीमारी की चुनौती बहुआयामी है। गेहूं की फसलें कवक, बैक्टीरिया, वायरस और कीटों सहित विभिन्न रोगजनकों के प्रति संवेदनशील होती हैं। यदि शीघ्र पता नहीं लगाया गया और प्रबंधित नहीं किया गया तो प्रत्येक पूरे क्षेत्र को तबाह करने में सक्षम है। एफिड्स और तना मक्खियों जैसे कीटों के साथ-साथ जंग, फफूंदी और झुलसा जैसी बीमारियाँ उपज की गुणवत्ता और मात्रा को काफी कम कर सकती हैं। आर्थिक प्रभाव गहरा है, न केवल किसानों को बल्कि वैश्विक खाद्य आपूर्ति श्रृंखला को भी प्रभावित कर रहा है। जिससे कमजोर क्षेत्रों में कीमतें बढ़ीं और खाद्य असुरक्षा पैदा हुई।',
                ],
            },
        ],
        'about': [
            {
                'heading': 'प्रारंभिक जांच में प्रौद्योगिकी की भूमिका',
                'paragraphs': [
                    'इन चुनौतियों के जवाब में, प्रौद्योगिकी एक शक्तिशाली समाधान प्रदान करती है। व्हीट डिटेक्शन वेब ऐप प्रारंभिक चरण में गेहूं की फसलों में बीमारियों की पहचान करने के लिए कृत्रिम बुद्धिमत्ता और मशीन लर्निंग की शक्ति का उपयोग करता है। गेहूं के खेतों की छवियों का विश्लेषण करके, ऐप बीमारी के लक्षणों का सटीक पता लगा सकता है, जिससे किसान तुरंत कार्रवाई कर सकेंगे। रोग के प्रसार को रोकने, फसल की पैदावार की रक्षा करने और स्थिर खाद्य आपूर्ति सुनिश्चित करने के लिए शीघ्र पता लगाना महत्वपूर्ण है।',
                ],
                'image': 'assets/farmer.webp',
            },
            {
                'heading': 'यह काम किस प्रकार करता है',
                'items': [
                    'छवि कैप्चर: किसान स्मार्टफोन या ड्रोन का उपयोग करके अपने गेहूं के खेतों की तस्वीरें खींचते हैं।',
                    'विश्लेषण: ऐप विशिष्ट रोग पैटर्न को पहचानने के लिए प्रशिक्षित उन्नत मशीन लर्निंग एल्गोरिदम का उपयोग करके इन छवियों को संसाधित करता है।',
                    'निदान: ऐप तत्काल निदान प्रदान करता है, बीमारी के प्रकार की पहचान करता है और उपचार के लिए सुझाव देता है।',
                    'कार्रवाई योग्य अंतर्दृष्टि: किसानों को प्रभाव को कम करने के लिए इष्टतम कीटनाशकों के उपयोग और कृषि संबंधी प्रथाओं सहित पता चला बीमारी का प्रबंधन करने के बारे में सिफारिशें प्राप्त होती हैं।',
                ],
                'numbered': True,
            },
            {
                'heading': 'प्रभाव',
                'paragraphs': [
                    'इस तकनीक को अपनी कृषि पद्धतियों में एकीकृत करके, किसान गेहूं की बीमारियों से होने वाले नुकसान को काफी कम कर सकते हैं। व्हीट डिटेक्शन ऐप न केवल फसल की पैदावार को संरक्षित करने में मदद करता है बल्कि खाद्य सुरक्षा प्राप्त करने और भूख को कम करने के वैश्विक प्रयासों में भी योगदान देता है। आर्थिक लाभ भी पर्याप्त हैं, जिससे किसानों को अपने मुनाफे को अधिकतम करने की अनुमति मिलती है और यह सुनिश्चित होता है कि गेहूं बाजार स्थिर बना रहे।',
                ],
            },
            {
                'heading': 'आंदोलन में शामिल हों',
                'paragraphs': [
                    'जैसे-जैसे हम ऐसे भविष्य की ओर बढ़ रहे हैं जहां प्रौद्योगिकी कृषि में एक अभिन्न भूमिका निभाएगी, गेहूं डिटेक्शन ऐप इस क्रांति में सबसे आगे है। दुनिया की सबसे महत्वपूर्ण फसलों में से एक की रक्षा करने और वैश्विक खाद्य सुरक्षा के भविष्य को सुरक्षित करने में हमारे साथ जुड़ें।',
                ],
            },
        ],
        'steps_heading': 'ऐप का उपयोग करने के चरण',
        'steps': [
            'साफ़ छवि लें',
            'छवि अपलोड करें',
            'छवि का विश्लेषण करें और बीमारी के नाम और आत्मविश्वास के स्तर के साथ-साथ कारण, रोकथाम और उपचार नीचे परिणाम पैनल में प्रदर्शित किए जाएंगे।',
        ],
        'upload_label': 'अपनी छवि अपलोड करें',
        'analyze_button': 'विश्लेषण करें',
        'upload_first': 'कृपया पहले एक छवि अपलोड करें।',
        'image_heading': 'छवि विज़ुअलाइज़ेशन',
        'result_heading': 'गेहूं की ये फसल हुई प्रभावित:',
        'no_disease': 'कोई बीमारी नहीं पाई गई',
        'low_confidence': 'मॉडल इस छवि को लेकर आश्वस्त नहीं है। पौधे के प्रभावित हिस्से की साफ़ और नज़दीक से ली गई तस्वीर आज़माएँ।',
        'disease_label': 'बीमारी',
        'confidence_label': 'आत्मविश्वास स्तर',
        'causes_label': 'कारण',
        'preventions_label': 'रोकथाम',
        'remedies_label': 'उपाय',
        'disease_names': {
            'Aphid': 'एफिड',
            'Brown Rust': 'भूरा जंग',
            'Mite': 'घुन',
            'Stem fly': 'तना मक्खी',
            'Black Rust': 'काला जंग',
            'Common Root Rot': 'सामान्य जड़ सड़न',
            'Leaf Blight': 'पत्ती का झुलसा रोग',
            'Septoria': 'सेप्टोरिया',
            'Tan spot': 'टैन स्पॉट',
            'Blast': 'ब्लास्ट',
            'Fusarium Head Blight': 'फ्यूजेरियम हेड ब्लाइट',
            'Mildew': 'फफूंदी',
            'Smut': 'मैल',
            'Yellow Rust': 'पीला रतुआ',
        },
        'diseases': {
            'Aphid': {
                'description': 'एफिड्स रस-चूसने वाले, मुलायम शरीर वाले कीड़ों का एक समूह है जो पिनहेड के आकार के होते हैं।',
                'causes': [
                    'एफिड्स रस चूसकर गेहूं के पौधों को प्रभावित करते हैं, जिससे उपज कम हो जाती है।',
                ],
                'preventions': [
                    'गेहूं की प्रतिरोधी किस्में लगाएं.',
                    'कीटनाशक साबुन या नीम के तेल का प्रयोग करें।',
                    'लेडीबग जैसे प्राकृतिक शिकारियों को प्रोत्साहित करें।',
                ],
                'remedies': [
                    'यदि संक्रमण गंभीर हो तो कीटनाशकों का प्रयोग करें।',
                    'एफिड जीवन चक्र को बाधित करने के लिए फसल चक्र जैसी सांस्कृतिक प्रथाओं का उपयोग करें।',
                ],
            },
            'Brown Rust': {
                'description': 'भूरा रतुआ गर्मियों के अंत में विकसित होता है और इसके परिणामस्वरूप हरी पत्ती के क्षेत्र में महत्वपूर्ण नुकसान होता है और इसलिए, उपज और विशिष्ट वजन में कमी आती है।',
                'causes': ['पुकिनिया ट्रिटिसिना कवक के कारण होता है।'],
                'preventions': [
                    'गेहूं की प्रतिरोधी किस्में लगाएं।',
                    'निवारक उपाय के रूप में फफूंदनाशकों का प्रयोग करें।',
                ],
                'remedies': [
                    'रोग का शीघ्र पता चलने पर फफूंदनाशी का प्रयोग करें।',
                    'संक्रमित पौधे के मलबे को हटा दें और नष्ट कर दें।',
                ],
            },
            'Mite': {
                'description': 'घुन छोटे, लाल-भूरे से लेकर काले, आठ पैरों वाले अरचिन्ड होते हैं जो विशेष रूप से गर्म, शुष्क परिस्थितियों में गेहूं की फसलों को संक्रमित करते हैं। वे हवा, मशीनरी और संक्रमित पौधों की सामग्री से फैलते हैं।',
                'causes': [
                    'घुन गेहूं के पौधों को संक्रमित करते हैं, रस चूसते हैं और वायरस फैलाते हैं।',
                ],
                'preventions': [
                    'घुन प्रतिरोधी गेहूं की किस्मों का प्रयोग करें।',
                    'यदि आवश्यक हो तो मिटिसाइड्स का प्रयोग करें।',
                    'उचित सिंचाई से संक्रमण के खतरे को कम करने में मदद मिल सकती है।',
                ],
                'remedies': [
                    'उचित माइटसाइड्स का प्रयोग करें।',
                    'क्षेत्र में उचित स्वच्छता बनाए रखें।',
                ],
            },
            'Stem fly': {
                'description': 'गेहूँ के तने का चूरा (सेफस सिंक्टस) हाइमनोप्टेरा (अर्थात मधुमक्खियाँ, ततैया और चींटियाँ) क्रम में सेफिडे परिवार का एक आदिम, ततैया जैसा कीट है। इसके लार्वा वसंत और सर्दियों के गेहूं के महत्वपूर्ण कीट हैं, जिससे फसलों की गुणवत्ता और उपज कम हो जाती है।',
                'causes': [
                    'तना मक्खियाँ गेहूँ के पौधों पर अंडे देती हैं, और लार्वा तने में दब जाते हैं।',
                ],
                'preventions': [
                    'चरम स्टेम फ्लाई गतिविधि से बचने के लिए जल्दी रोपण करें।',
                    'निवारक उपाय के रूप में कीटनाशकों का प्रयोग करें।',
                ],
                'remedies': [
                    'लार्वा अवस्था में कीटनाशकों का प्रयोग करें।',
                    'संक्रमित पौधों को हटा कर नष्ट कर दें।',
                ],
            },
            'Black Rust': {
                'description': 'काला रतुआ गेहूं के पौधों के तनों और पत्तियों को प्रभावित करता है, जिससे उपज में काफी नुकसान होता है और आर्थिक क्षति होती है। यह काले या गहरे भूरे रंग के उभरे हुए दाने पैदा करता है जिनमें जंग के रंग के बीजाणु होते हैं। अगर नियंत्रित नहीं किया गया तो यह तेजी से फैल सकता है और पूरे खेतों को तबाह कर सकता है।',
                'causes': ['पुकिनिया ग्रेमिनिस कवक के कारण होता है।'],
                'preventions': [
                    'गेहूं की प्रतिरोधी किस्में लगाएं।',
                    'फफूंदनाशकों का प्रयोग सावधानी से करें।',
                ],
                'remedies': [
                    'लक्षण दिखाई देने पर फफूंदनाशक लगाएं।',
                    'संक्रमित पौधे के मलबे को नष्ट कर दें।',
                ],
            },
            'Common Root Rot': {
                'description': 'गेहूं की जड़ सड़न विभिन्न कवक के कारण होती है जो गेहूं के पौधों की जड़ों और मुकुट ऊतक पर आक्रमण करते हैं। संक्रमित पौधों ने मुकुट और जड़ के ऊतकों को नष्ट कर दिया है, जिसके परिणामस्वरूप पानी और पोषक तत्वों का अवशोषण रुक गया है।',
                'causes': ['बाइपोलारिस सोरोकिनियाना जैसे कवक के कारण होता है।'],
                'preventions': [
                    'रोगमुक्त बीजों का प्रयोग करें।',
                    'गैर-मेज़बान फसलों के साथ फसल चक्र लागू करें।',
                ],
                'remedies': [
                    'उचित फफूंदनाशकों का प्रयोग करें।',
                    'मिट्टी की जल निकासी में सुधार करें।',
                ],
            },
            'Leaf Blight': {
                'description': 'युवा पौधों पर चमकीले पीले किनारों के साथ लाल भूरे अंडाकार धब्बे दिखाई देते हैं। गंभीर मामलों में, कई धब्बे मिलकर पत्तियों के सूखने का कारण बनते हैं।',
                'causes': ['बाइपोलारिस और अल्टरनेरिया प्रजाति जैसे कवक के कारण होता है।'],
                'preventions': [
                    'प्रतिरोधी किस्में लगाएं।',
                    'फफूंदनाशकों का प्रयोग सावधानी से करें।',
                ],
                'remedies': [
                    'लक्षणों की शुरुआत में फफूंदनाशी लगाएं।',
                    'संक्रमित पौधे के अवशेषों को हटाएं और नष्ट करें।',
                ],
            },
            'Septoria': {
                'description': 'सेप्टोरिया ट्रिटिसी ब्लॉच मौसमों के बीच ठूंठ पर जीवित रहता है। देर से शरद ऋतु और शुरुआती सर्दियों में, बारिश या भारी ओस के कारण ठूंठ में पेरिथेसिया से हवा-जनित एस्कॉस्पोर निकलते हैं, जिससे बीमारी बड़ी दूरी तक फैल जाती है।',
                'causes': ['सेप्टोरिया ट्रिटिसी कवक के कारण होता है।'],
                'preventions': [
                    'प्रतिरोधी किस्में लगाएं।',
                    'फफूंदनाशकों का प्रयोग सावधानी से करें।',
                ],
                'remedies': [
                    'लक्षण दिखाई देने पर फफूंदनाशक लगाएं।',
                    'संक्रमित पत्तियों को हटाकर नष्ट कर दें।',
                ],
            },
            'Tan spot': {
                'description': 'टैन स्पॉट, जिसे पीली पत्ती वाले धब्बे के रूप में भी जाना जाता है, अमेरिका और कनाडा में उगाए जाने वाले गेहूं में एक आर्थिक रूप से महत्वपूर्ण बीमारी है। यह प्रारंभ में अतिसंवेदनशील गेहूं की किस्मों की पत्तियों पर छोटे, भूरे धब्बों के रूप में दिखाई देता है।',
                'causes': ['पायरेनोफोरा ट्रिटिसी-रेपेंटिस कवक के कारण होता है।'],
                'preventions': [
                    'प्रतिरोधी किस्में लगाएं।',
                    'फसल चक्र और स्वच्छ बीज का प्रयोग करें।',
                ],
                'remedies': [
                    'संक्रमण के शुरुआती लक्षणों पर फफूंदनाशी लगाएं।',
                    'संक्रमित पौधे के मलबे को हटा दें और नष्ट कर दें।',
                ],
            },
            'Blast': {
                'description': 'व्हीट ब्लास्ट एक विनाशकारी बीमारी है जो 1980 के दशक में ब्राज़ील में उभरी और तब से आस-पास और दूर-दराज के देशों में फैल गई है। उम्मीद है कि जलवायु परिवर्तन से इसके प्रसार में आसानी होगी, खासकर उष्णकटिबंधीय क्षेत्रों में।',
                'causes': ['मैग्नापोर्थे ओराइजी कवक के कारण होता है।'],
                'preventions': [
                    'प्रतिरोधी किस्में लगाएं।',
                    'अत्यधिक नाइट्रोजन उर्वरक डालने से बचें।',
                ],
                'remedies': [
                    'लक्षणों के पहले संकेत पर फफूंदनाशी लगाएं।',
                    'फसल चक्र का अभ्यास करें।',
                ],
            },
            'Fusarium Head Blight': {
                'description': 'फ्यूसेरियम हेड ब्लाइट एक गंभीर कवक रोग है जिसके कारण अनाज मायकोटॉक्सिन से दूषित हो जाता है। इसके परिणामस्वरूप उपज में कमी, अनाज की खराब गुणवत्ता और गेहूं उत्पादकों को महत्वपूर्ण आर्थिक नुकसान होता है।',
                'causes': ['फ्यूसेरियम प्रजाति के कवक के कारण होता है।'],
                'preventions': [
                    'प्रतिरोधी किस्में लगाएं।',
                    'फसल चक्र और स्वच्छ बीज का प्रयोग करें।',
                ],
                'remedies': [
                    'फूल आने की अवस्था में फफूंदनाशकों का प्रयोग करें।',
                    'उच्च फ्यूजेरियम दबाव वाले खेतों में रोपण से बचें।',
                ],
            },
            'Mildew': {
                'description': 'गेहूं में ख़स्ता फफूंदी सफेद मायसेलियम की सतह पर धब्बे के रूप में शुरू होती है और अंततः पूरी पत्ती को कवर कर सकती है, जिसमें परिपक्व संक्रमण के साथ काले बीजाणु के मामले दिखाई देते हैं। हवा से फैलने वाली यह बीमारी ठंडे, गीले मौसम में पनपती है और उपज को 40% तक नुकसान पहुंचा सकती है।',
                'causes': ['ब्लूमेरिया ग्रेमिनिस कवक के कारण होता है।'],
                'preventions': [
                    'प्रतिरोधी किस्में लगाएं।',
                    'फफूंदनाशकों का प्रयोग रोकथाम के लिए करें।',
                ],
                'remedies': [
                    'लक्षण दिखाई देने पर फफूंदनाशक लगाएं।',
                    'खेत में अच्छा वायु संचार सुनिश्चित करें।',
                ],
            },
            'Smut': {
                'description': 'ढीली स्मट का व्यापक वितरण होता है और यह कहीं भी हो सकता है जहां गेहूं का उत्पादन होता है। शीर्षासन से पहले हल्के लक्षण मौजूद हो सकते हैं, जिनमें पीली पत्ती की धारियाँ और कड़ी, गहरे हरे रंग की पत्तियाँ शामिल हैं।',
                'causes': ['यूस्टिलैगो प्रजाति जैसे कवक के कारण होता है।'],
                'preventions': [
                    'स्मट-प्रतिरोधी किस्मों का उपयोग करें।',
                    'रोपण से पहले बीजों को फफूंदनाशकों से उपचारित करें।',
                ],
                'remedies': [
                    'संक्रमित पौधों को नष्ट कर दें।',
                    'उचित फफूंदनाशकों का प्रयोग करें।',
                ],
            },
            'Yellow Rust': {
                'description': 'पीले रतुआ का विशिष्ट लक्षण वयस्क पौधों की पत्तियों पर पीले नारंगी रंग की फुंसियों की समानांतर पंक्तियाँ होना है। पीले रतुआ की महामारी अक्सर व्यक्तिगत पौधों के रूप में शुरू होती है, आमतौर पर शरद ऋतु में।',
                'causes': ['पुकिनिया स्ट्राइफोर्मिस कवक के कारण होता है।'],
                'preventions': [
                    'प्रतिरोधी किस्में लगाएं।',
                    'फफूंदनाशकों का प्रयोग रोकथाम के लिए करें।',
                ],
                'remedies': [
                    'लक्षण दिखाई देने पर फफूंदनाशक लगाएं।',
                    'संक्रमित पौधे के मलबे को हटा दें और नष्ट कर दें।',
                ],
            },
        },
    },
    'pa': {
        'title': 'ਵੀਟਚੈੱਕ - ਕਣਕ ਦੀ ਬਿਮਾਰੀ ਦਾ ਪਤਾ ਲਗਾਓ',
        'intro': [
            {
                'heading': 'ਗਲੋਬਲ ਭੋਜਨ ਸੁਰੱਖਿਆ ਦੀ ਸੁਰੱਖਿਆ',
                'paragraphs': [
                    'ਕਣਕ ਮਨੁੱਖੀ ਖਪਤ ਲਈ ਸਭ ਤੋਂ ਮਹੱਤਵਪੂਰਨ ਫਸਲਾਂ ਵਿੱਚੋਂ ਇੱਕ ਹੈ, ਜੋ ਦੁਨੀਆ ਭਰ ਦੇ ਅਰਬਾਂ ਲੋਕਾਂ ਨੂੰ ਭੋਜਨ ਦਿੰਦੀ ਹੈ। ਹਾਲਾਂਕਿ, ਇਹ ਜ਼ਰੂਰੀ ਫਸਲ ਰੋਗਾਣੂਆਂ ਅਤੇ ਕੀੜਿਆਂ ਕਾਰਨ ਹੋਣ ਵਾਲੀਆਂ ਬਿਮਾਰੀਆਂ ਦੀ ਇੱਕ ਵਿਸ਼ਾਲ ਸ਼੍ਰੇਣੀ ਤੋਂ ਲਗਾਤਾਰ ਖਤਰੇ ਵਿੱਚ ਹੈ। ਹਰ ਸਾਲ, ਇਹਨਾਂ ਧਮਕੀਆਂ ਦੇ ਨਤੀਜੇ ਵਜੋਂ ਮਹੱਤਵਪੂਰਨ ਨੁਕਸਾਨ ਹੁੰਦਾ ਹੈ - ਵਿਸ਼ਵਵਿਆਪੀ ਕਣਕ ਉਤਪਾਦਨ ਦੇ 21.5% ਦੇ ਬਰਾਬਰ। ਇਹ ਇੱਕ ਹੈਰਾਨੀਜਨਕ 209 ਮਿਲੀਅਨ ਟਨ ਕਣਕ ਦਾ ਅਨੁਵਾਦ ਕਰਦਾ ਹੈ, ਜਿਸਦੀ ਕੀਮਤ $31 ਬਿਲੀਅਨ ਹੈ, ਸਾਲਾਨਾ ਗੁਆਚ ਜਾਂਦੀ ਹੈ।',
                ],
            },
            {
                'heading': 'ਚੁਣੌਤੀ ਨੂੰ ਸਮਝਣਾ',
                'paragraphs': [
                    'ਕਣਕ ਦੀ ਬਿਮਾਰੀ ਦੀ ਚੁਣੌਤੀ ਬਹੁਪੱਖੀ ਹੈ। ਕਣਕ ਦੀ ਫ਼ਸਲ ਉੱਲੀ, ਬੈਕਟੀਰੀਆ, ਵਾਇਰਸ ਅਤੇ ਕੀੜਿਆਂ ਸਮੇਤ ਵੱਖ-ਵੱਖ ਜਰਾਸੀਮਾਂ ਲਈ ਸੰਵੇਦਨਸ਼ੀਲ ਹੁੰਦੀ ਹੈ, ਹਰ ਇੱਕ ਪੂਰੇ ਖੇਤਰ ਨੂੰ ਤਬਾਹ ਕਰਨ ਦੇ ਸਮਰੱਥ ਹੈ ਜੇਕਰ ਜਲਦੀ ਖੋਜਿਆ ਅਤੇ ਪ੍ਰਬੰਧਿਤ ਨਾ ਕੀਤਾ ਜਾਵੇ। ਕੀੜਿਆਂ ਜਿਵੇਂ ਕਿ ਐਫੀਡਜ਼ ਅਤੇ ਸਟੈਮ ਫਲਾਈਜ਼ ਦੇ ਨਾਲ-ਨਾਲ ਜੰਗਾਲ, ਫ਼ਫ਼ੂੰਦੀ ਅਤੇ ਝੁਲਸ ਵਰਗੀਆਂ ਬਿਮਾਰੀਆਂ, ਉਪਜ ਦੀ ਗੁਣਵੱਤਾ ਅਤੇ ਮਾਤਰਾ ਨੂੰ ਬਹੁਤ ਜ਼ਿਆਦਾ ਘਟਾ ਸਕਦੀਆਂ ਹਨ। ਆਰਥਿਕ ਪ੍ਰਭਾਵ ਡੂੰਘਾ ਹੈ, ਜੋ ਨਾ ਸਿਰਫ਼ ਕਿਸਾਨਾਂ ਨੂੰ ਪ੍ਰਭਾਵਿਤ ਕਰਦਾ ਹੈ, ਸਗੋਂ ਵਿਸ਼ਵ ਖੁਰਾਕ ਸਪਲਾਈ ਲੜੀ ਨੂੰ ਵੀ ਪ੍ਰਭਾਵਿਤ ਕਰਦਾ ਹੈ, ਜਿਸ ਨਾਲ ਕਮਜ਼ੋਰ ਖੇਤਰਾਂ ਵਿੱਚ ਵਧੀਆਂ ਕੀਮਤਾਂ ਅਤੇ ਭੋਜਨ ਦੀ ਅਸੁਰੱਖਿਆ ਹੁੰਦੀ ਹੈ।',
                ],
            },
        ],
        'about': [
            {
                'heading': 'ਸ਼ੁਰੂਆਤੀ ਖੋਜ ਵਿੱਚ ਤਕਨਾਲੋਜੀ ਦੀ ਭੂਮਿਕਾ',
                'paragraphs': [
                    "ਇਹਨਾਂ ਚੁਣੌਤੀਆਂ ਦੇ ਜਵਾਬ ਵਿੱਚ, ਤਕਨਾਲੋਜੀ ਇੱਕ ਸ਼ਕਤੀਸ਼ਾਲੀ ਹੱਲ ਪੇਸ਼ ਕਰਦੀ ਹੈ। Wheat Detection ਵੈੱਬ ਐਪ ਸ਼ੁਰੂਆਤੀ ਪੜਾਅ 'ਤੇ ਕਣਕ ਦੀਆਂ ਫਸਲਾਂ ਵਿੱਚ ਬਿਮਾਰੀਆਂ ਦੀ ਪਛਾਣ ਕਰਨ ਲਈ ਨਕਲੀ ਬੁੱਧੀ ਅਤੇ ਮਸ਼ੀਨ ਸਿਖਲਾਈ ਦੀ ਸ਼ਕਤੀ ਨੂੰ ਵਰਤਦਾ ਹੈ। ਕਣਕ ਦੇ ਖੇਤਾਂ ਦੀਆਂ ਤਸਵੀਰਾਂ ਦਾ ਵਿਸ਼ਲੇਸ਼ਣ ਕਰਕੇ, ਐਪ ਬਿਮਾਰੀ ਦੇ ਲੱਛਣਾਂ ਦਾ ਸਹੀ ਪਤਾ ਲਗਾ ਸਕਦਾ ਹੈ, ਜਿਸ ਨਾਲ ਕਿਸਾਨਾਂ ਨੂੰ ਤੁਰੰਤ ਕਾਰਵਾਈ ਕਰਨ ਦੇ ਯੋਗ ਬਣਾਇਆ ਜਾ ਸਕਦਾ ਹੈ। ਬਿਮਾਰੀ ਦੇ ਫੈਲਣ ਨੂੰ ਰੋਕਣ, ਫਸਲਾਂ ਦੀ ਉਪਜ ਦੀ ਰੱਖਿਆ ਕਰਨ, ਅਤੇ ਇੱਕ ਸਥਿਰ ਭੋਜਨ ਸਪਲਾਈ ਨੂੰ ਯਕੀਨੀ ਬਣਾਉਣ ਲਈ ਸ਼ੁਰੂਆਤੀ ਖੋਜ ਮਹੱਤਵਪੂਰਨ ਹੈ।",
                ],
                'image': 'assets/farmer.webp',
            },
            {
                'heading': 'ਇਹ ਕਿਵੇਂ ਕੰਮ ਕਰਦਾ ਹੈ',
                'items': [
                    'ਚਿੱਤਰ ਕੈਪਚਰ: ਕਿਸਾਨ ਸਮਾਰਟਫੋਨ ਜਾਂ ਡਰੋਨ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਆਪਣੇ ਕਣਕ ਦੇ ਖੇਤਾਂ ਦੀਆਂ ਤਸਵੀਰਾਂ ਕੈਪਚਰ ਕਰਦੇ ਹਨ।',
                    "ਵਿਸ਼ਲੇਸ਼ਣ: ਐਪ ਖਾਸ ਰੋਗਾਂ ਦੇ ਪੈਟਰਨਾਂ ਨੂੰ ਪਛਾਣਨ ਲਈ ਸਿਖਲਾਈ ਪ੍ਰਾਪਤ ਤਕਨੀਕੀ ਮਸ਼ੀਨ ਸਿਖਲਾਈ ਐਲਗੋਰਿਦਮ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਇਹਨਾਂ ਚਿੱਤਰਾਂ 'ਤੇ ਪ੍ਰਕਿਰਿਆ ਕਰਦੀ ਹੈ।",
                    'ਨਿਦਾਨ: ਐਪ ਇੱਕ ਤਤਕਾਲ ਨਿਦਾਨ ਪ੍ਰਦਾਨ ਕਰਦਾ ਹੈ, ਬਿਮਾਰੀ ਦੀ ਕਿਸਮ ਦੀ ਪਛਾਣ ਕਰਦਾ ਹੈ ਅਤੇ ਇਲਾਜ ਲਈ ਸੁਝਾਅ ਪੇਸ਼ ਕਰਦਾ ਹੈ।',
                    'ਕਾਰਵਾਈਯੋਗ ਸੂਝ: ਕਿਸਾਨਾਂ ਨੂੰ ਇਸ ਬਾਰੇ ਸਿਫ਼ਾਰਸ਼ਾਂ ਮਿਲਦੀਆਂ ਹਨ ਕਿ ਖੋਜੀ ਗਈ ਬਿਮਾਰੀ ਦਾ ਪ੍ਰਬੰਧਨ ਕਿਵੇਂ ਕਰਨਾ ਹੈ, ਜਿਸ ਵਿੱਚ ਪ੍ਰਭਾਵ ਨੂੰ ਘਟਾਉਣ ਲਈ ਅਨੁਕੂਲ ਕੀਟਨਾਸ਼ਕਾਂ ਦੀ ਵਰਤੋਂ ਅਤੇ ਖੇਤੀ ਵਿਗਿਆਨਿਕ ਅਭਿਆਸਾਂ ਸ਼ਾਮਲ ਹਨ।',
                ],
                'numbered': True,
            },
            {
                'heading': 'ਪ੍ਰਭਾਵ',
                'paragraphs': [
                    'ਇਸ ਤਕਨੀਕ ਨੂੰ ਆਪਣੇ ਖੇਤੀ ਅਭਿਆਸਾਂ ਵਿੱਚ ਜੋੜ ਕੇ, ਕਿਸਾਨ ਕਣਕ ਦੀਆਂ ਬਿਮਾਰੀਆਂ ਕਾਰਨ ਹੋਣ ਵਾਲੇ ਨੁਕਸਾਨ ਨੂੰ ਕਾਫ਼ੀ ਹੱਦ ਤੱਕ ਘਟਾ ਸਕਦੇ ਹਨ। Wheat Detection ਐਪ ਨਾ ਸਿਰਫ਼ ਫ਼ਸਲਾਂ ਦੀ ਪੈਦਾਵਾਰ ਨੂੰ ਸੁਰੱਖਿਅਤ ਰੱਖਣ ਵਿੱਚ ਮਦਦ ਕਰਦੀ ਹੈ, ਸਗੋਂ ਭੋਜਨ ਸੁਰੱਖਿਆ ਨੂੰ ਪ੍ਰਾਪਤ ਕਰਨ ਅਤੇ ਭੁੱਖਮਰੀ ਨੂੰ ਘਟਾਉਣ ਵਿੱਚ ਵਿਸ਼ਵਵਿਆਪੀ ਯਤਨਾਂ ਵਿੱਚ ਵੀ ਯੋਗਦਾਨ ਪਾਉਂਦੀ ਹੈ। ਆਰਥਿਕ ਲਾਭ ਵੀ ਕਾਫੀ ਹੁੰਦੇ ਹਨ, ਜਿਸ ਨਾਲ ਕਿਸਾਨਾਂ ਨੂੰ ਵੱਧ ਤੋਂ ਵੱਧ ਲਾਭ ਪ੍ਰਾਪਤ ਹੁੰਦਾ ਹੈ ਅਤੇ ਕਣਕ ਦੀ ਮੰਡੀ ਸਥਿਰ ਰਹਿੰਦੀ ਹੈ।',
                ],
            },
            {
                'heading': 'ਅੰਦੋਲਨ ਵਿੱਚ ਸ਼ਾਮਲ ਹੋਵੋ',
                'paragraphs': [
                    'ਜਿਵੇਂ ਕਿ ਅਸੀਂ ਇੱਕ ਅਜਿਹੇ ਭਵਿੱਖ ਵੱਲ ਵਧਦੇ ਹਾਂ ਜਿੱਥੇ ਤਕਨਾਲੋਜੀ ਖੇਤੀਬਾੜੀ ਵਿੱਚ ਇੱਕ ਅਨਿੱਖੜਵਾਂ ਭੂਮਿਕਾ ਨਿਭਾਉਂਦੀ ਹੈ, ਕਣਕ ਖੋਜ ਐਪ ਇਸ ਕ੍ਰਾਂਤੀ ਵਿੱਚ ਸਭ ਤੋਂ ਅੱਗੇ ਹੈ। ਦੁਨੀਆ ਦੀਆਂ ਸਭ ਤੋਂ ਮਹੱਤਵਪੂਰਨ ਫਸਲਾਂ ਵਿੱਚੋਂ ਇੱਕ ਦੀ ਰੱਖਿਆ ਕਰਨ ਅਤੇ ਵਿਸ਼ਵ ਭੋਜਨ ਸੁਰੱਖਿਆ ਦੇ ਭਵਿੱਖ ਨੂੰ ਸੁਰੱਖਿਅਤ ਕਰਨ ਵਿੱਚ ਸਾਡੇ ਨਾਲ ਸ਼ਾਮਲ ਹੋਵੋ।',
                ],
            },
        ],
        'steps_heading': 'ਐਪ ਦੀ ਵਰਤੋਂ ਕਰਨ ਲਈ ਕਦਮ',
        'steps': [
            'ਇੱਕ ਸਪਸ਼ਟ ਚਿੱਤਰ ਲਓ',
            'ਚਿੱਤਰ ਅੱਪਲੋਡ ਕਰੋ',
            'ਚਿੱਤਰ ਦਾ ਵਿਸ਼ਲੇਸ਼ਣ ਕਰੋ ਅਤੇ ਬਿਮਾਰੀ ਦੇ ਨਾਮ ਅਤੇ ਵਿਸ਼ਵਾਸ ਪੱਧਰ ਦੇ ਨਾਲ ਕਾਰਨ, ਰੋਕਥਾਮ ਅਤੇ ਉਪਚਾਰ ਹੇਠਾਂ ਨਤੀਜੇ ਪੈਨਲ ਵਿੱਚ ਪ੍ਰਦਰਸ਼ਿਤ ਕੀਤੇ ਜਾਣਗੇ।',
        ],
        'upload_label': 'ਆਪਣੀ ਤਸਵੀਰ ਅੱਪਲੋਡ ਕਰੋ',
        'analyze_button': 'ਵਿਸ਼ਲੇਸ਼ਣ ਕਰੋ',
        'upload_first': 'ਕਿਰਪਾ ਕਰਕੇ ਪਹਿਲਾਂ ਇੱਕ ਤਸਵੀਰ ਅੱਪਲੋਡ ਕਰੋ।',
        'image_heading': 'ਚਿੱਤਰ ਵਿਜ਼ੂਅਲਾਈਜ਼ੇਸ਼ਨ',
        'result_heading': 'ਕਣਕ ਦੀ ਇਹ ਫਸਲ ਇਨ੍ਹਾਂ ਕਾਰਨਾਂ ਕਰਕੇ ਪ੍ਰਭਾਵਿਤ ਹੋਈ ਹੈ:',
        'no_disease': 'ਕੋਈ ਬਿਮਾਰੀ ਨਹੀਂ ਲੱਭੀ',
        'low_confidence': 'ਮਾਡਲ ਇਸ ਤਸਵੀਰ ਬਾਰੇ ਪੱਕਾ ਨਹੀਂ ਹੈ। ਪੌਦੇ ਦੇ ਪ੍ਰਭਾਵਿਤ ਹਿੱਸੇ ਦੀ ਸਾਫ਼ ਅਤੇ ਨੇੜਿਓਂ ਲਈ ਤਸਵੀਰ ਵਰਤ ਕੇ ਦੇਖੋ।',
        'disease_label': 'ਰੋਗ',
        'confidence_label': 'ਵਿਸ਼ਵਾਸ ਪੱਧਰ',
        'causes_label': 'ਕਾਰਨ',
        'preventions_label': 'ਰੋਕਥਾਮ',
        'remedies_label': 'ਉਪਾਅ',
        'disease_names': {
            'Aphid': 'ਐਫੀਡ',
            'Brown Rust': 'ਭੂਰਾ ਜੰਗਾਲ',
            'Mite': 'ਮਾਈਟ',
            'Stem fly': 'ਸਟੈਮ ਫਲਾਈ',
            'Black Rust': 'ਕਾਲਾ ਜੰਗਾਲ',
            'Common Root Rot': 'ਆਮ ਜੜ੍ਹ ਸੜਨ',
            'Leaf Blight': 'ਪੱਤਾ ਝੁਲਸ',
            'Septoria': 'ਸੇਪਟੋਰੀਆ',
            'Tan spot': 'ਟੈਨ ਸਪਾਟ',
            'Blast': 'ਬਲਾਸਟ',
            'Fusarium Head Blight': 'ਫੁਸਾਰਿਅਮ ਸਿਰ ਝੁਲਸ',
            'Mildew': 'ਫ਼ਫ਼ੂੰਦੀ',
            'Smut': 'ਸ੍ਮਟ',
            'Yellow Rust': 'ਪੀਲੀ ਜੰਗਾਲ',
        },
        'diseases': {
            'Aphid': {
                'description': 'ਐਫੀਡਜ਼ ਰਸ ਚੂਸਣ ਵਾਲੇ, ਨਰਮ ਸਰੀਰ ਵਾਲੇ ਕੀੜਿਆਂ ਦਾ ਇੱਕ ਸਮੂਹ ਹੈ ਜੋ ਕਿ ਪਿੰਨਹੈੱਡ ਦੇ ਆਕਾਰ ਦੇ ਹੁੰਦੇ ਹਨ।',
                'causes': [
                    'ਐਫੀਡਸ ਰਸ ਚੂਸ ਕੇ ਕਣਕ ਦੇ ਪੌਦਿਆਂ ਨੂੰ ਪ੍ਰਭਾਵਿਤ ਕਰਦੇ ਹਨ, ਜਿਸ ਨਾਲ ਝਾੜ ਘੱਟ ਜਾਂਦਾ ਹੈ।',
                ],
                'preventions': [
                    'ਰੋਧਕ ਕਣਕ ਦੀਆਂ ਕਿਸਮਾਂ ਬੀਜੋ।',
                    'ਕੀਟਨਾਸ਼ਕ ਸਾਬਣ ਜਾਂ ਨਿੰਮ ਦੇ ਤੇਲ ਦੀ ਵਰਤੋਂ ਕਰੋ।',
                    'ਲੇਡੀਬੱਗ ਵਰਗੇ ਕੁਦਰਤੀ ਸ਼ਿਕਾਰੀਆਂ ਨੂੰ ਉਤਸ਼ਾਹਿਤ ਕਰੋ।',
                ],
                'remedies': [
                    'ਕੀਟਨਾਸ਼ਕਾਂ ਨੂੰ ਲਾਗੂ ਕਰੋ ਜੇਕਰ ਸੰਕਰਮਣ ਗੰਭੀਰ ਹੋਵੇ।',
                    'ਐਫਿਡ ਜੀਵਨ ਚੱਕਰ ਨੂੰ ਵਿਗਾੜਨ ਲਈ ਫਸਲੀ ਚੱਕਰ ਵਰਗੀਆਂ ਸੱਭਿਆਚਾਰਕ ਅਭਿਆਸਾਂ ਦੀ ਵਰਤੋਂ ਕਰੋ।',
                ],
            },
            'Brown Rust': {
                'description': 'ਭੂਰੀ ਜੰਗਾਲ ਗਰਮੀਆਂ ਦੇ ਅਖੀਰ ਵਿੱਚ ਵਿਕਸਤ ਹੁੰਦਾ ਹੈ ਅਤੇ ਨਤੀਜੇ ਵਜੋਂ ਹਰੇ ਪੱਤਿਆਂ ਦੇ ਖੇਤਰ ਵਿੱਚ ਮਹੱਤਵਪੂਰਨ ਨੁਕਸਾਨ ਹੁੰਦਾ ਹੈ ਅਤੇ, ਇਸਲਈ, ਝਾੜ ਅਤੇ ਖਾਸ ਭਾਰ।',
                'causes': ['Puccinia triticina ਉੱਲੀ ਦੇ ਕਾਰਨ।'],
                'preventions': [
                    'ਰੋਧਕ ਕਣਕ ਦੀਆਂ ਕਿਸਮਾਂ ਬੀਜੋ।',
                    'ਰੋਕਥਾਮ ਉਪਾਅ ਵਜੋਂ ਉੱਲੀਨਾਸ਼ਕਾਂ ਨੂੰ ਲਾਗੂ ਕਰੋ।',
                ],
                'remedies': [
                    "ਬਿਮਾਰੀ ਦਾ ਛੇਤੀ ਪਤਾ ਲੱਗਣ 'ਤੇ ਉੱਲੀਨਾਸ਼ਕਾਂ ਦੀ ਵਰਤੋਂ ਕਰੋ।",
                    'ਲਾਗ ਵਾਲੇ ਪੌਦਿਆਂ ਦੇ ਮਲਬੇ ਨੂੰ ਹਟਾਓ ਅਤੇ ਨਸ਼ਟ ਕਰੋ।',
                ],
            },
            'Mite': {
                'description': 'ਦੇਕਣ ਛੋਟੇ, ਲਾਲ-ਭੂਰੇ ਤੋਂ ਕਾਲੇ, ਅੱਠ ਪੈਰਾਂ ਵਾਲੇ ਅਰਚਨਿਡ ਹੁੰਦੇ ਹਨ ਜੋ ਕਣਕ ਦੀਆਂ ਫਸਲਾਂ ਨੂੰ ਪ੍ਰਭਾਵਿਤ ਕਰਦੇ ਹਨ, ਖਾਸ ਕਰਕੇ ਗਰਮ, ਸੁੱਕੀਆਂ ਸਥਿਤੀਆਂ ਵਿੱਚ। ਇਹ ਹਵਾ, ਮਸ਼ੀਨਰੀ ਅਤੇ ਸੰਕਰਮਿਤ ਪੌਦਿਆਂ ਦੀ ਸਮੱਗਰੀ ਰਾਹੀਂ ਫੈਲਦੇ ਹਨ।',
                'causes': [
                    'ਕੀੜੇ ਕਣਕ ਦੇ ਪੌਦਿਆਂ ਨੂੰ ਸੰਕਰਮਿਤ ਕਰਦੇ ਹਨ, ਰਸ ਚੂਸਦੇ ਹਨ ਅਤੇ ਵਾਇਰਸ ਫੈਲਾਉਂਦੇ ਹਨ।',
                ],
                'preventions': [
                    'ਕੀਟ-ਰੋਧਕ ਕਣਕ ਦੀਆਂ ਕਿਸਮਾਂ ਦੀ ਵਰਤੋਂ ਕਰੋ।',
                    'ਜੇਕਰ ਲੋੜ ਹੋਵੇ ਤਾਂ ਮਾਈਟੀਸਾਈਡਸ ਲਾਗੂ ਕਰੋ।',
                    'ਸਹੀ ਸਿੰਚਾਈ ਸੰਕਰਮਣ ਦੇ ਜੋਖਮ ਨੂੰ ਘਟਾਉਣ ਵਿੱਚ ਮਦਦ ਕਰ ਸਕਦੀ ਹੈ।',
                ],
                'remedies': ['ਉਚਿਤ ਮਾਈਟੀਸਾਈਡਸ ਲਾਗੂ ਕਰੋ।', 'ਖੇਤ ਦੀ ਸਹੀ ਸਫਾਈ ਬਣਾਈ ਰੱਖੋ।'],
            },
            'Stem fly': {
                'description': 'ਕਣਕ ਦੇ ਤਣੇ ਦੀ ਆਰਾ (Cephus cinctus) Hymenoptera (ਜਿਵੇਂ ਕਿ ਮਧੂ-ਮੱਖੀਆਂ, ਭਾਂਡੇ ਅਤੇ ਕੀੜੀਆਂ) ਦੇ ਕ੍ਰਮ ਵਿੱਚ ਸੇਫੀਡੇ ਪਰਿਵਾਰ ਵਿੱਚੋਂ ਇੱਕ ਆਦਿਮ, ਭਾਂਡੇ-ਵਰਗੇ ਕੀੜੇ ਹਨ। ਇਸ ਦੇ ਲਾਰਵੇ ਬਸੰਤ ਅਤੇ ਸਰਦੀਆਂ ਦੀ ਕਣਕ ਦੇ ਮਹੱਤਵਪੂਰਨ ਕੀੜੇ ਹਨ, ਜਿਸ ਨਾਲ ਫਸਲਾਂ ਦੀ ਗੁਣਵੱਤਾ ਅਤੇ ਝਾੜ ਘਟਦਾ ਹੈ।',
                'causes': [
                    "ਡੰਡੀ ਦੀਆਂ ਮੱਖੀਆਂ ਕਣਕ ਦੇ ਪੌਦਿਆਂ 'ਤੇ ਅੰਡੇ ਦਿੰਦੀਆਂ ਹਨ, ਅਤੇ ਲਾਰਵੇ ਤਣੀਆਂ ਵਿੱਚ ਛਾ ਜਾਂਦੇ ਹਨ।",
                ],
                'preventions': [
                    'ਪੀਕ ਸਟੈਮ ਫਲਾਈ ਗਤੀਵਿਧੀ ਤੋਂ ਬਚਣ ਲਈ ਜਲਦੀ ਬੀਜੋ।',
                    'ਰੋਕਥਾਮ ਉਪਾਅ ਵਜੋਂ ਕੀਟਨਾਸ਼ਕਾਂ ਦੀ ਵਰਤੋਂ ਕਰੋ।',
                ],
                'remedies': [
                    "ਲਾਰਵੇ ਪੜਾਅ 'ਤੇ ਕੀਟਨਾਸ਼ਕਾਂ ਨੂੰ ਲਾਗੂ ਕਰੋ।",
                    'ਸੰਕਰਮਿਤ ਪੌਦਿਆਂ ਨੂੰ ਹਟਾਓ ਅਤੇ ਨਸ਼ਟ ਕਰੋ।',
                ],
            },
            'Black Rust': {
                'description': 'ਕਾਲੀ ਕੁੰਗੀ ਕਣਕ ਦੇ ਪੌਦਿਆਂ ਦੇ ਤਣੇ ਅਤੇ ਪੱਤਿਆਂ ਨੂੰ ਪ੍ਰਭਾਵਿਤ ਕਰਦੀ ਹੈ, ਜਿਸ ਨਾਲ ਉਪਜ ਦਾ ਮਹੱਤਵਪੂਰਨ ਨੁਕਸਾਨ ਅਤੇ ਆਰਥਿਕ ਨੁਕਸਾਨ ਹੁੰਦਾ ਹੈ। ਇਹ ਕਾਲੇ ਜਾਂ ਗੂੜ੍ਹੇ ਭੂਰੇ ਰੰਗ ਦੇ ਉੱਚੇ ਹੋਏ ਛਾਲੇ ਪੈਦਾ ਕਰਦਾ ਹੈ ਜਿਸ ਵਿੱਚ ਜੰਗਾਲ-ਰੰਗ ਦੇ ਬੀਜਾਣੂ ਹੁੰਦੇ ਹਨ। ਜੇਕਰ ਕੰਟਰੋਲ ਨਾ ਕੀਤਾ ਜਾਵੇ, ਤਾਂ ਇਹ ਤੇਜ਼ੀ ਨਾਲ ਫੈਲ ਸਕਦਾ ਹੈ ਅਤੇ ਪੂਰੇ ਖੇਤਾਂ ਨੂੰ ਤਬਾਹ ਕਰ ਸਕਦਾ ਹੈ।',
                'causes': ['Puccinia graminis ਉੱਲੀ ਕਾਰਨ ਹੁੰਦਾ ਹੈ।'],
                'preventions': [
                    'ਰੋਧਕ ਕਣਕ ਦੀਆਂ ਕਿਸਮਾਂ ਬੀਜੋ।',
                    'ਰੋਕਥਾਮ ਲਈ ਉੱਲੀਨਾਸ਼ਕਾਂ ਦੀ ਵਰਤੋਂ ਕਰੋ।',
                ],
                'remedies': [
                    "ਲੱਛਣ ਦਿਖਾਈ ਦੇਣ 'ਤੇ ਉੱਲੀਨਾਸ਼ਕਾਂ ਨੂੰ ਲਾਗੂ ਕਰੋ।",
                    'ਲਾਗ ਵਾਲੇ ਪੌਦਿਆਂ ਦੇ ਮਲਬੇ ਨੂੰ ਨਸ਼ਟ ਕਰੋ।',
                ],
            },
            'Common Root Rot': {
                'description': "ਕਣਕ ਦੀਆਂ ਜੜ੍ਹਾਂ ਦੀਆਂ ਸੜਨ ਵੱਖ-ਵੱਖ ਉੱਲੀ ਦੇ ਕਾਰਨ ਹੁੰਦੀਆਂ ਹਨ ਜੋ ਕਣਕ ਦੇ ਪੌਦਿਆਂ ਦੀਆਂ ਜੜ੍ਹਾਂ ਅਤੇ ਤਾਜ ਦੇ ਟਿਸ਼ੂ 'ਤੇ ਹਮਲਾ ਕਰਦੀਆਂ ਹਨ। ਸੰਕਰਮਿਤ ਪੌਦਿਆਂ ਨੇ ਤਾਜ ਅਤੇ ਜੜ੍ਹਾਂ ਦੇ ਟਿਸ਼ੂਆਂ ਨੂੰ ਨਸ਼ਟ ਕਰ ਦਿੱਤਾ ਹੈ, ਜਿਸਦੇ ਨਤੀਜੇ ਵਜੋਂ ਪਾਣੀ ਅਤੇ ਪੌਸ਼ਟਿਕ ਤੱਤਾਂ ਦੀ ਖਪਤ ਰੁਕ ਜਾਂਦੀ ਹੈ।",
                'causes': ['ਬਾਇਪੋਲਾਰਿਸ ਸੋਰੋਕਿਨਿਆਨਾ ਵਰਗੀ ਉੱਲੀ ਦੇ ਕਾਰਨ।'],
                'preventions': [
                    'ਰੋਗ ਮੁਕਤ ਬੀਜਾਂ ਦੀ ਵਰਤੋਂ ਕਰੋ।',
                    'ਗੈਰ-ਹੋਸਟ ਫਸਲਾਂ ਦੇ ਨਾਲ ਫਸਲੀ ਰੋਟੇਸ਼ਨ ਲਾਗੂ ਕਰੋ।',
                ],
                'remedies': [
                    'ਢੁਕਵੀਆਂ ਉੱਲੀਨਾਸ਼ਕਾਂ ਨੂੰ ਲਾਗੂ ਕਰੋ।',
                    'ਮਿੱਟੀ ਦੀ ਨਿਕਾਸੀ ਵਿੱਚ ਸੁਧਾਰ ਕਰੋ।',
                ],
            },
            'Leaf Blight': {
                'description': "ਚਮਕਦਾਰ ਪੀਲੇ ਹਾਸ਼ੀਏ ਵਾਲੇ ਛੋਟੇ ਬੂਟਿਆਂ 'ਤੇ ਲਾਲ ਭੂਰੇ ਅੰਡਾਕਾਰ ਧੱਬੇ ਦਿਖਾਈ ਦਿੰਦੇ ਹਨ। ਗੰਭੀਰ ਮਾਮਲਿਆਂ ਵਿੱਚ, ਕਈ ਚਟਾਕ ਪੱਤੇ ਦੇ ਸੁੱਕਣ ਦਾ ਕਾਰਨ ਬਣਦੇ ਹਨ।",
                'causes': [
                    'ਬਾਇਪੋਲਾਰਿਸ ਅਤੇ ਅਲਟਰਨੇਰੀਆ ਸਪੀਸੀਜ਼ ਵਰਗੀਆਂ ਉੱਲੀ ਦੇ ਕਾਰਨ ਹੁੰਦਾ ਹੈ।',
                ],
                'preventions': ['ਰੋਧਕ ਕਿਸਮਾਂ ਬੀਜੋ।', 'ਰੋਕਥਾਮ ਲਈ ਉੱਲੀਨਾਸ਼ਕਾਂ ਦੀ ਵਰਤੋਂ ਕਰੋ।'],
                'remedies': [
                    "ਲੱਛਣਾਂ ਦੀ ਸ਼ੁਰੂਆਤ 'ਤੇ ਉੱਲੀਨਾਸ਼ਕਾਂ ਨੂੰ ਲਾਗੂ ਕਰੋ।",
                    'ਲਾਗ ਵਾਲੇ ਪੌਦਿਆਂ ਦੀ ਰਹਿੰਦ-ਖੂੰਹਦ ਨੂੰ ਹਟਾਓ ਅਤੇ ਨਸ਼ਟ ਕਰੋ।',
                ],
            },
            'Septoria': {
                'description': "ਸੇਪਟੋਰੀਆ ਟ੍ਰਾਈਟੀਸੀ ਬਲੋਚ ਮੌਸਮਾਂ ਦੇ ਵਿਚਕਾਰ ਪਰਾਲੀ 'ਤੇ ਜਿਉਂਦਾ ਰਹਿੰਦਾ ਹੈ। ਪਤਝੜ ਦੇ ਅਖੀਰ ਅਤੇ ਸਰਦੀਆਂ ਦੇ ਸ਼ੁਰੂ ਵਿੱਚ, ਮੀਂਹ ਜਾਂ ਭਾਰੀ ਤ੍ਰੇਲ ਪਰਾਲੀ ਵਿੱਚ ਪੈਰੀਥੀਸੀਆ ਤੋਂ ਹਵਾ ਦੁਆਰਾ ਪੈਦਾ ਹੋਣ ਵਾਲੇ ਐਸਕੋਸਪੋਰਸ ਨੂੰ ਛੱਡਣ ਦਾ ਕਾਰਨ ਬਣਦੀ ਹੈ, ਜਿਸ ਨਾਲ ਬਿਮਾਰੀ ਵੱਡੀ ਦੂਰੀ ਤੱਕ ਫੈਲ ਜਾਂਦੀ ਹੈ।",
                'causes': ['ਸੇਪਟੋਰੀਆ ਟ੍ਰਾਈਟੀਸੀ ਉੱਲੀ ਦੇ ਕਾਰਨ।'],
                'preventions': ['ਰੋਧਕ ਕਿਸਮਾਂ ਬੀਜੋ।', 'ਰੋਕਥਾਮ ਲਈ ਉੱਲੀਨਾਸ਼ਕਾਂ ਦੀ ਵਰਤੋਂ ਕਰੋ।'],
                'remedies': [
                    "ਲੱਛਣ ਦਿਖਾਈ ਦੇਣ 'ਤੇ ਉੱਲੀਨਾਸ਼ਕਾਂ ਨੂੰ ਲਾਗੂ ਕਰੋ।",
                    'ਸੰਕਰਮਿਤ ਪੱਤਿਆਂ ਨੂੰ ਹਟਾਓ ਅਤੇ ਨਸ਼ਟ ਕਰੋ।',
                ],
            },
            'Tan spot': {
                'description': "ਟੈਨ ਸਪਾਟ, ਜਿਸ ਨੂੰ ਪੀਲੇ ਪੱਤੇ ਦੇ ਸਥਾਨ ਵਜੋਂ ਵੀ ਜਾਣਿਆ ਜਾਂਦਾ ਹੈ, ਅਮਰੀਕਾ ਅਤੇ ਕੈਨੇਡਾ ਵਿੱਚ ਉਗਾਈ ਜਾਣ ਵਾਲੀ ਕਣਕ ਵਿੱਚ ਆਰਥਿਕ ਤੌਰ 'ਤੇ ਮਹੱਤਵਪੂਰਨ ਬਿਮਾਰੀ ਹੈ। ਇਹ ਸ਼ੁਰੂਆਤੀ ਤੌਰ 'ਤੇ ਸੰਵੇਦਨਸ਼ੀਲ ਕਣਕ ਦੀਆਂ ਕਿਸਮਾਂ ਦੇ ਪੱਤਿਆਂ 'ਤੇ ਛੋਟੇ, ਭੂਰੇ ਧੱਬਿਆਂ ਦੇ ਰੂਪ ਵਿੱਚ ਦਿਖਾਈ ਦਿੰਦਾ ਹੈ।",
                'causes': ['ਪਾਈਰੇਨੋਫੋਰਾ ਟ੍ਰਾਈਟੀਸੀ-ਰੇਪੇਂਟਿਸ ਉੱਲੀ ਕਾਰਨ ਹੁੰਦਾ ਹੈ।'],
                'preventions': ['ਰੋਧਕ ਕਿਸਮਾਂ ਬੀਜੋ।', 'ਫਸਲ ਰੋਟੇਸ਼ਨ ਅਤੇ ਸਾਫ਼ ਬੀਜ ਦੀ ਵਰਤੋਂ ਕਰੋ।'],
                'remedies': [
                    "ਲਾਗ ਦੇ ਸ਼ੁਰੂਆਤੀ ਸੰਕੇਤਾਂ 'ਤੇ ਉੱਲੀਨਾਸ਼ਕਾਂ ਨੂੰ ਲਾਗੂ ਕਰੋ।",
                    'ਲਾਗ ਵਾਲੇ ਪੌਦਿਆਂ ਦੇ ਮਲਬੇ ਨੂੰ ਹਟਾਓ ਅਤੇ ਨਸ਼ਟ ਕਰੋ।',
                ],
            },
            'Blast': {
                'description': 'ਕਣਕ ਦਾ ਧਮਾਕਾ ਇੱਕ ਵਿਨਾਸ਼ਕਾਰੀ ਬਿਮਾਰੀ ਹੈ ਜੋ 1980 ਦੇ ਦਹਾਕੇ ਵਿੱਚ ਬ੍ਰਾਜ਼ੀਲ ਵਿੱਚ ਸਾਹਮਣੇ ਆਈ ਸੀ ਅਤੇ ਉਦੋਂ ਤੋਂ ਨੇੜਲੇ ਅਤੇ ਦੂਰ ਦੇ ਦੇਸ਼ਾਂ ਵਿੱਚ ਫੈਲ ਗਈ ਹੈ। ਜਲਵਾਯੂ ਪਰਿਵਰਤਨ ਤੋਂ ਉਮੀਦ ਕੀਤੀ ਜਾਂਦੀ ਹੈ ਕਿ ਉਹ ਇਸ ਦੇ ਫੈਲਣ ਵਿੱਚ ਮਦਦ ਕਰੇਗਾ, ਖਾਸ ਕਰਕੇ ਗਰਮ ਖੰਡੀ ਖੇਤਰਾਂ ਵਿੱਚ।',
                'causes': ['ਮੈਗਨਾਪੋਰਥ ਓਰੀਜ਼ਾ ਉੱਲੀ ਕਾਰਨ ਹੁੰਦਾ ਹੈ।'],
                'preventions': ['ਰੋਧਕ ਕਿਸਮਾਂ ਬੀਜੋ।', 'ਬਹੁਤ ਜ਼ਿਆਦਾ ਨਾਈਟ੍ਰੋਜਨ ਖਾਦ ਪਾਉਣ ਤੋਂ ਬਚੋ।'],
                'remedies': [
                    "ਲੱਛਣਾਂ ਦੇ ਪਹਿਲੇ ਲੱਛਣਾਂ 'ਤੇ ਉੱਲੀਨਾਸ਼ਕਾਂ ਨੂੰ ਲਾਗੂ ਕਰੋ।",
                    'ਫਸਲ ਰੋਟੇਸ਼ਨ ਦਾ ਅਭਿਆਸ ਕਰੋ।',
                ],
            },
            'Fusarium Head Blight': {
                'description': 'ਫੁਸੇਰੀਅਮ ਹੈੱਡ ਬਲਾਈਟ ਇੱਕ ਗੰਭੀਰ ਫੰਗਲ ਬਿਮਾਰੀ ਹੈ ਜੋ ਮਾਈਕੋਟੌਕਸਿਨ ਨਾਲ ਦੂਸ਼ਿਤ ਅਨਾਜ ਵੱਲ ਲੈ ਜਾਂਦੀ ਹੈ। ਇਸ ਦੇ ਨਤੀਜੇ ਵਜੋਂ ਝਾੜ ਘਟਦਾ ਹੈ, ਅਨਾਜ ਦੀ ਮਾੜੀ ਗੁਣਵੱਤਾ, ਅਤੇ ਕਣਕ ਉਤਪਾਦਕਾਂ ਲਈ ਮਹੱਤਵਪੂਰਨ ਆਰਥਿਕ ਨੁਕਸਾਨ ਹੁੰਦਾ ਹੈ।',
                'causes': ['ਫੁਸੇਰੀਅਮ ਸਪੀਸੀਜ਼ ਦੇ ਉੱਲੀ ਕਾਰਨ ਹੁੰਦਾ ਹੈ।'],
                'preventions': ['ਰੋਧਕ ਕਿਸਮਾਂ ਬੀਜੋ।', 'ਫਸਲ ਰੋਟੇਸ਼ਨ ਅਤੇ ਸਾਫ਼ ਬੀਜ ਦੀ ਵਰਤੋਂ ਕਰੋ।'],
                'remedies': [
                    "ਫੁੱਲਾਂ ਦੇ ਪੜਾਅ 'ਤੇ ਉੱਲੀਨਾਸ਼ਕਾਂ ਨੂੰ ਲਾਗੂ ਕਰੋ।",
                    'ਉੱਚ ਫੁਸੇਰੀਅਮ ਦਬਾਅ ਵਾਲੇ ਖੇਤਾਂ ਵਿੱਚ ਬੀਜਣ ਤੋਂ ਬਚੋ।',
                ],
            },
            'Mildew': {
                'description': 'ਕਣਕ ਵਿੱਚ ਪਾਊਡਰਰੀ ਫ਼ਫ਼ੂੰਦੀ ਚਿੱਟੇ ਮਾਈਸੀਲੀਅਮ ਦੇ ਸਤਹ ਧੱਬਿਆਂ ਦੇ ਰੂਪ ਵਿੱਚ ਸ਼ੁਰੂ ਹੁੰਦੀ ਹੈ ਅਤੇ ਅੰਤ ਵਿੱਚ ਪੂਰੇ ਪੱਤੇ ਨੂੰ ਢੱਕ ਸਕਦੀ ਹੈ, ਪਰਿਪੱਕ ਲਾਗਾਂ ਨਾਲ ਕਾਲੇ ਬੀਜਾਣੂ ਦੇ ਕੇਸ ਦਿਖਾਈ ਦਿੰਦੇ ਹਨ। ਇਹ ਹਵਾ ਦੁਆਰਾ ਫੈਲਣ ਵਾਲੀ ਬਿਮਾਰੀ ਠੰਡੇ, ਗਿੱਲੇ ਮੌਸਮ ਵਿੱਚ ਵਧਦੀ ਹੈ ਅਤੇ 40% ਤੱਕ ਝਾੜ ਦਾ ਨੁਕਸਾਨ ਕਰ ਸਕਦੀ ਹੈ।',
                'causes': ['ਬਲੂਮੇਰੀਆ ਗ੍ਰਾਮਿਨਿਸ ਉੱਲੀ ਕਾਰਨ ਹੁੰਦਾ ਹੈ।'],
                'preventions': ['ਰੋਧਕ ਕਿਸਮਾਂ ਬੀਜੋ।', 'ਰੋਕਥਾਮ ਲਈ ਉੱਲੀਨਾਸ਼ਕਾਂ ਨੂੰ ਲਾਗੂ ਕਰੋ।'],
                'remedies': [
                    "ਲੱਛਣ ਦਿਖਾਈ ਦੇਣ 'ਤੇ ਉੱਲੀਨਾਸ਼ਕਾਂ ਨੂੰ ਲਾਗੂ ਕਰੋ।",
                    'ਖੇਤ ਵਿੱਚ ਚੰਗੀ ਹਵਾ ਦਾ ਸੰਚਾਰ ਯਕੀਨੀ ਬਣਾਓ।',
                ],
            },
            'Smut': {
                'description': 'ਢਿੱਲੀ smut ਦੀ ਇੱਕ ਵਿਆਪਕ ਵੰਡ ਹੁੰਦੀ ਹੈ ਅਤੇ ਜਿੱਥੇ ਵੀ ਕਣਕ ਪੈਦਾ ਹੁੰਦੀ ਹੈ ਉੱਥੇ ਹੋ ਸਕਦੀ ਹੈ। ਸਿਰਲੇਖ ਤੋਂ ਪਹਿਲਾਂ ਹਲਕੇ ਲੱਛਣ ਮੌਜੂਦ ਹੋ ਸਕਦੇ ਹਨ, ਜਿਸ ਵਿੱਚ ਪੱਤਿਆਂ ਦੀਆਂ ਪੀਲੀਆਂ ਧਾਰੀਆਂ ਅਤੇ ਸਖ਼ਤ, ਗੂੜ੍ਹੇ ਹਰੇ ਪੱਤੇ ਸ਼ਾਮਲ ਹਨ।',
                'causes': ['Ustilago ਸਪੀਸੀਜ਼ ਵਰਗੀ ਉੱਲੀ ਕਾਰਨ ਹੁੰਦਾ ਹੈ.'],
                'preventions': [
                    'smut-ਰੋਧਕ ਕਿਸਮਾਂ ਦੀ ਵਰਤੋਂ ਕਰੋ।',
                    'ਬੀਜਣ ਤੋਂ ਪਹਿਲਾਂ ਬੀਜਾਂ ਨੂੰ ਉੱਲੀਨਾਸ਼ਕਾਂ ਨਾਲ ਇਲਾਜ ਕਰੋ।',
                ],
                'remedies': [
                    'ਸੰਕਰਮਿਤ ਪੌਦਿਆਂ ਨੂੰ ਨਸ਼ਟ ਕਰੋ।',
                    'ਢੁਕਵੀਆਂ ਉੱਲੀਨਾਸ਼ਕਾਂ ਦੀ ਵਰਤੋਂ ਕਰੋ।',
                ],
            },
            'Yellow Rust': {
                'description': "ਪੀਲੀ ਜੰਗਾਲ ਦਾ ਵਿਸ਼ੇਸ਼ ਲੱਛਣ ਬਾਲਗ ਪੌਦਿਆਂ ਦੇ ਪੱਤਿਆਂ 'ਤੇ ਪੀਲੇ ਸੰਤਰੀ ਰੰਗ ਦੇ ਛਾਲਿਆਂ ਦੀਆਂ ਸਮਾਨਾਂਤਰ ਕਤਾਰਾਂ ਹਨ। ਪੀਲੀ ਜੰਗਾਲ ਦੀ ਮਹਾਂਮਾਰੀ ਅਕਸਰ ਵਿਅਕਤੀਗਤ ਪੌਦਿਆਂ ਦੇ ਰੂਪ ਵਿੱਚ ਸ਼ੁਰੂ ਹੁੰਦੀ ਹੈ, ਆਮ ਤੌਰ 'ਤੇ ਪਤਝੜ ਵਿੱਚ।",
                'causes': ['Puccinia striformis ਉੱਲੀ ਦੇ ਕਾਰਨ ਹੁੰਦਾ ਹੈ।'],
                'preventions': ['ਰੋਧਕ ਕਿਸਮਾਂ ਬੀਜੋ।', 'ਰੋਕਥਾਮ ਲਈ ਉੱਲੀਨਾਸ਼ਕਾਂ ਨੂੰ ਲਾਗੂ ਕਰੋ।'],
                'remedies': [
                    "ਲੱਛਣ ਦਿਖਾਈ ਦੇਣ 'ਤੇ ਉੱਲੀਨਾਸ਼ਕਾਂ ਨੂੰ ਲਾਗੂ ਕਰੋ।",
                    'ਲਾਗ ਵਾਲੇ ਪੌਦਿਆਂ ਦੇ ਮਲਬੇ ਨੂੰ ਹਟਾਓ ਅਤੇ ਨਸ਼ਟ ਕਰੋ।',
                ],
            },
        },
    },
}
