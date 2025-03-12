{
  config,
  pkgs,
  inputs,
  lib,
  ...
}:
let
  user = "vitya";
in
{
  # Home Manager needs a bit of information about you and the paths it should
  # manage.

  imports = [
    # Include the results of the hardware scan.
    ../../modules/home-manager/packages_darwin.nix
    ../../modules/home-manager/zsh/default.nix
    ../../modules/home-manager/fzf.nix
  ];

  home = {
    username = user;
    homeDirectory = lib.mkForce "/Users/vitya";
    stateVersion = "24.11";
  };
}
