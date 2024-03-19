return {
  {
    "folke/which-key.nvim",
    opts = function(_, opts)
      defaults = {
        ["<leader>t"] = { name = "+terminal" },
      }
    end,
  },
}
