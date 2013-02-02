# Hello World example in JRuby

require "java"

stringHello= "Hello World"
stringDate = java.util.Date.new

puts "#{stringHello.to_s}"
puts "Date := #{stringDate.to_s}"
