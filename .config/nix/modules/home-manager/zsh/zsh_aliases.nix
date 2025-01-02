{ ... }:
{
  programs.zsh.shellAliases =
    let
      newAliases = builtins.listToAttrs (
        map
          (command: {
            name = command;
            value = "sudo ${command}";
          })
          [
            "mount"
            "umount"
            "sv"
            "pacman"
            "updatedb"
            "su"
            "shutdown"
            "poweroff"
            "reboot"
          ]
      );
    in
    {
      exa = "ls -lah";
      cp = "cp -iv";
      mv = "mv -iv";
      rm = "rm -vI";
      bc = "bc -ql";
      rsync = "rsync -vrPlu";
      mkd = "mkdir -pv";
      yt = "yt-dlp --embed-metadata -i";
      yta = "yt -x -f bestaudio/best";
      ytt = "yt --skip-download --write-thumbnail";
      ffmpeg = "ffmpeg -hide_banner";

      ls = "ls -h --color=auto";
      grep = "grep --color=auto";
      diff = "diff --color=auto";
      ccat = "highlight --out-format=ansi";
      ip = "ip -color=auto";

      cac = "cd $XDG_CACHE_HOME ls -A";
      cf = "cd $XDG_CONFIG_HOME && ls -A";
      D = "cd $HOME/Downloads && ls -A";
      d = "cd $HOME/Documents && ls -A";
      dt = "cd $HOME/.local/share && ls -A";
      rr = "cd $HOME/.local/src && ls -A";
      h = "cd $HOME && ls -A";
      m = "cd $HOME/Music && ls -A";
      mn = "cd /mnt && ls -A";
      pp = "cd $HOME/Pictures && ls -A";
      sc = "cd $HOME/.local/bin && ls -A";
      src = "cd $HOME/.local/src && ls -A";
      vv = "cd $HOME/Videos && ls -A";

      vim = "nvim";
    }
    // newAliases;

}
