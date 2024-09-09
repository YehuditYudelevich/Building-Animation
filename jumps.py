import pygame
import sys

pygame.init()
size = width, height = 1100, 750
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Building Animation")
# Colors
colors = {
    'black': (0, 0, 0),
    'white': (255, 255, 245),
    'red': (255, 0, 0),
    'green': (0, 255, 0),
    'blue': (0, 0, 255),
    'yellow': (255, 255, 0),
    'light_pink': (0, 255, 0)
}

def create_building(floors, window):
    pygame.draw.rect(screen, colors['light_pink'], (500, 90, 400, 220),5,border_radius=10)
    font = pygame.font.Font(None, 36)
    text = font.render("The code for the problem:", True, colors['black'])
    screen.blit(text, (512, 50))
    font = pygame.font.Font(None, 25)
    # Draw code
    code_lines=[
        "def Jumps1(h, bounce, window):",
        "    sum=0",
        "    current_height = h",
        "    while current_height>window:",
        "        sum+=1",
        "        if current_height*bounce>window:",
        "            sum+=1",
        "        current_height*=bounce",
        "    return sum"
    ]
    for i, line in enumerate(code_lines):
        text = font.render(line, True, colors['black'])
        screen.blit(text, (512, 100 + i * 20))
    pygame.draw.rect(screen, colors['light_pink'], (500, 380, 500, 100),5,border_radius=10)
    font = pygame.font.Font(None, 36)
    text = font.render("The second code for the problem:", True, colors['black'])
    screen.blit(text, (512, 340))
    font = pygame.font.Font(None, 25)
    code_lines1=[
        "def Jumps2(h, bounce, window):",
        "    count=2*int(math.log(window/h)/math.log(bounce))+1",
        "    return count"
    ]
    
    for i, line in enumerate(code_lines1):
        text = font.render(line, True, colors['black'])
        screen.blit(text, (512, 400 + i * 20))
   
    building_x, building_y = 100, 150
    floor_x, floor_y = 120, 160
    floor_width = (600 / floors) - 10
    # Draw building
    pygame.draw.rect(screen, colors['black'], (building_x, building_y, 250, 600), 5)
    #draw the floors
    for i in range(floors, 0, -1):
        if i == window:
            pygame.draw.rect(screen, colors['yellow'], (floor_x, floor_y, 200, floor_width))
        pygame.draw.rect(screen, colors['black'], (floor_x, floor_y, 200, floor_width), 2)
        
        font = pygame.font.Font(None, 22)
        text = font.render(f" {i}", True, colors['black'])
        screen.blit(text, (floor_x + 10, floor_y + 10))
        
        floor_y += floor_width + 10

def create_boy():
    #draw the boy
    x, y = 340, 70
    pygame.draw.circle(screen, colors['black'], (x, y), 12)
    pygame.draw.line(screen, colors['black'], (x, y), (x, y + 25), 2)
    pygame.draw.line(screen, colors['black'], (x, y + 25), (x - 10, y + 40), 2)
    pygame.draw.line(screen, colors['black'], (x, y + 25), (x + 10, y + 40), 2)
    pygame.draw.line(screen, colors['black'], (x, y + 25), (x, y + 60), 2)
    pygame.draw.line(screen, colors['black'], (x, y + 55), (x - 10, y + 80), 2)
    pygame.draw.line(screen, colors['black'], (x, y + 55), (x + 10, y + 80), 2)

def move_ball(floors, target_window, bounce):
    # Move the ball
    ball_x, ball_y = 368, 150  
    current_floor = floors
    speed = 5
    going_down = True
    bounces = 0
    
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 36)
    # Main loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        screen.fill(colors['white'])
        create_building(floors, target_window)
        create_boy()
        
        bounce_text = font.render(f"The bounce is {bounce}", True, colors['black'])
        screen.blit(bounce_text, (50, 50))
        pygame.draw.rect(screen, colors["yellow"], (500, 500, 400, 100) ,border_radius=10)
        pygame.draw.rect(screen, colors["light_pink"], (500, 500, 400, 100),5, border_radius=10)
        # move the ball
        if current_floor > target_window:
            if going_down:
                ball_y += speed
                if ball_y >= 750:  
                    going_down = False
                    bounces += 1
                    current_floor /= 1/bounce
            else:
                ball_y -= speed
                if ball_y <= 750 - (current_floor * (600 / floors)):  
                    going_down = True
                    bounces += 1
        
            pygame.draw.circle(screen, colors['green'], (int(ball_x), int(ball_y)), 12)
        else:
            # Ball has reached the target window
            pygame.draw.circle(screen, colors['green'], (368, 750 - (target_window * (600 / floors))), 12)
            pygame.draw.rect(screen, colors['yellow'], (120, 750 - (target_window * (600 / floors))+20, 200, 600 / floors +30), 2)
        
        bounces_text = font.render(f" We pass the window {bounces} times", True, colors['black'])
        screen.blit(bounces_text, (500, 530))

        pygame.display.flip()
        
        clock.tick(60)
        
        if current_floor <= target_window:
            pygame.time.wait(1000)
            return bounces

def main():
    floors = 15
    target_window = 3
    bounce = 0.7
    bounces = move_ball(floors, target_window, bounce)
    print(f"Total bounces: {bounces}")
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        screen.fill(colors['white'])
        create_building(floors, target_window)
        create_boy()
        pygame.draw.circle(screen, colors['green'], (368, 750 - (target_window * (600 / floors))), 12)
        
        pygame.draw.rect(screen,colors["yellow"],(500,500,550,100),border_radius=10)
        pygame.draw.rect(screen,colors["light_pink"],(500,500,550,100),5,border_radius=10)
        font=pygame.font.Font(None, 36)
        text=font.render(f"We performed {bounces} passes on the {target_window} window ", True, colors['black'])
        screen.blit(text, (510, 510))
        pygame.display.flip()

if __name__ == "__main__":
    main()