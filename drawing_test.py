from manim import *
import pygame

pygame.init()

width = 1200
height = 1200
running = True

scrn = pygame.display.set_mode((width, height))
img = pygame.image.load("C:/Users/CSC/Desktop/test_img_2.png", 'r')

scrn.fill(BLACK)
scrn.blit(img, (0, 0))
lst = []

txt_file = open("C:/Users/CSC/Desktop/CS/python_files/outlined_data_2.txt", 'r')
for i in range(1000):
    temp = txt_file.readline().split(" ")
    lst.append((int(temp[0]), int(temp[1][:-1])))
    # print((int(temp[0]), int(temp[1][:-1])))
txt_file.close()

# lst = [lst[x] for x in range(len(lst)) if not(x % 50)]
# print(lst)

for i in lst:
    scrn.set_at(i, PURE_RED)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

pygame.quit()