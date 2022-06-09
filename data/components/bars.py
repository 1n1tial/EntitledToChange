import pygame

from data.SETTINGS import *

def draw_health_bar(surf, x, y, bar_length, bar_height, obj):
    pct = obj.health*100/obj.max_health
    if pct < 0:
        pct = 0
    if pct > 100:
        pct = 100

    fill = (pct / 100) * bar_height
    outline_rect = pygame.Rect(x, y, bar_length, bar_height)
    fill_rect = pygame.Rect(x, y, bar_length, fill)
    pygame.draw.rect(surf, WHITE, outline_rect, 2)
    if pct > 55:
        pygame.draw.rect(surf, GREEN, fill_rect)
    if 30 < pct <= 55:
        pygame.draw.rect(surf, (255*((55-pct)*0.04), 255, 0), fill_rect)
    if 0 < pct <= 30:
        pygame.draw.rect(surf, (255, 255*pct/30, 0), fill_rect)
    