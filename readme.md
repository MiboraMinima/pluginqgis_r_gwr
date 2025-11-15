## **Plugin Qgis pour réaliser une analyse de GWR à l'aide du package GWmodel.**

**Des données test sont dans le dossier "data_test"**
  - Au format shape et geopackage
  - Des polygones et des points.

Pour installer plug-in télécharger dossier et décompresser dasn le dossier plugins de Qgis, (vous pouvez supprimer le dossier data_test), le chemin vers le dossier devrait ressembler sur windows à qqch comme ça : C:\Users\nomutilisateur\AppData\Roaming\QGIS\QGIS3\profiles\default\python\plugins


# Résumé du Plugin 

## Structure du Plugin
Architecture générale

gwr_plugin/
│
├── __init__.py                 # Point d'entrée du plugin
├── gwr_plugin_r.py            # Fichier principal - Interface utilisateur
├── gwr_analysis.py            # Module d'analyse GWR
├── mgwr_analysis.py           # Module d'analyse MGWR
├── lisa_analysis.py           # Module d'analyse LISA
├── config.ini                 # Fichier de configuration (chemin R)
└── metadata.txt               # Métadonnées du plugin (optionnel)

## Objectif du plugin
Réaliser une **Régression Géographiquement Pondérée (GWR)**, une **MGWR** ou une analyse de **LISA** directement depuis QGIS en utilisant R et les package `GWmodel` et `rgeoda`.

---

## Le processus

┌─────────────────────────────────────────────────────────────┐
│  1. UTILISATEUR                                             │
│     └─> Sélection du modèle (GWR/MGWR/LISA)                │
│     └─> Configuration des paramètres                        │
│     └─> Validation                                          │
└─────────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────────┐
│  2. PYTHON (gwr_plugin_r.py)                                │
│     └─> Récupération de la couche QGIS                     │
│     └─> Appel du module d'analyse approprié                │
└─────────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────────┐
│  3. MODULE D'ANALYSE (gwr/mgwr/lisa_analysis.py)           │
│     └─> Création d'un répertoire temporaire                │
│     └─> Mapping des noms de champs (limite 10 caractères)  │
│     └─> Export de la couche en shapefile                   │
│     └─> Génération du script R                             │
└─────────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────────┐
│  4. EXÉCUTION R (subprocess)                                │
│     └─> Lecture du shapefile                               │
│     └─> Création d'une copie des données (sp_data_work)    │
│     └─> Transformations sur la copie uniquement            │
│     └─> Calculs statistiques                               │
│     └─> Création de result_sf à partir des données         │
│         originales non modifiées                            │
│     └─> Ajout des résultats à result_sf                    │
│     └─> Export du shapefile de résultats                   │
└─────────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────────┐
│  5. RETOUR À PYTHON                                         │
│     └─> Chargement du shapefile de résultats               │
│     └─> Création d'une QgsVectorLayer                      │
│     └─> Nettoyage des fichiers temporaires                 │
└─────────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────────┐
│  6. AFFICHAGE DANS QGIS (process_results)                  │
│     └─> Ajout de la nouvelle couche au projet              │
│     └─> La couche originale reste intacte                  │
│     └─> Affichage du message de succès                     │
│     └─> Affichage des résultats détaillés                  │
└─────────────────────────────────────────────────────────────┘

## Installation

Les Prérequis

QGIS (version 3.x)
R (version 4.0+)
Packages R requis :

Pour GWR/MGWR : GWmodel, sp, sf
Pour LISA : rgeoda, sf



## Installation des packages R

'''{r}
# Dans R ou RStudio
install.packages("GWmodel")
install.packages("sp")
install.packages("sf")
install.packages("rgeoda")
'''

## L'utilisation

### Workflow général

Charger votre couche vectorielle dans QGIS

Formats supportés : Shapefile, GeoPackage, etc.
Doit contenir des attributs numériques


### Lancer le plugin

Menu Analyse Spatiale → Analyse GWR / MGWR / LISA
Ou icône dans la barre d'outils


### Choisir le type d'analyse

GWR 
MGWR
LISA


### Configurer les paramètres

Sélectionner la couche
Choisir les variables
Ajuster les paramètres


### Lancer l'analyse

Cliquer sur "Lancer l'analyse"
Patienter (peut prendre plusieurs minutes)


### Consulter les résultats

Une nouvelle couche est créée automatiquement
Contient toutes les colonnes originales + les résultats
La couche d'origine reste intacte