{ config, pkgs, inputs, ... }:

{
  # Home Manager needs a bit of information about you and the paths it should
  # manage.

  imports = [
    # Include the results of the hardware scan.
    ../../modules/home-manager/packages_x86.nix
    ../../modules/home-manager/foot.nix
    ../../modules/home-manager/sway.nix
    ../../modules/home-manager/zsh/default.nix
    ../../modules/home-manager/resolution/virtual.nix
    ../../modules/home-manager/swaync.nix
    ../../modules/home-manager/ags.nix
  ];

  home = {
    username = "vitya";
    homeDirectory = "/home/vitya";
    stateVersion = "24.11";
    file = { };

  };

  # Let Home Manager install and manage itself.
  programs.home-manager.enable = true;

}
