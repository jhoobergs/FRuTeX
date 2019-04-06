from lark import Lark
from lark.indenter import Indenter

class FrutexIndenter(Indenter):
    NL_type = '_NEWLINE'
    OPEN_PAREN_types = ['LPAR', 'LSQB', 'LBRACE']
    CLOSE_PAREN_types = ['RPAR', 'RSQB', 'RBRACE']
    INDENT_type = '_INDENT'
    DEDENT_type = '_DEDENT'
    tab_len = 2

class FrutexParser():
  def __init__(self):
    kwargs = dict(rel_to=__file__, postlex=FrutexIndenter(), start='file_input')
    self.parser = Lark.open('frutex.lark', parser='lalr', **kwargs)

  def parse(str):
    return frutex_parser.parse(_read(os.path.join(path, f)) + '\n')
