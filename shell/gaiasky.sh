#!/bin/bash
gaia-sky() {
# Function to install Gaia Sky
install_gaiasky() {
  # Install required packages for compilation
  sudo apt update
  sudo apt install -y git ant openjdk-8-jdk

  # Clone the Gaia Sky repository
  git clone https://codeberg.org/gaiasky/gaiasky.git

  # Compile the code
  cd gaiasky
  ant

  # Install the application
  sudo ant install

  # Remove unnecessary packages
  sudo apt remove -y git ant openjdk-8-jdk
  sudo apt autoremove -y
}

# Function to remove Gaia Sky
remove_gaiasky() {
  # Uninstall the application
  sudo ant uninstall

  # Remove any remaining files
  sudo rm -rf /usr/share/gaiasky
}

# Menu loop
while true; do
  # Print menu
  echo "Please select an option:"
  echo "1. Install Gaia Sky"
  echo "2. Remove Gaia Sky"
  echo "3. Exit"

  # Read user input
  read choice

  # Perform selected action
  case $choice in
    1)
      install_gaiasky
      ;;
    2)
      remove_gaiasky
      ;;
    3)
      exit 0
      ;;
    *)
      echo "Invalid choice. Please try again."
      ;;
  esac
done
}
gaia-sky
