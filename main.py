## Mathieu CUISSARD, 05/12/2023

import IPSADrone
from IPSADrone import Translation
from IPSADrone import Rotation
from IPSADrone import Change_Altitude
from IPSADrone import Decoller
from IPSADrone import Atterir

def Sequence():

    Decoller()

    Translation("AVANT",100)
    Translation("ARRIERE", 100)
    Rotation(45)
    Translation("GAUCHE",100)
    Translation("DROITE",100)
    #Translation("GAUCHE",100)

    Atterir()


    
    # ===== ECRIRE EN DESSOUS =====

    # =============================
    # === DECOLLAGE/ATTERISSAGE ===
    # =============================

    Decoller()



    # ========================
    # === LES TRANSLATIONS ===
    # ========================

    # Pour déplacer le drone vers l'avant
    # RELATIF A L'ORIENTATION DU DRONE

    Translation("AVANT", 100)  # déplacement vers l'avant de 100cm

    # Pour déplacer le drone vers la gauche
    # RELATIF A L'ORIENTAION DU DRONE

    Translation("GAUCHE", 100)  # déplacement vers la gauche de 100cm

    # Pour déplacer le drone vers la droite
    # RELATIF A L'ORIENTAION DU DRONE

    Translation("DROITE", 100)  # déplacement vers la droite de 100cm

    # Pour déplacer le drone vers l'arrière
    # RELATIF A L'ORIENTAION DU DRONE

    Translation("ARRIERE", 100)  # déplacement vers l'arrière de 100cm

    # ========================
    # ==== LES  ROTATIONS ====
    # ========================

    Rotation(45)  # Rotation de 45° dans le sens trigonométrique (anti horaire)
    Rotation(-45)  # Rotation de 45° dans le sens horaire

    # ========================
    # ====== LA HAUTEUR ======
    # ========================

    Change_Altitude(10)  # va à 10cm du sol

    Atterir()

    # ===== ECRIRE AU DESSUS =====
    pass


IPSADrone.DroneMovementSequence(Sequence)

