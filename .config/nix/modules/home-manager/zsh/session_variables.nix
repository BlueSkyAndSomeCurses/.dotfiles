{ ... }: {
  programs.zsh.sessionVariables = {
    EDITOR = "nvim";
    TERMINAL = "foot";

    TERMINAL_PROG = "foot";
    BROWSER = "brave";

    XDG_CONFIG_HOME = "$HOME/.config";
    XDG_DATA_HOME = "$HOME/.local/share";
    XDG_CACHE_HOME = "$HOME/.cache";
    XDG_SCREENSHOTS_DIR = "$HOME/Documents/pictures";
    XDG_PICTURES_DIR = "$HOME/Documents/pictures";
    XINITRC = "$XDG_CONFIG_HOME/x11/xinitrc";
  };
}
