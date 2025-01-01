{ pkgs, config, ... }: {

  homebrew = {
    enable = true;

    brews = [ ];

    casks = [
      "wezterm"   
      "sioyek"
    ];

    masApps = { };

    onActivation.cleanup = "zap";
    onActivation.autoUpdate = true;
    onActivation.upgrade = true;
  };
}
