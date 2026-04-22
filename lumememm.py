import pygame
import sys

pygame.init()
aken = pygame.display.set_mode((300, 300))
pygame.display.set_caption("Lumememm – Lisett Liplap")

VALGE = (255,255,255)
MUST = (0,0,0)
ORANZ = (255,150,0)
SININE = (150,200,255)
PRUUN = (120,70,20)
KOLLANE = (255,255,0)
PUNANE = (255,0,0)
ROHELINE = (0,255,0)
HALL = (120,120,120)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    aken.fill(SININE)

    pygame.draw.circle(aken, KOLLANE, (260,40), 20)
    for i in range(8):
        pygame.draw.line(aken, KOLLANE, (260,40),
                         (260 + i*5 -20, 10), 2)

    pygame.draw.circle(aken, VALGE, (50,40), 15)
    pygame.draw.circle(aken, VALGE, (65,40), 15)
    pygame.draw.circle(aken, VALGE, (80,40), 15)
    pygame.draw.circle(aken, VALGE, (120,60), 15)
    pygame.draw.circle(aken, VALGE, (135,60), 15)
    pygame.draw.circle(aken, VALGE, (150,60), 15)
    pygame.draw.circle(aken, VALGE, (200,70), 15)
    pygame.draw.circle(aken, VALGE, (215,70), 15)
    pygame.draw.circle(aken, VALGE, (230,70), 15)

    pygame.draw.circle(aken, VALGE, (150,210), 50)
    pygame.draw.circle(aken, VALGE, (150,140), 40)
    pygame.draw.circle(aken, VALGE, (150,80), 30)

    pygame.draw.circle(aken, MUST, (140,75), 3)
    pygame.draw.circle(aken, MUST, (160,75), 3)

    pygame.draw.polygon(aken, ORANZ,
        [(150,80),(150,85),(170,82)])

    pygame.draw.circle(aken, MUST, (150,140), 4)
    pygame.draw.circle(aken, MUST, (150,160), 4)
    pygame.draw.circle(aken, MUST, (150,180), 4)

    pygame.draw.line(aken, PRUUN, (110,140),(70,120),4)
    pygame.draw.line(aken, PRUUN, (190,140),(230,120),4)

    pygame.draw.line(aken, PRUUN, (230,120),(250,90),4)
    pygame.draw.rect(aken, MUST, (245,80,10,10))

    pygame.draw.rect(aken, MUST, (130,40,40,10))
    pygame.draw.rect(aken, MUST, (140,10,20,30))

    pygame.draw.polygon(aken, SININE,
        [(20,260),(60,260),(40,245)])

    pygame.draw.polygon(aken, MUST,
        [(22,255),(58,255),(40,238)])

    pygame.draw.polygon(aken, VALGE,
        [(25,250),(55,250),(40,235)])

    pygame.draw.rect(aken, HALL,(35,120,10,120))

    pygame.draw.rect(aken, MUST,(20,40,40,80))

    pygame.draw.circle(aken,PUNANE,(40,55),10)
    pygame.draw.circle(aken,KOLLANE,(40,75),10)
    pygame.draw.circle(aken,ROHELINE,(40,95),10)

    pygame.display.flip()