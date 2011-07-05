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
module Core
  #
  # Parses the user configuration file for beef.
  #
  # Example:
  #
  #   configuration = BeEF::Core::Configuration.instance
  #   p configuration.get('beef.http.host) # => "0.0.0.0"
  #
  class Configuration
    
    include Singleton
  
    #
    # Constructor
    #
    def initialize(configuration_file="#{$root_dir}/config.yaml")
      # argument type checking
      raise Exception::TypeError, '"configuration_file" needs to be a string' if not configuration_file.string?
      # test to make sure file exists
      raise Exception::TypeError, 'Configuration yaml cannot be found' if not File.exist?(configuration_file)
      #open base config
      @config = self.load(configuration_file)
      # set default value if key? does not exist
      @config.default = nil
      load_extensions_config
      load_modules_config
    end

    #
    # Loads yaml file
    #
    def load(file)
        return nil if not File.exists?(file)
        raw = File.read(file)
        return YAML.load(raw)
    end

    #
    # Returns the value of a selected key in the configuration file.
    #
    def get(key)
        subkeys = key.split('.')
        lastkey = subkeys.pop
        subhash = subkeys.inject(@config) do |hash, k|
            hash[k]
        end
        return (subhash != nil and subhash.has_key?(lastkey)) ? subhash[lastkey] : nil 
    end

    #
    # Sets the give key value pair to the config instance
    #
    def set(key, value)
        subkeys = key.split('.').reverse
        return false if subkeys.length == 0
        hash = {subkeys.shift.to_s => value}
        subkeys.each{|v|
            hash = {v.to_s => hash}
        }
        @config = @config.recursive_merge(hash)
        return true
    end
    
    #
    # load extensions configurations
    #
    def load_extensions_config
        Dir.glob("#{$root_dir}/extensions/*/config.yaml") do | cf |
            y = self.load(cf)
            if y != nil
                @config = y.recursive_merge(@config)
            end
        end
    end

    #
    # Load module configurations
    #
    def load_modules_config
        Dir.glob("#{$root_dir}/modules/**/*/config.yaml") do | cf |
            y = self.load(cf)
            if y != nil
                @config = y.recursive_merge(@config)
            end
        end
    end

  end
end
end
