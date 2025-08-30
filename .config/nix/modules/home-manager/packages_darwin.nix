{
  config,
  pkgs,
  inputs,
  ...
}:
{
  home.packages = with pkgs; [
    neovim
    mkalias
    tmux
    yazi
    prettierd
    # neofetch
    python312
    nixfmt-rfc-style
    nixd
    luarocks
    lua
    wget
    rustup
    ripgrep
    fd
    cmake
    boost
    ninja
    nodejs
  ];

}
