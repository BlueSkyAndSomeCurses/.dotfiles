#! /bin/bash
git clone --depth=1 https://github.com/AstroNvim/AstroNvim $HOME/.config/nvim
mkdir -p "$HOME/.zsh"
git clone --depth=1 https://github.com/spaceship-prompt/spaceship-prompt.git "$HOME/.zsh/spaceship"
git clone https://github.com/zsh-users/zsh-autosuggestions $HOME/.zsh/zsh-autosuggestions
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git $HOME/.zsh/zsh-syntax-highlighting
git clone https://aur.archlinux.org/yay.git $HOME/yay
cd ~/yay
makepkg -si
yay -Y --gendb
yay -Syu --devel

mv $HOME/.dotfiles/.zshrc $HOME/
mv $HOME/.dotfiles/.xinitrc $HOME/
mv $HOME/.dotfiles/.xprofile $HOME/
mv $HOME/.dotfiles/.config/i3/config $HOME/.dotfiles/.config/i3/
ln -s $HOME/.zshrc $HOME/.dotfiles/.zshrc
ln -s $HOME/.xinitrc $HOME/.dotfiles/.xinitrc
ln -s $HOME/.xprofile $HOME/.dotfiles/.xprofile
ln -s $HOME/.config/i3/config $HOME/.dotfiles/.config/i3/config
