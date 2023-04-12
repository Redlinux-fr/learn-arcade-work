"""
La norme est de mettre des triples guillemets en debut de programme
pour expliquer ce que le code va faire .
"""

# apres on utilise le diese pour faire des commentaire ponctuel

import arcade

print("chapitre 5")

# definie les dimensions de la fenetre
arcade.open_window(600, 600, "Fenetre Arcade")




# on definie la couleur d'arriere plan ( les trois code couleur RVB )
arcade.set_background_color(arcade.csscolor.WHITE)

# dit a python.arcade qu'on commencer a dessiner / afficher quelque chose
arcade.start_render()

# on indique le code pour dessiner ici
arcade.draw_lrtb_rectangle_filled(0, 100, 100, 0, arcade.csscolor.BLACK)
arcade.draw_lrtb_rectangle_filled(101, 200, 200, 101, arcade.csscolor.BLACK)



#  dit a python.arcade qu'on a finit de dessiner
arcade.finish_render()

arcade.run()
