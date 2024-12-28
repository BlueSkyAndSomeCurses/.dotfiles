{config, pkgs, lib, ...} :
{
  programs.foot = {
    enable = true;
    # settings = { 
      # main = «thunk»; scrollback = «thunk»; 
    # };
  };
  programs.firefox.enable =true;
}
