{ pkgs, config, ... }: {

  homebrew = {
    enable = true;

    brews = [ ];

    casks = [ ];

    masApps = { };

    onActivation.cleanup = "zap";
    onActivation.autoUpdate = true;
    onActivation.upgrade = true;
  };
}
