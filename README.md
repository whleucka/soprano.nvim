# soprano.nvim

Experimental plugin! 👷

Play music from my music application, <a href='https://github.com/whleucka/soprano-react' title='soprano-react'>Soprano</a>, inside of neovim.

View the music application demo, <a href='https://soprano.williamhleucka.com/' title='Soprano'>here</a>.

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
