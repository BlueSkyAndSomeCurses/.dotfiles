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
      "boost"
    ];

    casks = [
      "wezterm"
      "sioyek"
      "visual-studio-code"
    ];

    masApps = { };

    onActivation.cleanup = "zap";
    onActivation.autoUpdate = true;
    onActivation.upgrade = true;
  };
}
