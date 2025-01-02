{ pkgs, ... }:
{
  fonts = {
    enableDefaultPackages = true;
    packages = with pkgs; [ nerd-fonts.caskaydia-cove ];

    fontconfig = {
      defaultFonts = {
        monospace = [ "CaskaydiaCove" ];
      };
    };
  };
}
