#Projet VideoTracker

Le logiciel dans l’archive est un projet dans le cadre de l’UE Développement Logiciel en L1 Informatique durant l’année 2022/2023. Il a pour objectif de proposer un système de pointage vidéo permettant de suivre un objet durant son déplacement pour, par exemple, réaliser des mesures physiques.

Les seuls élèves ayant participé à la construction, au développement et au maintien de ce logiciel ainsi que du GitLab correspondant sont Léonard BETTCHER et Nathan DOÏMO

#Fonctionnalités spéciales :
- Mode édition : afin de commencer le pointage d’un objet, il faut d’abord activer le mode édition disponible dans Edit/Mode édition. Vous pourrez ainsi placer les points où vous voulez quand vous voulez. Ce mode est désactivé lorsque vous appuyez sur échap où lorsque vous arrivez à la dernière image (en avançant une par une).
- Effacer les points : Il est possible d’effacer les points crées par l’utilisateur, pour ceci il suffit de sélectionner l’option « Effacer les points » dans le menu Edit. L’opération peut se faire lorsque l’utilisateur revient au début d’une vidéo selon son choix et est automatiquement faite lors du chargement d’une autre vidéo.


#Fiche technique :
Le logiciel présent réponds à tous les critères obligatoires et facultatifs du cahier des charges.
L’éxécutable est atteignable en src/Application.py
Une vidéo de test est disponible en resources/videos/compteur.mp4
Le GitLab est dispobile à l’addresse suivante : https://gitlab.emi.u-bordeaux.fr/ndoimo/videotracker_b1.git
Le GitLab à été maintenu jusqu’à la date du rendu final, correspondant à la version 0.1.3 du projet.

Les librairies nécessaires sont :
Pillow==9.4.0
matplotlib==3.3.4
numpy==1.19.5
tkinter==8.6
cv2==4 .5.1
testé avec Python 3.9.2 sur Debian GNU/Linux 11 64 bits et Windows 10 64 bits
