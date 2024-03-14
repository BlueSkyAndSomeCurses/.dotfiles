-- bootstrap lazy.nvim, LazyVim and your plugins

vim.opt.clipboard = "unnamedplus"

local opt = vim.opt
opt.termguicolors = true

if vim.g.vscode then
  -- VSCode extension
  -- require("")
else
  -- ordinary Neovim
  require("config.lazy")
end
