{ pkgs, ... }:
{
  imports = [
    ./zsh_aliases.nix
    ./session_variables.nix
    ./dir_hashes.nix

  ];

  programs.zsh = {
    enable = true;
    enableCompletion = true;
    autocd = true;

    autosuggestion = {
      enable = true;
    };

    plugins = [

    ];
    dotDir = ".config/zsh";

    syntaxHighlighting = {
      enable = true;
    };

    initExtra = "
      autoload -U colors && colors\
      PS1=\"%B%{$fg[red]%}[%{$fg[yellow]%}%n%{$fg[green]%}@%{$fg[blue]%}%M %{$fg[magenta]%}%~%{$fg[red]%}]%{$reset_color%}$%b \"\n
      autoload -U compinit \n
      zstyle \':completion:*\' menu select \n
      zmodload zsh/complist \n
      compinit \n
      _comp_options+=(globdots) \n
    ";

  };
}
