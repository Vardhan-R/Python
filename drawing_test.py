from manim import *
import math, pygame

pygame.init()

test_img_no = 6
img = pygame.image.load(f"C:/Users/CSC/Desktop/CS/outlining_test_images/test_img_{test_img_no}.png", 'r')
width = img.get_width()
height = img.get_height()
running = True

scrn = pygame.display.set_mode((width, height))
scrn.fill(BLACK)
scrn.blit(img, (0, 0))

txt_file = open(f"C:/Users/CSC/Desktop/CS/python_files/outlined_data_{test_img_no}.txt", 'r')
lst = txt_file.readlines()
txt_file.close()
for i in range(len(lst)):
    temp = lst[i].split(" ")
    lst[i] = (int(temp[0]), int(temp[1][:-1]))

# lst = [lst[math.floor(x) - 1] for x in np.linspace(0, len(lst))]
# print(lst)

for i in lst:
    scrn.set_at(i, PURE_RED)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

pygame.quit()
