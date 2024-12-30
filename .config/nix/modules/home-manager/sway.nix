{pkgs, ...} :
{
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
        {command = "foot";}
      ];

      colors = {
        background = "#000000";
      };

      window = {
        border = 0;
        titlebar = false;
      };

      focus = {
        followMouse = true;
        mouseWarping = true;
      };

      fonts = {
        names = [ "monospace" ];
        style = "Regular";
      };

      input = {
        "type:keyboard" = {
          xkb_layout = "ru,ua,us";
          xkb_options = "caps:escape,grp:alt_shift_toggle";
          
        };
      };

      defaultWorkspace = "1";

      menu = "${pkgs.rofi-wayland}/bin/rofi -show drun ";

    };
  };
}
