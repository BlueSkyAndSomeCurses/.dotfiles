#! /bin/bash

sudo cp pacman.conf /etc/ 

#sudo pacman -S $(awk '{print $1}' pkglist.txt)
sudo pacman -S --needed - < pkglist.txt

sudo cp -r .local $HOME/
sudo cp -r .config $HOME/

ln -s $HOME/.config/shell/profile $HOME/.zprofile
ln -s $HOME/.config/x11/xprofile $HOME/.xprofile

git clone --depth=1 https://github.com/AstroNvim/AstroNvim $HOME/.config/nvim
cp -r user/ $HOME/.config/nvim/lua/
git clone https://github.com/zsh-users/zsh-autosuggestions $HOME/.config/zsh/zsh-autosuggestions
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git $HOME/.config/zsh/zsh-syntax-highlighting

git clone https://github.com/BlueSkyAndSomeCurses/dwm.git $HOME/.local/src/dwm
git clone https://github.com/BlueSkyAndSomeCurses/dwmblocks.git $HOME/.local/src/dwmblocks
git clone https://github.com/BlueSkyAndSomeCurses/st.git $HOME/.local/src/st
git clone https://github.com/BlueSkyAndSomeCurses/dmenu.git $HOME/.local/src/dmenu

cd $HOME/.local/src/dwm
sudo make clean install

cd $HOME/.local/src/dwmblocks
sudo make clean install

cd $HOME/.local/src/st
sudo make clean install

cd $HOME/.local/src/dmenu
sudo make clean install

git clone https://aur.archlinux.org/yay.git $HOME/.local/yay
cd $HOME/.local/yay
makepkg -si
yay -Y --gendb
yay -Syu --devel

sudo chsh -s $(which zsh)

./.local/bin/shortcuts 

cat "install amd gpu drivers set tear free and background"


