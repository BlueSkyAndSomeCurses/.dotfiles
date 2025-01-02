-- NOTE: Plugins can also be configured to run Lua code when they are loaded.
--
-- This is often very useful to both group configuration, as well as handle
-- lazy loading plugins that don't need to be loaded immediately at startup.
--
-- For example, in the following configuration, we use:
--  event = 'VimEnter'
--
-- which loads which-key before all the UI elements are loaded. Events can be
-- normal autocommands events (`:help autocmd-events`).
--
-- Then, because we use the `config` key, the configuration only runs
-- after the plugin has been loaded:
--  config = function() ... end

return {
  'nvim-tree/nvim-web-devicons',
  { -- Useful plugin to show you pending keybinds.
    'folke/which-key.nvim',
    event = 'VimEnter', -- Sets the loading event to 'VimEnter'

    config = function() -- This is the function that runs, AFTER loading
      local wk = require 'which-key'

      wk.setup()

      wk.add {
        { '<leader>c', group = '[C]ode' },
        { '<leader>d', group = '[D]debug' },
        { '<leader>h', group = 'Git [H]unk' },
        { '<leader>r', group = '[R]ename' },
        { '<leader>f', group = '[F]iles' },
        { '<leader>t', group = '[T]erminal' },
        { '<leader>w', group = '[W]orkspace' },
        { '<leader>s', desc = '[S]urround' },
        { '<leader>sa', desc = '[A]dd surrounding' },
        { '<leader>sd', desc = '[D]elete surrounding' },
        { '<leader>sr', desc = '[R]eplace surrounding' },
        { '<leader>sf', desc = '[F]ind surrounding (right)' },
        { '<leader>sF', desc = '[F]ind surrounding (left)' },
        { '<leader>sh', desc = '[H]ighlight surrounding' },
        { '<leader>sn', desc = '[N]umber line change' },
        { '<leader>h', desc = 'Git [H]unk', mode = 'v' },
      }
    end,
  },
}
