# In this project I  will optimize the brightness of an LED while minimizing power consumption. This code will simulate the LED and use Python to automate the test, collect data, and find the optimal parameters.



import numpy as np
import itertools
import matplotlib.pyplot as plt

def simulate_led(brightness, current):
    """
    Simulate the LED brightness and power consumption.
    
    Parameters:
    brightness (int): Desired brightness level (0 to 100)
    current (float): Current supplied to the LED (0 to 20 mA)
    
    Returns:
    tuple: Actual brightness and power consumption
    """
    actual_brightness = brightness *(current / 20.0)
    power_consumption = current * 3.3  # 3.3V power supply
    return actual_brightness, power_consumption

def automated_test_fixture(brightness_levels, current_levels):
    results = []
    for brightness, current in itertools.product(brightness_levels, current_levels):
        actual_brightness, power_consumption = simulate_led(brightness, current)
        results.append((brightness, current, actual_brightness, power_consumption))
    return results

def find_optimal_parameters(results):
    best_params = None
    highest_efficiency = float('-inf')
    
    for brightness, current, actual_brightness, power_consumption in results:
        efficiency = actual_brightness / power_consumption
        if efficiency > highest_efficiency:
            highest_efficiency = efficiency
            best_params = (brightness, current)
    
    return best_params, highest_efficiency

def visualize_results(results):
    brightness_levels = [r[0] for r in results]
    current_levels = [r[1] for r in results]
    actual_brightness = [r[2] for r in results]
    power_consumption = [r[3] for r in results]
    
    plt.figure(figsize=(12, 6))
    
    plt.subplot(1, 2, 1)
    plt.scatter(brightness_levels, actual_brightness, c='blue', label='Brightness')
    plt.xlabel('Desired Brightness Level')
    plt.ylabel('Actual Brightness')
    plt.title('Brightness vs Desired Brightness Level')
    plt.legend()
    
    plt.subplot(1, 2, 2)
    plt.scatter(current_levels, power_consumption, c='red', label='Power Consumption')
    plt.xlabel('Current (mA)')
    plt.ylabel('Power Consumption (mW)')
    plt.title('Power Consumption vs Current')
    plt.legend()
    
    plt.tight_layout()
    plt.show()

def main():
    brightness_levels = range(0, 101, 10)  # Brightness levels from 0 to 100
    current_levels = np.linspace(0, 20, 5)  
    
    results = automated_test_fixture(brightness_levels, current_levels)
    best_params, highest_efficiency = find_optimal_parameters(results)
    
    print(f'Best Parameters: Brightness={best_params[0]}, Current={best_params[1]} mA')
    print(f'Highest Efficiency: {highest_efficiency}')
    
    visualize_results(results)

if __name__ == '__main__':
    main()
