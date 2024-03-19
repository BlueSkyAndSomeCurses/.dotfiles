return {
  {
    "nvim-lualine/lualine.nvim",
    event = "VeryLazy",
    opts = function(_, opts)
      theme = "catppuccin"
      local lualine = require("lualine")
      return {
        --[[add your custom lualine config here]]
        options = {
          theme = bubbles_theme,
          component_separators = "",
          section_separators = { left = "", right = "" },
        },
        sections = {
          lualine_a = { { "mode", separator = { right = "" } } },
          lualine_b = { "filename", "branch" },
          lualine_c = {
            "%=", --[[ add your center compoentnts here in place of this comment ]]
          },
          lualine_x = {},
          lualine_y = { "filetype", "progress" },
          lualine_z = {
            { "location", separator = { left = "" } },
          },
        },
      }
    end,
  },
}
