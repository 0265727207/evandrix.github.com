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
module AdminUI
module Controllers
  
#
#
#
class Modules < BeEF::Extension::AdminUI::HttpController
  
  BD = BeEF::Extension::Initialization::Models::BrowserDetails
  
  def initialize
    super({
      'paths' => {
        '/select/commandmodules/all.json'   => method(:select_all_command_modules),
        '/select/commandmodules/tree.json'  => method(:select_command_modules_tree),
        '/select/commandmodule.json'        => method(:select_command_module),
        '/select/command.json'              => method(:select_command),
        '/select/command_results.json'      => method(:select_command_results),
        '/select/zombie_summary.json'       => method(:select_zombie_summary),
        '/commandmodule/commands.json'      => method(:select_command_module_commands),
        '/commandmodule/new'                => method(:attach_command_module),
        '/commandmodule/dynamicnew'         => method(:attach_dynamic_command_module),
        '/commandmodule/reexecute'          => method(:reexecute_command_module)
      }
    })
    
    @session = BeEF::Extension::AdminUI::Session.instance
  end
  
  # Returns a JSON array containing the summary for a selected zombie.
  def select_zombie_summary

    # get the zombie 
    zombie_session = @params['zombie_session'] || nil
    raise WEBrick::HTTPStatus::BadRequest, "Zombie session is nil" if zombie_session.nil?
    zombie = BeEF::Core::Models::HookedBrowser.first(:session => zombie_session)
    raise WEBrick::HTTPStatus::BadRequest, "Zombie is nil" if zombie.nil?

    # init the summary grid
    summary_grid_hash = {
      'success' => 'true', 
      'results' => []
    }

    # set and add the return values for the page title
    page_title = BD.get(zombie_session, 'PageTitle') 
    if not page_title.nil?
      encoded_page_title = CGI.escapeHTML(page_title)
      encoded_page_hash = { 'Page Title' => encoded_page_title }
      
      page_name_row = {
        'category' => 'Browser Hook Initialisation',
        'data' => encoded_page_hash,
        'from' => 'Initialisation'
      }
      
      summary_grid_hash['results'].push(page_name_row) # add the row
    end

    # set and add the return values for the host name
    host_name = BD.get(zombie_session, 'HostName') 
    if not host_name.nil?
      encoded_host_name = CGI.escapeHTML(host_name)
      encoded_host_name_hash = { 'Host Name' => encoded_host_name }
    
      page_name_row = {
        'category' => 'Browser Hook Initialisation',
        'data' => encoded_host_name_hash,
        'from' => 'Initialisation'
      }
    
      summary_grid_hash['results'].push(page_name_row) # add the row
    end
    
    # set and add the return values for the os name
    os_name = BD.get(zombie_session, 'OsName')
    if not host_name.nil?
      encoded_os_name = CGI.escapeHTML(os_name)
      encoded_os_name_hash = { 'OS Name' => encoded_os_name }
    
      page_name_row = {
        'category' => 'Browser Hook Initialisation',
        'data' => encoded_os_name_hash,
        'from' => 'Initialisation'
      }
    
      summary_grid_hash['results'].push(page_name_row) # add the row
    end
    
    # set and add the return values for the browser name
    browser_name = BD.get(zombie_session, 'BrowserName') 
    if not browser_name.nil?
      friendly_browser_name = BeEF::Core::Constants::Browsers.friendly_name(browser_name)
      browser_name_hash = { 'Detected Browser Name' => friendly_browser_name }

      browser_name_row = {
        'category' => 'Browser Hook Initialisation',
        'data' => browser_name_hash,
        'from' => 'Initialisation'
      }
    
      summary_grid_hash['results'].push(browser_name_row) # add the row
    end
    
    # set and add the return values for the browser version
    browser_version = BD.get(zombie_session, 'BrowserVersion') 
    if not browser_version.nil?
      encoded_browser_version = CGI.escapeHTML(browser_version)
      browser_version_hash = { 'Detected Browser Version' => encoded_browser_version }

      browser_version_row = {
        'category' => 'Browser Hook Initialisation',
         'data' => browser_version_hash,
        'from' => 'Initialisation'
      }
    
      summary_grid_hash['results'].push(browser_version_row) # add the row
    end
    
    # set and add the return values for the browser ua string
    browser_uastring = BD.get(zombie_session, 'BrowserReportedName')
    if not browser_uastring.nil?
      browser_uastring_hash = { 'Browser UA String' => browser_uastring }

      browser_uastring_row = {
        'category' => 'Browser Hook Initialisation',
         'data' => browser_uastring_hash,
        'from' => 'Initialisation'
      }
    
      summary_grid_hash['results'].push(browser_uastring_row) # add the row
    end
    
    # set and add the list of plugins installed in the browser
    browser_plugins = BD.get(zombie_session, 'BrowserPlugins')
    if not browser_plugins.nil? and not browser_plugins.empty?
      encoded_browser_plugins = CGI.escapeHTML(browser_plugins)
      encoded_browser_plugins_hash = { 'Browser Plugins' => encoded_browser_plugins }
      
      page_name_row = {
        'category' => 'Browser Hook Initialisation',
        'data' => encoded_browser_plugins_hash,
        'from' => 'Initialisation'
      }
      
      summary_grid_hash['results'].push(page_name_row) # add the row
    end
    
    # set and add the internal ip address
    internal_ip = BD.get(zombie_session, 'InternalIP')
    if not internal_ip.nil?
      encoded_internal_ip = CGI.escapeHTML(internal_ip)
      encoded_internal_ip_hash = { 'Internal IP' => encoded_internal_ip }
      
      page_name_row = {
        'category' => 'Browser Hook Initialisation',
        'data' => encoded_internal_ip_hash,
        'from' => 'Initialisation'
      }
      
      summary_grid_hash['results'].push(page_name_row) # add the row
    end
    
    # set and add the internal hostname
    internal_hostname = BD.get(zombie_session, 'InternalHostname')
    if not internal_hostname.nil?
      encoded_internal_hostname = CGI.escapeHTML(internal_hostname)
      encoded_internal_hostname_hash = { 'Internal Hostname' => encoded_internal_hostname }
      
      page_name_row = {
        'category' => 'Browser Hook Initialisation',
        'data' => encoded_internal_hostname_hash,
        'from' => 'Initialisation'
      }
      
      summary_grid_hash['results'].push(page_name_row) # add the row
    end
    
    @body = summary_grid_hash.to_json  
  end
      
  # Returns the list of all command_modules in a JSON format
  def select_all_command_modules
    @body = command_modules2json(BeEF::Modules.get_loaded.keys)
  end

  # Set the correct icon for the command module
  def set_command_module_icon(command_mod)
      command_module_icon_path = BeEF::Extension::AdminUI::Constants::Icons::MODULE_TARGET_IMG_PATH # add icon path
      case command_mod.verify_target()
      when BeEF::Core::Constants::CommandModule::VERIFIED_NOT_WORKING
        command_module_icon_path += BeEF::Extension::AdminUI::Constants::Icons::VERIFIED_NOT_WORKING_IMG
      when BeEF::Core::Constants::CommandModule::VERIFIED_USER_NOTIFY
        command_module_icon_path += BeEF::Extension::AdminUI::Constants::Icons::VERIFIED_USER_NOTIFY_IMG
      when BeEF::Core::Constants::CommandModule::VERIFIED_WORKING
        command_module_icon_path += BeEF::Extension::AdminUI::Constants::Icons::VERIFIED_WORKING_IMG
      when BeEF::Core::Constants::CommandModule::VERIFIED_UNKNOWN
        command_module_icon_path += BeEF::Extension::AdminUI::Constants::Icons::VERIFIED_UNKNOWN_IMG
      else
        command_module_icon_path += BeEF::Extension::AdminUI::Constants::Icons::VERIFIED_UNKNOWN_IMG
      end
      #return command_module_icon_path
      command_module_icon_path
  end

   # Set the correct working status for the command module
  def set_command_module_status(command_mod)
      case command_mod.verify_target()
      when BeEF::Core::Constants::CommandModule::VERIFIED_NOT_WORKING
        command_module_status = BeEF::Core::Constants::CommandModule::VERIFIED_NOT_WORKING
      when BeEF::Core::Constants::CommandModule::VERIFIED_USER_NOTIFY
        command_module_status = BeEF::Core::Constants::CommandModule::VERIFIED_USER_NOTIFY
      when BeEF::Core::Constants::CommandModule::VERIFIED_WORKING
        command_module_status = BeEF::Core::Constants::CommandModule::VERIFIED_WORKING
      when BeEF::Core::Constants::CommandModule::VERIFIED_UNKNOWN
        command_module_status = BeEF::Core::Constants::CommandModule::VERIFIED_UNKNOWN
      else
        command_module_status = BeEF::Core::Constants::CommandModule::VERIFIED_UNKNOWN
      end
