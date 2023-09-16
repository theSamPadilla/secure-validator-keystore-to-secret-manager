""" Utility functions for web3signer """

import os

def read_bashrc():
    """
    Checks .bashrc for lines of type 'export PATH=$PATH:<new-path>',
    then updates the os.environ['PATH'] with all the <new-path> entries found in .bashrc
    """
    # Specify the path to the .bashrc file
    bashrc_path = os.path.expanduser('~/.bashrc')

    # Initialize a list to store new paths
    new_paths = []

    try:
        # Open and read the .bashrc file
        with open(bashrc_path, 'r', encoding="utf-8") as file:
            for line in file:
                # Check if the line starts with 'export PATH=$PATH:'
                if line.startswith('export PATH=$PATH:'):
                    # Extract the <new-path> part
                    new_path = line.split('export PATH=$PATH:', 1)[1].strip()
                    new_paths.append(new_path)

        if new_paths:
            # Get the current PATH
            current_path = os.environ.get('PATH', '')

            # Append the new paths to the PATH with the appropriate separator (':' on Linux)
            updated_path = ':'.join([current_path] + new_paths)

            # Update the PATH environment variable
            os.environ['PATH'] = updated_path

            return True  # Successfully updated PATH
        else:
            return False  # No new paths found in .bashrc

    except FileNotFoundError:
        return False  # .bashrc file not found
    