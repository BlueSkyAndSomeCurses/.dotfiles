return {

  {
    'akinsho/toggleterm.nvim',

    config = function()
      require('toggleterm').setup {
        size = function(term)
          if term.direction == 'horizontal' then
            return 16
          elseif term.direction == 'vertical' then
            return vim.o.columns * 0.5
          end
        end,
        width = 20,
        close_on_exit = false,
        float_opts = {
          border = 'none',
        },
      }
      local terminal = require('toggleterm.terminal').Terminal
      local horizontal_terminal = terminal:new { direction = 'horizontal' }
      local float_terminal = terminal:new { direction = 'float' }
      local vert_terminal = terminal:new { direction = 'vertical' }

      local open_horizontal = function()
        return horizontal_terminal:toggle()
      end
      local open_float = function()
        return float_terminal:toggle()
      end
      local open_vertical = function()
        return vert_terminal:toggle()
      end

      local close_terms = function()
        if terminal.is_open(horizontal_terminal) then
          return horizontal_terminal:toggle()
        end

        if terminal.is_open(float_terminal) then
          return float_terminal:toggle()
        end

        if terminal.is_open(vert_terminal) then
          return vert_terminal:toggle()
        end
      end

      vim.keymap.set('n', '<leader>th', open_horizontal, { desc = '[H]orizontal' })
      vim.keymap.set('n', '<leader>tf', open_float, { desc = '[F]loating' })
      vim.keymap.set('n', '<leader>tv', open_vertical, { desc = '[V]ertical' })

      vim.keymap.set('t', '<C-j>', close_terms, { desc = 'Close terminals' })
    end,
  },
}
