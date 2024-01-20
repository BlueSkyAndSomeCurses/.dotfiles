#! /bin/bash

sudo pacman -Syu
sudo cp pacman.conf /etc/ 

sudo pacman -S $(awk '{print $1}' pkglist.txt)
# sudo pacman -S --needed - < pkglist.txt

cp -r .local $HOME/
cp -r .config $HOME/
mkdir $HOME/.local/src

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
sudo make install

cd $HOME/.local/src/dwmblocks
sudo make install

cd $HOME/.local/src/st
sudo make install

cd $HOME/.local/src/dmenu
sudo make install

git clone https://aur.archlinux.org/yay.git $HOME/.local/yay
cd $HOME/.local/yay
makepkg -si
yay -Y --gendb
yay -Syu --devel

chsh -s $(which zsh)

. $HOME/.local/bin/shortcuts 

sudo systemctl enable bluetooth.service
sudo systemctl start bluetooth.service

cd $HOME/.local/src
git clone https://github.com/DreamMaoMao/hycov.git
cd hycov
sudo meson setup build --prefix=/usr
sudo ninja -C build
sudo ninja -C build install # `libhycov.so` path: /usr/lib/libhycov.so

cd $HOME/.local/src
git clone https://github.com/vinceliuice/WhiteSur-icon-theme
./WhiteSur-icon-theme/install -t default -a -b

sudo mkdir -p /etc/sysctl.d
sudo echo "kernel.dmesg_restrict = 0" >> /etc/sysctl.d/dmesg.conf


echo "install amd gpu drivers set tear free and background"


