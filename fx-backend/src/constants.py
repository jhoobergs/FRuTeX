import frutex_parser


attrib_dict = {
        "content" : "content",
        "color"   : "color",
        "row_size": "row_size",
        "col_size": "col_size",
        }

cell_attrib_dict = {
        "content" : "content",
        "color"   : "color",
        }

attrib_to_default_dict = {
        "content": "default_content",
        "color": "default_color",
        "row_size": "default_row_size",
        "col_size": "default_col_size",
        }

default_config = {
        "default_content"  : frutex_parser.Integer(0),
        "default_color"    : frutex_parser.Integer(0xffd750),
        "default_col_size" : frutex_parser.Integer(75),
        "default_row_size" : frutex_parser.Integer(30),
        "num_rows"         : "20",
        "num_cols"         : "20",
}