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
    systemd.enable = true;

    config = {
      modifier = "Mod4";
      terminal = "foot";
      startup = [
        { command = "foot"; }
        { command = "autotiling"; }
        { command = "swaync "; }
      ];

      colors = { background = "#000000"; };

      window = {
        border = 0;
        titlebar = false;
      };

      focus = {
        followMouse = true;
        mouseWarping = true;
      };

      # bars = [
      # {
      # colors = {
      #   inactiveWorkspace = {
      #     background = "#000000";
      #     border = "#ffffff";
      #     text = "#ffffff";
      #   };
      #   focusedWorkspace = {
      #     background = "#ffffff";
      #     border = "#ffffff";
      #     text = "#000000";
      #   };

      # };
      # position = "top";
      # }
      # ];

      fonts = {
        names = [ "monospace" ];
        style = "Regular";
      };

      input = {
        "type:keyboard" = {
          xkb_layout = "us,ru,ua";
          xkb_options = "caps:escape,grp:alt_shift_toggle";
        };
        "type:pointer" = { natural_scroll = "enabled"; };
      };

      defaultWorkspace = "1";

      menu = "${pkgs.rofi-wayland}/bin/rofi -show drun ";

      keybindings =
        let modifier = config.wayland.windowManager.sway.config.modifier;
        in lib.mkOptionDefault {
          "${modifier}+q" = "kill";
          "${modifier}+r" = "exec ${pkgs.foot}/bin/foot -e yazi";
          "${modifier}+w" = "exec firefox";
          "${modifier}+Tab" = "swaymsg workspace next";
        };

    };
  };
}
