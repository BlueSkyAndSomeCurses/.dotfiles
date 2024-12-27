{ config, pkgs, inputs, ... }: {
  home.packages = with pkgs; [
          neovim
          mkalias
          tmux
          yazi
          kitty
          arc-browser
          nodejs_23
          neofetch
          python311
          nixfmt
          nixd
          #caskaydia-cove
  ];

}
