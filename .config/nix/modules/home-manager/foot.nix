{ config, pkgs, lib, ... }: {
  programs.foot = {
    enable = true;
    settings = { main = { font = "monospace"; }; };
  };
  programs.firefox.enable = true;
}
