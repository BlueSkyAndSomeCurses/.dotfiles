#! /bin/bash

sudo cp pacman.conf /etc/ 

sudo pacman -S $(awk '{print $1}' pkglist.txt)

cp -r .local $HOME/
cp -r .config $HOME/

ln -s $HOME/.config/shell/profile $HOME/.zprofile
ln -s $HOME/.config/x11/xprofile $HOME/.xprofile

git clone --depth=1 https://github.com/AstroNvim/AstroNvim $HOME/.config/nvim
cp -r user/ $HOME/.config/nvim/lua/
git clone https://github.com/zsh-users/zsh-autosuggestions $HOME/.config/zsh/zsh-autosuggestions
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git $HOME/.config/zsh/zsh-syntax-highlighting
git clone https://aur.archlinux.org/yay.git $HOME/.local/yay
cd $HOME/.local/yay
makepkg -si
yay -Y --gendb
yay -Syu --devel

sudo chsh -s $(which zsh)

cat "install amd gpu drivers set tear free and background"


