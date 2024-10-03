import pygame
import random
import sys
pygame.init()
W, H = 800, 600
C1 = (255, 255, 255)
C2 = (0, 0, 0)
C3 = (255, 0, 0)
C4 = (0, 255, 0)
C5 = (0, 0, 255)
FPS = 60
S = pygame.display.set_mode((W, H))
pygame.display.set_caption("Space Shooter")
def D1(c, x, y, w, h):
    pygame.draw.rect(S, c, [x, y, w, h])
def main():
    C = pygame.time.Clock()
    p_x, p_y = W // 2, H - 50
    p_s = 5
    b = []
    e = [{'x': random.randint(0, W - 50), 'y': random.randint(-150, -50)} for _ in range(5)]
    e_s = 3
    g_o = False
    r = True
    while r:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                r = False
        if not g_o:
            k = pygame.key.get_pressed()
            if k[pygame.K_LEFT]:
                p_x -= p_s
            if k[pygame.K_RIGHT]:
                p_x += p_s
            if k[pygame.K_SPACE]:
                if len(b) < 5:
                    b.append([p_x + 20, p_y])
            b = [[bx, by - 10] for bx, by in b if by > -20]
            for en in e:
                en['y'] += e_s
                if en['y'] > H:
                    en['y'] = random.randint(-150, -50)
                    en['x'] = random.randint(0, W - 50)
            for bu in b:
                b_r = pygame.Rect(bu[0], bu[1], 10, 20)
                for en in e:
                    e_r = pygame.Rect(en['x'], en['y'], 50, 30)
                    if b_r.colliderect(e_r):
                        b.remove(bu)
                        e.remove(en)
                        e.append({'x': random.randint(0, W - 50), 'y': random.randint(-150, -50)})
            p_r = pygame.Rect(p_x, p_y, 50, 30)
            for en in e:
                e_r = pygame.Rect(en['x'], en['y'], 50, 30)
                if p_r.colliderect(e_r):
                    g_o = True
        if g_o:
            print("GAME OVER")
            pygame.quit()
            sys.exit()
        S.fill(C2)
        if not g_o:
            D1(C4, p_x, p_y, 50, 30)
            for bu in b:
                D1(C5, bu[0], bu[1], 10, 20)
            for en in e:
                D1(C3, en['x'], en['y'], 50, 30)
        pygame.display.flip()
        C.tick(FPS)
    pygame.quit()
if __name__ == "__main__":
    main()