-- Keymaps are automatically loaded on the VeryLazy event
-- Default keymaps that are always set: https://github.com/LazyVim/LazyVim/blob/main/lua/lazyvim/config/keymaps.lua
-- Add any additional keymaps here

local Util = require("lazyvim.util")
local map = vim.keymap.set

local lazyterm = function()
  Util.terminal()
end

map("n", "<leader>tf", lazyterm, { desc = "float term" })
map("t", "<C-j>", "<cmd>close<cr>", { desc = "hide term" })
