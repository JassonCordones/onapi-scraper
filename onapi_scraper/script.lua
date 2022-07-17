local treat = require('treat')

function make_chars_table()
  local chartable = {}
  for i=1, 95 do
    chartable[i] = string.char(i+31)
  end
  return chartable
end

function main(splash, args)
  assert(splash:go(args.url))
  assert(splash:wait(0.5))
  local chars = make_chars_table()

--	for i, char in ipairs(chars) do
      splash:select("input.form-control").focus()
      splash:send_text('c')
      local button = splash:select('button.btn')
  		button:mouse_click()
      assert(splash:wait(0.5))
  		local code = {}
  		local inc = 0
  		next_li = splash:select('li.ng-scope:last-child')
  		next_btn = splash:select('li.ng-scope:last-child a')
  		next_li_class = next_li.node.attributes.class
  		local total_pages = 0
  		while(next_li_class ~= 'ng-scope disabled') do
    		total_pages = total_pages + 1
    		next_btn:mouse_click()
    		next_li = splash:select('li.ng-scope:last-child')
    		next_li_class = next_li.node.attributes.class
    	end
  		total_pages = total_pages + 1
  		--[[local pages = splash:select_all('li.ng-scope')
  		for j=2,#pages - 1 do
    		local rows = splash:select_all('table.table:nth-child(1) > tbody:nth-child(2) > tr')
    		for i=1,#rows do
          local row = splash:select('table.table:nth-child(1) > tbody:nth-child(2) > tr:nth-child('..i..')')
          row:mouse_click()
          assert(splash:wait(0.9))
          code[i+inc] = splash:html()
          back = splash:select('a.btn-success')
          back:mouse_click()
          assert(splash:wait(0.9))
  			end
    		inc = inc + 10
  			local next_p = splash:select('li.ng-scope:nth-child('.. j+1 ..') > a:nth-child(1)')
    		next_p:mouse_click()
      	assert(splash:wait(0.9))
  		end]]
  		
-- 	end

  return {
    total_pages
  }
end