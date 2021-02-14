#import pygame package after the installation
import pygame
from game import Game
from player import Player
pygame.init()






# generer la fenetre du jeu
pygame.display.set_caption("Zorai game")

#pour definir une image : 3 etapes : charger les assets,injecter l'image sur l'ecran, actualiser l'ecran
# definir largeur et haute de fenetre, recupere la surface sur une variable
screen = pygame.display.set_mode((1080,720))

background = pygame.image.load('assets/bg.jpg')


#charger le jeu
game = Game()

#charger notre joueur
player = Player()

running = True

# boucle tant que cette condition est vrai
while running:

    #appliquer l'arriere plan de notre jeu ( premier parametre largeur et 2 eme hauteur )
    screen.blit(background, (0,-200))

    #appliquer l'image de mon joueur
    screen.blit(game.player.image,game.player.rect)

    #mettre à jour l'écran
    pygame.display.flip()

    # si le joueur ferme cette fenetre
    for event in pygame.event.get():
        # que l'evenement est fermeture de fenetre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("fermeture du jeu")





    # This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
