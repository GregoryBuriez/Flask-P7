Vous êtes Data Scientist au sein d'une société financière, nommée "Prêt à dépenser", qui propose des crédits à la consommation pour des personnes ayant peu ou pas du tout d'historique de prêt.

L’entreprise souhaite mettre en œuvre un outil de “scoring crédit” pour calculer la probabilité qu’un client rembourse son crédit, puis classifie la demande en crédit accordé ou refusé. Elle souhaite donc développer un algorithme de classification en s’appuyant sur des sources de données variées (données comportementales, données provenant d'autres institutions financières, etc.).

De plus, les chargés de relation client ont fait remonter le fait que les clients sont de plus en plus demandeurs de transparence vis-à-vis des décisions d’octroi de crédit. Cette demande de transparence des clients va tout à fait dans le sens des valeurs que l’entreprise veut incarner.
Prêt à dépenser décide donc de développer un dashboard interactif pour que les chargés de relation client puissent à la fois expliquer de façon la plus transparente possible les décisions d’octroi de crédit, mais également permettre à leurs clients de disposer de leurs informations personnelles et de les explorer facilement. 


I. Votre mission
- Construire un modèle de scoring qui donnera une prédiction sur la probabilité de faillite d'un client de façon automatique.
- Construire un dashboard interactif à destination des gestionnaires de la relation client permettant d'interpréter les prédictions faites par le modèle, et d’améliorer la connaissance client des chargés de relation client.
- Mettre en production le modèle de scoring de prédiction à l’aide d’une API, ainsi que le dashboard interactif qui appelle l’API pour les prédictions.
- Michaël, votre manager, vous incite à sélectionner un ou des kernels Kaggle pour vous faciliter l’analyse exploratoire, la préparation des données et le feature engineering nécessaires à l’élaboration du modèle de scoring. Si vous le faites, vous devez analyser ce ou ces kernels et le ou les adapterpour vous assurer qu’ils répond(ent) aux besoins de votre mission.


II. Compétences évaluées
- Définir et mettre en œuvre une stratégie de suivi de la performance d’un modèle
- Évaluer les performances des modèles d’apprentissage supervisé
- Utiliser un logiciel de version de code pour assurer l’intégration du modèle
- Définir la stratégie d’élaboration d’un modèle d’apprentissage supervisé
- Réaliser un dashboard pour présenter son travail de modélisation
- Rédiger une note méthodologique afin de communiquer sa démarche de modélisation
- Présenter son travail de modélisation à l'oral
- Déployer un modèle via une API dans le Web
- Définir et mettre en œuvre un pipeline d’entraînement des modèles

III. Présentation de l'API

Notre projet Flask vise à créer une API permettant de déterminer la probabilité de remboursement d'un client. 
Cette API sera développée en utilisant Flask, un framework web léger et flexible en Python. 
Flask facilite la création d'applications web et d'API en fournissant des fonctionnalités de base tout en étant extensible.

Une fois que nous aurons développé l'API, nous prévoyons de la déployer sur la plateforme Heroku. 
Heroku est une plateforme en tant que service (PaaS) qui permet de déployer, de gérer et de mettre à l'échelle des applications web facilement. 
Elle offre une infrastructure robuste pour héberger nos applications Flask sans avoir à se soucier de la configuration et de la gestion des serveurs.

Après avoir déployé l'API sur Heroku, nous pourrons l'utiliser pour collecter des données en temps réel. 
Notre objectif est de créer un dashboard interactif qui fournira des informations pertinentes sur la probabilité de remboursement des clients. 
Grâce à l'API, nous serons en mesure de collecter les données nécessaires et de les afficher de manière conviviale sur le dashboard.

