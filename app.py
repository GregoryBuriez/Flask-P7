from flask import Flask, jsonify, render_template, request
import pandas as pd
import pickle
import json

app = Flask(__name__)

# Importer le dataframe
df = pd.read_csv('df_tabdashboard.csv')

# Importer le modèle
with open('model_streamlit.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def home():
    return render_template('index.html')

# url résultats formulaire
@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        # Obtenir l'identifiant du client à partir du formulaire
        client_id = int(request.form['client_id'])

        # Vérifier si l'identifiant du client est présent dans le dataframe
        if client_id in df['SK_ID_CURR'].values:
            # Obtenir les caractéristiques du client
            client_features = df[df['SK_ID_CURR'] == client_id].values[0]

            # Faire la prédiction
            prediction = model.predict([client_features])[0]

            # Afficher le résultat de la prédiction dans le template
            return render_template('result.html', prediction=prediction)
        else:
            # Afficher un message d'erreur si l'identifiant du client n'est pas trouvé
            return render_template('result.html', error="Identifiant non reconnu")

    return render_template('index.html')

# url résultats formulaire
@app.route('/api/predict', methods=['POST'])
def api_predict():
    if request.method == 'POST':
        # Obtenir l'identifiant du client à partir du formulaire
        client_id = int(request.form['client_id'])

        # Vérifier si l'identifiant du client est présent dans le dataframe
        if client_id in df['SK_ID_CURR'].values:
            # Obtenir les caractéristiques du client
            client_features = df[df['SK_ID_CURR'] == client_id].values[0]

            # Faire la prédiction
            prediction = model.predict([client_features])[0]

            # prédiction en résultat
            result = {'prediction': prediction}
        else:
            # erreur en résultat
            result = {'error': "Identifiant non reconnu", 'prediction': None}

        # renvoyer le résultat
        return jsonify(result)

if __name__ == '__main__':
    app.run(port=8000)
