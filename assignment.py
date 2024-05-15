import numpy as np
import matplotlib.pyplot as plt
import random

# Set grid size and number of time steps
GRID_SIZE = (20, 20)  # 20x20 grid for simplicity
TIME_STEPS = 10  # Simulate 10 time steps

# Initialize grid with green spaces and some initial urban areas
# 0 - Non-urban (green space), 1 - Urban
grid = np.zeros(GRID_SIZE)

# Define initial urban seed point
grid[10, 10] = 1  # Start with a single urban cell in the middle

# Define initial green spaces (random patches)
for _ in range(10):  # Add 10 green patches
    x, y = random.randint(0, 19), random.randint(0, 19)
    grid[x, y] = 2  # Green spaces marked as 2

# Define neighborhood structure (Moore neighborhood with 8 adjacent cells)
neighborhood_offsets = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1),         (0, 1),
    (1, -1), (1, 0), (1, 1),
]

# Define base transition probability
P_URBANIZE = 0.1  # Base probability for non-urban to become urban

# Function to count urban neighbors
def count_urban_neighbors(grid, x, y):
    count = 0
    for offset in neighborhood_offsets:
        nx, ny = x + offset[0], y + offset[1]
        if 0 <= nx < GRID_SIZE[0] and 0 <= ny < GRID_SIZE[1]:
            if grid[nx, ny] == 1:  # Count urban neighbors
                count += 1
    return count

# Simulate urban growth
def simulate_growth(grid, time_steps):
    results = [grid.copy()]  # Keep track of grid at each time step
    for _ in range(time_steps):
        new_grid = grid.copy()  # Create a new grid to update
        for x in range(GRID_SIZE[0]):
            for y in range(GRID_SIZE[1]):
                if grid[x, y] == 0:  # If the cell is non-urban (green space)
                    urban_neighbors = count_urban_neighbors(grid, x, y)
                    prob = P_URBANIZE  # Base probability of urbanization
                    if urban_neighbors > 0:  # Increase if there are urban neighbors
                        prob += 0.05 * urban_neighbors
                    if random.random() < prob:
                        new_grid[x, y] = 1  # Convert to urban
        results.append(new_grid)  # Save the updated grid
        grid = new_grid  # Update the grid for the next iteration
    return results

# Simulate and visualize results
growth_simulation = simulate_growth(grid, TIME_STEPS)

# Plotting the results to see urbanization and green spaces
for i, state in enumerate(growth_simulation):
    plt.imshow(state, cmap='viridis', vmin=0, vmax=2)  # Color map for better visualization
    plt.title(f'Time Step {i}')  # Title indicating the current time step
    plt.show()  # Show the plot
