local wezterm = require("wezterm")

local config = wezterm.config_builder()

config.color_scheme = "Gruvbox dark, hard (base16)"
config.hide_tab_bar_if_only_one_tab = true
config.tab_bar_at_bottom = true
config.use_fancy_tab_bar = true

config.font = wezterm.font("CaskaydiaCove Nerd Font Mono")
config.font_size = 15.0

return config
