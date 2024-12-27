{ pkgs, config, ... }: {

  system.defaults = {
    dock.autohide = true;
    dock.persistent-apps = [
      "${pkgs.kitty}/Applications/Kitty.app"
      "${pkgs.arc-browser}/Applications/Arc.app"
      "/System/Applications/Mail.app"
      "/System/Applications/Calendar.app"
    ];
    loginwindow.GuestEnabled = false;
    NSGlobalDomain.AppleICUForce24HourTime = true;
    NSGlobalDomain.AppleInterfaceStyle = "Dark";
  };

  system.stateVersion = 5;

}