#      return command_module_status
      command_module_status
  end

  def update_command_module_tree(tree, categories, cmd_category, cmd_icon_path, cmd_status, cmd_name, cmd_id)
      # construct the category branch if it doesn't exist for the command module tree
      if not categories.include? cmd_category
        categories.push(cmd_category) # flag that the category has been added
        tree.push({ # add the branch structure
          'text' => cmd_category,
          'cls' => 'folder',
          'children' => []
        })
      end

      # construct leaf node for the command module tree
      leaf_node = {
          'text' => cmd_name,
          'leaf' => true,
          'icon' => cmd_icon_path,
          'status' => cmd_status,
          'id' => cmd_id
      }

      # add the node to the branch in the command module tree
      tree.each {|x|
        if x['text'].eql? cmd_category
          x['children'].push( leaf_node )
            break
        end
      }
  end
  
  # Returns the list of all command_modules for a TreePanel in the interface.
  def select_command_modules_tree
    tree = []
    categories = []

    BeEF::Modules.get_loaded.each{|k, mod|
      # get the hooked browser session id and set it in the command module
      hook_session_id = @params['zombie_session'] || nil
      raise WEBrick::HTTPStatus::BadRequest, "hook_session_id is nil" if hook_session_id.nil?

      command_mod = BeEF::Core::Command.const_get(k.capitalize).new
      command_mod.session_id = hook_session_id

      # create url path and file for the command module icon
      command_module_icon_path = set_command_module_icon(command_mod)
      command_module_status = set_command_module_status(command_mod)

      update_command_module_tree(tree, categories, mod['category'], command_module_icon_path, command_module_status, mod['name'],mod['db']['id'])
    }

    # if dynamic modules are found in the DB, then we don't have yaml config for them
    # and loading must proceed in a different way.
    dynamic_modules = BeEF::Core::Models::CommandModule.all(:path.like => "Dynamic/")

    if(dynamic_modules != nil)
         all_modules = BeEF::Core::Models::CommandModule.all(:order => [:id.asc])
         all_modules.each{|dyn_mod|
         next if !dyn_mod.path.split('/').first.match(/^Dynamic/)

         hook_session_id = @params['zombie_session'] || nil
         raise WEBrick::HTTPStatus::BadRequest, "hook_session_id is nil" if hook_session_id.nil?

          dyn_mod_name = dyn_mod.path.split('/').last
          dyn_mod_category = nil
          if(dyn_mod_name == "Msf")
             dyn_mod_category = "Metasploit"
          else
             # future dynamic modules...
          end

          print_debug ("Loading Dynamic command module: category [#{dyn_mod_category}] - name [#{dyn_mod.name.to_s}]")
          command_mod = BeEF::Modules::Commands.const_get(dyn_mod_name.capitalize).new
          command_mod.session_id = hook_session_id
          command_mod.update_info(dyn_mod.id)
          command_mod_name = command_mod.info['Name'].downcase

          # create url path and file for the command module icon
          command_module_icon_path = set_command_module_icon(command_mod)
          command_module_status = set_command_module_status(command_mod)

         update_command_module_tree(tree, categories, dyn_mod_category, command_module_icon_path, command_module_status, command_mod_name,dyn_mod.id)
       }
    end
      
    # sort the parent array nodes 
    tree.sort! {|a,b| a['text'] <=> b['text']}
    
    # sort the children nodes by status
    tree.each {|x| x['children'] =
      x['children'].sort_by {|a| a['status']}
    }


      
    # append the number of command modules so the branch name results in: "<category name> (num)"
    tree.each {|command_module_branch|
      num_of_command_modules = command_module_branch['children'].length
      command_module_branch['text'] = command_module_branch['text'] + " (" + num_of_command_modules.to_s() + ")"
    }
      
    # return a JSON array of hashes
    @body = tree.to_json
  end
  
  # Returns the inputs definition of an command_module.
  def select_command_module
    command_module_id = @params['command_module_id'] || nil
    raise WEBrick::HTTPStatus::BadRequest, "command_module_id is nil" if command_module_id.nil?
    command_module = BeEF::Core::Models::CommandModule.get(command_module_id)

    if(command_module != nil && command_module.path.match(/^Dynamic/))
        payload_name = @params['payload_name'] || nil
        if not payload_name.nil?
          @body = dynamic_payload2json(command_module_id, payload_name)
        else
          @body = dynamic_modules2json(command_module_id);
        end
    else
      key = BeEF::Module.get_key_by_database_id(command_module_id)
      @body = command_modules2json([key]);
    end
  end
  
  # Returns the list of commands for an command_module
  def select_command_module_commands
    commands = []
    i=0

    # get params
    zombie_session = @params['zombie_session'] || nil
    raise WEBrick::HTTPStatus::BadRequest, "Zombie session is nil" if zombie_session.nil?
    command_module_id = @params['command_module_id'] || nil
    raise WEBrick::HTTPStatus::BadRequest, "command_module id is nil" if command_module_id.nil?
    # validate nonce
    nonce = @params['nonce'] || nil
    raise WEBrick::HTTPStatus::BadRequest, "nonce is nil" if nonce.nil?
    raise WEBrick::HTTPStatus::BadRequest, "nonce incorrect" if @session.get_nonce != nonce
    
    # get the browser id
    zombie = Z.first(:session => zombie_session)
    raise WEBrick::HTTPStatus::BadRequest, "Zombie is nil" if zombie.nil?
    zombie_id = zombie.id
    raise WEBrick::HTTPStatus::BadRequest, "Zombie id is nil" if zombie_id.nil?
      
    C.all(:command_module_id => command_module_id, :hooked_browser_id => zombie_id).each do |command|
      commands.push({
        'id' => i, 
        'object_id' => command.id, 
        'creationdate' => Time.at(command.creationdate.to_i).strftime("%Y-%m-%d %H:%M").to_s, 
        'label' => command.label
        })
      i+=1
    end
      
    @body = {
      'success' => 'true', 
      'commands' => commands}.to_json
      
  end
  
  # Attaches an command_module to a zombie.
  def attach_command_module
    
    definition = {}

    # get params
    zombie_session = @params['zombie_session'] || nil
    raise WEBrick::HTTPStatus::BadRequest, "Zombie id is nil" if zombie_session.nil?
    command_module_id = @params['command_module_id'] || nil
    raise WEBrick::HTTPStatus::BadRequest, "command_module id is nil" if command_module_id.nil?
    # validate nonce
    nonce = @params['nonce'] || nil
    raise WEBrick::HTTPStatus::BadRequest, "nonce is nil" if nonce.nil?
    raise WEBrick::HTTPStatus::BadRequest, "nonce incorrect" if @session.get_nonce != nonce
    
    @params.keys.each {|param| 
      raise WEBrick::HTTPStatus::BadRequest, "invalid key param string" if not BeEF::Filters.has_valid_param_chars?(param)
      raise WEBrick::HTTPStatus::BadRequest, "first char is num" if BeEF::Filters.first_char_is_num?(param)
      definition[param[4..-1]] = params[param]
      oc = BeEF::Core::Models::OptionCache.first_or_create(:name => param[4..-1])
      oc.value = params[param]
	    oc.save
    }

    zombie = Z.first(:session => zombie_session)
    raise WEBrick::HTTPStatus::BadRequest, "Zombie is nil" if zombie.nil?
    zombie_id = zombie.id
    raise WEBrick::HTTPStatus::BadRequest, "Zombie id is nil" if zombie_id.nil?
    
    C.new(  :data => definition.to_json,
            :hooked_browser_id => zombie_id,
            :command_module_id => command_module_id,
            :creationdate => Time.new.to_i
          ).save
    
    @body = '{success : true}'
  end
  
  # Re-execute an command_module to a zombie.
  def reexecute_command_module
    
    # get params
    command_id = @params['command_id'] || nil
    raise WEBrick::HTTPStatus::BadRequest, "Command id is nil" if command_id.nil?
    command = BeEF::Core::Models::Command.first(:id => command_id.to_i) || nil
    raise WEBrick::HTTPStatus::BadRequest, "Command is nil" if command.nil?
    # validate nonce
    nonce = @params['nonce'] || nil
    raise WEBrick::HTTPStatus::BadRequest, "nonce is nil" if nonce.nil?
    raise WEBrick::HTTPStatus::BadRequest, "nonce incorrect" if @session.get_nonce != nonce
    
    command.instructions_sent = false
    command.save
    
    @body = '{success : true}'
  end

  def attach_dynamic_command_module
    
    definition = {}

    # get params
    zombie_session = @params['zombie_session'] || nil
    raise WEBrick::HTTPStatus::BadRequest, "Zombie id is nil" if zombie_session.nil?
    command_module_id = @params['command_module_id'] || nil
    raise WEBrick::HTTPStatus::BadRequest, "command_module id is nil" if command_module_id.nil?
    # validate nonce
    nonce = @params['nonce'] || nil
    raise WEBrick::HTTPStatus::BadRequest, "nonce is nil" if nonce.nil?
    raise WEBrick::HTTPStatus::BadRequest, "nonce incorrect" if @session.get_nonce != nonce
    
    @params.keys.each {|param| 
      raise WEBrick::HTTPStatus::BadRequest, "invalid key param string" if not BeEF::Filters.has_valid_param_chars?(param)
      raise WEBrick::HTTPStatus::BadRequest, "first char is num" if BeEF::Filters.first_char_is_num?(param)
      definition[param[4..-1]] = params[param]
      oc = BeEF::Core::Models::OptionCache.first_or_create(:name => param[4..-1])
      oc.value = params[param]
	  oc.save
    }

    zombie = Z.first(:session => zombie_session)
    raise WEBrick::HTTPStatus::BadRequest, "Zombie is nil" if zombie.nil?
    zombie_id = zombie.id
    raise WEBrick::HTTPStatus::BadRequest, "Zombie id is nil" if zombie_id.nil?
    command_module = BeEF::Core::Models::CommandModule.get(command_module_id)

    if(command_module != nil && command_module.path.match(/^Dynamic/))
      dyn_mod_name = command_module.path.split('/').last
      e = BeEF::Modules::Commands.const_get(dyn_mod_name.capitalize).new
      e.update_info(command_module_id)
      e.update_data()
 	    ret = e.launch_exploit(definition)

      return {'success' => 'false'}.to_json if ret['result'] != 'success'

      basedef = {}
		  basedef['sploit_url'] = ret['uri']

      C.new(  :data => basedef.to_json,
        :hooked_browser_id => zombie_id,
        :command_module_id => command_module_id,
        :creationdate => Time.new.to_i
        ).save

      @body = '{success : true}'
    else
