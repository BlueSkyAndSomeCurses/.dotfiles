{ inputs, pkgs, ... }: {
  # add the home manager module
  imports = [ inputs.ags.homeManagerModules.default ];

  programs.ags = {
    enable = true;

    extraPackages = with pkgs; [
      inputs.ags.packages.${system}.battery
      inputs.ags.packages.${system}.mpris
      inputs.ags.packages.${system}.network
      inputs.ags.packages.${system}.tray
      inputs.ags.packages.${system}.wireplumber
    ];
  };
}
