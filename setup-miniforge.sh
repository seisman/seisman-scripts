#!/usr/bin/env bash
#
# Install miniforge and Python packages
#
# Reference: 
# - https://docs.anaconda.com/anaconda/install/silent-mode/
# - https://github.com/conda-forge/miniforge

# location to install miniforge
installdir=${HOME}/opt/miniforge
# mirror to download miniconda 
MIRROR=https://mirrors.tuna.tsinghua.edu.cn/github-release/conda-forge/miniforge/LatestRelease/
# the shell name: zsh, bash or csh
shell=$(basename ${SHELL})

# the miniconda installer
if [[ $(uname) == "Linux" ]]; then
	installer=Miniforge3-Linux-x86_64.sh
elif [[ $(uname) == "Darwin" ]]; then
	installer=Miniforge3-MacOSX-x86_64.sh
fi

# Download miniforge installer
wget -c ${MIRROR}/${installer} -O ${installer}

# Install miniforge
bash ${installer} -b -p ${installdir}

# Activate miniforge in current shell
eval "$(${installdir}/bin/conda shell.${shell} hook)"

# Initialize miniforge (run this if this is the first time you install miniforge)
conda init ${shell}

# Configure miniforge, changing the ~/.condarc file
conda config --set show_channel_urls true   # Show channel URLs
conda config --set channel_priority strict  # Set strict channel priority

# Use the Tsinghua mirror for the conda-forge channel (main channel not needed for miniforge)
conda config --set 'custom_channels.conda-forge' https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud