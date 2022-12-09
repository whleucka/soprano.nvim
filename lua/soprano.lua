local M = {}

local function is_win()
  return package.config:sub(1, 1) == '\\'
end

local function get_path_separator()
  if is_win() then
    return '\\'
  end
  return '/'
end

local function script_path()
  local str = debug.getinfo(2, 'S').source:sub(2)
  if is_win() then
    str = str:gsub('/', '\\')
  end
  return str:match('(.*' .. get_path_separator() .. ')')
end

-- Make sure local functions are defined first
local terminal = require('toggleterm.terminal').Terminal
local soprano = terminal:new({ cmd = script_path() .. "scripts/soprano", hidden = true, direction = "float" })

function M.search()
    soprano:toggle()
end

return M
