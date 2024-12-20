import pygame
from pygame.locals import *


class Window:
    def __init__(self, size, cell_size=10, fps=30):
        pygame.init()
        self.framerate = fps
        self.size = size
        self.cell_size = cell_size
        self.window_width = 800
        self.window_height = 600
        self.screen = pygame.display.set_mode((self.window_width, self.window_height))
        pygame.display.set_caption("Game of Life Viewer")
        self.clock = pygame.time.Clock()
        self.running = True
        self.offset_x = 0
        self.offset_y = 0
        self.min_cell_size = 2  # Taille minimale pour éviter des bugs
        self.max_cell_size = 50  # Taille maximale pour éviter des zooms trop gros

    def draw_matrix(self, matrix):
        """Dessine la matrice reçue sur la fenêtre."""
        self.screen.fill((30, 30, 30))  # Fond gris
        for i, row in enumerate(matrix):
            for j, cell in enumerate(row):
                # Calcul des positions avec zoom et offset
                x = self.offset_x + j * self.cell_size
                y = self.offset_y + i * self.cell_size
                color = (255, 255, 255) if cell == 0 else (0, 0, 0)
                pygame.draw.rect(self.screen, color, (x, y, self.cell_size, self.cell_size))

        pygame.display.flip()

    def handle_zoom(self, event):
        """Gère le zoom avec la molette de la souris."""
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:  # Molette vers le haut (zoom in)
                self.cell_size = min(self.cell_size + 2, self.max_cell_size)
            elif event.button == 5:  # Molette vers le bas (zoom out)
                self.cell_size = max(self.cell_size - 2, self.min_cell_size)

    def update_window(self, matrix):
        """Met à jour la fenêtre avec la nouvelle matrice."""
        for event in pygame.event.get():
            if event.type == QUIT:
                self.running = False
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.running = False
                elif event.key == K_UP:
                    self.offset_y -= 20
                elif event.key == K_DOWN:
                    self.offset_y += 20
                elif event.key == K_LEFT:
                    self.offset_x -= 20
                elif event.key == K_RIGHT:
                    self.offset_x += 20
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.handle_zoom(event)

        # Dessine la matrice et limite la fréquence d'images
        self.draw_matrix(matrix)
        self.clock.tick(self.framerate)

    def is_running(self):
        """Retourne l'état de la fenêtre."""
        return self.running

    def close(self):
        """Ferme proprement la fenêtre."""
        pygame.quit()
