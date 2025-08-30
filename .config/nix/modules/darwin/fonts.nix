{
  config,
  pkgs,
  inputs,
  ...
}:
{
  fonts.packages = [
    pkgs.nerd-fonts.caskaydia-cove
    pkgs.nerd-fonts.jetbrains-mono
  ];
}
