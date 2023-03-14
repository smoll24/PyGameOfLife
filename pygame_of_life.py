#SET UP ------------------------------------------------------------------------
import pygame
import random

# Set up the display
pygame.init()
screen = pygame.display.set_mode((500, 500)) 
pygame.display.set_caption("PyGame of Life")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
ORANGE = (255, 100, 10)
YELLOW = (255, 255, 0)
GRAY = (20, 20, 20)

# Create the 100x100 2D list of zeros
grid = [[0 for y in range(100)] for x in range(100)]
grid_colors = [[0 for y in range(100)] for x in range(100)]

#UI ------------------------------------------------------------------------

# Add a "Start" button
button_font = pygame.font.Font(None, 50//2)
start_button = button_font.render("Start", True, BLACK)
start_button_rect = start_button.get_rect(center=(200//2, 940//2))

# Add a "Stop" button
stop_button = button_font.render("Stop", True, BLACK)
stop_button_rect = stop_button.get_rect(center=(400//2, 940//2))

# Add a "Clear" button
clear_button = button_font.render("Clear", True, BLACK)
clear_button_rect = clear_button.get_rect(center=(600//2, 940//2))

# Add a "Random" button
rand_button = button_font.render("Random", True, BLACK)
rand_button_rect = rand_button.get_rect(center=(800//2, 940//2))

# Add counter for number of times the simulation has been run
stats_font = pygame.font.Font(None, 40//2)
counter = 0
counter_text = stats_font.render(f"Generation: {counter}00", True, WHITE)
counter_rect = counter_text.get_rect(center=(350//2, 50//2))

# Add text for state of simulation
simulating = False
state_text = stats_font.render(f"Simulating: {simulating}", True, WHITE)
state_rect = state_text.get_rect(center=(650//2, 50//2))

# Draw a 20x20 pixel border around the screen
border_color = BLACK
border_thickness = 40//2
screen_width = screen.get_width()
screen_height = screen.get_height()

#EVENT LOOP ------------------------------------------------------------------------

running = True
simulating = False  # Added variable to track simulation state

while running:
    
    for event in pygame.event.get():
        #To quit game
        if event.type == pygame.QUIT:
            running = False
            
        #If left mouse button clicked
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                #X and Y coordinates of the mouse
                x, y = event.pos
                #If pressing start button
                
                if start_button_rect.collidepoint(x, y):
                    simulating = True
                    state_text = stats_font.render(f"Simulating: {simulating}", True, WHITE)
                    
                #If pressing stop button
                elif stop_button_rect.collidepoint(x, y):
                    simulating = False
                    state_text = stats_font.render(f"Simulating: {simulating}", True, WHITE)
                    
                 #If pressing clear button
                elif clear_button_rect.collidepoint(x, y):
                    grid = [[0 for y in range(100)] for x in range(100)]
                    grid_colors = [[0 for y in range(100)] for x in range(100)]
                    simulating = False
                    counter = 0
                    counter_text = stats_font.render(f"Generation: {counter}", True, WHITE)
                    state_text = stats_font.render(f"Simulating: {simulating}", True, WHITE)
                    
                #If pressing random button
                elif rand_button_rect.collidepoint(x, y):
                    grid = [[random.randint(0,1) for y in range(100)] for x in range(100)]
                    grid_colors = [[0 for y in range(100)] for x in range(100)]
                    simulating = False
                    counter = 0
                    counter_text = stats_font.render(f"Generation: {counter}", True, WHITE)
                    state_text = stats_font.render(f"Simulating: {simulating}", True, WHITE)
                    for y in range(100):
                        for x in range(100):
                            if grid[y][x] == 1:
                                grid_colors[y][x] = 1
                    
                elif not simulating:
                    spot_x = x // 10
                    spot_y = y // 10
                    grid[spot_y][spot_x] = 1
                    grid_colors[spot_y][spot_x] = 1

    if simulating:
        # Create a copy of the grid to store the next generation
        new_grid = [[0 for y in range(100)] for x in range(100)]

        # Iterate over every spot in the grid
        for y in range(100):
            for x in range(100):
                # If the current spot is 1, set all adjacent spots to 1 in the new grid
#                 if grid[y][x] == 1:
#                     for j in range(y-1, y+2):
#                         for i in range(x-1, x+2):
#                             if 0 <= i < 100 and 0 <= j < 100:
#                                 new_grid[j][i] = 1
#                                 
                # Count the number of alive neighbors for the current cell
                alive_neighbors = 0
                for j in range(y-1, y+2):
                    for i in range(x-1, x+2):
                        if 0 <= i < 100 and 0 <= j < 100 and (i != x or j != y):
                            if grid[j][i] != 0:
                                alive_neighbors += 1

                # Apply the rules of Conway's Game of Life
                if grid[y][x] > 0:
                    if alive_neighbors < 2 or alive_neighbors > 3:
                        new_grid[y][x] = 0
                    else:
                        new_grid[y][x] = 1
                else:
                    if alive_neighbors == 3:
                        new_grid[y][x] = 1
                        
        # Update the grid with the new state
        grid = new_grid
        
        # Create a copy of the grid
        grid_colors = [[0 for y in range(100)] for x in range(100)]

        # Gets colors of grid
        # Iterate over every spot in the grid
        for y in range(100):
            for x in range(100):
                if grid[y][x] != 0:
                    # Count the number of alive neighbors for the current cell
                    alive_neighbors = 0
                    for j in range(y-1, y+2):
                        for i in range(x-1, x+2):
                            if 0 <= i < 100 and 0 <= j < 100 and (i != x or j != y):
                                if grid[j][i] != 0:
                                    alive_neighbors += 1

                    # Set the value of the spot in the grid to the number of alive neighbors
                    grid_colors[y][x] = alive_neighbors
        
        counter += 1
        
        # Update the counter display
        counter_text = stats_font.render(f"Generation: {counter}", True, WHITE)

        # Stop the simulation
        if all(all(row) for row in grid):
            simulating = False

    # Clear the screen
    screen.fill(BLACK)

    # Draw the grid
    for x in range(0, 1000, 10):  # Every 100 pixels horizontally
        pygame.draw.line(screen, GRAY, (x, 0), (x, 1000))
    for y in range(0, 1000, 10):  # Every 100 pixels vertically
        pygame.draw.line(screen, GRAY, (0, y), (1000, y))

    # Draw the colored spots
    for y in range(100):
        for x in range(100):
            if grid_colors[y][x] == 1:
                pygame.draw.rect(screen, YELLOW, pygame.Rect(x * 10, y * 10, 10, 10))
            if grid_colors[y][x] == 2:
                pygame.draw.rect(screen, ORANGE, pygame.Rect(x * 10, y * 10, 10, 10))
            if grid_colors[y][x] == 3:
                pygame.draw.rect(screen, ORANGE, pygame.Rect(x * 10, y * 10, 10, 10))
            if grid_colors[y][x] > 3:
                pygame.draw.rect(screen, RED, pygame.Rect(x * 10, y * 10, 10, 10))
                
    # Draw the buttons
    # Start button
    pygame.draw.rect(screen, WHITE, start_button_rect)
    screen.blit(start_button, start_button_rect)
    # Stop button
    pygame.draw.rect(screen, WHITE, stop_button_rect)
    screen.blit(stop_button, stop_button_rect)
    # Clear button
    pygame.draw.rect(screen, WHITE, clear_button_rect)
    screen.blit(clear_button, clear_button_rect)
    # Random button
    pygame.draw.rect(screen, WHITE, rand_button_rect)
    screen.blit(rand_button, rand_button_rect)
    
    # Draw the counter
    pygame.draw.rect(screen, BLACK, counter_rect)
    screen.blit(counter_text, counter_rect)
    
    # Draw the state box
    pygame.draw.rect(screen, BLACK, state_rect)
    screen.blit(state_text, state_rect)
    
    #Draw the borders
    # Top border
    pygame.draw.rect(screen, border_color, pygame.Rect(0, 0, screen_width, border_thickness))
    # Bottom border
    pygame.draw.rect(screen, border_color, pygame.Rect(0, screen_height - border_thickness, screen_width, border_thickness))
    # Left border
    pygame.draw.rect(screen, border_color, pygame.Rect(0, 0, border_thickness, screen_height))
    # Right border
    pygame.draw.rect(screen, border_color, pygame.Rect(screen_width - border_thickness, 0, border_thickness, screen_height))

    # Update the display
    pygame.display.flip()

# Quit
pygame.quit()
