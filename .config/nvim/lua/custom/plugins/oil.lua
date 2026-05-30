return {
  { -- Edit your filesystem like a normal buffer
    'stevearc/oil.nvim',
    dependencies = { 'nvim-tree/nvim-web-devicons' },
    lazy = false,
    opts = {
      view_options = { show_hidden = true },
    },
    keys = {
      { '-', '<cmd>Oil<CR>', desc = 'Open parent dir (oil)' },
      -- Space-discoverable alias
      { '<leader>o', '<cmd>Oil<CR>', desc = '[O]il file editor (or press -)' },
    },
  },
}
