{ pkgs, ... }:
let
  home = builtins.getEnv "HOME"; # Getting the $HOME variable
  xdgCacheHome = builtins.getEnv "XDG_CACHE_HOME";
  xdgConfigHome = builtins.getEnv "XDG_CONFIG_HOME";
  xdgDownloadDir = builtins.getEnv "XDG_DOWNLOAD_DIR";
  xdgDocumentsDir = builtins.getEnv "XDG_DOCUMENTS_DIR";
  xdgDataHome = builtins.getEnv "XDG_DATA_HOME";
  xdgMusicDir = builtins.getEnv "XDG_MUSIC_DIR";
  xdgPicturesDir = builtins.getEnv "XDG_PICTURES_DIR";
  xdgVideosDir = builtins.getEnv "XDG_VIDEOS_DIR";
in
{
  programs.zsh = {
    enable = true;
    enableCompletion = true;
    autocd = true;

    autosuggestion = {
      enable = true;
    };

    defaultKeymap = "vicmd";

    dirHashes = {
      cac = xdgCacheHome;
      cf = xdgConfigHome;
      D = xdgDownloadDir;
      d = xdgDocumentsDir;
      dt = xdgDataHome;
      rr = "${home}/.local/src"; # Custom path (no fallback required)
      h = home;
      m = xdgMusicDir;
      mn = "/mnt";
      pp = xdgPicturesDir;
      sc = "${home}/.local/bin"; # Custom path (no fallback required)
      src = "${home}/.local/src"; # Custom path (no fallback required)
      vv = xdgVideosDir;
    };

    dotDir = "${xdgConfigHome}/zsh";
  };
}
