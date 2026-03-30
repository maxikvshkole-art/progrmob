import pygame as pg

pg.init()

font = pg.font.SysFont(None, 74)

screen = pg.display.set_mode((800, 200))
prog = 200
count = 0

while True:
    screen.fill((0, 0, 0))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            import sys

            sys.exit()
        if event.type == pg.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            if mouse_x < 400:
                prog -= 10
            else:
                prog += 10
    prog -= 0.005
    if prog <= 0 or prog > 620:
        import sys
        from time import sleep
        text = font.render(f"count:{int(count)}", True, (255, 0, 0))
        screen.fill((0, 0, 0))
        screen.blit(text, (0, 0))
        pg.display.flip()
        sleep(5)
        pg.quit()
        sys.exit()
    if prog > 600:
        count += 0.001
    pg.draw.rect(screen, (255, 0, 0), (0, 0, prog, 200))
    pg.draw.line(screen, (0, 255, 0), [600, 0], [600, 200], 1)
    pg.draw.line(screen, (0, 255, 0), [620, 0], [620, 200], 1)
    pg.display.flip()