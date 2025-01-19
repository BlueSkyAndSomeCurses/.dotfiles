{ pkgs, config, ... }:
{

  system.defaults = {
    dock.autohide = true;
    dock.persistent-apps = [
      "${pkgs.wezterm}/Applications/WezTerm.app"
      "${pkgs.arc-browser}/Applications/Arc.app"
      "/System/Applications/Mail.app"
      "/System/Applications/Calendar.app"
    ];
    finder.FXPreferredViewStyle = "clmv";
    loginwindow.GuestEnabled = false;
    NSGlobalDomain.AppleICUForce24HourTime = true;
    NSGlobalDomain.AppleInterfaceStyle = "Dark";
  };

  system.stateVersion = 5;

}
