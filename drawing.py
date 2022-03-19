import math, pygame, random, time
import import_number_system_converter as nsc

pygame.init()

width = 460
height = 460
rows = 20
cols = 20
row_height = height / rows
col_width = width / cols
black = (0, 0, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
pts = []
running = True
pmb1s = False # pmb1s ==> previous mouse button 1 state
done = 0

scrn = pygame.display.set_mode((width, height))
# bg = pygame.image.load('owl.jpg')

temp = []
for i in range(cols):
    temp.append(0)

for i in range(rows):
    pts.append(temp.copy())

dataset_file = open("datasets/shapes_ai_datasets/rect_pts.txt", 'r')
all_data = dataset_file.readlines() # = [POQQQ, SJZ0A, D7EJF]
for i in range(4, 5):
    temp_lst = []
    temp = nsc.convertNum(all_data[i][:-1], 36, 2)[2:] # nsc.convertNum(all_data[i][-1], 36, 2) = 101110001 (first character will be a "1", since the answer is "[1, 0]" and its length is 402)
    for j in temp:
        temp_lst.append(int(j))
dataset_file.close()

for i in range(rows):
    for j in range(cols):
        pts[i][j] = temp_lst[i * cols + j]
print(pts)

while running:
    scrn.fill(black)
    # scrn.blit(bg, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if pygame.key.name(event.key) == "s":
                temp = ""
                for i in pts:
                    for j in i:
                        temp += str(j)
                # temp = nsc.convertNum("10" + temp, 2, 36)
                # dataset_file = open("datasets/shapes_ai_datasets/rect_pts.txt", 'a')
                # dataset_file.write(temp + '\n')
                # dataset_file.close()
                temp = nsc.convertNum("1" + temp, 2, 36) # 01 = 1
                # dataset_file = open("datasets/shapes_ai_datasets/circ_pts.txt", 'a')
                # dataset_file.write(temp + '\n')
                # dataset_file.close()

                # dataset_file = open("datasets/shapes_ai_datasets/rect_pts.txt", 'a')
                # dataset_file.write(str([1, 0]) + str(pts) + '\n')
                # dataset_file.close()
                # temp = []
                # for i in pts:
                #     for j in i:
                #         temp.append(j)
                # print(temp)
                # check_length = open("datasets/shapes_ai_datasets/rect_pts.txt", 'r')
                # print(len(check_length.readlines()))
                # check_length.close()
                check_length = open("datasets/shapes_ai_datasets/circ_pts.txt", 'r')
                print(len(check_length.readlines()))
                check_length.close()
                # done += 1
                # print(done)
                for i in range(len(pts)):
                    for j in range(len(pts[i])):
                        pts[i][j] = 0

            if pygame.key.name(event.key) == "r":
                for i in range(len(pts)):
                    for j in range(len(pts[i])):
                        pts[i][j] = 0

    for i in range(rows):
        pygame.draw.line(scrn, white, (0, i * row_height), (width, i * row_height))
    for i in range(cols):
        pygame.draw.line(scrn, white, (i * col_width, 0), (i * col_width, height))

    if pygame.mouse.get_pressed()[0]:
        x = math.floor(pygame.mouse.get_pos()[0] / col_width)
        y = math.floor(pygame.mouse.get_pos()[1] / row_height)
        pts[y][x] = 1

    for i in range(len(pts)):
        for j in range(len(pts[i])):
            if pts[i][j] == 1:
                pygame.draw.rect(scrn, blue, pygame.Rect(j * col_width, i * row_height, col_width, row_height))

    pygame.display.update()

pygame.quit()