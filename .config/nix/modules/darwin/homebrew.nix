{ pkgs, config, ... }:
{

  homebrew = {
    enable = true;

    brews = [
      "pkg-config"
      "ffmpeg"
      "boost"
      "boost-mpi"
      "python@3.10"
      "uv"
    ];

    taps = [
      # "homebrew/bundle"
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
