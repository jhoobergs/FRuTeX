from lark import Lark
FRuTeX = Lark(r"""
    ?expr: if_exp
        | value
        | comp_exp
        | add_exp
    ?if_exp: "if" "(" expr ")" expr ["else" expr] 
    ?comp_exp: expr _comp_op expr
    ?add_exp: term_exp (_add_op term_exp)*
    ?term_exp: factor (_mult_op factor)*
    ?factor: _factor_op factor | pow_exp
    ?pow_exp: value ["**" factor]
    ?value: float
     | integer
     | "(" expr ")"
     | "true" -> true
     | "false" -> false
     | NAME "(" [arguments] ")" -> funccall
     | NAME -> var
     | string
     
    string : ESCAPED_STRING
    integer: INT
    float: DECIMAL

    arguments: expr ("," expr)*

    !_comp_op: ">"|"<"|">="|"<="|"=="|"!="
    !_mult_op: "*"|"/"|"//"|"%"
    !_factor_op: "+"|"-"
    !_add_op: "+"|"-"
    NAME: /[a-zA-Z_][\w:]*/

    %import common.DECIMAL
    %import common.INT
    %import common.ESCAPED_STRING
    %import common.SIGNED_NUMBER
    %import common.WS
    %ignore WS

    """, start='expr')

text = '"ster"'
print( FRuTeX.parse(text).pretty() )
text = 'if (5>7) 6'
print( FRuTeX.parse(text).pretty() )
text = """if (5>7)
 6 else 7"""
print( FRuTeX.parse(text).pretty() )
text = 'if (5<7) 6 else 7'
print( FRuTeX.parse(text).pretty() )
text = 'if (5==7) 6 else 7'
print( FRuTeX.parse(text).pretty() )
text = 'if (5>=7) 6 else 7'
print( FRuTeX.parse(text).pretty() )
text = 'if (5<=7) 6 else 7'
print( FRuTeX.parse(text).pretty() )
text = 'if (5!=7) 6 else 7'
print( FRuTeX.parse(text).pretty() )
text = 'if (5!=7) 3 + 6 * 7 else 7 * 5 * 3 + 5'
print( FRuTeX.parse(text).pretty() )
text = 'if (5!=7) (3 + 6) * 7 else 7 * 5 * 3 + 5'
print( FRuTeX.parse(text).pretty() )
text = 'if (5!=7) (3 + 6) ** 7 else 7 ** 5 ** 3 + 5'
print( FRuTeX.parse(text).pretty() )
text = 'if (5!=7) (3 + 6) ** 7 else (7 ** 5) ** 3 + 5'
print( FRuTeX.parse(text).pretty() )
text = """if (5!=7)
 (3 + 6) ** 7 else (7 ** 5) ** 3 +- 5.2"""
print( FRuTeX.parse(text).pretty() )
text = """if (A5:5!=7)
 (3 + 6) ** 7 else (7 ** 5) ** 3 +- 5.2"""
print( FRuTeX.parse(text).pretty() )
text = """if ((A5:5!=7) == true )
 (3 + 6) ** 7 else (7 ** 5) ** 3 +- 5.2"""
print( FRuTeX.parse(text).pretty() )
text = """if (A5:5!=7)
 (3 + 6 * 8) ** 7 else (7 ** 5) ** 3 +- 5.2"""
print( FRuTeX.parse(text) )
text = """if (func())
 (3 + 6 * 8) ** 7 else (7 ** 5) ** 3 +- 5.2"""
print( FRuTeX.parse(text) )
text = """if (func(A5:5!=7))
 (3 + 6 * 8) ** 7 else (7 ** 5) ** 3 +- 5.2"""
print( FRuTeX.parse(text) )

json_parser = Lark(r"""
    ?value: dict
          | list
          | string
          | SIGNED_NUMBER      -> number
          | "true"             -> true
          | "false"            -> false
          | "null"             -> null

    list : "[" [value ("," value)*] "]"

    dict : "{" [pair ("," pair)*] "}"
    pair : string ":" value

    string : ESCAPED_STRING

    %import common.ESCAPED_STRING
    %import common.SIGNED_NUMBER
    %import common.WS
    %ignore WS

    """, start='value')

#text = '{"key": ["item0", "item1", 3.14, true]}'
#print( json_parser.parse(text).pretty() )