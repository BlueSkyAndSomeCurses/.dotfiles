{ config, pkgs, inputs, system, ... }: {
  home.packages = with pkgs; [
    signal-desktop
    keepassxc
    kitty
    wget
    git
    nixd
    nixfmt-classic
    nodejs_23
    libgcc
    clang
    zip
    python311
    unzip
    grim
    slurp
    wl-clipboard
    swaynotificationcenter
    swww
    rofi-wayland
    sway
  ];

}
