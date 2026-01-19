def sensor_data_stream():
    """Simulate an infinite stream of sensor data."""
    import random
    while True:
        yield random.uniform(0, 100)  # Simulate sensor data

def sliding_window_average(stream, window_size):
    """ Calculate the average over a sliding window of readings."""
    window = []
    for value in stream:
        window.append(value)
        if len(window) > window_size:
            window.pop(0)
        if len(window) == window_size:
            yield sum(window) / window_size

# Generator pipeline
sensor_stream = sensor_data_stream()
averages = sliding_window_average(sensor_stream, window_size=10)

# Print the average every second
for avg in averages:
    print(f"Average temperature: {avg:.2f}")