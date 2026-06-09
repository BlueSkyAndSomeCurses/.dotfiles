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
        -- Group labels (show when you press <leader> and hold)
        { '<leader>c', group = '[C]ode' },
        { '<leader>d', group = '[D]ebug' },
        { '<leader>h', group = 'Git [H]unk' },
        { '<leader>r', group = '[R]ename' },
        { '<leader>f', group = '[F]iles' },
        { '<leader>t', group = '[T]oggle/Terminal' },
        { '<leader>w', group = '[W]orkspace' },
        { '<leader>x', group = '[X] Trouble' },
        { '<leader>h', group = 'Git [H]unk', mode = 'v' },

        -- Show every registered keymap (incl. standalone keys like s, S, -).
        {
          '<leader>?',
          function()
            require('which-key').show { global = true }
          end,
          desc = 'Show all keymaps',
        },
      }
    end,
  },
}
