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
module Metasploit
  
  #
  # XML RPC Client for Metasploit
  #
	class RpcClient < ::XMLRPC::Client
		
		include Singleton

	  def initialize
			@config = BeEF::Core::Configuration.instance
			@enabled = (@config.get('beef.extension.metasploit.enable'))
			
		  return if (not @enabled)
		  
			host = @config.get('beef.extension.metasploit.host')
			path = @config.get('beef.extension.metasploit.path')
			port = @config.get('beef.extension.metasploit.port')
			@un = @config.get('beef.extension.metasploit.user')
			@pw = @config.get('beef.extension.metasploit.pass')
			@apurl = @config.get('beef.extension.metasploit.autopwn_url') || "autopwn"
      @lock = false
      
			if(not host or not path or not port or not @un or not @pw)
				print_error 'There is not enough information to initalize Metasploit connectivity at this time'
				print_error 'Please check your options in config.yaml to verify that all information is present'
				@enabled = false
			end

			@token = nil
			@lastauth = nil

			super(host,path,port)
	  end
    
    def get_lock()
      sleep 0.2 while @lock 
      @lock = true
    end
    
    def release_lock()
      @lock = false
    end
    
		# is metasploit enabled in the configuration
		def is_enabled
			@enabled	
		end
    
    # login into metasploit
		def login
      get_lock()
			res = self.call("auth.login", @un ,@pw )
			
		 	if(not (res and res['result'] == "success")) 
				@enabled = false
        release_lock()
        print_error 'Could not authenticate to Metasploit xmlrpc.'
				return false
			end
			
			print_info 'Successful connection with Metasploit.' if not @lastauth
			
			@token = res['token']
			@lastauth = Time.now
      
      release_lock()
			true
		end
    
    # sends commands to the metasploit xml rpc server
		def call(meth, *args)
			return if not @enabled

			if(meth != "auth.login")
				self.login() if not @token
				args.unshift(@token)
			end
			
			begin
				super(meth, *args)
			rescue Errno::ECONNREFUSED
				print_error "Connection to Metasploit backend failed."
				@enabled = false
				return false
			rescue XMLRPC::FaultException => e
				if e.faultCode == 401 and meth == "auth.login"
					print_error "Your username and password combination was rejected by the Metasploit backend server"
					@enabled = false
				elsif e.faultCode == 401
					res = self.login()
				else
					print_error "An unknown exception has occured while talking to the Metasploit backend."
					print_error "The Exception text is (#{e.faultCode} : #{e.faultString}."
					print_error "Please check the Metasploit logs for more details."
				end
				return false
			rescue Exception => e
					print_error "An unknown exception (#{e}) has occured while talking to the Metasploit backend."
					print_error "Please check the Metasploit logs for more details."
					return false
			end
		end
    
		def browser_exploits()
			return if not @enabled
                
      get_lock()
			res = self.call('module.exploits')
			return [] if not res or not res['modules']

			mods = res['modules']
			ret = []
			
			mods.each do |m|
				ret << m if(m.include? '/browser/')
			end
			
      release_lock()
			ret.sort
	  end

		def get_exploit_info(name)
			return if not @enabled
      get_lock()
			res = self.call('module.info','exploit',name)
      release_lock()
			res || {}
		end
		
		def get_payloads(name)
			return if not @enabled
      get_lock()
			res = self.call('module.compatible_payloads',name)
      release_lock()
			res || {}
		end
		
		def get_options(name)
			return if not @enabled
      get_lock()
			res = self.call('module.options','exploit',name)
      release_lock()
			res || {}
		end
		
		def payloads()
			return if not @enabled
      get_lock()
			res = self.call('module.payloads')
      release_lock()
			return {} if not res or not res['modules']
			res['modules']
		end
		
		def payload_options(name)
			return if not @enabled
      get_lock()
			res = self.call('module.options','payload',name)
      release_lock
			return {} if not res
			res
		end
		
		def launch_exploit(exploit,opts)
			return if not @enabled
      get_lock()
			begin
				res = self.call('module.execute','exploit',exploit,opts)
			rescue Exception => e
				print_error "Exploit failed for #{exploit} \n"
        release_lock()
				return false
			end
      
      release_lock()

			uri = ""
			if opts['SSL'] 
				uri += "https://"
			else
				uri += "http://"
			end

			uri += @config.get('beef.extension.metasploit.callback_host') + ":" + opts['SRVPORT'] + "/" + opts['URIPATH']

			res['uri'] = uri
			res
		end

		def launch_autopwn
			return if not @enabled
			opts = {
				'LHOST' => @config.get('beef.extension.metasploit.callback_host') ,
				'URIPATH' => @apurl
				}
      			get_lock()
			begin
				res = self.call('module.execute','auxiliary','server/browser_autopwn',opts)
			rescue Exception => e
				print_error "Failed to launch autopwn\n"
        			release_lock()
				return false
			end
      			release_lock()

		end
		
	end
	
end
end
end
