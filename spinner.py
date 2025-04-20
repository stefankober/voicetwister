import pygame
import pyttsx3
import random
import sys

pygame.init()

# Setup screen
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Voice Twister")

# Text-to-Speech setup
engine = pyttsx3.init()

# Define extremities and colors
extremities = ["Right hand", "Left hand", "Left foot", "Right foot"]
colors = ["Red", "Blue", "Green", "Yellow"]

# Set a timer event every 6 seconds
COMMAND_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(COMMAND_EVENT, 4000)

current_extremity_index = 0
command = ""
rounds = 1

def speak(text):
    engine.say(text)
    engine.runAndWait()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or \
           (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False

        if event.type == COMMAND_EVENT:
            # Cycle through extremities
            extremity = extremities[current_extremity_index % len(extremities)]
            current_extremity_index += 1

            # Randomly choose color
            color = random.choice(colors)

            # Prepare command
            command = f"{extremity} on {color}"
            
            # Speak the command
            speak(command)

            # Display command visually as backup
            screen.fill((0, 0, 0))
            font = pygame.font.SysFont(None, 48)
            text_surf = font.render(command+" - "+str(rounds), True, pygame.Color(color))
            rounds += 1
            rect = text_surf.get_rect(center=(200,150))
            screen.blit(text_surf, rect)
            pygame.display.flip()

pygame.quit()
sys.exit()
