{ config, pkgs, inputs, ... }: {
  home.packages = with pkgs; [
    signal-desktop
    keepassxc
    kitty
    wget
    git
    nixd
    nixfmt
    nodejs_23
    libgcc
    clang
    zip
    python311
    unzip
  ];

}
