
import h5py
import matplotlib.pyplot as plt
import numpy as np
import os

def read_actions_hand(file_path):
    with h5py.File(file_path, 'r') as f:
        actions_hand = f['actions_hand'][:]
    return actions_hand

def plot_and_save_actions_hand(folder_path, output_file):
    plt.figure(figsize=(10, 6))
    
    # List all .h5 files in the folder
    file_paths = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith('.h5')]
    for i in range(17):
        for file_path in file_paths:
            actions_hand = read_actions_hand(file_path)
            start_index = np.argmax(actions_hand[:, i] >= 0.8)

            plt.plot(actions_hand[start_index:,i], label=os.path.basename(file_path))
            # print(actions_hand[:,0])
        
        plt.xlabel('Time Step')
        plt.ylabel('Actions Hand')
        plt.title('Actions Hand Data from Multiple Files')
        # plt.legend()
        
        # Save the plot to a file
        plt.savefig(f'plots/{i}_{output_file}')
        plt.close()

# Folder path containing the .h5 files
folder_path = '/home/ubuntu/Data/Recordings_10_12'
# Output file path to save the plot
output_file = 'actions_hand_plot.png'

plot_and_save_actions_hand(folder_path, output_file)