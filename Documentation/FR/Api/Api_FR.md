# Documentation de l'API

## Technologies de l'API

L'API à été réalisée sous *Python 3.8.1* avec une base de données *SQLite*.

## L'arborescence de l'API

L'API est divisée en plusieurs dossiers contenant méthodes, modèles objets, tests, fichiers de base de données et coverage.

### Liste des dossiers et ce qu'ils contiennent.

![alt text](../../pictures/Api/Api_resume.png)

- **csv_test** : contient les fichiers CSV nécessaires pour les tests.
- **database** : contient les méthodes de création et de remise à 0 de base de données.
- **databases_files** : contient les dossiers contenant les fichiers de base de données.
  - *activities_items_db* : contient les fichiers de base de données des bases contenant les activités et objets.
  - *projects_db* : contient le fichier de base de données contenant les projets.
- **htmlcov** : contient les fichiers de nécessaire au lancement du coverage.
- **import_in_database** : contient méthodes d'import de donnée en base de données.
- **methods_on_activities_item_database** : contient les methodes de récuperation ainsi que de supression sur la base de données d'activités et d'objets.
- **methods_on_csv** : contient les methodes de transformation de CSV.
- **methods_on_project_database** : contient les méthodes de récuperation ainsi que de supression sur la base de données des projets.
- **model** : contient les modèles objets de l'application
- **tests** : contient les fichiers permettant de lancer les tests

## Description des méthodes.

- **database** : les méthodes dans database sont :
  - *init_database_activities_items* : méthode appelée pour créer la base de données des activités et des objets.
  - *init_databse_project* : méthode appelée pour créer la base de données des projets.
  - *reset_database_activities_items* : méthode appelée pour remettre à 0 les données de la base de données d'activités et d'objets.
  - *reset_database_project* : méthode appelée pour remettre à 0 les données de la base de données de projets.

  ![alt text](../../pictures/Api/Api_detail_1.png)
  
  
- **import_in_database** : les méthodes dans import_in_database sont :
  - *activity_item_import* : méthode permettant, avec une ligne de CSV envoyée par une méthodes de methods_on_csv.
  - *create_project* : méthode permettant de créer un projet ainsi que la base de données d'activités et d'objets qui lui est lié.
  - *update_activity_item* : méthode permettant d'appeler reset_database_activities_items et d'ensuite réimporter des données.

  ![alt text](../../pictures/Api/Api_detail_2.png)
  

- **methods_on activities_items_database** : les méthodes dans methods_on activities_items_database sont :
  - *delete_activities_items_database* : méthode permettant de supprimer la base de donnée des activités liée à un projet.
  - *get_activities_with_project_id* : méthode récuperant les activités liée à un projet en base de données.
  - *get_activities_items_project_with_project_id* : méthode récuperant les activités, objets et données du projet auquels les activités et objets sont liés. 
  - *get_activities_items_with_project_id* : méthode récuperant les activités, objets et id du projet auquels activité et objets sont liés.
  - *get_items_with_project_id* : méthode récuperant les objets lié à un projet.

  ![alt text](../../pictures/Api/Api_detail_3.png)

  
- **methods_on_csv** : les méthodes dans methods_on_csv sont : 
  - *import_activity_csv* : méthode permettant d'importer un fichier CSV contenant les activités dans un format spécifique.
  - *import_item_csv* : méthode permettant d'importer un fichier CSV contenant les objets dans un format spécifique. 

  ![alt text](../../pictures/Api/Api_detail_4.png)

- **methods_on_project_database** : les méthodes dans méthods_on_project_database : 
  - *delete_project* : méthode permettant de supprimer un projet et de supprimer la base de données d'activités et d'objets lié à ce projet.
  - *get_project_id_with_name* :  méthode qui, grace au nom du projet, permet de récuperer l'ID de celui-ci.
  - *get_project_with_id* : méthode qui, grace à l'ID du projet, permet de récuperer le projet en entier (sans les activités et objets).
  - *get_projects* : méthode qui renvoie une liste de tout les projets existant (sans les activités et objets).
  - *project_not_exist* : méthode qui, grace au nom du projet, permet de savoir si un projet du même nom existe déja.
  - *rename_project* : méthode qui, grace à l'id du projet, permet de renommer un projet.
  - *update_project_last_opening_date* : méthode qui permet grace à l'id d'un projet, de changer la date de dernière ouverture.

  ![alt text](../../pictures/Api/Api_detail_5.png) 
 

## Les Tests
Les tests ont tous un numéro (test1_******* par exemple) ils doivent être lancer dans cette ordre sinon ils buggeront.
Le test "all_tests" lance tout les autres fichiers de test dans l'ordre, permettant une création et reinitialisation de base de données

![alt text](../../pictures/Api/Api_test.png)