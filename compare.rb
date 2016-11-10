require 'benchmark'
require 'fast_blank'
require "ffi"

module Rust
  extend FFI::Library
  lib_ext = "dylib" if `uname` =~ /Darwin/
  lib_ext = "so" if `uname` =~ /Linux/
  ffi_lib "./libfastblank/target/release/libfastblank.#{lib_ext}"
  attach_function :fast_blank, [:string], :bool
end

n = 5000000

text = """
Hi, thank you for your talk proposal. We've received a lot of high quality talks and we had very hard time to pick the best one.
"""

puts "normal text"

Benchmark.bm(20) do |x|
  x.report("blank?") { n.times do; text.blank?; end }
  x.report("Rust.fast_blank") { n.times do; Rust.fast_blank(text); end }
end

text_spaces = """
                                                                                                                                x
Hi, thank you for your talk proposal. We've received a lot of high quality talks and we had very hard time to pick the best one.
"""

puts ""
puts "text with leading spaces"

Benchmark.bm(20) do |x|
  x.report("blank?") { n.times do; text_spaces.blank?; end }
  x.report("Rust.fast_blank") { n.times do; Rust.fast_blank(text_spaces); end }
end
