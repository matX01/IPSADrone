## Mathieu CUISSARD, 05/12/2023

import IPSADrone
from IPSADrone import translation
from IPSADrone import rotation
from IPSADrone import change_altitude


def Sequence():
    # ===== ECRIRE EN DESSOUS =====

    # ========================
    # === LES TRANSLATIONS ===
    # ========================

    # Pour déplacer le drone vers l'avant
    # RELATIF A L'ORIENTATION DU DRONE

    translation("AVANT", 100)  # déplacement vers l'avant de 100cm

    # Pour déplacer le drone vers la gauche
    # RELATIF A L'ORIENTAION DU DRONE

    translation("GAUCHE", 100)  # déplacement vers la gauche de 100cm

    # Pour déplacer le drone vers la droite
    # RELATIF A L'ORIENTAION DU DRONE

    translation("DROITE", 100)  # déplacement vers la droite de 100cm

    # Pour déplacer le drone vers l'arrière
    # RELATIF A L'ORIENTAION DU DRONE

    translation("ARRIERE", 100)  # déplacement vers l'arrière de 100cm

    # ========================
    # ==== LES  ROTATIONS ====
    # ========================

    rotation(45)  # Rotation de 45° dans le sens trigonométrique (anti horaire)
    rotation(-45)  # Rotation de 45° dans le sens horaire

    # ========================
    # ====== LA HAUTEUR ======
    # ========================

    change_altitude(10)  # va à 10cm du sol

    # ===== ECRIRE AU DESSUS =====
    pass


IPSADrone.DroneMovementSequence(Sequence)
