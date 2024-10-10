import spacy

# Load the pre-trained spaCy model (e.g., English model)
nlp = spacy.load('en_core_web_sm')

# Define keywords for categories
categories = {
    'Terrorism / protest / political unrest / riot': ['terrorism', 'protest', 'political unrest', 'riot'],
    'Positive/Uplifting': ['positive', 'uplifting', 'success'],
    'Natural Disasters': ['earthquake', 'flood', 'hurricane', 'natural disaster'],
    'Others': []
}

def classify_article(content):
    doc = nlp(content)
    category_scores = {cat: 0 for cat in categories}

    # Check for keyword matches in article content
    for token in doc:
        for category, keywords in categories.items():
            if token.lemma_ in keywords:
                category_scores[category] += 1

    # Assign the category with the highest score
    assigned_category = max(category_scores, key=category_scores.get)
    return assigned_category if category_scores[assigned_category] > 0 else 'Others'
