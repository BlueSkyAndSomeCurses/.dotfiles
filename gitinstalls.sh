#! /bin/bash

sudo pacman -Syu
sudo cp pacman.conf /etc/

sudo pacman -S $(awk '{print $1}' pkglist.txt)

cp -r .local $HOME/
cp -r .config $HOME/
cp .ideavimrc $HOME/
mkdir $HOME/.local/src
mkdir $HOME/.local/share/icons

ln -s $HOME/.config/shell/profile $HOME/.zprofile
ln -s $HOME/.config/x11/xprofile $HOME/.xprofile

git clone https://github.com/zsh-users/zsh-autosuggestions $HOME/.config/zsh/zsh-autosuggestions
git clone https://github.com/zdharma-continuum/fast-syntax-highlighting.git $HOME/.config/zsh/fast-syntax-highlighting
git clone https://github.com/zsh-users/zsh-completions.git $HOME/.config/zsh/zsh-completions

git clone https://github.com/BlueSkyAndSomeCurses/dwm.git $HOME/.local/src/dwm --depth=1
git clone https://github.com/BlueSkyAndSomeCurses/dwmblocks.git $HOME/.local/src/dwmblocks --depth=1
git clone https://github.com/BlueSkyAndSomeCurses/st.git $HOME/.local/src/st --depth=1
git clone https://github.com/BlueSkyAndSomeCurses/dmenu.git $HOME/.local/src/dmenu --depth=1

cd $HOME/.local/src/dwm
sudo make install

cd $HOME/.local/src/dwmblocks
sudo make install

cd $HOME/.local/src/st
sudo make install

cd $HOME/.local/src/dmenu
sudo make install

curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh

git clone https://aur.archlinux.org/paru.git $HOME/.local/src/paru
cd $HOME/.local/src/paru
makepkg -si
paru -Y --gendb
paru -Syu --devel

chsh -s $(which zsh)

. $HOME/.local/bin/shortcuts

sudo systemctl enable bluetooth.service
sudo systemctl start bluetooth.service

paru -S $(awk '{print $1}' foreignpkglist.txt)

cd $HOME/.local/src
git clone https://github.com/vinceliuice/WhiteSur-icon-theme --depth=1
./WhiteSur-icon-theme/install -t default -a -b

git clone https://github.com/vinceliuice/WhiteSur-cursors --depth=1
./WhiteSur-cursors/install

git clone https://github.com/vinceliuice/WhiteSur-gtk-theme.git --depth=1
./WhiteSur-gtk-theme/install.sh -c Dark -t default -m -l -HD

systemctl --user enable --now pipewire.socket
systemctl --user enable --now pipewire.service

sudo mkdir -p /etc/sysctl.d
sudo echo "kernel.dmesg_restrict = 0" >>/etc/sysctl.d/dmesg.conf

echo "install amd gpu drivers set tear free and background"
