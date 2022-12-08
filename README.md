# soprano.nvim

Experimental plugin! 👷

Play music from my music application <a href='https://github.com/whleucka/soprano.nvim' title='Soprano'>Soprano</a> inside of neovim.


### Requirements
- mpv
- *nix OS

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

- Create binding
```
vim.keymap.set('n', '<C-s>', '<cmd>lua require("soprano").search()<CR>')
```
