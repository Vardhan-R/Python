import manim, math, pygame, random, time

pygame.init()

width = 1200
height = 400
running = True
# pts = [(297, 156), (303, 141), (311, 125), (318, 108), (325, 97), (333, 85), (341, 74), (350, 63), (360, 53), (371, 41), (382, 32), (395, 24), (408, 17), (419, 12), (434, 8), (452, 6), (469, 5), (484, 8), (499, 12), (511, 18), (524, 27), (535, 35), (545, 43), (553, 53), (560, 64), (566, 73), (572, 84), (577, 96), (581, 109), (585, 123), (588, 137), (590, 153), (591, 170), (591, 186), (590, 203), (588, 218), (586, 233), (582, 249), (579, 263), (575, 277), (570, 290), (565, 305), (560, 318), (554, 331), (548, 343), (541, 357), (534, 370), (527, 382), (520, 394), (513, 404), (505, 417), (495, 429), (485, 441), (476, 452), (465, 465), (453, 478), (442, 487), (433, 497), (423, 507), (409, 518), (397, 527), (386, 537), (374, 546), (363, 553), (353, 561), (342, 567), (329, 575), (319, 582), (308, 588), (298, 593), (287, 588), (273, 581), (261, 572), (249, 565), (235, 556), (221, 546), (208, 537), (195, 526), (183, 515), (171, 505), (161, 497), (151, 486), (141, 478), (131, 468), (122, 458), (114, 446), (104, 435), (93, 422), (84, 409), (76, 398), (67, 383), (59, 368), (50, 352), (42, 335), (35, 319), (28, 302), (22, 287), (17, 269), (13, 253), (8, 235), (6, 217), (5, 202), (3, 186), (3, 171), (4, 160), (5, 147), (7, 132), (10, 119), (13, 106), (17, 94), (24, 82), (30, 71), (37, 59), (46, 49), (55, 38), (66, 29), (79, 21), (91, 14), (104, 9), (120, 6), (135, 6), (150, 7), (163, 8), (176, 12), (188, 18), (199, 23), (212, 32), (222, 40), (230, 48), (239, 56), (247, 64), (254, 74), (263, 87), (270, 97), (276, 109), (284, 127), (291, 142)]
pts = []
# pmb1s = False
# bg = pygame.image.load('heart.png')

scrn = pygame.display.set_mode((width, height))

while running:
    scrn.fill(manim.BLACK)
    # scrn.blit(bg, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if event.type == pygame.KEYDOWN:
        #     if pygame.key.name(event.key) == "s":
        #         print(pts)
        #     if pygame.key.name(event.key) == "o":
        #         pts.pop(-1)
        #     if pygame.key.name(event.key) == "l":
        #         print(len(pts))

    if pygame.mouse.get_pressed()[0]:
        # if not(pmb1s):
            pts.append(pygame.mouse.get_pos())
            # pmb1s = True
    # else:
    #     pmb1s = False

    # for i in pts:
    #     pygame.draw.circle(scrn, manim.BLUE, i, 2)

    pygame.display.update()
    time.sleep(0.01)

pygame.quit()

print(len(pts))

# txt_file = open("python_files/signature.txt", 'w')
# for i in pts:
#     txt_file.write(f"{i[0]} {i[1]} \n")
# txt_file.close()

while len(pts) > 100:
    for i in range(len(pts) - 1, 0, -2):
        pts.pop(i)

print(pts)
print(len(pts))
