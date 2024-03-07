# too_long_did_not_listen

*Ce toy project a pour objectif de tester l'API open ai pour créer une application RAG ('Retrieval Augmented Generation').*

RAG est une approche permettant d'améliorer l'efficacité des LLM en tirant parti de données personnalisées. Il s'agit de fournir comme contexte au LLM des données/documents pertinents pour une question/tâche spécifique. RAG a notamment fait ses preuves dans les chatbots et les systèmes de questions-réponses.

Dans ce cas d'espèce j'ai créé un **chat bot** entrainé sur deux épisodes du podcast Huberman Lab. Ce sont des podcast longs et denses en information (contenu scientifique). L'idée est de pouvoir accéder rapidement aux informations souhaitées sans avoir à écouter les épisodes dans leur intégralité.

A noter : le chat bot pourrais être entrainé sur la totalité des épisodes de podcats, emmagasinant ainsi une large database de connaissance spécifique (contenu 'scientifique' sur le bio hacking mis à disposition par le docteur Huberman via ses podcasts)

Ci dessous quelques captures d'écran du dashboard avec des exemples de questions / réponses

#

![image](https://github.com/estellec18/too_long_did_not_listen/assets/126951321/b3772272-ad7e-4c7c-9b84-2125cc6886ac)

#

![image](https://github.com/estellec18/too_long_did_not_listen/assets/126951321/8bdd2342-f908-4c75-8223-845b918b69db)

#
Le modèle connait uniquement le context spécifique fourni (le transcript des podcasts ne fait pas mention de Donald Trump)
##
![image](https://github.com/estellec18/too_long_did_not_listen/assets/126951321/c57d2c87-9ea0-4f11-9a59-c5aa9f93214b)

#
Mise en évidence d'une limite : Athletic greens est un sponsort du podcast et ce produit est mis en avant lors des coupures pub. Ces coupures pub n'étant pas flaguées comme telles dans le transcript, le bot prend les information 'at face value'
##
![image](https://github.com/estellec18/too_long_did_not_listen/assets/126951321/2a24503a-d746-4b35-b67f-22db81deb3c1)


