#!/usr/bin/env ruby

sender, receiver, flags = ARGV[0].match(/from:(\+?\w+)?\].*to:(\+?\w+)?\].*flags?:([-:\d]+)?/).captures

puts "#{sender},#{receiver},#{flags}"
