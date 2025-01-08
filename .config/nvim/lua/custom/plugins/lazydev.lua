return {
  'justinsgithub/wezterm-types',
  {
    'folke/lazydev.nvim',
    ft = 'lua', -- only load on lua files
    opts = {
      library = {
        'LazyVim',
        -- Load the wezterm types when the `wezterm` module is required
        -- Needs `` to be installed
        { path = 'wezterm-types', mods = { 'wezterm' } },
      },
    },
  },
}
