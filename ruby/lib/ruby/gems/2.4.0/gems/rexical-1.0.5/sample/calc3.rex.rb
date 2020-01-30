#
# DO NOT MODIFY!!!!
# This file is automatically generated by rex 1.0.0
# from lexical definition file "calc3.rex".
#

require 'racc/parser'
#
# calc3.rex
# lexical scanner definition for rex
#

class Calculator3 < Racc::Parser
  require 'strscan'

  class ScanError < StandardError ; end

  attr_reader :lineno
  attr_reader :filename

  def scan_setup ; end

  def action &block
    yield
  end

  def scan_str( str )
    scan_evaluate  str
    do_parse
  end

  def load_file( filename )
    @filename = filename
    open(filename, "r") do |f|
      scan_evaluate  f.read
    end
  end

  def scan_file( filename )
    load_file  filename
    do_parse
  end

  def next_token
    @rex_tokens.shift
  end

  def scan_evaluate( str )
    scan_setup
    @rex_tokens = []
    @lineno  =  1
    ss = StringScanner.new(str)
    state = nil
    until ss.eos?
      text = ss.peek(1)
      @lineno  +=  1  if text == "\n"
      case state
      when nil
        case
        when (text = ss.scan(/\s+/))
          ;

        when (text = ss.scan(/\d+/))
           @rex_tokens.push action { [:NUMBER, text.to_i] }

        when (text = ss.scan(/.|\n/))
           @rex_tokens.push action { [text, text] }

        else
          text = ss.string[ss.pos .. -1]
          raise  ScanError, "can not match: '" + text + "'"
        end  # if

      else
        raise  ScanError, "undefined state: '" + state.to_s + "'"
      end  # case state
    end  # until ss
  end  # def scan_evaluate

end # class

if __FILE__ == $0
  exit  if ARGV.size != 1
  filename = ARGV.shift
  rex = Calculator3.new
  begin
    rex.load_file  filename
    while  token = rex.next_token
      p token
    end
  rescue
    $stderr.printf  "%s:%d:%s\n", rex.filename, rex.lineno, $!.message
  end
end