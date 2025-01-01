{ config, pkgs, inputs, ... }:

{
  # Home Manager needs a bit of information about you and the paths it should
  # manage.

  imports = [ # Include the results of the hardware scan.
    ../../modules/home-manager/packages_x86.nix
    ../../modules/home-manager/foot.nix
    ../../modules/home-manager/sway.nix
    ../../modules/home-manager/zsh/default.nix
    ../../modules/home-manager/resolution/virtual.nix
  ];

  home = {
    username = "vitya";
    homeDirectory = "/home/vitya";
    stateVersion = "24.11"; # Please read the comment before changing.
    file = {
      # # Building this configuration will create a copy of 'dotfiles/screenrc' in
      # # the Nix store. Activating the configuration will then make '~/.screenrc' a
      # # symlink to the Nix store copy.
      # ".screenrc".source = dotfiles/screenrc;

      # # You can also set the file content immediately.
      # ".gradle/gradle.properties".text = ''
      #   org.gradle.console=verbose
      #   org.gradle.daemon.idletimeout=3600000
      # '';
    };

  };

  # Let Home Manager install and manage itself.
  programs.home-manager.enable = true;

}
