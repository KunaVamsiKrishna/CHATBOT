from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Predefined remedies data
remedies_data = {
    
  
  "Constipation": {
    "remedy": "Prunes, Flaxseed, Psyllium Husk",
    "preparation": "Eat a handful (5-7) of prunes or drink prune juice. Flaxseed should be ground and added to smoothies, oatmeal, or yogurt. For psyllium husk, mix 1 tablespoon in a glass of water and drink it immediately, followed by another glass of water.",
    "use": "Prunes help soften stools, flaxseed adds fiber, and psyllium husk promotes bowel movement by absorbing water in the gut."
  },
  "Indigestion": {
    "remedy": "Baking Soda, Lemon Juice, Fennel",
    "preparation": "Mix 1/2 teaspoon of baking soda in a glass of water and drink it. For lemon juice, squeeze half a lemon into warm water and drink before meals. Fennel seeds can be chewed after meals or brewed into tea by steeping a teaspoon of seeds in hot water for 10 minutes.",
    "use": "Baking soda neutralizes stomach acid, lemon juice aids digestion, and fennel reduces bloating and discomfort."
  },
  "Cough": {
    "remedy": "Honey, Thyme, Licorice Root",
    "preparation": "Take a spoonful of honey directly or mix it into warm tea. Thyme tea is made by steeping a tablespoon of dried thyme in boiling water for 10 minutes, then straining and drinking. Licorice root tea can be prepared by simmering 1-2 teaspoons of dried root in water for 10 minutes, then straining.",
    "use": "Honey soothes the throat, thyme works as an expectorant, and licorice root calms irritated airways."
  },
  "Menstrual Cramps": {
    "remedy": "Ginger, Cinnamon, Heat Therapy",
    "preparation": "Ginger and cinnamon can be boiled together in water for 10 minutes to make tea. For heat therapy, apply a hot water bottle or heating pad to your lower abdomen for 20-30 minutes.",
    "use": "Ginger and cinnamon reduce pain by lowering inflammation, and heat relaxes the muscles, relieving cramps."
  },
 
  "Ear Infection": {
    "remedy": "Garlic Oil, Mullein Oil, Warm Compress",
    "preparation": "Warm garlic oil slightly and put a few drops into the affected ear. Mullein oil can be applied in the same way. To use a warm compress, soak a clean cloth in hot water, wring it out, and place it over the ear for 10-15 minutes.",
    "use": "Garlic oil has antimicrobial properties, mullein oil reduces swelling, and a warm compress eases pain."
  },
  "Cholesterol": {
    "remedy": "Oats, Garlic, Green Tea",
    "preparation": "Cook oats as a breakfast porridge or add them to smoothies. Garlic can be eaten raw or taken as a supplement. Green tea is brewed by steeping tea leaves in hot water for 3-5 minutes.",
    "use": "Oats help lower bad cholesterol levels, garlic improves circulation, and green tea boosts overall heart health."
  },
  "Hair Loss": {
    "remedy": "Rosemary Oil, Aloe Vera, Biotin",
    "preparation": "Mix a few drops of rosemary oil with a carrier oil (like coconut oil) and massage into the scalp for 5-10 minutes before washing. Apply fresh aloe vera gel to the scalp and let it sit for 30 minutes before rinsing. Biotin supplements are taken as directed on the package.",
    "use": "Rosemary oil stimulates hair growth, aloe vera strengthens hair, and biotin supports hair and nail health."
  },
  "Dry Skin": {
    "remedy": "Coconut Oil, Shea Butter, Oatmeal Bath",
    "preparation": "Apply coconut oil or shea butter directly to the skin after a shower when the skin is still damp. For an oatmeal bath, grind a cup of oats into a fine powder and add it to lukewarm water, soaking for 15-20 minutes.",
    "use": "Coconut oil and shea butter moisturize the skin, while oatmeal soothes and hydrates dry skin."
  },
  "Fatigue": {
    "remedy": "Ginseng, Ashwagandha, Green Tea",
    "preparation": "Ginseng can be taken as a supplement or brewed as a tea by steeping the root in hot water. Ashwagandha is available in capsule form or as a powder to mix into drinks. Green tea is brewed by steeping tea leaves in hot water for 3-5 minutes.",
    "use": "Ginseng boosts energy levels, ashwagandha helps manage stress, and green tea provides a mild caffeine boost."
  },
  "Allergies": {
    "remedy": "Quercetin, Butterbur, Neti Pot",
    "preparation": "Quercetin is available as a supplement and should be taken as directed. Butterbur can also be taken in capsule form. A neti pot can be used with a saline solution to rinse nasal passages.",
    "use": "Quercetin and butterbur reduce histamine release, while a neti pot helps clear allergens from the nasal passages."
  },
  "Anxiety": {
    "remedy": "Chamomile Tea, Lavender Oil, Ashwagandha",
    "preparation": "Brew chamomile tea by steeping dried flowers in hot water for 5-10 minutes. Lavender oil can be diffused or applied topically. Ashwagandha supplements can be taken as directed.",
    "use": "Chamomile and lavender promote relaxation, while ashwagandha helps manage stress levels."
  },
  "High Blood Pressure": {
    "remedy": "Garlic, Omega-3 Fatty Acids, Dark Chocolate",
    "preparation": "Garlic can be consumed raw or in supplement form. Omega-3s can be found in fish oil supplements or fatty fish. Dark chocolate should be 70% cocoa or higher and can be consumed in moderation.",
    "use": "Garlic helps lower blood pressure, omega-3s improve heart health, and dark chocolate may help improve circulation."
  },
  "Toothache": {
    "remedy": "Clove Oil, Salt Water Rinse, Garlic",
    "preparation": "Apply a drop of clove oil to the painful tooth with a cotton swab. For a saltwater rinse, dissolve 1/2 teaspoon of salt in warm water and swish it in your mouth for 30 seconds. Chew on a fresh garlic clove or apply crushed garlic directly to the affected area for pain relief.",
    "use": "Clove oil numbs the pain, salt water cleans the area and reduces inflammation, and garlic acts as a natural antibiotic."
  },
  "Dandruff": {
    "remedy": "Apple Cider Vinegar, Coconut Oil, Tea Tree Oil",
    "preparation": "Mix equal parts apple cider vinegar and water and apply it to the scalp for 10-15 minutes before rinsing. Massage coconut oil into the scalp and leave it on for 30 minutes before washing. Add a few drops of tea tree oil to your shampoo and wash your hair as usual.",
    "use": "Apple cider vinegar restores the scalp's pH balance, coconut oil moisturizes, and tea tree oil fights fungus that causes dandruff."
  },
  "Dry Skin": {
    "remedy": "Coconut Oil, Honey, Oatmeal",
    "preparation": "Apply coconut oil directly to dry areas of the skin. Mix honey with water for a moisturizing mask, leave it on for 15 minutes, then rinse. For an oatmeal bath, grind oatmeal into a fine powder and add it to warm bathwater.",
    "use": "Coconut oil provides moisture, honey hydrates, and oatmeal soothes and protects the skin."
  },
  "Indigestion": {
    "remedy": "Ginger, Peppermint, Apple Cider Vinegar",
    "preparation": "Make ginger tea by boiling fresh ginger slices in water for 10 minutes. Brew peppermint tea by steeping peppermint leaves in hot water for 5-10 minutes. Mix 1-2 tablespoons of apple cider vinegar in a glass of water and drink before meals.",
    "use": "Ginger aids digestion, peppermint relaxes the digestive tract, and apple cider vinegar helps balance stomach acidity."
  },
  "Ear Infections": {
    "remedy": "Garlic Oil, Warm Compress, Apple Cider Vinegar",
    "preparation": "Make garlic oil by heating minced garlic in olive oil, then strain and apply a few drops to the affected ear. Use a warm compress by soaking a cloth in warm water, wringing it out, and applying it to the ear. Mix equal parts of apple cider vinegar and water and use it as ear drops.",
    "use": "Garlic has antibacterial properties, warm compresses relieve pain, and apple cider vinegar helps restore pH balance."
  },
  "Fever": {
    "remedy": "Ginger Tea, Basil Leaves, Apple Cider Vinegar",
    "preparation": "Boil a few slices of ginger in water to make tea and drink 2-3 times a day. Chew 4-5 fresh basil leaves or boil them in water and sip. Mix 1 tablespoon of apple cider vinegar in a glass of water and drink it.",
    "use": "Ginger tea reduces body temperature, basil has antibacterial properties, and apple cider vinegar promotes sweating to reduce fever."
  },
"Oil Face": {
    "remedy": "Aloe Vera, Honey, Tea Tree Oil",
    "preparation": "Apply fresh aloe vera gel on the face, leave it for 10-15 minutes, and rinse. Mix 1 tablespoon of honey with a few drops of tea tree oil, apply as a mask, and leave for 20 minutes before rinsing.",
    "use": "Aloe vera controls oil production, honey moisturizes without making skin oily, and tea tree oil has antibacterial properties to prevent acne."
  },
"Cold": {
    "remedy": "Honey, Lemon, Garlic",
    "preparation": "Mix 1 tablespoon of honey with a few drops of lemon juice and warm water, and drink. Crush 2-3 garlic cloves and eat them raw or add them to soups.",
    "use": "Honey soothes the throat, lemon boosts immunity, and garlic has antiviral properties to reduce cold symptoms."
  },
"Weight Gain": {
    "remedy": "Peanut Butter, Milk, Bananas",
    "preparation": "Eat peanut butter with bread or in smoothies. Drink full-fat milk 2-3 times a day. Eat ripe bananas or blend them into smoothies.",
    "use": "Peanut butter is rich in healthy fats and calories, milk provides protein and nutrients, and bananas are calorie-dense and help with weight gain."
  },
"Weight Loss": {
    "remedy": "Green Tea, Lemon Water, Cinnamon",
    "preparation": "Brew green tea and drink 2-3 cups a day. Squeeze half a lemon into a glass of warm water and drink in the morning. Add 1 teaspoon of cinnamon powder to warm water or tea and drink daily.",
    "use": "Green tea boosts metabolism, lemon water aids digestion, and cinnamon regulates blood sugar and reduces cravings."
  },
  "High Blood Pressure": {
    "remedy": "Garlic, Banana, Flaxseeds",
    "preparation": "Crush 1-2 cloves of raw garlic and consume it with water daily. Eat a banana every day as part of your diet. Add 1 tablespoon of flaxseeds to your smoothies, yogurt, or salads.",
    "use": "Garlic helps relax blood vessels and reduce pressure, bananas are rich in potassium which helps balance sodium levels, and flaxseeds contain omega-3 fatty acids that lower blood pressure."
  },
"Low Blood Pressure": {
    "remedy": "Salt Water, Raisins, Coffee",
    "preparation": "Mix 1/2 teaspoon of salt in a glass of water and drink when you feel lightheaded. Soak 7-10 raisins in water overnight and eat them on an empty stomach in the morning. Drink a cup of strong coffee if you're experiencing low blood pressure symptoms.",
    "use": "Salt increases sodium levels in the body, raisins support adrenal function to normalize blood pressure, and coffee temporarily boosts blood pressure by stimulating the heart."
  },
  "Sugar": {
    "remedy": "Cinnamon, Fenugreek Seeds, Bitter Gourd",
    "preparation": "Add 1/2 teaspoon of cinnamon powder to your tea or smoothies daily. Soak 1 tablespoon of fenugreek seeds in water overnight and drink the water in the morning. Drink fresh bitter gourd juice or include it in your meals.",
    "use": "Cinnamon helps regulate blood sugar levels, fenugreek improves insulin sensitivity, and bitter gourd contains compounds that help lower blood sugar."
  },
"Stomach Pain": {
    "remedy": "Peppermint Tea, Ginger, Ajwain (Carom Seeds)",
    "preparation": "Brew peppermint tea by steeping fresh leaves or tea bags in hot water and drink 2-3 times a day. Chew small pieces of fresh ginger or drink ginger tea. Roast 1/2 teaspoon of ajwain and consume it with a pinch of black salt.",
    "use": "Peppermint relaxes stomach muscles, ginger reduces inflammation and soothes the digestive system, and ajwain relieves gas and indigestion, reducing stomach pain."
  },
  "Acidity": {
    "remedy": "Cold Milk, Fennel Seeds, Baking Soda",
    "preparation": "Drink a glass of cold milk when you feel symptoms of acidity. Chew a teaspoon of fennel seeds after meals. Mix 1/2 teaspoon of baking soda in a glass of water and drink it for quick relief.",
    "use": "Cold milk neutralizes stomach acid, fennel seeds soothe the digestive tract, and baking soda acts as an antacid to reduce acidity."
  },
  "Headache": {
    "remedy": "Peppermint Oil, Ginger Tea, Lavender Oil",
    "preparation": "Apply a few drops of peppermint oil to the temples and massage gently. Drink ginger tea made by boiling fresh ginger slices in water. Inhale the aroma of lavender oil or apply it to the temples.",
    "use": "Peppermint oil relaxes muscles and improves circulation, ginger reduces inflammation, and lavender oil helps relieve tension headaches."
  },
"Joint Pain": {
    "remedy": "Turmeric, Epsom Salt, Ginger",
    "preparation": "Mix 1/2 teaspoon of turmeric in warm milk and drink daily. Add Epsom salt to warm bath water and soak the affected joints. Drink ginger tea twice a day.",
    "use": "Turmeric has anti-inflammatory properties, Epsom salt reduces swelling, and ginger helps with pain relief."
  },
"Anxiety": {
    "remedy": "Chamomile Tea, Ashwagandha, Deep Breathing",
    "preparation": "Drink chamomile tea 2-3 times a day. Take ashwagandha supplements as recommended. Practice deep breathing for 10-15 minutes.",
    "use": "Chamomile helps relax the nervous system, ashwagandha reduces stress hormones, and deep breathing calms the mind and reduces anxiety."
  },
  "Back Pain": {
    "remedy": "Turmeric, Epsom Salt, Ginger",
    "preparation": "Mix 1/2 teaspoon of turmeric powder in warm milk and drink daily. Add 2 cups of Epsom salt to warm bathwater and soak for 15-20 minutes. Drink ginger tea made by boiling fresh ginger slices in water twice a day.",
    "use": "Turmeric has anti-inflammatory properties that reduce pain, Epsom salt relaxes muscles and reduces swelling, and ginger helps alleviate muscle soreness and inflammation."
  },
  "Tan": {
    "remedy": "Lemon Juice, Yogurt, Cucumber",
    "preparation": "Mix the juice of one lemon with 2 tablespoons of yogurt and apply it to the tanned areas. Leave it on for 30 minutes before rinsing off with lukewarm water. Grate half a cucumber and apply the pulp to the skin for 15-20 minutes.",
    "use": "Lemon juice acts as a natural bleaching agent, yogurt moisturizes the skin while helping to lighten tan, and cucumber soothes the skin and provides hydration."
  },
"Pimples": {
    "remedy": "Tea Tree Oil, Aloe Vera, Honey",
    "preparation": "Apply a few drops of tea tree oil directly onto the pimple using a cotton swab. Use fresh aloe vera gel as a spot treatment and leave it overnight. Mix honey with a few drops of lemon juice and apply it as a mask for 15-20 minutes.",
    "use": "Tea tree oil has antibacterial properties, aloe vera soothes inflammation, and honey helps reduce bacteria and heal the skin."
  },
"Dark Spots": {
    "remedy": "Vitamin C Serum, Apple Cider Vinegar, Papaya",
    "preparation": "Apply vitamin C serum to the affected areas daily. Mix equal parts of apple cider vinegar and water, apply to dark spots, and rinse after 10 minutes. Mash ripe papaya and apply it as a mask for 20-30 minutes.",
    "use": "Vitamin C brightens skin, apple cider vinegar helps lighten dark spots, and papaya contains enzymes that exfoliate and rejuvenate the skin."
  },
"Hair Fall": {
    "remedy": "Coconut Oil, Amla, Fenugreek Seeds",
    "preparation": "Warm 2 tablespoons of coconut oil and massage it into the scalp, leave it for at least 30 minutes before washing. Soak 2 tablespoons of amla overnight, grind it to a paste, and apply to the hair for 30 minutes before rinsing. Soak fenugreek seeds overnight, grind to a paste, and apply to the scalp for 30 minutes.",
    "use": "Coconut oil nourishes hair, amla strengthens hair follicles, and fenugreek seeds promote hair growth."
  },
"Hair Thinning": {
    "remedy": "Onion Juice, Olive Oil, Castor Oil",
    "preparation": "Extract onion juice and apply it to the scalp, leaving it on for 30-60 minutes before washing. Mix equal parts of olive oil and castor oil, warm slightly, and massage into the scalp. Leave it overnight and wash in the morning.",
    "use": "Onion juice promotes hair growth due to sulfur content, olive oil adds moisture, and castor oil nourishes and strengthens hair."
  },
"Laziness": {
    "remedy": "Ginger Tea, Green Tea, Honey",
    "preparation": "Brew ginger tea by boiling fresh ginger slices in water and drink it in the morning. Drink 1-2 cups of green tea daily. Mix honey with warm water and consume it in the morning.",
    "use": "Ginger tea boosts energy levels, green tea enhances metabolism, and honey provides natural energy."
  },
"Period Cramps": {
    "remedy": "Ginger Tea, Heating Pad, Chamomile Tea",
    "preparation": "Brew ginger tea by boiling fresh ginger slices and drink it several times a day. Use a heating pad on the abdomen for relief. Brew chamomile tea and drink it before bed.",
    "use": "Ginger has anti-inflammatory properties, a heating pad relaxes muscles, and chamomile tea helps ease cramps and promote relaxation."
  },
"Skin Allergy": {
    "remedy": "Oatmeal Bath, Aloe Vera, Honey",
    "preparation": "Add colloidal oatmeal to warm bathwater and soak for 15-20 minutes. Apply fresh aloe vera gel to the affected areas. Mix honey with a few drops of lemon juice and apply as a mask.",
    "use": "Oatmeal soothes irritated skin, aloe vera provides relief and hydration, and honey has antibacterial properties."
  },
"Fat Burning": {
    "remedy": "Green Tea, Apple Cider Vinegar, Lemon Water",
    "preparation": "Drink 2-3 cups of green tea daily. Mix 1-2 tablespoons of apple cider vinegar in a glass of water and drink it before meals. Squeeze the juice of half a lemon in warm water and drink it every morning.",
    "use": "Green tea boosts metabolism, apple cider vinegar helps control appetite, and lemon water aids digestion and detoxification."
  }







    # Add other remedies as necessary...
}

# Function to get remedy based on the question
def get_remedy(question):
    for key in remedies_data.keys():
        if key.lower() in question.lower():
            return remedies_data[key]
    return {"remedy": "No remedy found", "preparation": "", "use": ""}

# Define a route for the home page
@app.route('/')
def index():
    return render_template('index.html')

# Define a route for the chatbot page
@app.route('/chat')
def chat():
    return render_template('chat.html')

# Define a route to get remedy based on user input
@app.route('/get_remedy', methods=['POST'])
def get_remedy_api():
    data = request.json
    question = data.get('question', '')
    remedy_info = get_remedy(question)
    return jsonify(remedy_info)

if __name__ == "__main__":
    app.run(debug=True)
