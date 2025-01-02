return {
  {
    'echasnovski/mini.comment',
    event = 'VeryLazy',
    config = function()
      require('mini.comment').setup {
        options = {
          ignore_blank_line = true,
        },
        mappings = {
          comment = '<leader>/',
          comment_line = '<leader>/',
          comment_visual = '<leader>/',
          textobject = '<leader>/',
        },
      }
    end,
  },
}
