local group = vim.api.nvim_create_augroup("asdf", { clear = true })
vim.api.nvim_create_autocmd("BufEnter", { command = "echo 'asdf'", group = group })
