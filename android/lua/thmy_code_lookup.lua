local M = {}

local lookup = nil
local lookup_path = "thmy_code_lookup.tsv"
local last_commit_text = ""

local function trim(text)
  return (text or ""):match("^%s*(.-)%s*$") or ""
end

local function has_cjk(text)
  for _, byte in ipairs({ text:byte(1, #text) }) do
    if byte and byte >= 0x80 then
      return true
    end
  end
  return false
end

local function last_utf8_char(text)
  if not text or text == "" then
    return ""
  end
  local pos = #text
  while pos > 1 do
    local byte = text:byte(pos)
    if byte < 0x80 or byte >= 0xC0 then
      break
    end
    pos = pos - 1
  end
  return text:sub(pos)
end

local function user_data_dir()
  if type(rime_api) ~= "nil" then
    local ok, dir = pcall(function()
      return rime_api:get_user_data_dir()
    end)
    if ok and dir and dir ~= "" then
      return dir
    end

    ok, dir = pcall(function()
      return rime_api.get_user_data_dir()
    end)
    if ok and dir and dir ~= "" then
      return dir
    end
  end
  return "."
end

local function load_lookup()
  if lookup then
    return lookup
  end

  lookup = {}
  local base = user_data_dir()
  local paths = {
    base .. "/" .. lookup_path,
    lookup_path,
  }

  for _, path in ipairs(paths) do
    local file = io.open(path, "r")
    if file then
      for line in file:lines() do
        if line:sub(1, 1) ~= "#" then
          local text, codes = line:match("^([^\t]+)\t(.+)$")
          if text and codes then
            lookup[text] = codes
          end
        end
      end
      file:close()
      break
    end
  end

  return lookup
end

local function commit_text_from_context(ctx)
  if type(ctx) == "string" then
    return ctx
  end

  local ok, text = pcall(function()
    if ctx and ctx.get_commit_text then
      return ctx:get_commit_text()
    end
    return nil
  end)
  if ok and type(text) == "string" then
    return text
  end

  ok, text = pcall(function()
    if ctx and ctx.text then
      return ctx.text
    end
    return nil
  end)
  if ok and type(text) == "string" then
    return text
  end

  return ""
end

local function remember_commit(ctx)
  local text = trim(commit_text_from_context(ctx))
  if text ~= "" and has_cjk(text) then
    last_commit_text = text
  end
end

local function emit_lookup_candidate(input, seg, label, text, emitted)
  if text == "" or emitted[text] then
    return false
  end

  local codes = load_lookup()[text]
  if not codes then
    return false
  end

  emitted[text] = true
  yield(Candidate("thmy_code_lookup", seg.start, seg._end, codes, label .. " " .. text))
  return true
end

function M.init(env)
  local ok_schema, schema_id = pcall(function()
    return env.engine.schema.schema_id
  end)
  if ok_schema and schema_id == "thmy_jj" then
    lookup_path = "thmy_jj_code_lookup.tsv"
  else
    lookup_path = "thmy_code_lookup.tsv"
  end

  local ok, connection = pcall(function()
    return env.engine.context.commit_notifier:connect(remember_commit)
  end)
  if ok then
    env.thmy_code_lookup_commit_connection = connection
  end
end

function M.fini(env)
  if env.thmy_code_lookup_commit_connection then
    pcall(function()
      env.thmy_code_lookup_commit_connection:disconnect()
    end)
  end
end

function M.func(input, seg, env)
  if input:sub(1, 2) ~= "//" then
    return
  end

  local query = trim(input:sub(3))
  if query == "" then
    query = last_commit_text
  end

  if query == "" then
    yield(Candidate("thmy_code_lookup", seg.start, seg._end, "无最近上屏", "先输入一个字或词"))
    return
  end

  local emitted = {}
  local matched = false
  matched = emit_lookup_candidate(input, seg, "反查", query, emitted) or matched

  local last_char = last_utf8_char(query)
  if last_char ~= "" and last_char ~= query then
    matched = emit_lookup_candidate(input, seg, "末字", last_char, emitted) or matched
  end

  if not matched then
    yield(Candidate("thmy_code_lookup", seg.start, seg._end, "未收录", query))
  end
end

return M
