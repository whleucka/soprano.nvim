# soprano.nvim

Experimental plugin! 👷

Play music from my music application, <a href='https://github.com/whleucka/soprano.nvim' title='Soprano'>Soprano</a>, inside of neovim.


### Requirements
- python
- mpv
- Linux

### Setup
- Packer
```
use {
    "whleucka/soprano.nvim",
    requires = {
        "akinsho/toggleterm.nvim"
    }
}
```

- Plug
```
Plug "whleucka/soprano.nvim"
```

- Example binding
```
vim.keymap.set('n', '<leader>s', '<cmd>lua require("soprano").search()<CR>')
```
