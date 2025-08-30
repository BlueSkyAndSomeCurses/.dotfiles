{ pkgs, config, ... }:
{

  homebrew = {
    enable = true;

    brews = [
      "pkg-config"
      "ffmpeg"
      "boost"
      "boost-mpi"
      "octave"
      "python@3.10"
      "gobject-introspection"
    ];

    taps = [
      # "homebrew/bundle"
    ];

    casks = [
      "wezterm"
      "sioyek"
      "visual-studio-code"
      "mactex-no-gui"
      "zed"
    ];

    masApps = { };

    onActivation.cleanup = "zap";
    onActivation.autoUpdate = true;
    onActivation.upgrade = true;
  };
}
