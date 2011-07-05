#
#   Copyright 2011 Wade Alcorn wade@bindshell.net
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
# The following file contains patches for WEBrick.
module WEBrick
  
  class HTTPResponse

    #
    # set caching headers none
    #
    def set_no_cache()
      @header['ETag'] = nil
      @header['Last-Modified'] = Time.now + 100**4
      @header['Expires'] = Time.now - 100**4
      @header['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0'
      @header['Pragma'] = 'no-cache'      
    end
    
    #
    # set the cookie in the response
    # Limit: only one set-cookie will be within the response
    #
    def set_cookie(name, value, path = '/', httponly = true, secure = true)
      
      cookie = WEBrick::Cookie.new(name, value)
      cookie.path = path
      cookie.httponly = httponly
      cookie.secure = secure
      
      # add cookie to response header
      @header['Set-Cookie'] = cookie.to_s
    end

    #
    # This patch should prevent leakage of directory listing, access
    # auth errors, etc.
    #   
    def set_error(ex, backtrace=false)

      # set repsonse headers
      @status = 404;
      @header['content-type'] = "text/html; charset=UTF-8"

      # set response content
      @body = ''
      @body << <<-_end_of_html_
      
      <HTML>
      <HEAD>
      <TITLE>No page for you!</TITLE>

      <STYLE type="text/css">
        BODY { font: 8pt/12pt verdana }
        H1 { font: 13pt/15pt verdana }
        H2 { font: 8pt/12pt verdana }
        A:link { color: black; text-decoration: none }
        A:visited { color: black; text-decoration: none }
      </STYLE>

      </HEAD><BODY>
      <TABLE width=500 border=0 cellspacing=10>
      <TR>
      <TD>

      <h1><a href="http://www.bindshell.net/tools/beef/">These aren't the pages you're looking for</a></h1>
      
      </TD>
      </TR>
      </TABLE>
      </BODY>
      </HTML>
      
      _end_of_html_
      
    end
  end
end
