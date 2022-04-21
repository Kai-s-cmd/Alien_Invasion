import pygame


class Music:
    """Initialize music."""
    def sound_play_button(self):
        """Sound for Yes, Indeed button."""
        pygame.mixer.init()
        pygame.mixer.music.load("sounds/Yes, indeed.wav")
        pygame.mixer.music.play()

    def main_theme(self):
        """Sound for main theme. """
        pygame.mixer.init()
        main_music = pygame.mixer.Sound("sounds/main.wav")
        main_music.set_volume(0.6)
        main_music.play(loops= -1)

    def casual(self):
        """Sound in casual mode."""
        pygame.mixer.init()
        casual = pygame.mixer.Sound("sounds/action.wav")
        casual.set_volume(0.7)
        casual.play(loops= -1)

    def action(self):
        """Sound in battle."""
        pygame.mixer.init()
        action = pygame.mixer.Sound("sounds/action.wav")
        action.set_volume(0.8)
        action.play(loops= -1)

    def laser(self):
        """Sound for laser"""
        pygame.mixer.init()
        laser = pygame.mixer.Sound("sounds/laser.wav")
        laser.set_volume(1)
        laser.play()

    def explode(self):
        """Sound when alien die."""
        pygame.mixer.init()
        ex = pygame.mixer.Sound("sounds/explode.wav")
        ex.set_volume(0.3)
        ex.play()

    def stop(self):
        """Stop all sounds."""
        pygame.mixer.init()
        pygame.mixer.stop()

