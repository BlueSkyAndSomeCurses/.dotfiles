return {
  { -- LSP Configuration & Plugins
    'neovim/nvim-lspconfig',

    dependencies = {
      -- Automatically install LSPs and related tools to stdpath for Neovim
      { 'mason-org/mason.nvim', opts = {} }, -- NOTE: Must be loaded before dependants
      'mason-org/mason-lspconfig.nvim',
      'WhoIsSethDaniel/mason-tool-installer.nvim',

      -- Useful status updates for LSP.
      { 'j-hui/fidget.nvim', opts = {} },

      -- Allows extra capabilities provided by blink.cmp
      'saghen/blink.cmp',
    },
    config = function()
      -- LSP provides Neovim with features like go-to-definition, find references,
      -- autocompletion, symbol search and more. Servers are external tools managed
      -- by `mason` and enabled below via the Neovim 0.11+ `vim.lsp.config` API.

      vim.lsp.inlay_hint.enable(true)

      --  This function gets run when an LSP attaches to a particular buffer.
      vim.api.nvim_create_autocmd('LspAttach', {
        group = vim.api.nvim_create_augroup('kickstart-lsp-attach', { clear = true }),
        callback = function(event)
          local map = function(keys, func, desc)
            vim.keymap.set('n', keys, func, { buffer = event.buf, desc = 'LSP: ' .. desc })
          end

          -- Jump to the definition of the word under your cursor.
          map('gd', require('telescope.builtin').lsp_definitions, '[G]oto [D]efinition')

          -- Find references for the word under your cursor.
          map('gr', require('telescope.builtin').lsp_references, '[G]oto [R]eferences')

          -- Jump to the implementation of the word under your cursor.
          map('gI', require('telescope.builtin').lsp_implementations, '[G]oto [I]mplementation')

          -- Jump to the type of the word under your cursor.
          map('<leader>D', require('telescope.builtin').lsp_type_definitions, 'Type [D]efinition')

          -- Fuzzy find all the symbols in your current document.
          map('<leader>cs', require('telescope.builtin').lsp_document_symbols, '[C]ode [S]ymbols')

          -- Fuzzy find all the symbols in your current workspace.
          map('<leader>ws', require('telescope.builtin').lsp_dynamic_workspace_symbols, '[W]orkspace [S]ymbols')

          -- Rename the variable under your cursor.
          map('<leader>rn', vim.lsp.buf.rename, '[R]e[n]ame')

          -- Execute a code action, usually your cursor needs to be on top of an error
          -- or a suggestion from your LSP for this to activate.
          map('<leader>ca', vim.lsp.buf.code_action, '[C]ode [A]ction')

          -- Opens a popup that displays documentation about the word under your cursor
          map('K', vim.lsp.buf.hover, 'Hover Documentation')

          -- WARN: This is not Goto Definition, this is Goto Declaration.
          map('gD', vim.lsp.buf.declaration, '[G]oto [D]eclaration')

          -- Highlight references of the word under your cursor when it rests there.
          local client = vim.lsp.get_client_by_id(event.data.client_id)
          if client and client.server_capabilities.documentHighlightProvider then
            local highlight_augroup = vim.api.nvim_create_augroup('kickstart-lsp-highlight', { clear = false })
            vim.api.nvim_create_autocmd({ 'CursorHold', 'CursorHoldI' }, {
              buffer = event.buf,
              group = highlight_augroup,
              callback = vim.lsp.buf.document_highlight,
            })

            vim.api.nvim_create_autocmd({ 'CursorMoved', 'CursorMovedI' }, {
              buffer = event.buf,
              group = highlight_augroup,
              callback = vim.lsp.buf.clear_references,
            })

            vim.api.nvim_create_autocmd('LspDetach', {
              group = vim.api.nvim_create_augroup('kickstart-lsp-detach', { clear = true }),
              callback = function(event2)
                vim.lsp.buf.clear_references()
                vim.api.nvim_clear_autocmds { group = 'kickstart-lsp-highlight', buffer = event2.buf }
              end,
            })
          end
        end,
      })

      -- LSP servers and clients communicate which features they support. blink.cmp
      -- expands Neovim's default capabilities; broadcast that to every server.
      local capabilities = require('blink.cmp').get_lsp_capabilities()
      vim.lsp.config('*', { capabilities = capabilities })

      -- Per-server configuration. Each is merged with the defaults above.
      --  Add/remove servers here; installed ones are auto-enabled by mason-lspconfig.
      local servers = {
        nixd = {
          settings = {
            nixd = {
              nixpkgs = { expr = 'import <nixpkgs> { }' },
              formatting = { command = { 'nixfmt' } },
            },
          },
        },
        clangd = {
          settings = {
            clangd = {
              InlayHints = {
                Designators = true,
                Enabled = true,
                ParameterNames = true,
                DeducedTypes = true,
              },
              fallbackFlags = { '-std=c++20' },
            },
          },
        },
        rust_analyzer = {
          settings = {
            ['rust-analyzer'] = {
              inlayHints = {
                bindingModeHints = { enable = false },
                chainingHints = { enable = true },
                closingBraceHints = { enable = true, minLines = 25 },
                closureReturnTypeHints = { enable = 'never' },
                lifetimeElisionHints = { enable = 'never', useParameterNames = false },
                maxLength = 25,
                parameterHints = { enable = true },
                reborrowHints = { enable = 'never' },
                renderColons = true,
                typeHints = {
                  enable = true,
                  hideClosureInitialization = false,
                  hideNamedConstructor = false,
                },
              },
            },
          },
        },
        -- pyright = intellisense only (completion/hover/goto). Type-check
        -- diagnostics off; ruff handles all linting/diagnostics + import sorting.
        pyright = {
          settings = {
            pyright = { disableOrganizeImports = true },
            python = {
              analysis = { typeCheckingMode = 'off' },
            },
          },
        },
        ruff = {},
        lua_ls = {
          settings = {
            Lua = {
              completion = { callSnippet = 'Replace' },
              hint = { enable = true },
            },
          },
        },
      }

      -- Register each server's overrides with the new vim.lsp.config API.
      for name, config in pairs(servers) do
        vim.lsp.config(name, config)
      end

      -- Ensure servers and tools are installed.
      require('mason').setup()

      -- Servers NOT installed by mason (provided by the system, e.g. nix).
      local system_servers = { nixd = true }

      -- Non-LSP tools — installed by mason directly, so these are mason package
      -- names (not lspconfig server names; mason-tool-installer does no translation).
      require('mason-tool-installer').setup {
        ensure_installed = {
          'stylua', -- Used to format Lua code
          'clang-format', -- Used to format C/C++
          'tree-sitter-cli', -- Required by nvim-treesitter `main` branch to compile parsers
        },
      }

      -- LSP servers — mason-lspconfig translates lspconfig names (lua_ls,
      -- rust_analyzer, ...) into mason packages and installs them. System-provided
      -- servers are excluded. v2 dropped `handlers`; we enable servers ourselves
      -- (automatic_enable would also start formatters lspconfig ships, e.g. stylua).
      local mason_servers = vim.tbl_filter(function(name)
        return not system_servers[name]
      end, vim.tbl_keys(servers))
      require('mason-lspconfig').setup {
        ensure_installed = mason_servers,
        automatic_enable = false,
      }

      -- Enable every configured server (mason-installed + system-provided).
      vim.lsp.enable(vim.tbl_keys(servers))
    end,
  },
}
-- vim: ts=2 sts=2 sw=2 et
