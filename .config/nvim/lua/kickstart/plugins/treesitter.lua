return {
  { -- Highlight, edit, and navigate code
    'nvim-treesitter/nvim-treesitter',
    branch = 'main', -- master branch is frozen; main is the actively maintained API
    build = ':TSUpdate',
    config = function()
      -- [[ Configure Treesitter ]] See `:help nvim-treesitter`
      local ts = require 'nvim-treesitter'

      -- Languages to keep installed. Install runs asynchronously.
      local ensure_installed = {
        'bash',
        'c',
        'diff',
        'html',
        'lua',
        'luadoc',
        'markdown',
        'markdown_inline',
        'vim',
        'vimdoc',
        'python',
        'rust',
      }
      ts.install(ensure_installed)

      -- Start highlighting + indent for any buffer whose parser is available.
      vim.api.nvim_create_autocmd('FileType', {
        group = vim.api.nvim_create_augroup('kickstart-treesitter', { clear = true }),
        callback = function(args)
          -- Ruby relies on vim's regex indent; let treesitter highlight skip it gracefully.
          local ok = pcall(vim.treesitter.start, args.buf)
          if ok then
            -- Experimental treesitter-based indentation.
            vim.bo[args.buf].indentexpr = "v:lua.require'nvim-treesitter'.indentexpr()"
          end
        end,
      })
    end,
  },
}
-- vim: ts=2 sts=2 sw=2 et
