import subprocess
import pygame

pygame.init()
screen = pygame.display.set_mode((150,40))


def ping():
    # Option for the number of packets as a function of
    param = '-n'

    # Building the command. Ex: "ping -c 1 google.com"
    command = ['ping', param, '1', 'www.google.com']

    return subprocess.call(command) == 0


running = True
while running:
    if ping():
        screen.fill((0, 255, 0))
    else:
        screen.fill((255, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()