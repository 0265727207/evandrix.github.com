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
module BeEF
module Extension
module Initialization
  
  module RegisterHttpHandler
    # use of the API right here
    extend BeEF::API::Server::Handler
    
    #
    # Register the http handler for the initialization script that retrieves
    # all the information about hooked browsers.
    #
    def self.mount_handlers(beef_server)
      beef_server.mount('/init', false, BeEF::Extension::Initialization::Handler)
    end
    
  end
  
end
end
end