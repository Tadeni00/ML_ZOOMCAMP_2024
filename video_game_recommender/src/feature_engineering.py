import pandas as pd
import spacy
from sklearn.preprocessing import normalize
import logging

nlp = spacy.load('en_core_web_md')

def clean_and_vectorize(text):
    doc = nlp(str(text))
    # Lemmatize, remove stop words and punctuation
    cleaned_text = ' '.join([token.lemma_ for token in doc if not token.is_stop and not token.is_punct])
    return cleaned_text, doc.vector.tolist()


def feature_engineering(data):
    # Apply text cleaning and vectorization
    data[['cleaned_combined_features', 'combined_features_vector']] = data['combined_features'] \
        .apply(clean_and_vectorize).apply(pd.Series)
    
    # Normalize the vectors
    normalized_vectors = normalize(data['combined_features_vector'].tolist(), norm='l2', axis=1)

    # Create vector columns
    vector_columns = pd.DataFrame(
        normalized_vectors,
        columns=[f'combined_features_vec_{i}' for i in range(nlp.vocab.vectors_length)]
    )

    # Concatenate vector columns to the data
    data = pd.concat([data, vector_columns], axis=1)

    logging.info("Feature engineering completed successfully.")
    return data

