import matplotlib.pyplot as plt
import pandas as pd
import os

def visualize_events(log_file):
    if not os.path.exists(log_file):
        print("Log file does not exist.")
        return

    data = pd.read_csv(log_file)
    if 'Timestamp' not in data.columns:
        print("Invalid log file format. 'Timestamp' column is missing.")
        return

    data['Timestamp'] = pd.to_datetime(data['Timestamp'])
    data.set_index('Timestamp', inplace=True)

    # Count events per minute
    event_counts = data.resample('1T').count()

    # Plot the data
    plt.figure(figsize=(10, 5))
    plt.plot(event_counts.index, event_counts['Event'], marker='o', linestyle='-', color='b', label='Events per minute')
    plt.xlabel("Time")
    plt.ylabel("Number of Events")
    plt.title("Event Logging Over Time")
    plt.legend()
    plt.grid()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Example usage
if __name__ == "__main__":
    visualize_events("C:\\Users\\Utkarsh Agarwal\\OneDrive - Lovely Professional University\\Desktop\\OS_project\\security_events.csv")
