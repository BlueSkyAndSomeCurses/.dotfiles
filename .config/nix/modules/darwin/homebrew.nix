{ pkgs, config, ... }:
{

  homebrew = {
    enable = true;

    brews = [
      "pango"
      "pkg-config"
      "scipy"
      "py3cairo"
      "ffmpeg"
    ];

    casks = [
      "wezterm"
      "sioyek"
      "mactex-no-gui"
      "visual-studio-code"
    ];

    masApps = { };

    onActivation.cleanup = "zap";
    onActivation.autoUpdate = true;
    onActivation.upgrade = true;
  };
}
