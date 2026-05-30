return {
  { -- Autocompletion
    'saghen/blink.cmp',
    event = 'InsertEnter',
    version = '1.*',
    dependencies = {
      -- Snippet Engine
      {
        'L3MON4D3/LuaSnip',
        version = 'v2.*',
        build = (function()
          -- Build Step is needed for regex support in snippets.
          -- Not supported in many windows environments.
          if vim.fn.has 'win32' == 1 or vim.fn.executable 'make' == 0 then
            return
          end
          return 'make install_jsregexp'
        end)(),
        dependencies = {
          -- `friendly-snippets` contains a variety of premade snippets.
          {
            'rafamadriz/friendly-snippets',
            config = function()
              require('luasnip.loaders.from_vscode').lazy_load()
            end,
          },
        },
      },
    },
    --- @module 'blink.cmp'
    --- @type blink.cmp.Config
    opts = {
      keymap = {
        -- 'default' (recommended) keeps cmp-like behaviour:
        --   <C-y> accept, <C-n>/<C-p> or <Up>/<Down> select,
        --   <C-Space> open menu, <C-e> hide, <C-k> signature toggle.
        -- See `:help blink-cmp-config-keymap` for the full list.
        preset = 'default',
      },
      appearance = { nerd_font_variant = 'mono' },
      completion = {
        -- Show documentation popup automatically after a short delay.
        documentation = { auto_show = true, auto_show_delay_ms = 200 },
      },
      sources = {
        default = { 'lsp', 'path', 'snippets', 'lazydev' },
        providers = {
          lazydev = { module = 'lazydev.integrations.blink', score_offset = 100 },
        },
      },
      snippets = { preset = 'luasnip' },
      -- Signature help while typing (replaces lsp_signature.nvim).
      signature = { enabled = true },
      fuzzy = { implementation = 'prefer_rust_with_warning' },
    },
  },
}
-- vim: ts=2 sts=2 sw=2 et
