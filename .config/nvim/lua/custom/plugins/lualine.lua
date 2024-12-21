local kanagawa_colors = require 'kanagawa.colors'

local kanagawa = {
  normal = {
    a = { fg = kanagawa_colors.fg, bg = kanagawa_colors.blue, gui = 'bold' },
    b = { fg = kanagawa_colors.fg, bg = kanagawa_colors.bg_dark },
    c = { fg = kanagawa_colors.fg, bg = kanagawa_colors.bg },
  },
  insert = {
    a = { fg = kanagawa_colors.bg, bg = kanagawa_colors.green, gui = 'bold' },
  },
  visual = {
    a = { fg = kanagawa_colors.bg, bg = kanagawa_colors.purple, gui = 'bold' },
  },
  replace = {
    a = { fg = kanagawa_colors.bg, bg = kanagawa_colors.red, gui = 'bold' },
  },
  inactive = {
    a = { fg = kanagawa_colors.fg, bg = kanagawa_colors.bg_dark, gui = 'bold' },
    b = { fg = kanagawa_colors.fg, bg = kanagawa_colors.bg },
    c = { fg = kanagawa_colors.fg, bg = kanagawa_colors.bg },
  },
}

return {
  {
    'nvim-lualine/lualine.nvim',
    dependencies = { 'nvim-tree/nvim-web-devicons' },
    priority = 0,

    opts = function()
      require('lualine').setup {
        options = {
          -- theme = kanagawa,
          component_separators = '',
          section_separators = { left = '', right = '' },
        },
        sections = {
          lualine_a = { { 'mode', right_padding = 2 } },
          lualine_b = { 'filename', 'branch' },
          lualine_c = {
            '%=', --[[ add your center compoentnts here in place of this comment ]]
          },
          lualine_x = {},
          lualine_y = { 'filetype', 'progress' },
          lualine_z = {
            { 'location', left_padding = 2 },
          },
        },
        inactive_sections = {
          lualine_a = { 'filename' },
          lualine_b = {},
          lualine_c = {},
          lualine_x = {},
          lualine_y = {},
          lualine_z = { 'location' },
        },
        tabline = {},
        extensions = {},
      }
    end,
  },
}
