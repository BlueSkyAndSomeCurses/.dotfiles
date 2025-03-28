{
  config,
  pkgs,
  inputs,
  system,
  ...
}:
{
  home.packages = with pkgs; [
    neofetch
    neovim
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
    signal-desktop
    wezterm
    sioyek
    luarocks
    lua
    wget
    rustup
    ripgrep
    fd
  ];
}
