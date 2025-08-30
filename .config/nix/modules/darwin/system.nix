{ pkgs, config, ... }:
{

  system.primaryUser = "vitya";

  system.defaults = {
    dock.autohide = true;
    dock.persistent-apps = [
      "/System/Applications/Mail.app"
      "/System/Applications/Calendar.app"
    ];
    finder = {
      FXPreferredViewStyle = "clmv";
      AppleShowAllExtensions = true;
      AppleShowAllFiles = true;
      CreateDesktop = false;
    };
    loginwindow.GuestEnabled = false;
    NSGlobalDomain.AppleICUForce24HourTime = true;
    NSGlobalDomain.AppleInterfaceStyle = "Dark";
  };

  system.stateVersion = 5;

}
