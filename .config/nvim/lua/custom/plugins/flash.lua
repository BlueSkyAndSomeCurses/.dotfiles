return {
  { -- Jump anywhere on screen with a few keystrokes
    'folke/flash.nvim',
    event = 'VeryLazy',
    opts = {},
    keys = {
      -- Ergonomic primaries
      {
        's',
        mode = { 'n', 'x', 'o' },
        function()
          require('flash').jump()
        end,
        desc = 'Flash jump',
      },
      {
        'S',
        mode = { 'n', 'x', 'o' },
        function()
          require('flash').treesitter()
        end,
        desc = 'Flash Treesitter',
      },
      -- Space-discoverable alias (shows in the which-key leader menu)
      {
        '<leader>j',
        mode = { 'n', 'x', 'o' },
        function()
          require('flash').jump()
        end,
        desc = 'Flash [J]ump (or press s)',
      },
    },
  },
}