#       return {'success' => 'false'}.to_json
      {'success' => 'false'}.to_json
    end



  end
  
  # Returns the results of a command
  def select_command_results
    results = []
    
    # get params
    command_id = @params['command_id'] || nil
    raise WEBrick::HTTPStatus::BadRequest, "Command id is nil" if command_id.nil?
    command = BeEF::Core::Models::Command.first(:id => command_id.to_i) || nil
    raise WEBrick::HTTPStatus::BadRequest, "Command is nil" if command.nil?

    # get command_module
    command_module = BeEF::Core::Models::CommandModule.first(:id => command.command_module_id)
    raise WEBrick::HTTPStatus::BadRequest, "command_module is nil" if command_module.nil?
    
    resultsdb = BeEF::Core::Models::Result.all(:command_id => command_id)
    raise WEBrick::HTTPStatus::BadRequest, "Command id result is nil" if resultsdb.nil?
    
    resultsdb.each{ |result| results.push({'date' => result.date, 'data' => JSON.parse(result.data)}) }
    
    @body = {
      'success'             => 'true', 
      'command_module_name' => command_module.name,
      'command_module_id'   => command_module.id,
      'results'             => results}.to_json

  end
  
  # Returns the definition of a command.
  # In other words it returns the command that was used to command_module a zombie.
  def select_command
    
    # get params
    command_id = @params['command_id'] || nil
    raise WEBrick::HTTPStatus::BadRequest, "Command id is nil" if command_id.nil?
    command = BeEF::Core::Models::Command.first(:id => command_id.to_i) || nil
    raise WEBrick::HTTPStatus::BadRequest, "Command is nil" if command.nil?

    command_module = BeEF::Core::Models::CommandModule.get(command.command_module_id)
    raise WEBrick::HTTPStatus::BadRequest, "command_module is nil" if command_module.nil?

    if(command_module.path.split('/').first.match(/^Dynamic/))
      dyn_mod_name = command_module.path.split('/').last
      e = BeEF::Modules::Commands.const_get(dyn_mod_name.capitalize).new
    else
      command_module_name = command_module.name
      e = BeEF::Core::Command.const_get(command_module_name.capitalize).new
    end
            
    @body = {
      'success' => 'true', 
      'command_module_name'  => command_module_name,
      'command_module_id'    => command_module.id,
      'data'                 => JSON.parse(command.data),
      'definition'           => JSON.parse(e.to_json)
    }.to_json

  end
  
  private
  
  # Takes a list of command_modules and returns them as a JSON array
  def command_modules2json(command_modules)
    command_modules_json = {}
    i = 1
    config = BeEF::Core::Configuration.instance
    command_modules.each do |command_module|
      mod = config.get('beef.module.'+command_module)
      next if not File.exists?("#{$root_dir}"+mod['db']['path'])
      
      e = BeEF::Core::Command.const_get(mod['class']).new
      command_modules_json[i] = JSON.parse(e.to_json)
      i += 1
    end
    
    if not command_modules_json.empty?
      return {'success' => 'true', 'command_modules' => command_modules_json}.to_json
    else
      return {'success' => 'false'}.to_json
    end
  end

  # return the input requred for the module in JSON format
  def dynamic_modules2json(id)
    command_modules_json = {}
    
    mod = BeEF::Core::Models::CommandModule.first(:id => id)

    # if the module id is not in the database return false
    return {'success' => 'false'}.to_json if(not mod)
    
    # the path will equal Dynamic/<type> and this will get just the type
		dynamic_type = mod.path.split("/").last
		
    e = BeEF::Modules::Commands.const_get(dynamic_type.capitalize).new
    e.update_info(mod.id)
    e.update_data()
    command_modules_json[1] = JSON.parse(e.to_json)
    if not command_modules_json.empty?
        return {'success' => 'true', 'dynamic' => 'true', 'command_modules' => command_modules_json}.to_json
    else
        return {'success' => 'false'}.to_json
    end
  end

  def dynamic_payload2json(id, payload_name)
    command_modules_json = {}

    dynamic_command_module = BeEF::Core::Models::CommandModule.first(:id => id)
    raise WEBrick::HTTPStatus::BadRequest, "Module does not exists" if dynamic_command_module.nil?

    # the path will equal Dynamic/<type> and this will get just the type
		dynamic_type = dynamic_command_module.path.split("/").last

    # get payload options in JSON
    e = BeEF::Modules::Commands.const_get(dynamic_type.capitalize).new
    payload_options_json = []
    payload_options_json[1] = e.get_payload_options(payload_name)
    raise WEBrick::HTTPStatus::BadRequest, "Payload JSON generation error" if payload_options_json.empty?
    
    return {'success' => 'true', 'command_modules' => payload_options_json}.to_json

  end
  
end

end
end
end
end
