return {
  {
    "rebelot/kanagawa.nvim",
  },
  "catppuccin/nvim",
  {
    "williamboman/mason-lspconfig.nvim",
    -- overrides `require("mason-lspconfig").setup(...)`
    opts = {
      ensure_installed = {
        "lua_ls",
        "bashls",
        -- "clangd",
        "pylsp",
      }
    }
  },
  -- use mason-null-ls to configure Formatters/Linter installation for null-ls sources
  {
    "jay-babu/mason-null-ls.nvim",
    -- overrides `require("mason-null-ls").setup(...)`
    opts = {
      ensure_installed = {
        "lua_ls",
        "bashls",
        -- "clangd",
        "pylsp",
      }
    }
  },
  {
    "jay-babu/mason-nvim-dap.nvim",
    -- overrides `require("mason-nvim-dap").setup(...)`
    opts = {
      ensure_installed = {
        "lua_ls",
        "bashls",
        -- "clangd",
        "pylsp",
      }
    }
  },
  {
    "nvim-treesitter/nvim-treesitter",
    opts = {
      ensure_installed = {
        "bash",
        "lua",
        "c",
        "cpp",
        "python",
      }
    }
  }
}
