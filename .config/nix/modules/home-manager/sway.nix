{ pkgs, lib, config, ... }: {
  home.packages = with pkgs; [
    grim
    slurp
    wl-clipboard
    swaynotificationcenter
    swww
    rofi-wayland
  ];
  wayland.windowManager.sway = {
    enable = true;
    wrapperFeatures.gtk = true; # Fixes common issues with GTK 3 apps
    config = rec {
      modifier = "Mod4";
      # Use kitty as default terminal
      terminal = "kitty";
      startup = [
        # Launch Firefox on start
        { command = "kitty"; }
      ];
    };
  };
  services.gnome-keyring.enable = true;
}
