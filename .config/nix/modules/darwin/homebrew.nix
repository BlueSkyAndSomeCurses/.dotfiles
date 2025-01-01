{ pkgs, config, ... }: {

  homebrew = {
    enable = true;

    brews = [ ];

    casks = [
      "wezterm"   
    ];

    masApps = { };

    onActivation.cleanup = "zap";
    onActivation.autoUpdate = true;
    onActivation.upgrade = true;
  };
}
