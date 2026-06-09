return {

  { -- Linting
    'mfussenegger/nvim-lint',
    event = { 'BufReadPre', 'BufNewFile' },
    config = function()
      local lint = require 'lint'
      -- No filetypes linted via nvim-lint currently:
      --   * python -> ruff runs as an LSP (lspconfig.lua), so nvim-lint would double-lint.
      --   * markdown -> removed (markdownlint binary not installed; opinionated style nags).
      -- Add entries like `markdown = { 'markdownlint' }` here, and install the
      -- linter binary (e.g. mason), to re-enable.
      lint.linters_by_ft = {}

      local lint_augroup = vim.api.nvim_create_augroup('lint', { clear = true })
      vim.api.nvim_create_autocmd({ 'BufEnter', 'BufWritePost', 'InsertLeave' }, {
        group = lint_augroup,
        callback = function()
          require('lint').try_lint()
        end,
      })
    end,
  },
}
